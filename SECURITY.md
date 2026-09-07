# Security reporting

The current `main` is an unreleased development foundation (`1.0.0a1`). There are
no tagged releases with a maintenance/support commitment yet. Please identify the
exact commit or package version when reporting a concern.

## Arrange a private channel first

Private vulnerability reporting is currently disabled for this repository. To
request a private reporting channel, open an Issue with a generic title such as
“Private contact request”, without vulnerability details, reproduction steps,
credentials, personal data or private-source information. A Human maintainer must
arrange a private channel before you send the technical report. This follows the
existing [contributor reporting boundary](CONTRIBUTING.md).

Once a private channel is established, provide the affected version, impact and a
minimal reproduction using synthetic data. Do not include real credentials, private
repository material or raw operational logs. Maintainers coordinate remediation
and disclosure; no response-time guarantee is currently offered.

## Scope of the library

TBC checks exact-action bindings and returns unsigned evaluation records. Its host
owns authentication, issuer authority, domain policy, evidence verification and
actual enforcement. Hashes do not authenticate host assertions, and receipts are
not permission or replay tokens. Report malformed-input or binding failures that
violate the documented contract; do not use live systems or real secrets to prove
a report against the offline examples.
