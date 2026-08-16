# 基金画像规范（grant-profile.yaml）

## 这个文件解决什么问题

`skills/` 下的写作类 skill 原先按固定路径寻址，例如立项依据写死 `extraTex/1.1.立项依据.tex`。仓库里实际存在的四种模板并不共用一套章节切分：

| 项目 | 立项依据 | 研究内容 | 特色与创新 | 年度研究计划 |
|---|---|---|---|---|
| `NSFC_Young` | `1.1.立项依据.tex` | `2.1.研究内容.tex` | `2.2` 独立文件 | `2.3` 独立文件 |
| `NSFC_2026_Education` | `1.1.立项依据.tex` | `1.2.内容目标问题.tex` | `1.4` 独立文件 | `1.5` 独立文件 |
| `GDNSF_General` | `1.**立论**依据.tex` | `2.研究内容.tex` | 并入研究内容 | 并入研究内容 |
| `GXNSF_General` | `1.1.立项依据.tex` | `1.2.研究内容目标与关键科学问题.tex` | `1.4` 独立文件 | `1.5` 独立文件 |

广东省基金把"立项依据"写作"立**论**依据"，靠文件名匹配的 glob（`*立项依据*.tex`）直接漏掉；它也没有独立的创新与年度计划文件，但官方提纲明确要求"应提炼出研究目标、特色与创新点、年度研究计划"。

画像把"章节角色 → 实际文件"抽出来放在项目里，skill 只认角色、不认路径。

## 文件位置

标书项目根目录下的 `grant-profile.yaml`，与 `main.tex` 同级。

**画像可选**。项目里没有这个文件时，各 skill 回退到 `config.yaml` 里的 NSFC 默认路径，既有项目行为不变。

## 生成与校验

```bash
# 从 main.tex 的 \input 链推断并生成（会跳过被注释掉的章节）
python scripts/grant_profile.py infer --project-dir projects/GDNSF_General

# 只打印不写文件
python scripts/grant_profile.py infer --project-dir <dir> --dry-run

# 校验画像与项目实际文件是否一致
python scripts/grant_profile.py validate --project-dir <dir>

# 查询单个角色解析到哪里
python scripts/grant_profile.py show --project-dir <dir> --role justification
```

推断结果**必须人工复核**。脚本能认出的只是文件名里的关键词，认不出"这个模板要不要求写创新点"。

## 结构

```yaml
grant:
  name: "广东省自然科学基金-面上项目"
  agency: "广东省科学技术厅"
  duration_years: 3       # 决定年度计划写几年
  source: "2024年度申请书模板"

roles:
  justification:
    file: "extraTex/1.立论依据.tex"
  innovation:
    merged_into: research_content
  expected_results:
    absent: true

length_budget:
  unit: cjk_chars
  pages:
    max: 28
    hard_max: 30
  by_role:
    justification: [7000, 9000]

review:
  grant_type: "省级面上项目"
  criteria:
    - "研究的科学技术价值"
```

### grant

| 字段 | 说明 |
|---|---|
| `name` | 基金全称，出现在各 skill 的日志与报告里 |
| `agency` | 资助机构 |
| `duration_years` | 资助年限。**不是常数**：NSFC 面上 4 年、青年 3 年、多数省基金 3 年。年度计划检查按此判断写没写全，写死 3 年会让 4 年期项目漏掉第 4 年 |
| `source` | 依据的官方模板版本，便于日后核对 |

### roles

每个角色**必须且只能**是以下五种状态之一：

| 状态 | 含义 | skill 行为 |
|---|---|---|
| `file: <相对路径>` | 有独立文件承载 | 直接读写该文件 |
| `files: [路径, …]` | 该角色跨多个文件 | 第一个为主写入目标，其余一并放行；按各文件的小节主题分配内容 |
| `merged_into: <角色>` | 无独立文件，内容须写进目标角色 | 跟随到宿主文件，**只改写对应小节**，不整文件覆盖 |
| `absent: true` | 本模板确实不要求 | 跳过对应阶段 |
| `unresolved: true` | 推断不出，待人工裁决 | **停下来问用户**，不得当作 absent |

`files:` 用于一个角色被模板拆成多节的情况。广西 2026 自治区重点研发把"立项依据"拆成"国外研究现状及趋势"与"国内研究现状及趋势"两节，各限 1500 字；只认第一个文件会让另一半内容无处落地且不报错。

## 两种寻址方式

顶层 `addressing` 决定正文放在哪里，默认 `file`。

### file（默认）

一节一文件，正文在 `extraTex/*.tex`。角色用 `file:` / `files:` 声明。

### macro

部分模板不按文件切分，而是把正文集中定义成 `\newcommand` 宏，再由版式文件按固定坐标渲染。`projects/NSFC_2027_Silk_Road_Smart_Logistic_v2` 即如此：22 个宏定义在 `content.tex`，由 `sections/form-pages.tex` 的 `\ApplicationAnswer{x}{y}{\宏名}` 摆放。

```yaml
addressing: macro
macro_file: "content.tex"
roles:
  justification:
    macros: [ForeignResearchContent, DomesticResearchContent]
  research_content:
    macro: ResearchContent
```

**写作红线**：宏级寻址下所有角色共用同一个 `macro_file`。必须只替换目标宏的宏体，整文件重写会冲掉其余二十多个角色的正文。`resolve_role_files` 返回的是 `macro_file`，真正的定位靠 `resolve_role_macros` 拿到的宏名。

读写用 `grant_profile_reader.py` 提供的原语，不要自己写正则：

- `read_macro_body(text, name)` → 宏体原文，找不到或括号不配对返回 `None`
- `replace_macro_body(text, name, new_body)` → `(新全文, 是否成功)`

它们逐字符配对花括号，正确处理嵌套 `\textbf{...{...}}`、转义 `\{` `\}`，以及 `$\geq 99\%$` 这类会被误判成注释的转义百分号。边界由 `tests/grant-profile/test_macro_addressing.py` 锁定。

宏模式下会自动关闭两项不适用的诊断：小节数量检查（宏体内没有 `\subsubsection`）与页数估算（表单模板按固定坐标框排版）。

**篇幅红线**：`\ApplicationAnswer` 展开成 `\parbox[t][高度][t]{宽度}`，是固定坐标定宽框。内容超框时 **LaTeX 不报错、页数不变、超出部分直接从 PDF 里消失**。

实测（把 `projects/NSFC_2027_Silk_Road_Smart_Logistic_v2` 的一节灌到 4 倍）：

| 信号 | 结果 |
|---|---|
| `Overfull \vbox` 警告 | **0**（完全没报） |
| 页数 | 14 → 14（无变化） |
| 注入 28 个重复段落 | PDF 中只剩 **12** 个 |

所以基于编译日志或 bbox 的检查会漏报。真实上限取"模板标注字数"与"框高容量"的**较小者**，而框高容量只能实测：

```bash
python skills/nsfc-length-aligner/scripts/check_box_overflow.py --project-dir <项目> --build
```

它回读 PDF 逐个核对宏的尾句是否还在，截断时报出丢失字数与比例。写作后必须跑一次——字数达标不等于内容完整。

`infer` 会自动识别寻址方式：某个 `.tex` 定义了 ≥8 个宏且过半命中宏名词表（`MACRO_KEYWORDS`）时判为宏级寻址，否则走 `main.tex` 的 `\input` 链。判错会导致画像几乎全是 `absent`，务必核对 `infer` 输出的 `[识别]` 行。

`merged_into` 与 `absent` 的区别是这套设计的关键。广东省基金没有创新与年度计划文件，但模板要求写；标成 `absent` 会让 writer 静默丢掉这两块内容，评审时才发现。`unresolved` 的存在是为了让"推断不出"无法被默默糊弄过去——`validate` 会直接判失败。

角色词表（`scripts/grant_profile.py:ROLE_KEYWORDS`，新增模板时优先在此扩充别名）：

通用角色：`justification` 立项依据 / `research_content` 研究内容 / `key_questions` 关键科学问题 / `research_scheme` 研究方案与可行性 / `innovation` 特色与创新 / `yearly_plan` 年度研究计划 / `expected_results` 预期研究结果 / `research_foundation` 研究基础 / `work_conditions` 工作条件 / `team_members` 项目组人员 / `ongoing_projects` 申请或承担科研项目 / `completed_projects` 项目完成情况 / `ai_disclosure` 生成式人工智能声明 / `budget_plan` 经费与预算 / `management` 组织实施与管理 / `site_scale` 实施地点及规模 / `attachments` 附件清单 / `other` 其他

产业/重点研发类基金常见的独立章节（NSFC 模板里并入其它章节，故 NSFC 项目中多为 `absent`）：`guideline_alignment` 与指南方向的关联 / `assessment_indicators` 考核指标与评测方式 / `economic_benefits` 预期经济社会效益 / `partners` 协作单位 / `task_division` 任务分工 / `intl_cooperation` 国际合作与交流 / `safeguards` 保障措施 / `ip_strategy` 知识产权与成果管理 / `risk_analysis` 风险分析及对策

其中 `justification`、`research_content`、`innovation`、`yearly_plan`、`research_foundation` 是**核心写作角色**：推断不到时产出 `unresolved` 而非 `absent`。

承诺性说明章节（"不同类型国基情况""同年单位不一致"等）不映射角色，写作类 skill 本就不碰它们，`infer` 只作提示不作待办。

### length_budget

`by_role` 的键是角色名，值是 `[min, max]` 区间（单位由 `unit` 决定）。`nsfc-length-aligner` 会把它解析成**精确文件路径**，比 `config.yaml` 里的文件名 glob 准确。

`pages.max` / `pages.hard_max` 差异最大：NSFC 正文 30 页，多数省基金远低于此。填 `null` 表示未知，此时页数检查会跳过并明说，而不是拿 NSFC 口径顶替。

### review

`grant_type` 与 `criteria` 供 `nsfc-reviewers` 使用。

**额度红线**：`nsfc-reviewers/config.yaml:funding_context` 里的额度区间（30–40 万 / 50–60 万）只适用于 NSFC。非 NSFC 基金且画像未给额度时走保守策略，不得套用。

## 各 skill 的接入方式

| Skill | 读取项 | 落地方式 |
|---|---|---|
| `nsfc-justification-writer` | `roles.justification` | `config.yaml:grant_profile.role_map`，另有 `readonly_role_map` 供术语一致性对照（**不进写入白名单**） |
| `nsfc-research-content-writer` | `roles.research_content/innovation/yearly_plan`、`grant.duration_years` | 合并角色的内容检查转到宿主文件执行，不跳过 |
| `nsfc-research-foundation-writer` | `roles.research_foundation/work_conditions` | 工作条件可为 `absent`，此时在研究基础正文内查条件表述 |
| `nsfc-length-aligner` | `length_budget` 全部 | 覆盖 `config.yaml:length_standard` |
| `nsfc-qc` | `length_budget.pages`、`grant.name`、`roles` | 检查逻辑本身模板无关，仅用于报告口径 |
| `nsfc-reviewers` | `review.*`、`grant.duration_years` | SKILL.md 指令层 |
| `nsfc-full-pipeline` | `roles` 全部 | Stage 00 优先用画像，回退才走 `main.tex` 启发式 |

## 维护约定

- 角色词表、推断与校验逻辑只在 `scripts/grant_profile.py` 维护
- 各 skill 里的 `grant_profile_reader.py` 是它的精简**只读**版，随 skill 分发（skill 安装到 `~/.claude/skills/` 后是自包含目录，不能跨 skill import）。改动优先改仓库根那份，再同步
- 新增基金模板时，先 `infer` 再人工复核，不要手写整个文件
- 不要为了让某个模板跑通而往 `nsfc-full-pipeline/config.yaml:layout.known` 里继续堆布局——那是画像出现前的旧机制
