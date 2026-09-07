"""Synthetic approval-bound deletion proposal; no file is read or deleted.

The host has already authenticated the actor and approver and verified approval
for this exact proposal. Constructing a Grant illustrates that trust boundary;
it is not approval collection or proof that a Human approved anything.
"""
from copy import deepcopy
import json

from tbc import action_digest, dumps_receipt, evaluate, load_request


def scenarios():
    request = load_request('{"schema":"tbc.request.v1","action":{"actor":"demo-agent","transition":"delete-document","resource":"synthetic/document-a","payload":{"revision":"draft-1"}}}')
    digest = action_digest(request["action"])
    # Synthetic stand-in for the host's already verified exact-action approval.
    # Never mint this fact merely because an untrusted request asks for it.
    context = {
        "schema": "tbc.context.v1", "evaluation_time": 100,
        "authenticated_actor": "demo-agent", "action_digest": digest,
        "grant": {"id": "approval-1", "issuer": "demo-human-authority",
                  "action_digest": digest, "not_before": 90, "expires_at": 110},
        "policy": {"id": "deletion-policy", "version": "1",
                   "digest": "sha256:" + "1" * 64, "action_digest": digest,
                   "decision": "ALLOW", "not_before": 90, "expires_at": 110,
                   "required_evidence_ids": []},
        "evidence": [],
    }
    absent = deepcopy(context)
    absent["grant"] = None
    changed = deepcopy(request)
    changed["action"]["payload"]["revision"] = "draft-2"
    changed_context = deepcopy(context)
    changed_digest = action_digest(changed["action"])
    # Even if the host independently verifies policy for the changed proposal,
    # the earlier Human approval cannot be carried over to the new revision.
    changed_context["action_digest"] = changed_digest
    changed_context["policy"]["action_digest"] = changed_digest
    return {
        "approved_action": (request, context),
        "approval_absent": (request, absent),
        "changed_action_old_grant": (changed, changed_context),
    }


def main():
    receipts = {name: evaluate(request, context=context)
                for name, (request, context) in scenarios().items()}
    assert receipts["approved_action"]["decision"] == "ALLOW"
    assert receipts["approval_absent"]["reason_codes"] == ["AUTHORITY_MISSING"]
    assert receipts["changed_action_old_grant"]["reason_codes"] == ["ACTION_BINDING_MISMATCH"]
    assert all(receipt["executed"] is False for receipt in receipts.values())
    print(json.dumps({"simulation": True, "cases": {
        name: json.loads(dumps_receipt(receipt)) for name, receipt in receipts.items()
    }}, sort_keys=True, separators=(",", ":")))
    # ALLOW is only an evaluation. The host owns final enforcement, target-state
    # rechecks, replay handling and output sanitization. Nothing executes here.


if __name__ == "__main__":
    main()
