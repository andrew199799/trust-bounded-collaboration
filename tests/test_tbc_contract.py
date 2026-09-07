"""Acceptance cases for the public contracts, written before the implementation."""
import copy
import hashlib
import json
from collections import UserDict

import pytest

from tbc import InputError, action_digest, dumps_receipt, evaluate, load_request


ACTION_BYTES = b'{"actor":"demo-agent","payload":{"head":"a","steps":[2,1]},"resource":"demo/contributor","transition":"proposal"}'
# Golden input is independent of TBC's encoder.
ACTION_DIGEST = "sha256:" + hashlib.sha256(b"tbc.action.v1\n" + ACTION_BYTES).hexdigest()


def facts():
    request = {"schema": "tbc.request.v1", "action": json.loads(ACTION_BYTES)}
    context = {
        "schema": "tbc.context.v1", "evaluation_time": 100,
        "authenticated_actor": "demo-agent", "action_digest": ACTION_DIGEST,
        "grant": {"id": "g", "issuer": "host", "action_digest": ACTION_DIGEST,
                  "not_before": 90, "expires_at": 110},
        "policy": {"id": "p", "version": "1", "digest": "sha256:" + "1" * 64,
                   "action_digest": ACTION_DIGEST, "decision": "ALLOW",
                   "not_before": 90, "expires_at": 110,
                   "required_evidence_ids": ["e"]},
        "evidence": [{"id": "e", "subject_digest": ACTION_DIGEST, "verifier": "host",
                      "observed_at": 90, "expires_at": 110, "passed": True}],
    }
    return request, context


def test_valid_binding_and_no_input_mutation():
    request, context = facts()
    before = copy.deepcopy((request, context))
    receipt = evaluate(request, context=context)
    assert receipt == {
        "schema": "tbc.receipt.v1", "action_digest": ACTION_DIGEST,
        "context_digest": CONTEXT_DIGEST, "evaluation_time": 100,
        "affected_transition": "proposal", "decision": "ALLOW", "reason_codes": [], "executed": False,
    }
    assert (request, context) == before
    assert dumps_receipt(receipt).encode("utf-8") == RECEIPT_BYTES
    assert action_digest(request["action"]) == ACTION_DIGEST
    assert evaluate(UserDict(request), context=UserDict(context)) == receipt


@pytest.mark.parametrize("field", ["actor", "resource", "transition", "payload"])
def test_action_mutation_invalidates_all_old_facts(field):
    request, context = facts()
    request["action"][field] = {"head": "b"} if field == "payload" else "changed"
    receipt = evaluate(request, context=context)
    assert receipt["decision"] == "DENY"
    assert "ACTION_BINDING_MISMATCH" in receipt["reason_codes"]
    assert "POLICY_BINDING_MISMATCH" in receipt["reason_codes"]
    assert receipt["executed"] is False


def test_old_policy_denies_with_current_context_and_grant():
    request, context = facts()
    request["action"]["payload"]["head"] = "new-sha"
    current = action_digest(request["action"])
    context["action_digest"] = context["grant"]["action_digest"] = current
    receipt = evaluate(request, context=context)
    assert receipt["decision"] == "DENY"
    assert receipt["reason_codes"] == ["POLICY_BINDING_MISMATCH"]


@pytest.mark.parametrize("parent,field,value,code", [
    (None, "authenticated_actor", "other", "ACTOR_MISMATCH"),
    (None, "grant", None, "AUTHORITY_MISSING"),
    (None, "policy", None, "POLICY_MISSING"),
    (None, "evidence", [], "EVIDENCE_MISSING"),
    ("grant", "action_digest", "sha256:" + "0" * 64, "ACTION_BINDING_MISMATCH"),
    ("grant", "expires_at", 100, "AUTHORITY_NOT_CURRENT"),
    ("grant", "not_before", 101, "AUTHORITY_NOT_CURRENT"),
    ("policy", "expires_at", 100, "POLICY_NOT_CURRENT"),
    ("policy", "not_before", 101, "POLICY_NOT_CURRENT"),
    ("policy", "decision", "DENY", "POLICY_DENIED"),
    ("evidence", "passed", False, "EVIDENCE_FAILED"),
    ("evidence", "observed_at", 101, "EVIDENCE_NOT_CURRENT"),
    ("evidence", "expires_at", 100, "EVIDENCE_NOT_CURRENT"),
    ("evidence", "subject_digest", "sha256:" + "0" * 64, "EVIDENCE_BINDING_MISMATCH"),
])
def test_negative_facts(parent, field, value, code):
    request, context = facts()
    target = context if parent is None else context[parent]
    if parent == "evidence":
        target = target[0]
    target[field] = value
    receipt = evaluate(request, context=context)
    assert receipt["decision"] == "DENY"
    assert code in receipt["reason_codes"]


def test_policy_owns_requirements_and_no_global_stop():
    request, context = facts()
    context["policy"]["required_evidence_ids"] = ["missing"]
    blocked = evaluate(request, context=context)
    assert blocked["reason_codes"] == ["EVIDENCE_MISSING"]
    context["required_evidence_ids"] = []
    with pytest.raises(InputError):
        evaluate(request, context=context)
    allowed_request, allowed_context = facts()
    assert evaluate(allowed_request, context=allowed_context)["decision"] == "ALLOW"
    del context["required_evidence_ids"]
    assert evaluate(request, context=context) == blocked


def test_normalization_and_payload_array_order():
    request, context = facts()
    extra = {**context["evidence"][0], "id": "a"}
    context["evidence"].append(extra)
    context["policy"]["required_evidence_ids"].append("a")
    receipt = evaluate(request, context=context)
    context["evidence"].reverse()
    context["policy"]["required_evidence_ids"].reverse()
    assert dumps_receipt(evaluate(request, context=context)) == dumps_receipt(receipt)
    changed = copy.deepcopy(request["action"])
    changed["payload"]["steps"].reverse()
    assert action_digest(changed) != ACTION_DIGEST
    context["policy"]["required_evidence_ids"] = []
    assert evaluate(request, context=context)["context_digest"] != receipt["context_digest"]


@pytest.mark.parametrize("change", [
    lambda r,c: r.update(schema="tbc.request.v2"),
    lambda r,c: r.update(trusted=True),
    lambda r,c: r["action"].update(trusted=True),
    lambda r,c: r["action"].update(actor=""),
    lambda r,c: r["action"].update(payload=[]),
    lambda r,c: c.update(schema="tbc.context.v2"),
    lambda r,c: c.update(evaluation_time=True),
    lambda r,c: c.update(evaluation_time="100"),
    lambda r,c: c.update(action_digest="not-a-digest"),
    lambda r,c: c["grant"].update(issuer=""),
    lambda r,c: c["grant"].update(not_before=110),
    lambda r,c: c["policy"].update(decision="unknown"),
    lambda r,c: c["policy"].pop("action_digest"),
    lambda r,c: c["policy"].pop("required_evidence_ids"),
    lambda r,c: c["policy"].update(required_evidence_ids=["e", "e"]),
    lambda r,c: c["evidence"].append(c["evidence"][0].copy()),
    lambda r,c: c["evidence"][0].update(passed="true"),
    lambda r,c: c["evidence"][0].update(observed_at=110),
])
def test_malformed_facts_are_input_errors(change):
    request, context = facts()
    change(request, context)
    with pytest.raises(InputError):
        evaluate(request, context=context)


@pytest.mark.parametrize("value", [1.0, float("nan"), float("inf"), 2**53, -(2**53),
                                       "\ud800", {1: "value"}, {"\udfff": "value"}, (1, 2)])
def test_restricted_json_values(value):
    action = facts()[0]["action"]
    action["payload"] = {"value": value}
    with pytest.raises(InputError):
        action_digest(action)


@pytest.mark.parametrize("text", ['{"schema":"x","schema":"y"}', '{"a":{"x":1,"x":2}}',
                                  'NaN', 'Infinity', '1.0', '{}', '\ufeff{}', '[]', '{'])
def test_bad_json(text):
    with pytest.raises(InputError):
        load_request(text)


def test_request_roundtrip_and_sanitized_errors():
    request, context = facts()
    assert load_request(json.dumps(request)) == request
    with pytest.raises(InputError) as exc:
        load_request('{"private-value-do-not-echo":1}')
    assert "private-value-do-not-echo" not in str(exc.value)
    assert exc.value.code and exc.value.path.startswith("$")
    request["action"]["payload"] = {"private-value-do-not-echo": 1.1}
    with pytest.raises(InputError) as exc:
        evaluate(request, context=context)
    assert "private-value-do-not-echo" not in str(exc.value)


def test_cycles_and_safety_limits_fail_closed():
    request, context = facts()
    request["action"]["payload"]["cycle"] = request
    with pytest.raises(InputError):
        evaluate(request, context=context)
    action = facts()[0]["action"]
    action["payload"] = {"large": "a" * (1024 * 1024 + 1)}
    with pytest.raises(InputError):
        action_digest(action)
    with pytest.raises(InputError):
        load_request('[' * 1000 + '0' + ']' * 1000)
    with pytest.raises(InputError):
        load_request(' ' * (1024 * 1024 + 1))


def test_unicode_and_escaping_golden():
    action = facts()[0]["action"]
    action["payload"] = {"中": ["é", "😀", '"\\\n\t\b\f\r/', None, True, False, 9007199254740991, -9007199254740991]}
    golden = r'{"actor":"demo-agent","payload":{"中":["é","😀","\"\\\n\t\b\f\r/",null,true,false,9007199254740991,-9007199254740991]},"resource":"demo/contributor","transition":"proposal"}'.encode("utf-8")
    assert action_digest(action) == "sha256:" + hashlib.sha256(b"tbc.action.v1\n" + golden).hexdigest()
    action["payload"]["中"][0] = "e\u0301"
    assert action_digest(action) != "sha256:" + hashlib.sha256(b"tbc.action.v1\n" + golden).hexdigest()


@pytest.mark.parametrize("field,value", [("executed", True), ("decision", "unknown"),
                                        ("schema", "tbc.receipt.v2"), ("extra", 1)])
def test_receipt_validation(field, value):
    receipt = evaluate(*facts()[:1], context=facts()[1])
    receipt[field] = value
    with pytest.raises(InputError):
        dumps_receipt(receipt)


def test_receipt_reason_normalization():
    request, context = facts()
    context["grant"] = None
    receipt = evaluate(request, context=context)
    receipt["reason_codes"] *= 2
    assert json.loads(dumps_receipt(receipt))["reason_codes"] == ["AUTHORITY_MISSING"]


# Fixed golden values captured before the implementation existed.
CONTEXT_BYTES = b'{"action_digest":"sha256:b9c96866f2a12024838e457dde619465cb8791794335f58bd92b8237df58f799","authenticated_actor":"demo-agent","evaluation_time":100,"evidence":[{"expires_at":110,"id":"e","observed_at":90,"passed":true,"subject_digest":"sha256:b9c96866f2a12024838e457dde619465cb8791794335f58bd92b8237df58f799","verifier":"host"}],"grant":{"action_digest":"sha256:b9c96866f2a12024838e457dde619465cb8791794335f58bd92b8237df58f799","expires_at":110,"id":"g","issuer":"host","not_before":90},"policy":{"action_digest":"sha256:b9c96866f2a12024838e457dde619465cb8791794335f58bd92b8237df58f799","decision":"ALLOW","digest":"sha256:1111111111111111111111111111111111111111111111111111111111111111","expires_at":110,"id":"p","not_before":90,"required_evidence_ids":["e"],"version":"1"},"schema":"tbc.context.v1"}'
CONTEXT_DIGEST = 'sha256:6d87503596977eaf97b276059c2c4cd1f4d1ac05779cdee19f8ed63cd23d4cca'
RECEIPT_BYTES = b'{"action_digest":"sha256:b9c96866f2a12024838e457dde619465cb8791794335f58bd92b8237df58f799","affected_transition":"proposal","context_digest":"sha256:6d87503596977eaf97b276059c2c4cd1f4d1ac05779cdee19f8ed63cd23d4cca","decision":"ALLOW","evaluation_time":100,"executed":false,"reason_codes":[],"schema":"tbc.receipt.v1"}'
