# Capability disposition before 1.0 freeze

This is an integration boundary map for the current four-function library, not a
roadmap commitment or a new schema. The audit uses the public implementation,
contract tests and synthetic examples only. No private source was needed or read.

| Capability | Disposition | Public evidence and boundary |
| --- | --- | --- |
| Exact-action binding | IN_1_0_CORE | [Contract tests](../tests/test_tbc_contract.py) change actor, resource, transition and payload and reject old bindings. The host must encode decision-relevant details in the action. |
| Authority binding | IN_1_0_CORE | [Approval example](../examples/approval_bound_action.py) distinguishes a current exact-action Grant, absent approval and an old Grant. Authentication and approval collection remain host-owned. |
| Policy/evidence binding | IN_1_0_CORE | [Transition example](../examples/evidence_bound_transition.py) requires a bound current ALLOW Policy and its required passing evidence; missing/stale/failed/mismatched observations deny. TBC does not verify external observations. |
| Deterministic receipts | IN_1_0_CORE | [Golden-byte tests](../tests/test_tbc_contract.py) cover action/context digests and receipt encoding. These are unsigned records, not authenticated attestations or execution tokens. |
| Repository authority example | PROJECT_POLICY_OR_RULE_PACK | The [fixed repository demo](../examples/README.md) ships today, but contributor/canonical roles and allowed operations are example policy. Live identity, permission and state collection/enforcement belong to the host, not generic Core. This classification does not remove the demo. |
| Scoped blocking / independent evaluation | IN_1_0_CORE | [Scoped-blocker tests](../tests/test_tbc_examples.py) evaluate blocked and safe work repeatedly in either order. Each call is independent; Core has no mission state, lane scheduler or independence detector. |
| Change-surface / entropy-style risk observation | PUBLIC_EXTENSION_CANDIDATE | A future generic observation exchange could help hosts reuse verified change observations. Current binding tests establish no risk-model validity or need for a new Core schema. Scoring, formulas, weights, thresholds and project mappings stay project policy. |
| Assumption governance | PROJECT_POLICY_OR_RULE_PACK | A host may decide which assumptions require evidence under its own Policy. Existing evidence checks can consume that host decision, but do not track assumptions, determine their truth or manage a workflow. |
| Outcome calibration / rule promotion | DEFER_INSUFFICIENT_EVIDENCE | Current tests establish evaluation behavior, not improved downstream outcomes or safe adaptive policy changes. No public calibration dataset or validated promotion procedure is established by this slice. |

## Change-risk decision

Keep change-risk observation **outside 1.0 Core**. The extension classification is
an investigation candidate, not an implemented feature or a requirement to add an
API. No observation schema, risk score, formula, weight, threshold, path map, hot
zone, domain vocabulary or implementation is proposed or imported here.

Before defining a public extension, demonstrate reusable observations in multiple
public host integrations, explicit subject/freshness semantics and measurable value
over host-owned evidence passed through today's contract. A risk assessment alone
must never mint authority or bypass required evidence. Local interpretation and
consequence policy remain with each project.

## Freeze recommendation

Keep the current API, schemas, CLI, version and runtime dependencies unchanged.
The [four runnable use cases](../examples/README.md) cover the promised generic
binding behaviors. No finding requires Core expansion. Revisit extension candidates
only with public adoption evidence; changes to a frozen boundary need a separate
Human architecture decision. Do not treat deferred capabilities as delivered features.
