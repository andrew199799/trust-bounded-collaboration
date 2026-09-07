# Runnable TBC examples

Build and install the wheel using the root [Quick Start](../README.md#quick-start),
then run these commands from the checkout (or unpacked source distribution).
Python 3.11–3.14 is required. All examples are synthetic, offline and credential-free;
they print deterministic evaluation receipts and never perform the proposed action.

| Use case | Command | Expected behavior |
| --- | --- | --- |
| Repository authority | `python -m tbc demo repository --json` | Contributor proposal ALLOW; canonical mutations DENY; independent inspection ALLOW. |
| Approval-bound consequential action | `python examples/approval_bound_action.py` | Approved deletion proposal ALLOW; absent approval or changed revision with old Grant DENY. No file is deleted. |
| Evidence-bound transition/release | `python examples/evidence_bound_transition.py` | Bound current facts ALLOW; missing, stale, failed or mismatched evidence DENY. Changed action invalidates old Policy/evidence. Nothing is released. |
| Scoped blocker and independent safe work | `python examples/scoped_blocker.py` | Consequential proposal DENY; separately authorized inspection ALLOW. Neither action executes. |

The three scripts assert their expected results and emit `simulation=true` with
named cases. That output wrapper and the scripts' helper functions are examples,
not a new stable schema, API or CLI. Expected DENY is a successful demonstration.
The existing [compact integration snippet](tbc_integration.py) remains an additional
four-function starting point: `python examples/tbc_integration.py` prints one ALLOW receipt.

## Host trust and enforcement

Only `load_request`, `action_digest`, `evaluate` and `dumps_receipt` are used from TBC.
The host must authenticate identities, verify exact-action approval and evidence,
establish policy and supply time **before** constructing context. The fixed issuers,
policy digests and observations in these examples are placeholders, not credentials
or proof of verification. Never let an untrusted caller supply authority context.

TBC does not collect Human approval, authenticate approvers, verify an external test
run, decide which work is independent or enforce a release. ALLOW is an unsigned
evaluation record, not an execution token. The host owns final enforcement, fresh
target-state checks, replay handling and public-output sanitization. Every receipt
has `executed=false`; no runtime or scheduler is demonstrated.

## Legacy v0.1 reference material

- `action_requests/*.json`: mock `ActionRequest` fixtures for the separate legacy
  `src/tbao/` regression tests. They are **not** `tbc.request.v1` inputs and must not
  be passed to `load_request`.
- `action-spine-mvp/README.md`: historical mock-only design placeholder, not a
  current runnable example or a commitment to implement a runtime.

Those files remain in place for reference. They are excluded from the current
wheel/source distribution. Start with the table above for the current library.
