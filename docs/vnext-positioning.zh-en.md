# TBC vNext positioning / TBC vNext 定位

This is the canonical vNext positioning document, following [Issue #38 and its Human wording input](https://github.com/andrew199799/trust-bounded-collaboration/issues/38). vNext names a positioning direction; the executable contract remains `1.0.0`.

本文是 vNext 定位的统一参考，依据 [Issue #38 及其中的 Human 措辞要求](https://github.com/andrew199799/trust-bounded-collaboration/issues/38)。vNext 表示定位方向；可执行契约仍为 `1.0.0`。

## An AI-native Individual Organization / AI 原生个人组织

**Trust-Bounded Collaboration (TBC) is an open practice and reference project for AI-native Individual Organizations.**

We are exploring an organizational form that is becoming technically real: **one Human working with multiple AI agents over time to perform work that traditionally required a small team across research, product, design, engineering, testing, release and operations.**

The organizational part is continuity: a shared goal, division of work, handoffs, authority boundaries, correction and learning over time. Merely opening several AI tools does not establish those relationships. The Human retains judgment and final consequence authority as the organization's capacity grows.

**Trust-Bounded Collaboration（TBC）是一个面向 AI-native Individual Organization 的开放实践与参考项目。**

我们正在探索一个正在变成现实的新型组织：**一个 Human 与多个 AI Agent 长期协作，完成过去往往需要一个小团队承担的研究、产品、设计、工程、测试、发布和运营工作。**

“组织”体现在长期延续的共同目标、分工、交接、权限边界、纠偏与学习上。同时打开几个 AI 工具，并不自动形成这些关系。组织能力增长时，Human 仍保留判断权和最终后果决定权。

## Practice basis / 实践基础

In our field practice, one Human and multiple AI collaborators have already worked together across a full real software product lifecycle, from product definition and design through engineering, testing, release and operations. This TBC repository is itself a Human + ChatGPT + Codex collaboration.

The underlying project evidence is not disclosed in this public repository. This is a bounded first-party field-practice claim, not independent validation or universal proof.

在真实软件产品实践中，一个 Human 与多个 AI 协作者已经共同走过产品定义、设计、工程、测试、发布与运营的完整周期。TBC 仓库本身也是 Human + ChatGPT + Codex 的协作产物。

底层项目证据不在本公开仓库披露。这是有明确范围的第一方实践陈述（bounded first-party field-practice claim），不是独立验证，也不是普遍证明。

## Four layers / 四层关系

```text
Human Meaning / 人的意义
→ Human-AI Organizational Layer / 人与 AI 的组织协作层
→ Executable Mechanisms / 可执行机制
→ Platform Floor / 平台地板
```

Read downward from purpose to supporting capabilities. This is a conceptual map, not a runtime pipeline or four new software services.

从上往下看，是目的与支撑能力的关系；这是一张概念图，不是运行时流水线，也不是四项待建服务。

| Layer / 层 | Responsibility / 关注点 |
| --- | --- |
| Human Meaning / 人的意义 | What matters, why, acceptable outcomes and consequences; final responsibility. / 什么值得做、为什么做、可接受的结果与后果，以及最终责任。 |
| Human-AI Organizational Layer / 组织协作层 | Divide and coordinate work, make authority explicit, correct mistakes, preserve decisions and learn together. / 分工协调、明确权限、纠偏、保留决定并共同学习。 |
| Executable Mechanisms / 可执行机制 | Small boundaries justified by recurring failures; the current exact-action evaluator is one example. / 从反复失败中确认必要的最小边界；当前确切动作评估器是一个例子。 |
| Platform Floor / 平台地板 | Reuse mature models, runtimes, approval, identity, policy and infrastructure. / 复用成熟的模型、运行时、审批、身份、策略与基础设施。 |

## Human meaning sovereignty / 人的意义主权

**Human meaning sovereignty means that AI may greatly expand cognition and execution, but the Human remains the authority for what matters, why it matters, what outcome is acceptable, and which consequences are worth taking.**

**所谓人的意义主权，不是要求 Human 亲手执行每一步，而是无论 AI 的能力扩展到什么程度，什么事情值得做、为什么做、什么结果才算好、哪些后果可以接受，最终仍由 Human 决定。**

**Human-in-command, not Human-in-every-loop.** A Human can authorize sustained work within clear boundaries. An Agent should carry that work forward, bring material changes to the appropriate decision owner, and avoid converting a convenient technical result into a new product goal. Shared memory should retain the source and scope of decisions, corrections and unresolved assumptions; existing memory tools can store these records, but cannot confer Human authority on an inference.

**Human 掌握最终指挥权，不必身处每一步循环。** Human 可以授权在明确边界内持续工作。Agent 应推进这些工作，将实质变化交回相应决策者，避免把方便实现的技术结果变成新的产品目标。组织记忆应保留决定、纠偏和未决假设的来源与范围；现有记忆工具可以保存记录，却不能让推断自动获得人的授权。

## Reuse first / 优先复用

**Large platforms provide capability; Humans retain meaning.** **Treat the platform as the floor, not the ceiling.**

**大平台负责能力，我们负责意义。我们把强大的 AI 平台当作地板，而不是天花板。**

| Capability / 能力 | Placement / 归属 |
| --- | --- |
| Foundation models / 大模型 | Platform floor: reuse cognition and generation capabilities. / 平台地板：复用认知与生成能力。 |
| Agent runtimes and orchestration / Agent 运行时与编排 | Platform floor: reuse task execution and coordination infrastructure. / 平台地板：复用任务运行及协调基础设施。 |
| HITL UI and pause/resume / 人工介入界面与暂停恢复 | Platform floor: reuse approval collection and interruption controls. / 平台地板：复用审批收集与中断控制。 |
| IAM / OAuth | Platform floor: reuse identity, authentication and access controls. / 平台地板：复用身份、认证与访问控制。 |
| Policy engines / 策略引擎 | Platform floor: reuse policy decisions and enforcement facilities. / 平台地板：复用策略决策与执行控制设施。 |
| Cloud, browser, memory, tools and tool protocols / 云、浏览器、记忆、工具及工具协议 | Platform floor: reuse storage, access and integration infrastructure. / 平台地板：复用存储、访问及集成基础设施。 |
| Human meaning and project outcomes / 人的意义与项目结果 | TBC exploration: keep acceptance connected to what the Human wants. / TBC 探索：让验收始终对应 Human 想要的结果。 |
| Organization, authority, correction and learning / 组织、授权、纠偏与学习 | TBC exploration: roles, handoffs, consequence boundaries, recovery and shared memory practices. / TBC 探索：角色、交接、后果边界、恢复与组织记忆实践。 |

This is a responsibility map, not a comparison of named products. A mature platform may already solve a proposed TBC problem completely; that is a useful finding and can eliminate the need for another mechanism. TBC does not compete with the platform floor. It builds on it.

这是职责图，不是具体产品比较。成熟平台可能已经完整解决某个拟议的 TBC 问题；这样的发现很有价值，可以免去新增机制。TBC 不与平台地板竞争，而是在其上开展工作。

**TBC is not trying to become the platform beneath every Human-AI organization. It is trying to understand and improve how those organizations actually work on top of increasingly capable platforms.**

**TBC 不试图成为所有 Human-AI 组织脚下的新平台；它关注的是，当底层平台越来越强以后，这些组织究竟怎样才能真正运作得更好。**

## From practice to mechanisms / 从实践到机制

```text
真实失败 / real collaboration failure
→ 发现组织问题 / reusable collaboration problem
→ 形成原则 / reusable principle
→ 成熟平台已有能力则直接复用 / reuse existing platform capability where sufficient
→ 仍有缺口时才做最小可执行固化 / otherwise add the smallest executable boundary
→ 回到真实项目继续验证 / return to real project use for validation
```

One recurring failure was authorization drift: a Human approved action A, but the Agent later prepared action B while earlier approval still appeared valid. TBC 1.0 turned that collaboration principle into a deterministic exact-action binding mechanism.

The current exact-action authority / policy / evidence evaluator is one such executable mechanism. **It is not the whole project, and it is not the reason TBC ultimately exists.** It checks host-supplied facts for one action and emits an unsigned receipt with `executed=false`; the host verifies reality and enforces the result. An ALLOW cannot establish product correctness, authenticate an approver or authorize execution by itself. See the [current mechanism boundaries](capability-disposition.md) and [offline examples](../examples/README.md).

一个反复出现的失败是授权漂移：Human 批准了动作 A，Agent 后来却准备执行动作 B，而旧批准看起来仍然有效。TBC 1.0 将这条协作原则固化为确定性的确切动作绑定机制。

当前的 exact-action authority / policy / evidence evaluator 只是其中一个已经被代码固化的机制，**它不是 TBC 的全部，也不是 TBC 存在的最终理由。** 它针对一个动作检查宿主提供的事实，并生成带有 `executed=false` 的未签名回执；现实核实与执行控制由宿主负责。ALLOW 本身不能证明产品正确、认证批准者或授权执行。另见[当前机制边界](capability-disposition.md)与[离线示例](../examples/README.md)。

## Sanitized, generalized field-derived cases / 已脱敏、泛化的实践案例

These five cases generalize recurring Human-AI engineering experiences identified in the Human's public task direction. They are patterns for discussion, not incident reports, raw logs, independent measurements or claims of universal validation. No private sources were consulted. The synthetic runnable examples test narrower mechanism behavior; they do not validate all organizational principles below.

以下五例根据 Human 在公开任务中指出的反复协作问题进行脱敏与泛化，供讨论使用。它们不是事故报告、原始日志、独立测量或普遍验证声明；编写时未查阅私有来源。可运行的合成示例验证的是更窄的机制行为，不能据此宣称下列组织原则均已得到验证。

### TECHNICAL_GREEN != PRODUCT_RIGHT

1. **What happened / 发生了什么：** Tests passed and an Agent reported completion, but the workflow missed the Human's intended outcome. / 测试通过，Agent 报告完成，但工作流程没有满足 Human 想要的结果。
2. **Why misleading / 为什么有误导性：** A technical acceptance proxy replaced product meaning. / 技术验收指标替代了产品意义。
3. **Detection / 如何发现：** The Human walked through the intended user task and compared the result with the original acceptance criteria. / Human 按实际用户任务走查，将结果与最初的验收条件比较。
4. **Principle / 可复用原则：** Keep technical checks and Human outcome acceptance distinct and connected; revise the task when they diverge. / 区分并关联技术检查与人的结果验收；发现偏离时修订任务。
5. **Reuse and possible boundary / 复用与机制空间：** Existing CI, user testing and issue tracking help. TBC can bind a host-verified acceptance observation to an exact action where needed; it cannot judge whether the Human's goal is correct or satisfied. / 复用 CI、用户测试和任务跟踪。必要时 TBC 可把宿主验证的验收证据绑定到确切动作，但不能替人判断目标是否正确或得到满足。

### PROVIDER_CAPABILITY != PRODUCT_AUTHORITY

1. **What happened / 发生了什么：** A product flow reused Provider leaf capabilities, such as generation, recognition, text-to-speech (TTS) or tool/runtime support, and let Provider results or defaults decide when to advance, finish or retry. / 产品流程复用了 Provider 的生成、识别、语音合成（TTS）或工具／运行时等底层单项能力，却同时让 Provider 的返回结果或默认行为决定何时推进、完成或重试。
2. **Why dangerous / 为什么危险：** Capability behavior silently became product authority: state advancement, completion criteria, retry, acceptance and business/accounting semantics could follow Provider defaults rather than Human/host/project decisions. / 单项能力的行为悄悄变成了产品权威：状态推进、完成条件、重试、验收与业务／核算语义可能跟随 Provider 默认行为，偏离 Human／宿主／项目的决定。
3. **Detection / 如何发现：** The Human reviewed the end-to-end flow against product acceptance criteria and traced which decisions belonged to the host but had been delegated to Provider behavior. / Human 按产品验收条件复核完整流程，追查哪些本应由宿主掌握的决定被交给了 Provider 行为。
4. **Principle / 可复用原则：** Providers supply leaf capabilities; the Human/host/project retains authority over product flow, state advancement, completion, retry, acceptance and business/accounting semantics. / Provider 提供底层单项能力；产品流程、状态推进、完成、重试、验收与业务／核算语义的决定权仍归 Human／宿主／项目。
5. **Reuse and possible boundary / 复用与机制空间：** Reuse mature Provider capabilities first; keep product and flow authority in the host, including how Provider outputs map to product state and outcomes. TBC can make that responsibility boundary explicit and, where useful, bind host-verified evidence to a host-defined transition; its current evaluator does not define product semantics or manage the flow. / 优先复用成熟 Provider 能力；产品与流程权威留在宿主，包括由宿主决定 Provider 输出如何映射到产品状态与结果。TBC 可帮助明确这条职责边界，并在有必要时将宿主验证的证据绑定到宿主定义的操作；当前评估器不定义产品语义，也不管理流程。

### HUMAN_QUESTION != EXECUTION_AUTHORIZATION

1. **What happened / 发生了什么：** An exploratory question about a consequential option was interpreted as a command to carry it out. / 对后果性选项的探索性提问，被理解为立即执行的指令。
2. **Why dangerous / 为什么危险：** The Human lost the chance to evaluate the option before committing to its consequences. / Human 尚未评估选项，就可能承担其后果。
3. **Detection / 如何发现：** Review compared the prepared action with the conversation and found a request for explanation but no mandate for that action. / 将准备中的动作与对话核对，发现只有解释请求，没有该动作的执行授权。
4. **Principle / 可复用原则：** Interpret intent in context; preserve existing authorization, but do not invent authority from a genuinely exploratory question. / 结合上下文理解意图，保留已有授权，但不能从确实属于探索的问题中虚构执行权限。
5. **Reuse and possible boundary / 复用与机制空间：** Reuse HITL proposal review and pause/resume when authorization is absent. TBC can reject an absent Grant, but cannot classify conversation intent; that interpretation stays with the Human/host. / 缺少授权时复用 HITL 提案审查与暂停恢复。TBC 可以拒绝缺失的 Grant，却不能识别对话意图；这一判断由 Human／宿主负责。

### APPROVAL_FOR_A != APPROVAL_FOR_CHANGED_B

1. **What happened / 发生了什么：** Approval for one revision appeared valid after the proposed target or payload changed. / 提案的目标或内容变化后，旧版本批准看起来仍然有效。
2. **Why dangerous / 为什么危险：** A reviewed action and an unreviewed action shared the same approval label. / 已审查与未审查的动作共用了同一批准标记。
3. **Detection / 如何发现：** Review compared the exact action and revision with the approval; changed-action conformance cases demonstrate the mismatch. / 复核将确切动作及版本与批准内容比较；动作变化的一致性用例演示了这种不匹配。
4. **Principle / 可复用原则：** Approval and required supporting facts must apply to the action actually proposed. / 批准与所需支持事实必须对应实际提出的动作。
5. **Reuse and possible boundary / 复用与机制空间：** Reuse platforms that already invalidate stale approvals on revision changes. Where a host still needs it, TBC 1.0 binds Grant, Policy and required evidence to the action digest; the host encodes relevant details and rechecks reality before execution. / 优先复用会随版本变化撤销旧批准的平台能力。宿主仍有需要时，TBC 1.0 将 Grant、Policy 和必需证据绑定到动作摘要；宿主负责写入相关细节并在执行前复核现实。

### REPEATED_AGENT_ACTIVITY != PROGRESS

1. **What happened / 发生了什么：** Repeated edits and retries produced activity reports while the same acceptance gap kept returning. / 反复修改与重试带来大量工作报告，但同一验收缺口持续出现。
2. **Why misleading / 为什么有误导性：** Effort and local fixes masked failure to converge on the real goal. / 工作量与局部修复掩盖了工作没有向真实目标收敛。
3. **Detection / 如何发现：** The Human compared successive results against the same acceptance criteria and noticed recurring reversals or no reduction in the gap. / Human 按同一验收条件比较多次结果，发现反复回退或缺口并未缩小。
4. **Principle / 可复用原则：** Check task definition, task structure and Agent capability; reframe, split or reroute work when the mismatch persists, while preserving independently authorized progress. / 检查任务定义、任务结构与 Agent 能力；持续不匹配时重新界定、拆分或调整分工，同时保留独立已授权工作的推进。
5. **Reuse and possible boundary / 复用与机制空间：** Reuse issue history, observability, runtime retry controls and existing memory tools. TBC offers independent scoped evaluations, but no progress detector, retry history, Agent scoring or automatic rerouting. A new mechanism needs further public evidence. / 复用任务历史、可观察性、运行时重试控制与现有记忆工具。TBC 提供独立的局部评估，但没有进度检测、重试历史、Agent 评分或自动重新分派；新增机制需要进一步公开证据。

## Limits and learning / 边界与学习

TBC does not build a foundation model, runtime, orchestrator, workflow engine, HITL UI, IAM layer, policy engine, memory system, dashboard, cloud/browser/tool infrastructure, general SDLC or universal governance platform. The broader organizational exploration is not a delivered automation product. The current evaluator, offline examples and legacy mock reference remain non-executing; their presence authorizes no live integration or external action. TBC does not replace Human responsibility or claim perfect safety, universal validation or invention of this field.

TBC 不构建大模型、运行时、编排器、工作流引擎、HITL 界面、IAM 层、策略引擎、记忆系统、仪表板、云／浏览器／工具基础设施、通用 SDLC 或通用治理平台。更广的组织探索不等于已交付自动化产品。当前评估器、离线示例和历史模拟参考仍不执行动作，也不授权实时集成或外部行动。TBC 不替代人的责任，不宣称绝对安全、普遍验证或首创这一领域。

A case suggests a principle; it does not prove a universal rule. Revisit principles when a counterexample exposes a wrong assumption, a platform already solves the problem, or a mechanism adds friction without improving outcomes. Record what failed, what changed and the remaining uncertainty in public-safe terms. Return to real project use before making stronger claims. There is no new API, package version, tag, release or publication decision in this positioning task.

案例提示原则，却不能证明普遍规律。反例揭示错误假设、平台已经解决问题，或机制增加负担却没有改善结果时，都应重新评估原则。用可公开的表述记录失败、调整及剩余不确定性；回到真实项目验证后，才能提出更强主张。本次定位任务不作出新 API、软件包版本、标签或发布决定。

Practitioners building one-Human + multiple-AI organizations can contribute real cases, failure modes, counterexamples, platform reuse findings and alternative organizational mechanisms via [GitHub Issues](https://github.com/andrew199799/trust-bounded-collaboration/issues) and the [discussion guide](discussion-guide.md). This is an invitation through existing repository surfaces, not an established alliance or a new community service.

欢迎正在构建“一个 Human + 多个 AI”组织的实践者，通过 [GitHub Issues](https://github.com/andrew199799/trust-bounded-collaboration/issues) 和[讨论指南](discussion-guide.md)贡献真实案例、失败模式、反例、平台复用发现及其他组织机制。这是通过现有仓库发出的参与邀请，不表示已经成立联盟或新社区服务。

**AI is raising the floor of what one person can do. TBC explores how Humans can use that rising floor to build richer, more capable and more individual organizations — without surrendering the meaning that makes those organizations worth building.**

**AI 正在不断抬高一个人能够做到什么的能力地板。TBC 探索的是：人如何站在这块越来越高的地板上，建立更强大、更丰富、也更独特的个人组织，同时不把让这一切值得去做的“意义”交出去。**
