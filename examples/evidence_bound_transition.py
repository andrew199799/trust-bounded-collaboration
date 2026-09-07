"""Synthetic release eligibility checks; nothing is built, deployed or released.

The host verifies authority, policy, evidence and time before supplying context.
The fixed facts below simulate that completed verification; TBC does not perform it.
"""
from copy import deepcopy
import json

from tbc import action_digest, dumps_receipt, evaluate, load_request


def scenarios():
    request = load_request('{"schema":"tbc.request.v1","action":{"actor":"demo-maintainer","transition":"release-artifact","resource":"synthetic/artifact","payload":{"revision":"candidate-a"}}}')
    digest = action_digest(request["action"])
    context = {
        "schema": "tbc.context.v1", "evaluation_time": 100,
        "authenticated_actor": "demo-maintainer", "action_digest": digest,
        "grant": {"id": "release-grant", "issuer": "demo-authority",
                  "action_digest": digest, "not_before": 90, "expires_at": 110},
        "policy": {"id": "release-policy", "version": "1",
                   "digest": "sha256:" + "2" * 64, "action_digest": digest,
                   "decision": "ALLOW", "not_before": 90, "expires_at": 110,
                   "required_evidence_ids": ["conformance"]},
        "evidence": [{"id": "conformance", "subject_digest": digest,
                      "verifier": "demo-host", "observed_at": 90,
                      "expires_at": 110, "passed": True}],
    }
    missing, stale, failed, mismatched = (deepcopy(context) for _ in range(4))
    missing["evidence"] = []
    stale["evidence"][0]["expires_at"] = 100  # Exclusive expiry, at evaluation time.
    failed["evidence"][0]["passed"] = False
    mismatched["evidence"][0]["subject_digest"] = "sha256:" + "0" * 64

    changed = deepcopy(request)
    changed["action"]["payload"]["revision"] = "candidate-b"
    current_digest = action_digest(changed["action"])
    old_policy = deepcopy(context)
    # Hypothetical host re-verification of authority for candidate-b does not
    # make candidate-a's policy or observations applicable to candidate-b.
    old_policy["action_digest"] = old_policy["grant"]["action_digest"] = current_digest
    old_evidence = deepcopy(old_policy)
    old_evidence["policy"]["action_digest"] = current_digest
    # Required evidence comes only from the exact-action-bound ALLOW policy.
    # Unbound policy denies first; rebinding policy alone still leaves stale binding.
    return {
        "ready_transition": (request, context),
        "missing_evidence": (request, missing),
        "stale_evidence": (request, stale),
        "failed_evidence": (request, failed),
        "mismatched_evidence": (request, mismatched),
        "changed_action_old_policy": (changed, old_policy),
        "changed_action_old_evidence": (changed, old_evidence),
    }


def main():
    receipts = {name: evaluate(request, context=context)
                for name, (request, context) in scenarios().items()}
    expected = {
        "ready_transition": [], "missing_evidence": ["EVIDENCE_MISSING"],
        "stale_evidence": ["EVIDENCE_NOT_CURRENT"], "failed_evidence": ["EVIDENCE_FAILED"],
        "mismatched_evidence": ["EVIDENCE_BINDING_MISMATCH"],
        "changed_action_old_policy": ["POLICY_BINDING_MISMATCH"],
        "changed_action_old_evidence": ["EVIDENCE_BINDING_MISMATCH"],
    }
    for name, reasons in expected.items():
        assert receipts[name]["reason_codes"] == reasons
        assert receipts[name]["decision"] == ("DENY" if reasons else "ALLOW")
        assert receipts[name]["executed"] is False
    print(json.dumps({"simulation": True, "cases": {
        name: json.loads(dumps_receipt(receipt)) for name, receipt in receipts.items()
    }}, sort_keys=True, separators=(",", ":")))
    # Receipts are unsigned evaluation records, not release tokens. A real host
    # must enforce at the transition, recheck state/freshness and prevent replay.


if __name__ == "__main__":
    main()
