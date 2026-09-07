# TBAO v0.1 Public Roadmap

> Historical v0.1 reference. For the current purpose and scope, read the
> [TBC vNext positioning](vnext-positioning.zh-en.md). This roadmap is not a current
> runtime or platform implementation commitment.

## Current v0.1 Status

TBAO v0.1 is a public manifesto, framework spec, mock-only static demo, and local-only mock Action Policy Kernel v0.1. It is not the full TBAO product, not production-ready, and not an execution runtime.

The current public material explains the Action Spine shape for inspectable agent action proposals:

```text
intent
  -> proposed_action
  -> risk_tier
  -> required_confirmation
  -> execution_status
  -> audit_note
```

The local mock Action Policy Kernel makes risk classification, approval gating, and ledger recording testable without enabling real execution.

## What Is Intentionally Public

- Core manifesto language around human meaning sovereignty.
- Framework concepts for knowledge, advisory, and action governance.
- Mock-only Action Spine documentation.
- Static fixture semantics for risk tier, confirmation token, audit note, and mandatory non-execution.
- Local-only mock Action Policy Kernel v0.1 semantics for risk classification, approval tickets, and ledger records.
- Contributor discussion material for serious framework critique.

## What Remains Protected / Outside This Repo

- Private implementation details and source material.
- Proprietary or sensitive architecture, prompts, workflows, data, or operational records.
- Runtime behavior, real integrations, credentials, deployment material, and execution-capable systems.
- Business-sensitive material and personal data.

## Near-Term Public Roadmap

- Tighten public terminology and bilingual framing.
- Refine static and local mock Action Spine examples without adding execution.
- Tighten risk-tier, approval-ticket, and ledger semantics through critique.
- Invite contributor discussion around authority boundaries and review language.
- Keep documentation navigation concise and reviewable.
- Avoid runtime expansion.

## Possible Future Public Reference Material

Future public material may be extracted only after it is abstracted, non-executing, non-proprietary, and non-sensitive.

Possible candidates include:

- higher-level framework diagrams;
- generalized governance patterns;
- terminology refinements;
- static examples that do not reveal implementation details;
- public discussion notes that preserve the mock-only boundary.

## Non-Goals

- No production runtime.
- No live API.
- No scheduler.
- No worker.
- No credentials.
- No real file writes or deletion.
- No real funds, payments, or trades.
- No external side effects.
- No productization language or production-readiness framing.
- No expansion into scenario-specific product work unless explicitly scoped later.
