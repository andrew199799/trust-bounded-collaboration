# Trust-Bounded Collaboration

TBC checks whether host-verified authority, policy and evidence bind to one exact
proposed action. It returns an explainable decision and a reproducible unsigned
receipt. Evaluation is pure: it performs no authentication, network access, clock
lookup, persistence or action execution.

**Status:** reviewed 1.0 foundation merged on `main`; development version `1.0.0a1`.
No tagged release or package publication is announced. CPython 3.11–3.14 is the conformance target. Runtime dependencies:
Python standard library only.

## Quick Start

From a checkout of this repository, with Python 3.11–3.14 available:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install build==1.6.0
python -m build
python -m pip install --no-index --no-deps dist/*.whl
tbc demo repository --json
python -m tbc demo repository --json
```

On Windows, activate with `.venv\Scripts\activate`; pass the generated wheel's
filename to pip instead of the shell wildcard. These commands build/install locally;
they do not upload a package. Build tooling may download dependencies. The installed
demo needs no credentials or network.

The fixed `simulation=true` output includes an allowed contributor proposal,
denied canonical main/tag/delete/non-fast-forward/merge/release cases, a changed
proposal denied for stale binding, and independently allowed inspection. Expected
DENY cases count as a successful demo (exit 0). An unexpected result exits 1;
invalid usage exits 2. CLI scope is help, version and this fixed example.

## Integrate the library

Run the compact, synthetic [four-function example](examples/tbc_integration.py):

```sh
python examples/tbc_integration.py
```

- `load_request(text)` validates a `tbc.request.v1` mapping with one action:
  `actor`, `transition`, `resource`, and JSON-object `payload`.
- `action_digest(action)` binds every action field with SHA-256.
- `evaluate(request, *, context)` validates host-owned `tbc.context.v1` facts and
  returns a `tbc.receipt.v1` mapping with ALLOW/DENY, reason codes, action/context
  digests, explicit time, affected transition and `executed=false`.
- `dumps_receipt(receipt)` validates receipt structure and emits deterministic JSON.
  Malformed input raises `InputError`, with `code` and a sanitized `path`.

Context must come from trusted host code, never from caller-provided JSON or a
`trusted=true` flag. The host authenticates actor/issuer, establishes grant authority,
decides domain policy, verifies evidence and supplies time. Grant **and Policy** must
bind to the recomputed action digest. Required evidence IDs come only from that bound
Policy. Required observations must match the action, pass verification and remain
within their explicit validity interval. A blocker affects only that evaluation.

The host/platform enforces the result at the actual transition, including fresh
repository identity/permission/state checks and replay handling. Remote names and
technical credentials do not establish task authority. The synthetic repository
profile demonstrates the boundary; it is not a live GitHub collector or guard.

Receipts are unsigned evaluation records. Hashes do not authenticate their contents,
prove execution or make them reusable permission tokens. `dumps_receipt` checks
structure, not truth. Host code owns output sanitization and retention.

## Encoding and tests

The shared encoding uses `sort_keys=True`, `ensure_ascii=False`,
`separators=(",", ":")`, `allow_nan=False`, UTF-8, no BOM or trailing newline.
Only string keys and JSON null/bool/string/integer/list/object values are accepted;
floats, surrogates, duplicate object keys and integers outside ±(2^53−1) are rejected.
Unicode is not normalized. Evidence sorts by unique ID; Policy required IDs sort
(duplicates rejected); receipt reasons sort/deduplicate. Payload array order stays
unchanged. Digests include the ASCII `tbc.action.v1` or `tbc.context.v1` domain,
one newline byte, then the encoded JSON. No RFC 8785/in-toto/DSSE compliance is claimed.
Initial 1 MiB/depth 32 limits are defensive implementation defaults, not authority rules.

```sh
python -m pip install -e . pytest==9.1.1 build==1.6.0
python -m pytest -q
python -m build
python tests/check_distribution.py
git diff --check
```

CI runs fixed golden bytes/digests, contract and demo tests on Python 3.11–3.14,
then inspects wheel/sdist contents and measures a fresh offline wheel install/demo.
The local first-run target is under ten minutes; the check reports actual elapsed time.

## Legacy and contribution

`src/tbao/`, its tests and historical v0.1 docs remain reference/regression material;
they are outside the new distribution and stable API. Start with the example above
for the current library. No historical rewrite or compatibility migration is implied.

Contribute through [fork → branch → test → PR](CONTRIBUTING.md). Human maintainers own
merge/release/publication; AI Agents follow [AGENTS.md](AGENTS.md). Current release-readiness
preparation is [Issue #29](https://github.com/andrew199799/trust-bounded-collaboration/issues/29).

See [security reporting](SECURITY.md), [community conduct](CODE_OF_CONDUCT.md) and
[unreleased changes](CHANGELOG.md). Built by Andrew with ChatGPT and Codex as AI
engineering collaborators; this does not imply organizational endorsement.
Copyright ownership remains with the applicable Human copyright holder.

Licensed under the complete [MIT License](LICENSE). The new package vendors no
third-party code and has no third-party runtime dependencies. No independently required third-party notice
was identified for this slice; future contributions must preserve any
applicable third-party notices.
