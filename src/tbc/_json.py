"""Shared restricted JSON profile. Limits are implementation safety defaults."""
from collections.abc import Mapping
import json

MAX_BYTES = 1024 * 1024
MAX_DEPTH = 32
MAX_INTEGER = 2**53 - 1


class InputError(ValueError):
    """Invalid input, with a stable code and a path that never echoes user keys."""

    def __init__(self, code: str, path: str = "$"):
        self.code = code
        self.path = path
        super().__init__(f"{code} at {path}")


def snapshot(value, path="$", depth=0, ancestors=None, budget=None):
    """Copy JSON data without coercion or caller-owned mutable containers."""
    if ancestors is None:
        ancestors, budget = set(), [MAX_BYTES]
    budget[0] -= 1
    if budget[0] < 0 or depth > MAX_DEPTH:
        raise InputError("RESOURCE_LIMIT", path)
    kind = type(value)
    if value is None or kind is bool:
        return value
    if kind is int:
        if abs(value) > MAX_INTEGER:
            raise InputError("INTEGER_RANGE", path)
        return value
    if kind is str:
        if len(value) > MAX_BYTES:
            raise InputError("RESOURCE_LIMIT", path)
        try:
            size = len(value.encode("utf-8"))
        except UnicodeEncodeError:
            raise InputError("SURROGATE", path) from None
        budget[0] -= size
        if budget[0] < 0:
            raise InputError("RESOURCE_LIMIT", path)
        return value
    if not isinstance(value, Mapping) and kind is not list:
        raise InputError("JSON_TYPE", path)
    identity = id(value)
    if identity in ancestors:
        raise InputError("CYCLIC_INPUT", path)
    ancestors.add(identity)
    try:
        if isinstance(value, Mapping):
            result = {}
            for key, item in value.items():
                if type(key) is not str:
                    raise InputError("KEY_TYPE", path)
                # Arbitrary payload keys may be sensitive: use a wildcard path.
                snapshot(key, path + ".*", depth + 1, ancestors, budget)
                result[key] = snapshot(item, path + ".*", depth + 1, ancestors, budget)
        else:
            result = [snapshot(item, path + f"[{i}]", depth + 1, ancestors, budget)
                      for i, item in enumerate(value)]
        return result
    finally:
        ancestors.remove(identity)


def encode(normalized):
    data = json.dumps(normalized, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    if len(data) > MAX_BYTES:
        raise InputError("RESOURCE_LIMIT")
    return data


def checked_copy(value):
    try:
        result = snapshot(value)
        encode(result)
        return result
    except (RecursionError, OverflowError):
        raise InputError("RESOURCE_LIMIT") from None


def decode_request(text):
    if type(text) is not str:
        raise InputError("TEXT_REQUIRED")
    if len(text) > MAX_BYTES:
        raise InputError("RESOURCE_LIMIT")
    try:
        if len(text.encode("utf-8")) > MAX_BYTES:
            raise InputError("RESOURCE_LIMIT")
    except UnicodeEncodeError:
        raise InputError("SURROGATE") from None

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise InputError("DUPLICATE_KEY")
            result[key] = value
        return result

    def reject_number(value):
        raise InputError("JSON_NUMBER")

    try:
        value = json.loads(text, object_pairs_hook=pairs,
                           parse_float=reject_number, parse_constant=reject_number)
    except InputError:
        raise
    except (ValueError, RecursionError, OverflowError):
        raise InputError("INVALID_JSON") from None
    return checked_copy(value)
