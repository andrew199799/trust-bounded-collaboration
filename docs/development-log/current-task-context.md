# Current Task Context

## Project and authority

Trust-Bounded Collaboration — canonical repository: [andrew199799/trust-bounded-collaboration](https://github.com/andrew199799/trust-bounded-collaboration).

Current task: [v1.0 Phase 1 — Multi-Agent Fork/PR Collaboration Baseline (#23)](https://github.com/andrew199799/trust-bounded-collaboration/issues/23), under [umbrella #22](https://github.com/andrew199799/trust-bounded-collaboration/issues/22). Read the current Issue body and applicable Human comments before acting; this file is continuity context, not additional authority.

## Scope

- Establish native Git/GitHub collaboration: canonical read/fetch → isolated Agent workspace → contributor fork branch → canonical Draft PR → Human review.
- Keep the execution contract vendor-neutral and the contributor path familiar. Apply the public artifact rule and bounded hygiene to directly touched current-facing docs.
- Start each Agent/task from exact current canonical `main` in an isolated workspace. Verify API/transport identity, fork parent, remote roles, and permissions before mutation.
- Add a custom guard only if evidence shows native permissions and documentation are insufficient. Canonical read-only permission is sufficient denial evidence; no dangerous write probe is required.
- Phase 1 authorizes one executing Agent fork if needed and exactly one canonical Draft PR. Use the PR for intermediate progress and the Issue for the final sanitized checkpoint.

## Boundaries and validation

No direct canonical push, permission changes, merge, tag, release, private-source copying, broad v1 implementation, or repository-wide historical rewrite. Every GitHub artifact must be assumed public before writing; follow [AGENTS.md](../../AGENTS.md) and [CONTRIBUTING.md](../../CONTRIBUTING.md).

The existing v0.1 reference remains local-only, mock-only, non-executing, and not production-ready, with no real credentials, funds, or external side effects.

Run `python3 -m pytest -q` and `git diff --check`. Verify the PR base/head repository, branch, and exact SHA; test updates only on the contributor branch. Record available CI results accurately, including when no workflow exists. Human maintainers retain final merge/release authority.
