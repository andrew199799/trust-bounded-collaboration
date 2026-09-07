"""A blocked consequential proposal and independently authorized safe work.

All facts are synthetic. No release or inspection actually occurs. The host owns
identity/authority/evidence verification, time and enforcement for each action.
"""
import json

from tbc import action_digest, dumps_receipt, evaluate, load_request


def scenarios():
    blocked = load_request('{"schema":"tbc.request.v1","action":{"actor":"demo-agent","transition":"promote-artifact","resource":"synthetic/artifact","payload":{"revision":"candidate-a"}}}')
    safe = load_request('{"schema":"tbc.request.v1","action":{"actor":"demo-agent","transition":"inspect-draft","resource":"synthetic/review-draft","payload":{"revision":"draft-1"}}}')
    cases = {}
    for name, request, required in [
        ("blocked_transition", blocked, ["conformance"]),
        ("independent_inspection", safe, []),
    ]:
        digest = action_digest(request["action"])
        # Each action gets independently established host facts. Safe work is
        # allowed by its own grant/policy, not by bypassing the other blocker.
        context = {
            "schema": "tbc.context.v1", "evaluation_time": 100,
            "authenticated_actor": "demo-agent", "action_digest": digest,
            "grant": {"id": name + "-grant", "issuer": "demo-authority",
                      "action_digest": digest, "not_before": 90, "expires_at": 110},
            "policy": {"id": name + "-policy", "version": "1",
                       "digest": "sha256:" + ("3" if required else "4") * 64,
                       "action_digest": digest, "decision": "ALLOW",
                       "not_before": 90, "expires_at": 110,
                       "required_evidence_ids": required},
            "evidence": [],
        }
        cases[name] = (request, context)
    return cases


def main():
    # Two independent calls, with no global mission/runtime STOP state.
    receipts = {name: evaluate(request, context=context)
                for name, (request, context) in scenarios().items()}
    assert receipts["blocked_transition"]["decision"] == "DENY"
    assert receipts["blocked_transition"]["reason_codes"] == ["EVIDENCE_MISSING"]
    assert receipts["independent_inspection"]["decision"] == "ALLOW"
    assert all(receipt["executed"] is False for receipt in receipts.values())
    print(json.dumps({"simulation": True, "cases": {
        name: json.loads(dumps_receipt(receipt)) for name, receipt in receipts.items()
    }}, sort_keys=True, separators=(",", ":")))
    # TBC does not schedule lanes, collect missing evidence or execute safe work.
    # Hosts decide which work is independent and enforce each result separately.


if __name__ == "__main__":
    main()
