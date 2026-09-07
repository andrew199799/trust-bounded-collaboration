# Current Task Context

Canonical repository: [andrew199799/trust-bounded-collaboration](https://github.com/andrew199799/trust-bounded-collaboration).

Current task: [Phase 4 — Thin Vertical Implementation & Distribution Baseline (#27)](https://github.com/andrew199799/trust-bounded-collaboration/issues/27), using the frozen architecture in #26. Read the current Issue and Human review before acting; they supersede this continuity note.

The authorized slice is the complete MIT license, attribution/name preflight,
acceptance tests, a small standard-library-only `tbc` package, offline repository
demo, wheel/sdist and clean-install validation, Python 3.11–3.14 CI and a minimal
Quick Start. Authentication, policy ownership, raw evidence verification, live
collection/enforcement and execution remain with the host/platform.

Work from exact canonical main in one isolated task workspace. Push only to the
Agent fork and use exactly one canonical Draft PR; iterate ordinary failures in
that PR, then stop for Human / ChatGPT implementation review. Follow AGENTS.md and
CONTRIBUTING.md. No private-source copying, ruleset change, merge, tag, release,
package publication, runtime or broad historical cleanup is authorized.

Run the tests/build/clean-install checks documented in README.md. Record actual
matrix results, exact PR head SHA and first-run time; do not promote unrun checks
to PASS. Legacy `tbao` remains reference-only and outside the new distribution.
