# TBC at a glance / TBC 一页摘要

**Trust-Bounded Collaboration (TBC) is an open practice and reference project for AI-native Individual Organizations.**

**Trust-Bounded Collaboration（TBC）是一个面向 AI-native Individual Organization 的开放实践与参考项目。**

## Who and why / 为谁、为何

One Human works with multiple AI agents over time across research, product, design, engineering, testing, release and operations, building the effective capacity of a small organization. Shared goals, division of work, handoffs, correction and learning give this continuity beyond using several AI tools.

一个 Human 与多个 AI Agent 长期协作，覆盖研究、产品、设计、工程、测试、发布与运营，形成小型组织的工作能力。共同目标、分工、交接、纠偏与学习，让这种协作超越同时使用多个 AI 工具。

**Human meaning sovereignty means that AI may greatly expand cognition and execution, but the Human remains the authority for what matters, why it matters, what outcome is acceptable, and which consequences are worth taking.**

**所谓人的意义主权，不是要求 Human 亲手执行每一步，而是无论 AI 的能力扩展到什么程度，什么事情值得做、为什么做、什么结果才算好、哪些后果可以接受，最终仍由 Human 决定。**

**Human-in-command, not Human-in-every-loop.** Humans retain final responsibility while Agents advance authorized work. Technical success must not silently redefine the goal.

**Human 掌握最终指挥权，不必身处每一步循环。** Agent 推进已授权工作，人保留最终责任；技术成功不能悄悄改写真正的目标。

## Build on the floor / 站在平台地板上

**We treat powerful AI platforms as the floor, not the ceiling.** Reuse mature models, runtimes/orchestration, HITL, IAM/OAuth, policy engines, cloud, browser, memory and tools. TBC explores Human meaning, project outcomes, collaboration structure, authority, coordination, correction and shared learning above that floor. It does not build a general SDLC or universal governance platform.

**我们把强大的 AI 平台当作地板，而不是天花板。** 优先复用成熟的模型、运行时／编排、HITL、IAM／OAuth、策略引擎、云、浏览器、记忆与工具。TBC 探索地板之上的人的意义、项目结果、协作结构、授权、协调、纠偏与共同学习，不建设通用 SDLC 或通用治理平台。

## Practice and code / 实践与代码

Real collaboration failures suggest reusable principles. Reuse existing platform capability where sufficient; otherwise add the smallest useful executable boundary, then return to real project use for validation.

真实协作失败帮助形成可复用原则；成熟平台已有足够能力则直接复用，仍有缺口才增加最小可执行边界，再回到真实项目验证。

The `1.0.0` exact-action authority / policy / evidence evaluator is one such mechanism: approval for action A must not silently authorize changed action B. It returns deterministic unsigned receipts and never executes actions. Hosts verify facts and enforce decisions. **vNext** upgrades the positioning, with no package version or executable contract change. The broader organization principles remain open to counterexamples; neither field cases nor conformance tests establish universal validation.

`1.0.0` 的 exact-action authority / policy / evidence evaluator 是其中一个机制：动作 A 的批准不能悄悄授权已变化的动作 B。它返回确定性未签名回执，不执行动作；事实验证与执行控制由宿主负责。**vNext** 升级的是定位，不改变软件包版本或可执行契约。更广的组织原则仍接受反例检验；实践案例与一致性测试均不构成普遍验证。

Read the [canonical vNext positioning and five generalized field cases](vnext-positioning.zh-en.md), [organization/mechanism overview](framework-overview.zh-en.md), [current evaluator quick start](../README.md#quick-start) and [participation guide](discussion-guide.md). Existing v0.1 material remains historical, local-only and mock-only.

继续阅读 [vNext 统一定位与五个泛化实践案例](vnext-positioning.zh-en.md)、[组织与机制概览](framework-overview.zh-en.md)、[当前评估器快速开始](../README.zh-CN.md#快速开始)和[参与指南](discussion-guide.md)。现有 v0.1 材料保留为历史、本地模拟参考。
