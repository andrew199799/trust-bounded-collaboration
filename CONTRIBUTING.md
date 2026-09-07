# Contributing

Human and AI-assisted contributions are welcome. The canonical project is [andrew199799/trust-bounded-collaboration](https://github.com/andrew199799/trust-bounded-collaboration). Human maintainers decide what to merge and release.

## Contribute organizational practice

Practitioners building one-Human + multiple-AI organizations are welcome to share
real cases, failure modes, counterexamples, existing platform solutions and alternative
organizational mechanisms in [GitHub Issues](https://github.com/andrew199799/trust-bounded-collaboration/issues).
Use the [discussion guide](docs/discussion-guide.md) and [vNext positioning](docs/vnext-positioning.zh-en.md)
to describe the problem and evidence without private details. Code is useful where a
recurring problem needs an executable boundary after mature platform reuse has been considered.

欢迎构建“一个 Human + 多个 AI”组织的实践者，通过现有 Issues 贡献真实案例、失败模式、反例、
成熟平台已解决问题的经验，以及其他组织机制。请参照讨论指南和 vNext 定位，说明问题与证据，
不公开私有细节；先考虑复用成熟平台，确有必要时再用代码固化反复出现的问题边界。

## Fork, branch, test, PR

1. Discuss substantial changes in a public Issue first. Keep each PR focused on one problem.
2. Fork the canonical repository into your own GitHub account. Clone your fork into a fresh directory; replace `YOUR-USERNAME` below with your account:

   ```sh
   git clone https://github.com/YOUR-USERNAME/trust-bounded-collaboration.git
   cd trust-bounded-collaboration
   git remote add upstream https://github.com/andrew199799/trust-bounded-collaboration.git
   git fetch upstream main
   git switch --create your-task --no-track upstream/main
   ```

   `upstream` is the canonical read/fetch source; `origin` is your writable fork. Check both fetch and push URLs with `git remote -v`, and verify the fork's owner and parent on GitHub before pushing. Do not infer repository identity from a remote name.

3. Make a small change. Use Python 3.11–3.14 and install the package/test tools, then run from the repository root:

   ```sh
   python3 -m pip install -e . pytest==9.1.1 build==1.6.0
   python3 -m pytest -q
   git diff --check
   ```

   Tests cover the current TBC contracts/demo and the separate legacy mock reference. Add focused positive and negative tests when introducing a tool or changing behavior.

4. Review `git status` and your diff before staging only intended files. Commit and push your task branch to your fork:

   ```sh
   git push --set-upstream origin your-task
   ```

5. Open a PR with base `andrew199799/trust-bounded-collaboration:main` and head your fork's task branch. Use a Draft PR while work is in progress. Explain the problem, resulting behavior, relevant tests, and limitations. Push follow-up commits to the same fork branch to update the PR.

AI Agents also follow [AGENTS.md](AGENTS.md), including one isolated workspace per Agent/task and verified API/transport identity. Credentials do not grant task authority. Agents propose changes; Human maintainers retain merge, tag, and release authority.

## Keep contributions public-safe

**Every GitHub artifact in this repository must be assumed public before it is written.**

Check files, commits, PR/Issue text, comments, attachments, and shared logs before publishing. Include public facts and sanitized results only. Do not include secrets, private-source code or repository references, internal operational details, sensitive paths, personal data, or private provider/account/business information.

If you encounter legacy private references in a file you are changing, make a small, scoped correction that preserves useful public meaning. Do not expand into a historical rewrite. For actual secrets or materially sensitive disclosures, stop the affected publication/remediation step, notify a Human maintainer with sanitized information, and arrange a private reporting channel before sharing details. Do not post the sensitive value or rewrite history/rotate credentials without authorization.

## Contribution and license boundary

Submit only material you have the right to contribute under this repository's [LICENSE](LICENSE). Preserve third-party attribution and identify any additional license obligations in your PR. Contributors remain responsible for reviewing AI-assisted work and ensuring it contains no private-source material. AI tools may be credited factually; they are not represented as copyright owners or project endorsers.

The existing v0.1 reference code remains local-only, mock-only, non-executing, and not production-ready. A contribution does not authorize live integrations, real credentials, real funds, or external execution.
