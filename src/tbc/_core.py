"""Pure exact-action evaluation of explicitly host-verified facts."""
import hashlib
import re
from collections.abc import Mapping

from ._json import InputError, checked_copy, decode_request, encode

_DIGEST = re.compile(r"sha256:[0-9a-f]{64}\Z")
_REASONS = frozenset({
    "ACTOR_MISMATCH", "ACTION_BINDING_MISMATCH", "AUTHORITY_MISSING",
    "AUTHORITY_NOT_CURRENT", "POLICY_MISSING", "POLICY_BINDING_MISMATCH",
    "POLICY_NOT_CURRENT", "POLICY_DENIED", "EVIDENCE_MISSING", "EVIDENCE_FAILED",
    "EVIDENCE_NOT_CURRENT", "EVIDENCE_BINDING_MISMATCH",
})


def fields(value, names, path):
    if type(value) is not dict or set(value) != set(names.split()):
        raise InputError("FIELDS", path)


def identifier(value, path):
    if type(value) is not str or not value:
        raise InputError("IDENTIFIER", path)


def digest_field(value, path):
    if type(value) is not str or not _DIGEST.fullmatch(value):
        raise InputError("DIGEST", path)


def integer(value, path):
    if type(value) is not int:
        raise InputError("INTEGER", path)


def interval(value, start, path):
    for key in (start, "expires_at"):
        integer(value[key], path + "." + key)
    if value[start] >= value["expires_at"]:
        raise InputError("TIME_INTERVAL", path)


def schema(value, expected, path):
    if value != expected:
        raise InputError("SCHEMA_VERSION", path)


def action_valid(action):
    fields(action, "actor transition resource payload", "$.action")
    for key in ("actor", "transition", "resource"):
        identifier(action[key], "$.action." + key)
    if type(action["payload"]) is not dict:
        raise InputError("PAYLOAD_OBJECT", "$.action.payload")


def request_valid(request):
    fields(request, "schema action", "$")
    schema(request["schema"], "tbc.request.v1", "$.schema")
    action_valid(request["action"])


def context_valid(context):
    fields(context, "schema evaluation_time authenticated_actor action_digest grant policy evidence", "$.context")
    schema(context["schema"], "tbc.context.v1", "$.context.schema")
    integer(context["evaluation_time"], "$.context.evaluation_time")
    identifier(context["authenticated_actor"], "$.context.authenticated_actor")
    digest_field(context["action_digest"], "$.context.action_digest")
    grant = context["grant"]
    if grant is not None:
        fields(grant, "id issuer action_digest not_before expires_at", "$.context.grant")
        for key in ("id", "issuer"):
            identifier(grant[key], "$.context.grant." + key)
        digest_field(grant["action_digest"], "$.context.grant.action_digest")
        interval(grant, "not_before", "$.context.grant")
    policy = context["policy"]
    if policy is not None:
        fields(policy, "id version digest action_digest decision not_before expires_at required_evidence_ids", "$.context.policy")
        for key in ("id", "version"):
            identifier(policy[key], "$.context.policy." + key)
        for key in ("digest", "action_digest"):
            digest_field(policy[key], "$.context.policy." + key)
        if policy["decision"] not in ("ALLOW", "DENY"):
            raise InputError("DECISION", "$.context.policy.decision")
        interval(policy, "not_before", "$.context.policy")
        required = policy["required_evidence_ids"]
        if type(required) is not list:
            raise InputError("ID_LIST", "$.context.policy.required_evidence_ids")
        for item in required:
            identifier(item, "$.context.policy.required_evidence_ids.*")
        if len(required) != len(set(required)):
            raise InputError("DUPLICATE_ID", "$.context.policy.required_evidence_ids")
        required.sort()
    evidence = context["evidence"]
    if type(evidence) is not list:
        raise InputError("EVIDENCE_LIST", "$.context.evidence")
    ids = set()
    for item in evidence:
        path = "$.context.evidence.*"
        fields(item, "id subject_digest verifier observed_at expires_at passed", path)
        for key in ("id", "verifier"):
            identifier(item[key], path + "." + key)
        digest_field(item["subject_digest"], path + ".subject_digest")
        interval(item, "observed_at", path)
        if type(item["passed"]) is not bool:
            raise InputError("BOOLEAN", path + ".passed")
        if item["id"] in ids:
            raise InputError("DUPLICATE_ID", path)
        ids.add(item["id"])
    evidence.sort(key=lambda item: item["id"])


def bound_digest(domain, value):
    return "sha256:" + hashlib.sha256(domain.encode("ascii") + b"\n" + encode(value)).hexdigest()


def load_request(text: str) -> dict:
    """Decode/validate an untrusted request; never accept authority from it."""
    request = decode_request(text)
    request_valid(request)
    return request


def action_digest(action: Mapping) -> str:
    """Bind all exact action fields using the versioned TBC JSON profile."""
    action = checked_copy(action)
    action_valid(action)
    return bound_digest("tbc.action.v1", action)


def evaluate(request: Mapping, *, context: Mapping) -> dict:
    """Evaluate host-verified facts. No authentication, clock, I/O or execution."""
    request, context = checked_copy(request), checked_copy(context)
    request_valid(request)
    context_valid(context)
    action = request["action"]
    digest = bound_digest("tbc.action.v1", action)
    now = context["evaluation_time"]
    grant, policy = context["grant"], context["policy"]
    reasons = set()
    if context["authenticated_actor"] != action["actor"]:
        reasons.add("ACTOR_MISMATCH")
    if context["action_digest"] != digest:
        reasons.add("ACTION_BINDING_MISMATCH")
    if grant is None:
        reasons.add("AUTHORITY_MISSING")
    else:
        if grant["action_digest"] != digest:
            reasons.add("ACTION_BINDING_MISMATCH")
        if not grant["not_before"] <= now < grant["expires_at"]:
            reasons.add("AUTHORITY_NOT_CURRENT")
    if policy is None:
        reasons.add("POLICY_MISSING")
    else:
        bound = policy["action_digest"] == digest
        current = policy["not_before"] <= now < policy["expires_at"]
        if not bound:
            reasons.add("POLICY_BINDING_MISMATCH")
        if not current:
            reasons.add("POLICY_NOT_CURRENT")
        if policy["decision"] != "ALLOW":
            reasons.add("POLICY_DENIED")
        if bound and current and policy["decision"] == "ALLOW":
            evidence = {item["id"]: item for item in context["evidence"]}
            for required in policy["required_evidence_ids"]:
                item = evidence.get(required)
                if item is None:
                    reasons.add("EVIDENCE_MISSING")
                    continue
                if item["subject_digest"] != digest:
                    reasons.add("EVIDENCE_BINDING_MISMATCH")
                if not item["observed_at"] <= now < item["expires_at"]:
                    reasons.add("EVIDENCE_NOT_CURRENT")
                if not item["passed"]:
                    reasons.add("EVIDENCE_FAILED")
    return {
        "schema": "tbc.receipt.v1", "action_digest": digest,
        "context_digest": bound_digest("tbc.context.v1", context),
        "evaluation_time": now, "affected_transition": action["transition"],
        "decision": "DENY" if reasons else "ALLOW", "reason_codes": sorted(reasons),
        "executed": False,
    }


def dumps_receipt(receipt: Mapping) -> str:
    """Validate/encode a receipt's shape, without authenticating its contents."""
    receipt = checked_copy(receipt)
    fields(receipt, "schema action_digest context_digest evaluation_time affected_transition decision reason_codes executed", "$")
    schema(receipt["schema"], "tbc.receipt.v1", "$.schema")
    for key in ("action_digest", "context_digest"):
        digest_field(receipt[key], "$." + key)
    integer(receipt["evaluation_time"], "$.evaluation_time")
    identifier(receipt["affected_transition"], "$.affected_transition")
    if receipt["executed"] is not False:
        raise InputError("NON_EXECUTING_RECEIPT", "$.executed")
    if receipt["decision"] not in ("ALLOW", "DENY"):
        raise InputError("DECISION", "$.decision")
    reasons = receipt["reason_codes"]
    if type(reasons) is not list:
        raise InputError("REASON_LIST", "$.reason_codes")
    if any(type(code) is not str or code not in _REASONS for code in reasons):
        raise InputError("REASON_CODE", "$.reason_codes")
    receipt["reason_codes"] = sorted(set(reasons))
    if (receipt["decision"] == "ALLOW") != (not reasons):
        raise InputError("DECISION_REASONS", "$.reason_codes")
    return encode(receipt).decode("utf-8")
