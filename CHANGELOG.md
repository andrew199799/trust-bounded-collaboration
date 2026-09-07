# Changelog

## Unreleased

Development metadata is `1.0.0a1`. This section records the merged foundation;
it does not announce a tagged release or package publication.

- Four-function Python API: request validation, exact action digest, pure scoped
  evaluation and deterministic unsigned receipt serialization.
- Independent Grant and Policy action binding; required evidence belongs to the
  bound Policy. A blocked action does not change an independent evaluation.
- Restricted UTF-8 JSON profile and domain-separated SHA-256 digests, with fixed
  golden tests and fail-closed malformed-input handling.
- Credential-free offline repository demo and a compact host integration example.
- MIT distribution with a Human copyright notice, zero third-party runtime
  dependencies and exclusion of the historical `tbao` implementation.
- Wheel/sdist metadata assertions for Python `>=3.11,<3.15`; Python 3.11–3.14
  conformance, build and clean-install checks.
- Public security-reporting and community-conduct guidance.

Authentication, policy ownership, evidence verification, live repository
observation/enforcement, execution and persistence remain host responsibilities.
A final version, release notes and publication require a separate Human decision.
