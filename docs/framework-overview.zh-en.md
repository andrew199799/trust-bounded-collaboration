# TBC organization and mechanisms / TBC 组织与机制概览

The [canonical vNext positioning](vnext-positioning.zh-en.md) defines TBC as an open practice and reference project for AI-native Individual Organizations: one Human and multiple AI agents working together over time. This overview connects that purpose to the existing code; it does not specify a new runtime.

[vNext 统一定位](vnext-positioning.zh-en.md)将 TBC 定义为面向 AI-native Individual Organization 的开放实践与参考项目：一个 Human 与多个 AI Agent 长期协作。本概览说明这一目的与现有代码的关系，不定义新的运行时。

## Four layers / 四层关系

```text
Human Meaning / 人的意义
→ Human-AI Organizational Layer / 人与 AI 的组织协作层
→ Executable Mechanisms / 可执行机制
→ Platform Floor / 平台地板
```

The Human decides what matters and which outcomes and consequences are acceptable. The organizational layer concerns division of work, coordination, authority, correction and shared learning. Executable mechanisms solidify a recurring principle where useful. Mature platform capabilities supply the infrastructure; use them directly whenever sufficient. The arrows express purpose and support, not an execution pipeline.

Human 决定什么值得做、哪些结果与后果可以接受。组织协作层关注分工、协调、授权、纠偏与共同学习。可执行机制在有用之处固化反复出现的原则。基础设施由成熟平台能力提供，足够解决问题时就直接复用。箭头表示目的与支撑关系，不是执行流水线。

## Where the evaluator fits / 评估器的位置

Authorization drift is one concrete organizational failure: action B inherits the apparent approval of action A. The current `1.0.0` library compares one proposed action with host-verified authority, policy and evidence bindings, returning ALLOW/DENY and an unsigned deterministic receipt with `executed=false`.

授权漂移是一类具体的组织失败：动作 B 看似继承了动作 A 的批准。当前 `1.0.0` 库将一个拟执行动作与宿主验证的授权、策略、证据绑定进行比较，返回 ALLOW／DENY 和带有 `executed=false` 的确定性未签名回执。

The host authenticates, verifies facts and policy, rechecks reality and enforces decisions using its existing platform. TBC does not collect approvals, own project intent, execute actions, maintain organizational memory or automatically correct/reroute Agents. A product outcome still needs Human acceptance even when technical checks pass. See the [capability disposition](capability-disposition.md) for precise current boundaries.

宿主通过已有平台负责认证、事实与策略验证、现实复核及执行控制。TBC 不收集批准、不拥有项目意图、不执行动作、不维护组织记忆，也不自动纠偏或重新分派 Agent。即使技术检查通过，产品结果仍需要人的验收。确切的当前边界见[能力归属说明](capability-disposition.md)。

## How to evolve / 如何演进

Begin with a real failure and a reusable principle, check whether mature platform capabilities already solve it, add the smallest executable boundary only if a gap remains, then test the idea again in real work. Counterexamples and evidence that a mechanism is unnecessary are welcome. This is exploration, not a universally validated organizational framework or a platform roadmap.

从真实失败和可复用原则出发，先检查成熟平台是否已经解决问题；仍有缺口才增加最小可执行边界，再回到真实工作检验。欢迎反例，以及说明某个机制并无必要的证据。这是探索，不是经过普遍验证的组织框架，也不是平台建设路线图。

Start with the [five sanitized field cases and reuse map](vnext-positioning.zh-en.md), then the [offline executable examples](../examples/README.md) and [non-goals](non-goals.zh-en.md). The earlier [v0.1 principles](principles.zh-en.md) and [Action Spine specification](action-spine-mvp.zh-en.md) remain historical reference material, not the current public API or a requirement to build every proposed component.

建议先看[五个脱敏实践案例与复用能力图](vnext-positioning.zh-en.md)，再看[离线可执行示例](../examples/README.md)和[非目标](non-goals.zh-en.md)。早期 [v0.1 原则](principles.zh-en.md)与 [Action Spine 规格](action-spine-mvp.zh-en.md)保留为历史参考，不代表当前公开 API，也不要求实现其中每个拟议组件。
