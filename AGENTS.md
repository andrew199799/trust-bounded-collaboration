# AI Agent execution contract

These rules apply equally to Codex, OpenClaw, Claude Code, and future compatible AI Agents. An Agent's authority comes from the current Human-authorized task, not its vendor or technical credentials.

## Before changing anything

- Read `docs/development-log/current-task-context.md` for continuity, then the current task Issue and its applicable Human instructions. The current authorization takes precedence over stale task notes.
- Read only files needed for that task. Do not scan archives, evidence, history, or unrelated material by default.
- Canonical repository truth is `andrew199799/trust-bounded-collaboration:main`. Refresh canonical `main` and record its exact SHA before starting a task branch.
- Give each Agent/task one isolated clone or worktree. Concurrent Agents must not share a mutable working tree. Keep remotes and credentials isolated too; a separate clone is preferable when worktrees would share conflicting Git configuration.
- Verify the GitHub API identity, Git transport identity, and commit attribution. Verify both fetch and push repository identities, the contributor fork's owner/parent, and effective permissions. Remote names alone are not proof.
- Use `upstream` for canonical read/fetch and `origin` for the Agent-owned contributor fork. If identities, roles, or authority are ambiguous, stop the affected transition and continue only safe read-only diagnosis.

## Repository authority

- Normal Agent writes go to a task branch in its contributor fork. Do not push branches, tags, deletions, or force updates to canonical.
- Normal Agent credentials should have canonical read access without write/admin authority. Report any permission cutover to the Human; do not change permissions or escalate authority yourself.
- A canonical Pull Request is a proposal. Human maintainers own merge and release decisions. No Agent self-merge, self-release, or self-tag; no auto-merge activation.
- Keep PRs small, scoped, and reviewable. Follow the task's tighter PR limit within the maximum of four PRs per phase. Use the PR body for intermediate status and create final evidence only at phase end.
- Run relevant tests and `git diff --check`. Verify the canonical PR base, contributor head repository/branch, and exact head SHA after publishing or updating a proposal.
- Ordinary implementation, test, and debugging failures remain Agent-owned inside authorized scope. Interrupt the Human only for material authority, product meaning, architecture, security/privacy, or release/consequence changes; stop only the affected transition.

## Public artifacts

**Every GitHub artifact in this repository must be assumed public before it is written.**

- Apply this to files, commits, Issues, PRs, comments, attachments, and published test/CI output. Publish public repository facts and sanitized engineering evidence only.
- Never publish secrets, private repository/source references, raw internal logs, sensitive paths or infrastructure, personal data, or private provider/account/business details. Do not copy or lightly rename private implementations.
- Sanitize small legacy disclosures encountered in current-facing files within task scope, preserving useful public meaning. Do not expand into historical cleanup by default.
- If an actual secret, credential, or materially sensitive disclosure is found, stop the affected security transition and report only sanitized evidence. File edits do not erase history; history rewriting, credential rotation, and destructive cleanup need explicit Human authorization.

## Project scope

The existing v0.1 reference remains local-only, mock-only, and non-executing, with no real credentials, funds, or external side effects. Repository collaboration operations require task authorization; they do not authorize a product runtime, live integration, scheduler, worker, or production plugin. Do not claim production readiness or expand into unrelated scenarios.
