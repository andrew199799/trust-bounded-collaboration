"""Run with an installed wheel. All host facts here are synthetic, not credentials."""
from tbc import action_digest, dumps_receipt, evaluate, load_request

request = load_request('{"schema":"tbc.request.v1","action":{"actor":"demo-agent","transition":"propose","resource":"demo/contributor","payload":{"head":"abc"}}}')
digest = action_digest(request["action"])
# A real host authenticates the actor/issuer, decides policy and verifies evidence
# before constructing context. Never accept this context from an untrusted caller.
context = {
    "schema": "tbc.context.v1", "evaluation_time": 100,
    "authenticated_actor": "demo-agent", "action_digest": digest,
    "grant": {"id": "g", "issuer": "demo-host", "action_digest": digest,
              "not_before": 90, "expires_at": 110},
    "policy": {"id": "p", "version": "1", "digest": "sha256:" + "1" * 64,
               "action_digest": digest, "decision": "ALLOW", "not_before": 90,
               "expires_at": 110, "required_evidence_ids": ["e"]},
    "evidence": [{"id": "e", "subject_digest": digest, "verifier": "demo-host",
                  "observed_at": 90, "expires_at": 110, "passed": True}],
}
print(dumps_receipt(evaluate(request, context=context)))
# This receipt does not authorize execution. The host owns final enforcement,
# target-state/freshness checks, replay handling and public-output sanitization.
