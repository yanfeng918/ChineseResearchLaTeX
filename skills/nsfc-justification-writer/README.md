# nsfc-justification-writer — 用户使用指南

本 README 面向使用者：说明如何触发、准备输入、分阶段写作和安全写入。AI 执行规范见 [`SKILL.md`](SKILL.md)，默认参数见 [`config.yaml`](config.yaml)。

## 它适合做什么

当你需要撰写、重构、审查或润色 NSFC/科研基金申请书的立项依据、研究意义、国内外现状、科学问题或科学假设时使用本 skill。

它重点检查以下论证链：

```text
领域价值 → 已有证据 → 认知缺口 → 科学问题 → 可证伪假设 → 项目切入点 → 研究内容
```

代码负责目标定位、引用/字数检查、diff、备份和回滚；宿主 AI/用户负责理解课题，并自主规划逻辑、术语、论证维度、可读性检查和正文生成。Skill 不会编造文献、实验结果或无法核验的事实。

## 最小可用调用

推荐先只读分析并生成可审阅建议：

```text
请使用 nsfc-justification-writer skill 重构我的立项依据。
输入：/path/to/project/justification.tex，以及相关研究内容和参考文献。
要求：只改正文，保留标题、LaTeX 结构命令、标签和引用；先输出问题清单、修改后正文和 unified diff，不要写入文件。
输出：可审阅的正文建议、引用核验提示和未修改范围说明。
```

确认目标和 diff 后，再明确授权：

```text
我确认上一步的目标文件和 diff。仅将确认的正文变更写入该文件，先备份，写入后再次展示 diff；不要修改其它文件。
```

目标文件可以由用户指定、项目配置声明，或由脚本从 `main.tex` 中只读发现唯一的 `\input`/`\include` 候选。候选不唯一时会停止写入并请你确认；不要求固定文件名、固定标题或 `\subsubsection`。

## 从零开始写作

### 1. 准备信息表

没有成熟草稿时，先生成信息表模板：

```bash
python skills/nsfc-justification-writer/scripts/run.py init
```

也可以交互式填写：

```bash
python skills/nsfc-justification-writer/scripts/run.py init --interactive
```

至少提供：

- 研究对象或应用场景；
- 问题定义和现有研究的 2–4 条关键瓶颈；
- 1–3 条科学问题（疑问句，追问认知缺口）；
- 1 条核心科学假设（可证伪陈述句，不写验证方式）；
- 项目切入点及其与研究内容的衔接。

可选提供前期基础、代表性文献、方法概览、目标字数和术语口径。缺少事实或文献时，先补信息，不要让 AI 猜测。

### 2. 运行写作教练

```bash
python skills/nsfc-justification-writer/scripts/run.py coach \
  --project-root <项目目录> \
  --stage skeleton \
  --info-form <信息表路径>
```

各阶段用途如下：

| 阶段 | 作用 |
| --- | --- |
| `skeleton` | 确认正文边界，梳理事实、缺口、瓶颈→约束映射，并列出待补问题 |
| `draft` | 按已确认范围生成或扩写正文，建立科学问题和假设的论证链 |
| `revise` | 修复逻辑跳跃、缺失引用和不可核验表述 |
| `polish` | 先保护事实与论证，再改善长句、指代、缩写界定和段内衔接 |
| `final` | 按字数、引用、结构和授权范围做最终检查 |
| `auto` | 根据当前正文状态自动选择阶段 |

`coach` 的输出是阶段指导和可复制提示词；真正的正文由 AI/用户生成。若 AI responder 不可用，skill 会返回确定性的检查清单，不会凭空生成事实。

### 3. 形成完整提案并预览

让 AI 输出包含目标文件完整内容的提案，保存为临时文件后运行：

```bash
python skills/nsfc-justification-writer/scripts/run.py preview \
  --project-root <项目目录> \
  --proposal-file /tmp/proposal.tex
```

`preview` 不解析标题、不写入项目文件，只检查：

- 修改行和 unified diff；
- 缺失 bibkey；
- 标题、标签、环境、配置命令或其它结构变化；
- 目标路径和项目根目录边界。

如果发现结构命令变化，先让 AI 重新生成“正文-only”提案；只有明确授权扩大范围时才继续。

### 4. 用户确认后写入

新结构优先由宿主 AI 按确认后的 diff 写入。旧项目可使用兼容入口：

```bash
python skills/nsfc-justification-writer/scripts/run.py apply-section \
  --project-root <项目目录> \
  --title "历史标题" \
  --body-file /tmp/new_body.txt
```

`apply-section` 依赖标题替换，仅用于迁移旧项目；它不是新项目的默认流程。写入前应备份，写入后查看实际 diff，并保留回滚入口。

## 已有草稿的推荐流程

先做只读诊断：

```bash
python skills/nsfc-justification-writer/scripts/run.py diagnose --project-root <项目目录>
python skills/nsfc-justification-writer/scripts/run.py refs --project-root <项目目录>
```

重点看“证据/缺口 → 科学问题 → 科学假设 → 研究内容”是否闭环。`diagnose` 默认且必须执行 Tier2 宿主 AI 语义检查，由宿主 AI 自主规划检查范围；宿主 AI 不可用时必须标记“Tier2 未完成”并转人工复核。随后让 AI 只修改用户指定的正文范围，生成完整提案并运行 `preview`。用户确认后再写入。

## 引用与 DOI 核验

生成引用摘要：

```bash
python skills/nsfc-justification-writer/scripts/run.py refs --project-root <项目目录>
```

按摘要将 DOI、链接或可核验题录补入项目 `references/*.bib`。缺失 key 默认拒绝写入；`apply-section --allow-missing-citations` 仅用于迁移或临时诊断，不应作为常规写作路径。

## 独立检查工具

```bash
# 字数（默认中文字符口径）
python skills/nsfc-justification-writer/scripts/run.py wordcount --project-root <项目目录>

# 语义审查或写作引导（完整流程必须包含 Tier2）
python skills/nsfc-justification-writer/scripts/run.py review --project-root <项目目录>
python skills/nsfc-justification-writer/scripts/run.py coach --project-root <项目目录> --stage auto
```

`diagnose`、`coach` 和 `review` 的结果是建议，不以固定小节数量、标题关键词或固定术语/维度清单作为写入门槛；但完整流程必须包含 Tier2。逻辑、术语、论证维度和专业可读性均由宿主 AI 自主规划，宿主 AI 不可用时报告“Tier2 未完成”并转人工复核。对于“国际领先”“填补空白”等吹牛式或绝对化表述，脚本不维护固定词表；请由宿主 AI 按 [`references/boastful_expression_guidelines.md`](references/boastful_expression_guidelines.md) 进行语义复核。

## 写作边界

- 科学问题应追问未知关系、机制、性质或适用边界，不写成“开发/构建/实现”的研究目标。
- 科学假设应是可证伪的预测性陈述，不把“通过某实验验证”写进假设句。
- 假设前优先放领域事实、已有研究和认知缺口；本项目干预、比较、终点和技术路线集中放在假设之后。
- 外部论文的方法学描述可以作为现状证据，不自动判定为本项目方案。
- 不使用“国际领先”“国内首次”等无法核验的绝对化表述；应改为可比较的指标、基线或适用边界。
- 专业可读性复核不是科普化：保留已核验事实、必要术语、限定条件、引用命令和 LaTeX 结构。
- 默认不修改 `main.tex`、配置文件、`.cls`、`.sty` 或用户未授权的正文范围。

## 配置要点

| 配置 | 作用 |
| --- | --- |
| `style.mode` | `theoretical`、`mixed` 或 `engineering`，改变措辞和证据重心 |
| `targets.justification_tex` | 目标正文相对路径；为空时只读发现唯一候选 |
| `references.allow_missing_citations` | 默认 `false`，缺失 bibkey 时拒绝写入 |
| `guardrails.output_mode` | 默认 `preview`；写入必须有明确授权 |
| `guardrails.allowed_write_files` | 自定义正文目标的精确白名单 |
| `word_count` | 字数统计目标和口径，不强制固定章节结构 |

自定义目标文件时，请同步在 `guardrails.allowed_write_files` 中声明相对路径。不要把 `.cls`、`.sty`、`main.tex` 或配置文件加入白名单，除非你明确承担相应风险并授权。

## 写入后的版本管理

```bash
python skills/nsfc-justification-writer/scripts/run.py list-runs
python skills/nsfc-justification-writer/scripts/run.py diff \
  --project-root <项目目录> --run-id <run_id>
python skills/nsfc-justification-writer/scripts/run.py rollback \
  --project-root <项目目录> --run-id <run_id> --yes
```

## 常见问题

**为什么没有直接写文件？**

默认是可逆的 `preview` 模式。先确认目标和 diff，再明确授权写入。

**文件名或标题宏不同会被判为空吗？**

不会。新流程不依赖固定文件名、标题命令或小节数量；旧 `apply-section` 仅保留为兼容提示。

**假设前出现方法名是否一定错误？**

不一定。外部论文的方法学描述可以作为现状证据；只有把本项目方案提前作为论证主线时，才建议后移。

**为什么建议拆句或补过渡？**

这是面向大同行的阅读负担复核。建议应说明位置、障碍、影响和保真改法；已经清楚的专业表述不需要为了通俗而改写。

**缺少引用怎么办？**

Skill 不会编造引用。请提供 DOI、链接或可核验题录，并先补齐项目 `references/*.bib`。
