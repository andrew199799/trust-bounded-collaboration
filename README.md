# Trust-Bounded Collaboration

Canonical repository: [andrew199799/trust-bounded-collaboration](https://github.com/andrew199799/trust-bounded-collaboration). For the fork → branch → test → PR workflow, see [CONTRIBUTING.md](CONTRIBUTING.md). The v0.1 reference described below retains its historical TBAO name.

Trust-Bounded Agent OS is a public framework and local mock prototype for making AI agent actions inspectable, bounded, confirmable, and auditable before execution.

TBAO does not restrict the growth of intelligence. It restricts uncontrolled agent power.

**Status:** `v0.1 public draft with local mock Action Policy Kernel`  
**Current scope:** conceptual framework, governance spine, mock-only Action Spine design, and local-only Action Policy Kernel prototype  
**Production readiness:** not production-ready

## Public Identity

TBAO protects **human meaning sovereignty** by separating what an agent can infer from what a human has authorized.

Its governance model has three connected surfaces:

```text
Knowledge Governance -> Advisory Governance -> Action Governance
```

The current implementation focus is **Action Spine** and its first local mock enforcement slice, **Action Policy Kernel v0.1**. The broader framework also preserves provenance, challengeability, confirmation status, and recovery paths. The present repository remains non-production, local-only, mock-only, and non-executing.

## Core Doctrine

```text
1. Human beings retain sovereignty over meaning.
2. Human knowledge, experience, and preferences must retain provenance, boundaries, and confirmation status.
3. AI may interpret, advise, and act only within authorized boundaries.
4. Judgment-shaping advice must be source-grounded, challengeable, verifiable, and downgradeable.
5. Side-effectful action must be decidable, traceable, and recoverable.
```
<img width="1196" height="1315" alt="image" src="https://github.com/user-attachments/assets/6e5d4a49-04cf-4e9a-8d9c-281437156c4e" />

## Why This Exists

AI agents are becoming capable of acting across files, tools, APIs, workflows, and external systems. The core risk is not only model intelligence. It is also unsafe action boundaries, unclear authority, missing confirmation, weak auditability, and over-trusting autonomous behavior.

TBAO starts from a simple position: humans retain sovereignty over meaning, authority, and responsibility. Agents may interpret, propose, and assist, but side-effectful action should be structured for review before anything real happens.

The project keeps its ambition clear: help AI systems mature toward bounded, reviewable, recoverable action. The current repository does not provide that as a production runtime.

## Project Value

- Gives developers a shared language for discussing agent action boundaries before implementation.
- Keeps public examples self-contained, without depending on private implementations.
- Shows how intent, proposed action, risk, confirmation, execution status, and audit notes can be inspected before action.
- Adds a local mock policy kernel that makes risk classification, approval gating, and ledger recording testable without enabling real-world execution.
- Helps researchers and builders discuss trust-bounded agent governance without pretending a runtime exists.
- Gives contributors a public entry point for small, reviewable improvements.
- Keeps human meaning sovereignty and controlled agent power at the center.

## Core Idea

The central concept is the **Action Spine**: a minimal structure that turns an agent's intent into an inspectable proposal before execution.

```text
ActionRequest
  -> RiskClassifier
  -> PolicyDecision
  -> ApprovalTicket
  -> ActionLedger
```

The current local mock kernel demonstrates this path as policy code. It does not execute actions, call services, schedule work, operate as a production runtime, or create real external side effects.

## What Is Included Now

- Conceptual framework for trust-bounded agent governance.
- Governance spine for knowledge, advice, and action boundaries.
- Mock-only Action Spine MVP design.
- Local mock Action Policy Kernel v0.1 under `src/tbao/`.
- L0-L4 action request examples under `examples/action_requests/`.
- Pytest coverage for risk classification, approval ticket validation, policy decisions, and ledger append behavior.
- Human-readable risk rules mirror under `configs/risk_rules.v0.1.yaml`.
- Static mock proposal example with `execution_status: not_executed`.
- v0.1 public manifesto, static demo release note, and Action Policy Kernel release note.
- Public roadmap and discussion guide.
- Non-executable reference skeleton.
- Mermaid diagram sources.
- Collaboration and scope-control baseline for narrow public PRs.

## What Is Not Included

TBAO v0.1 is not production-ready and does not include:

- runtime execution;
- live API integration;
- scheduler;
- worker;
- credentials;
- real file writes or deletion;
- real funds, payments, or trades;
- real email or external message sending;
- production environment mutation;
- trading, health, legal, or personal-data runtime scenarios.

It is also not a general agent framework, a content moderation system, a generic permission platform, or a claim that AI can be given real conscience.

## Current Demo Status

v0.1 is in public draft / local mock prototype stage.

The current repository includes both static Action Spine documentation and a local-only, mock-only Action Policy Kernel. The kernel demonstrates how a proposed action can be represented, classified, gated by approval semantics, and recorded in an in-memory ledger without enabling real execution.

No production runtime exists. No live API integration, scheduler, worker, credential path, or external side-effect path exists.

## Repository Map

- [`docs/one-page-summary.zh-en.md`](docs/one-page-summary.zh-en.md): concise bilingual public summary.
- [`docs/position-paper.zh-en.md`](docs/position-paper.zh-en.md): v0.1 position paper and design stance.
- [`docs/principles.zh-en.md`](docs/principles.zh-en.md): core principles behind TBAO.
- [`docs/glossary.zh-en.md`](docs/glossary.zh-en.md): bilingual terminology reference.
- [`docs/action-spine-mvp.zh-en.md`](docs/action-spine-mvp.zh-en.md): Action Spine MVP design and safety boundary.
- [`docs/action-policy-kernel-v0.1.md`](docs/action-policy-kernel-v0.1.md): local mock Action Policy Kernel explanation.
- [`docs/roadmap.md`](docs/roadmap.md): public-framework roadmap.
- [`docs/discussion-guide.md`](docs/discussion-guide.md): contributor discussion guide.
- [`docs/release-notes/v0.1-public-manifesto-static-demo.md`](docs/release-notes/v0.1-public-manifesto-static-demo.md): v0.1 public manifesto and static demo release note.
- [`docs/release-notes/v0.1-action-policy-kernel.md`](docs/release-notes/v0.1-action-policy-kernel.md): local mock Action Policy Kernel release note.
- [`docs/action-spine-reference-skeleton.md`](docs/action-spine-reference-skeleton.md): non-executable Action Spine pseudo-interface skeleton.
- [`configs/risk_rules.v0.1.yaml`](configs/risk_rules.v0.1.yaml): human-readable risk rule mirror.
- [`examples/action_requests/`](examples/action_requests/): L0-L4 mock action request examples.
- [`src/tbao/`](src/tbao/): local-only, mock-only Action Policy Kernel primitives.
- [`tests/`](tests/): pytest coverage for the local mock kernel.
- [`docs/diagrams/action-spine-flow.mmd`](docs/diagrams/action-spine-flow.mmd): Mermaid source for the Action Spine flow.
- [`docs/diagrams/public-protected-boundary.mmd`](docs/diagrams/public-protected-boundary.mmd): Mermaid source for the public/protected repository boundary.
- [`docs/non-goals.zh-en.md`](docs/non-goals.zh-en.md): explicit non-goals and scope limits.
- [`docs/development-log/action-spine-static-mock-example.md`](docs/development-log/action-spine-static-mock-example.md): static mock proposal example.
- [`docs/development-log/phase-1-release-note.md`](docs/development-log/phase-1-release-note.md): Phase 1 collaboration baseline summary.
- [`AGENTS.md`](AGENTS.md): vendor-neutral AI Agent execution contract.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): public fork, branch, test, and PR guide.

## Historical v0.1 Roadmap Snapshot

Current collaboration work is tracked in [Issue #23](https://github.com/andrew199799/trust-bounded-collaboration/issues/23), under [Issue #22](https://github.com/andrew199799/trust-bounded-collaboration/issues/22). The phases below describe the earlier v0.1 work.

- **Phase 1:** completed collaboration baseline and static mock.
- **Phase 2:** public narrative and README framing.
- **Phase 3:** Action Spine static demo.
- **Phase 4:** local mock Action Policy Kernel v0.1.
- **Next:** documentation tightening, example refinement, and public-safe critique of risk/approval semantics.

## Safety Boundary

The current repository boundary is:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

Any future work that could create side effects, access credentials, call live systems, write real files, or execute actions requires explicit human confirmation and a separate scoped review.

## Final Test

Every future addition must answer:

```text
Does it protect human meaning sovereignty?
Does it preserve provenance, boundaries, and confirmation status?
Does it make judgment-shaping advice reviewable and downgradeable?
Does it make side-effectful action decidable, traceable, and recoverable?
```

If not, it should not enter the TBAO main line.

## License

This repository is a public experimental draft under the Apache License 2.0. Documentation and examples may be refined as the project boundary becomes clearer.
