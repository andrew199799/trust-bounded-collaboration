# TBC practitioner discussion / TBC 实践者讨论指南

If you are building an organization around one Human and multiple AI agents, help us understand what makes that work over time. TBC is an open practice and reference project for AI-native Individual Organizations. Start with the [vNext positioning and generalized field cases](vnext-positioning.zh-en.md).

如果你正在让一个 Human 与多个 AI Agent 组成长期工作的组织，欢迎分享怎样才能让这种协作持续有效。TBC 是面向 AI-native Individual Organization 的开放实践与参考项目。请先阅读 [vNext 定位与泛化实践案例](vnext-positioning.zh-en.md)。

## Useful contributions / 欢迎的贡献

- Real cases and failure modes: where intent, handoffs, authorization, correction or shared learning broke down. / 真实案例与失败模式：意图、交接、授权、纠偏或共同学习在哪一步出了问题。
- Counterexamples: where a TBC principle fails or adds friction without improving the result. / 反例：哪些原则不成立，或只增加负担而没有改善结果。
- Platform reuse findings: where mature models, runtimes, HITL, IAM, policy or infrastructure already solve the problem. / 平台复用发现：成熟模型、运行时、HITL、IAM、策略或基础设施已解决哪些问题。
- Alternative organizational mechanisms: clearer roles, acceptance, handoffs, correction or decision memory, with the limits of the evidence. / 其他组织机制：更清楚的角色、验收、交接、纠偏或决策记忆，并说明证据边界。
- Small documentation or current evaluator improvements grounded in an actual problem. / 基于实际问题的小范围文档或当前评估器改进。

## Share through the existing repository / 使用现有仓库入口

Open a [GitHub Issue](https://github.com/andrew199799/trust-bounded-collaboration/issues) with a public-safe case: what happened, why it mattered, how it was detected, the proposed principle, and which existing platform capability can help or what gap remains. Identify generalizations and uncertainty. A platform that solves the problem without TBC is a useful contribution.

通过 [GitHub Issue](https://github.com/andrew199799/trust-bounded-collaboration/issues) 提交可公开案例：发生了什么、为什么重要、如何发现、可提炼什么原则，以及现有平台能提供什么帮助或还缺什么。说明哪些内容经过泛化、哪些仍不确定。即使平台不需要 TBC 就解决了问题，也是一项有用贡献。

Use [CONTRIBUTING.md](../CONTRIBUTING.md) for scoped fork-based PRs. Human maintainers decide merge and release. This is a lightweight practitioner invitation through existing Issues and contributions; it does not announce an established alliance, a new organization or an external community service.

范围明确的 fork PR 请遵循 [CONTRIBUTING.md](../CONTRIBUTING.md)。合并与发布由 Human 维护者决定。这只是通过现有 Issues 和贡献渠道发出的轻量实践者邀请，不表示已经成立联盟、新组织或外部社区服务。

## Public boundaries / 公开边界

Share generic, sanitized engineering meaning only. Do not include private repository/source references, copied private implementation, raw internal logs, infrastructure details, credentials, personal data or business-sensitive material. Public cases are not evidence of universal validation. For sensitive security reports, follow [SECURITY.md](../SECURITY.md) before sharing details.

仅分享泛化、脱敏后的工程含义。不要提交私有仓库或来源引用、复制的私有实现、原始内部日志、基础设施细节、凭据、个人信息或业务敏感内容。公开案例不构成普遍验证。敏感安全报告请在提供细节前遵循 [SECURITY.md](../SECURITY.md)。

TBC reuses the platform floor. Discussion does not authorize a runtime, live integration, scheduler, worker or external execution. Current examples remain offline and non-executing; see [non-goals](non-goals.zh-en.md).

TBC 优先复用平台地板。讨论不授权运行时、实时集成、调度器、worker 或外部执行。当前示例继续保持离线且不执行动作；另见[非目标](non-goals.zh-en.md)。
