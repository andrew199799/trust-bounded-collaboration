# Changelog

## 1.0.0

Repository contract changes for `1.0.0` are listed below. Tagging, GitHub Release
and package publication are separate Human-controlled steps.

- Four-function Python API: request validation, exact action digest, pure scoped
  evaluation and deterministic unsigned receipt serialization.
- Independent Grant and Policy action binding; required evidence belongs to the
  bound Policy. A blocked action does not change an independent evaluation.
- Restricted UTF-8 JSON profile and domain-separated SHA-256 digests, with fixed
  golden tests and fail-closed malformed-input handling.
- Credential-free offline repository demo, approval-bound action, evidence-bound
  transition/release and scoped-blocker examples, plus a compact integration snippet.
- Current/legacy example routing and 127 contract/demo/legacy tests; shipped current
  examples run against a clean offline wheel installation.
- MIT distribution with a Human copyright notice, zero third-party runtime
  dependencies and exclusion of the historical `tbao` implementation.
- Wheel/sdist metadata assertions for Python `>=3.11,<3.15`; Python 3.11–3.14
  conformance, build and clean-install checks.
- Separate English/Chinese READMEs, a Human/Host correction loop and a compact
  capability map that keeps project policy and future extensions outside Core.
- Public security-reporting and community-conduct guidance.

Authentication, policy ownership, evidence verification, live repository
observation/enforcement, execution and persistence remain host responsibilities.
Merge, tagging, GitHub Release and package publication require separate Human decisions.
