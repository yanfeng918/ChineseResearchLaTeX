---
name: nsfc-justification-writer
description: 当用户要求写作、重构、审查或润色 NSFC/科研基金申请书的立项依据、研究意义、国内外现状、科学问题或科学假设时使用。以语义论证和可核验性为核心，支持任意文件名、标题命令和 LaTeX 结构；默认全自动完成诊断、成稿、校正、备份和写入，不向用户发起中途确认或审核问题。
metadata:
  author: Bensz Conan
  short-description: 科研立项依据语义写作与安全改写
  keywords:
    - nsfc-justification-writer
    - 立项依据
    - 科学问题
    - 科学假设
    - 研究意义
    - 国内外现状
    - LaTeX
  triggers:
    - nsfc-justification-writer
    - 立项依据
    - 研究意义
    - 为什么要做
    - 国内外现状
    - 现有不足
    - 科学问题
    - 科学假设
---

# 科研立项依据写作器

## BenszAPI 任务工作区

本 Skill 的新任务中间文件统一写入 `./.bensz-api/task-{yyyymmdd-hhmm}-{简短描述}/{skill名}/input|output|log/`。同一任务复用一个任务根目录；多 Skill 协作才创建 `shared/`。正式交付物不写入该目录，历史隐藏目录只允许显式兼容读取、迁移或清理。

## 与 bensz-collect-bugs 的协作

- 本 skill 设计缺陷导致 bug 时，按 `bensz-collect-bugs` 记录到 `~/.bensz-skills/bugs/`，不要改用户本地已安装 skill；可用 workaround 时先记录再继续。
- 仅用户明确要求公开上报时，才用本地 `gh` 通过该 skill 上传新增 bug 到 `huangwb8/bensz-bugs`；不 pull/clone 整仓库。

## 任务边界

- 自动理解目标文件、段落和目标，直接生成成稿并写入安全目标；同时输出 unified diff、备份路径和假设记录。
- 只改自动确定且通过白名单的正文；保留标题、章节/环境命令、标签、引用命令和配置命令。
- 只改白名单正文文件，不改 `main.tex`、配置文件、`.cls`、`.sty`。目标不唯一时按“已配置目标 → 文件名含立项依据/justification → 字典序首项”自动选择并记录选择依据。
- 目标可来自用户或配置，不假定固定文件名。
- 引用 key 必须能在项目 `.bib` 中核验；不新增无法核验的引用、结果或绝对化结论。

## 语义写作规则

1. 先写领域价值/必要性与已有证据，再将瓶颈转成待解释的关系、机制、性质或边界。
2. 科学问题用疑问句追问认知缺口；假设用可证伪陈述句预测结果。研究目标、路线、验证终点不冒充问题/假设。
3. 假设前以事实、文献和缺口为主；干预、比较、终点、路线放在假设后。外部文献的方法描述可作证据，不等于本项目方案前置。
4. 切入点/贡献无需固定标题或段数；理论、混合、工程导向只改变措辞与证据重心，不是通过门槛。
5. 逻辑与引用检查后必须读取 `references/tier2_semantic_review.md`，由当前宿主 AI 直接执行 Tier2 语义检查。由宿主 AI 自主规划术语、论证维度和可读性，输出“位置/障碍/影响/保真改法”。检查长句层级、指代、缩写/新概念、抽象名词、衔接和无效修饰；不科普化或因必要限定强改。
6. 可读性改写须保留已核验事实、对象、限定、问题/假设、引用、标签和 LaTeX 结构；无法保真保留原句并记录风险，不补事实/证据。

措辞边界：吹牛式、绝对化或无依据夸大由宿主 AI 按 `references/boastful_expression_guidelines.md` 语义复核并归入逻辑/表达建议；Python 只做路径、结构命令、引用 key 等确定性检查，不用固定词表判定。

## 推荐工作流

1. 读取目标文件和上下文；目标缺失时自动追踪 `main.tex`，按确定性优先级选择候选，必要时创建白名单内的默认正文文件。
2. 检查问题—假设—证据—研究内容闭环及引用 key；随后必做 Tier2，结果分为“事实问题、逻辑问题、表达建议”。
3. 完成检查后自动复核专业可读性；`polish` 先在内部锁定事实/逻辑/引用，再做受约束精修，不向用户提问。
4. 自动生成完整正文或 unified diff；发现结构命令变化时自动回退为正文-only 提案并重试。
5. 通过白名单、引用和质量检查后自动写入；写入前备份，写入后展示 diff、假设与回滚入口。
6. 字数与引用检查可独立运行；流程不绑定固定标题或维度清单。

## 输出契约

默认输出：

```text
目标文件（自动选择及依据）：...
修改范围：仅白名单正文
主要问题：...
建议正文或 unified diff：...
引用与事实守护：...
未修改：标题、结构命令、配置和样式文件
```

可读性发现归入“表达建议”，不当作事实错误；Tier2 是完整诊断必选项，由当前宿主 AI 直接完成，不经过 Python responder 或 fallback。

无法明确正文边界时按最小安全正文范围继续；若材料不足，采用保守假设并在“假设与待核验项”中记录，不暂停等待用户输入。始终执行白名单、备份、缺失 bibkey 检查并报告实际变更。

## 脚本说明

- `scripts/run.py preview`：自动生成 diff 并按 `guardrails.output_mode` 写入；需要只读检查时显式加 `--dry-run`。
- `refs`、`wordcount`：独立引用/字数工具；术语、论证维度和可读性由 Tier2 宿主 AI 规划。
- `diagnose`：仅执行 Tier1 确定性诊断，并提示宿主 AI 读取 `references/tier2_semantic_review.md`；不主动调用模型、不生成 Tier2 fallback 结论。
- `coach`、`review`：主流程必须包含由宿主 AI 直接执行的 Tier2 语义检查。吹牛式/绝对化风险按参考准则由 AI 判断，脚本不做固定短语命中。
- `apply-section`：legacy 标题替换写入；新流程优先使用完整正文提案自动写入，不依赖 `\\subsubsection`。
- `diff`、`rollback`：查看或回滚自动写入变更；回滚命令仍需显式 `--yes` 以避免误操作。

## 参考资料

按任务先阅读 `references/tier2_semantic_review.md`，再按其中需要阅读 `references/scientific_question_guidelines.md`、`references/scientific_hypothesis_guidelines.md`、`references/professional_readability_guidelines.md` 和 `references/boastful_expression_guidelines.md`。用户流程、脚本用法和架构边界见 `README.md`；检查维度由宿主 AI 自主规划，不依赖固定术语矩阵或四维度门槛。
