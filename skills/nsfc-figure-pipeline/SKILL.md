---
name: nsfc-figure-pipeline
description: >
  Grant-specific academic figure planning and prompt pipeline for finalized NSFC-style proposal PDFs.
  It MUST include a research background figure, an overall research framework figure, and a technical route figure,
  and may recommend additional figures when they add clear scientific communication value. Reuses
  Azhi-ss/academic-figure-skills and stops before image generation.
---

# NSFC Academic Figure Pipeline

## Role

This skill is a grant-specific adapter over `Azhi-ss/academic-figure-skills`.
It does not replace or copy the upstream skills. It orchestrates them for a Chinese research-grant proposal and stops at prompt delivery.

The finalized proposal PDF is the scientific source of truth.

Pipeline:

`Final proposal PDF -> Figure Plan -> Visual Logic -> Prompts for ALL selected figures -> STOP`

## Upstream skills

Read each upstream skill only when its stage runs:

- Figure planning:
  `/home/yanfeng/.agents/skills/academic-paper-analyzer-figure-planner/SKILL.md`
- Color / visual logic:
  `/home/yanfeng/.agents/skills/academic-figure-color-expert/SKILL.md`
- Academic figure prompt:
  `/home/yanfeng/.agents/skills/academic-figure-prompt/SKILL.md`

Do not edit the upstream skills.
Do not use any image-generation backend in this workflow.

## Inputs

Required:

- `PROJECT_DIR`: the grant project directory.
- Final proposal PDF: `${PROJECT_DIR}/main.pdf` unless the user explicitly provides another PDF.

If `PROJECT_DIR` is not explicitly provided, infer it from the user's target path or current working directory. Do not silently switch to another project.

## Mandatory core figure set

The Figure Plan MUST contain at least these three figures:

1. 研究背景图
2. 总体研究框架图
3. 技术路线图

These are mandatory anchors, not an exclusive list.

## Additional figure recommendation policy

After analyzing the proposal, actively consider whether additional figures would materially improve the application.

Possible additional figure types include, but are not limited to:

- 科学问题关系图 / 科学问题分解图
- 关键机制或核心方法机理图
- 研究内容之间的耦合关系图
- 数据—知识—模型关系图
- 实验与验证框架图
- 创新点映射图
- 场景—问题—方法—成果对应图
- 研究基础 / 可行性支撑图
- 多源数据或多模态资源组织图
- 评价指标与验证闭环图

Do NOT add figures merely to increase quantity.

An additional figure should be recommended only when all of the following are true:

1. It communicates an important idea that is not already clear in the three mandatory figures.
2. The figure has direct evidence in the proposal.
3. It would reduce cognitive load compared with explaining the same content only in prose.
4. It has a distinct scientific communication purpose.
5. It does not substantially duplicate another planned figure.

Normally 3–6 total figures is a reasonable planning range, but do not impose a hard maximum if the proposal clearly justifies more.

## Output layout

Create if missing:

```text
${PROJECT_DIR}/figures/
├── figure-plan.md
├── visual-logic.md
├── prompts/
│   ├── 01-research-background.md
│   ├── 02-overall-framework.md
│   ├── 03-technical-route.md
│   └── 04-<additional-figure-slug>.md   # only when recommended
└── pipeline-summary.md
```

The exact prompt filenames for additional figures MUST be declared in `figure-plan.md`.
Use stable numbered ASCII kebab-case filenames.

Do not create raster or vector image files in this skill.

---

## Stage 0 — Preflight and freshness gate

Before any figure work:

1. Confirm `${PROJECT_DIR}/main.pdf` exists and is readable.
2. Confirm it is non-empty and can be parsed/read.
3. Check whether proposal source files are newer than the PDF. At minimum inspect `.tex` and `.bib` files under the project directory.
4. If relevant proposal sources are newer than `main.pdf`, treat the PDF as stale and STOP. Ask the parent proposal pipeline to rebuild it first.
5. Never use a stale PDF merely because it exists.

Useful shell check:

```bash
find "$PROJECT_DIR" -type f \( -name '*.tex' -o -name '*.bib' \) -newer "$PROJECT_DIR/main.pdf" -print
```

If the command prints relevant proposal source files, the PDF must be rebuilt before continuing.

---

## Stage 1 — Proposal understanding

Read the finalized proposal PDF sufficiently to understand, at minimum:

- 立项依据 / 研究背景与意义
- 国内外研究现状或研究缺口
- 核心科学问题 / 关键问题
- 研究目标
- 研究内容 and its internal decomposition
- 拟解决的关键机制 or method logic
- 研究方案 / 技术路线
- 数据、实验、验证与评价设计
- 创新点
- 研究基础与可行性 when relevant

For every planned visual element, keep an evidence trail to the proposal. Prefer section/page anchors when available.

Do not invent research content to make a figure look fuller.

---

## Stage 2 — Figure Plan

Read and strictly follow:

`/home/yanfeng/.agents/skills/academic-paper-analyzer-figure-planner/SKILL.md`

Adapt its paper-oriented planning to a grant-application context.

### Required figure-selection behavior

The planner MUST:

1. Include the three mandatory core figures.
2. Scan the proposal for additional figure opportunities.
3. Recommend additional figures only when they pass the Additional figure recommendation policy.
4. Explain why each additional figure is worth adding.
5. Explicitly reject redundant figure ideas.

### Figure 1 — 研究背景图

Primary communication task:

`现实/政策/产业需求 -> 研究对象或资源特征 -> 核心矛盾 -> 现有研究缺口 -> 科学问题`

This figure explains **why the project is necessary**.

Avoid turning it into a method pipeline.

### Figure 2 — 总体研究框架图

Primary communication task:

`研究对象/输入 -> 核心研究内容 -> 关键科学机制/关系 -> 研究目标 -> 统一验证体系`

This figure explains **what the project studies and how the research contents fit together conceptually**.

Avoid duplicating step-by-step implementation details from the technical route.

### Figure 3 — 技术路线图

Primary communication task:

`数据/输入 -> 处理与建模步骤 -> 关键方法/模型 -> 实验与验证 -> 输出/指标`

This figure explains **how the project will actually be executed**.

Avoid repeating the background problem narrative.

### Additional figures

For every additional figure, define a distinct communication task in one sentence and state exactly which gap in the three mandatory figures it fills.

### Required per-figure fields

For EVERY selected figure, include:

- Figure ID and Chinese title
- Status: `MANDATORY` or `RECOMMENDED`
- Priority: `P0`, `P1`, or `P2`
- Recommended prompt filename
- Scientific communication purpose
- One-sentence take-home message
- Why this figure is needed
- Proposal evidence / source sections
- Core scientific question or concept represented
- Information hierarchy
- Major modules
- Module contents and labels
- Logical relations
- Arrow / connector semantics
- Reading direction
- Recommended composition/layout
- Suggested aspect ratio
- Complexity level
- Expected placement in the proposal
- Content intentionally excluded
- Difference from every closely related figure
- Risks of redundancy or ambiguity

### Figure-set prioritization

Use:

- `P0`: indispensable; normally the three mandatory core figures
- `P1`: strongly recommended; materially improves scientific communication
- `P2`: optional; useful only if page space permits

Do not generate prompts for rejected figure ideas.

### Cross-figure consistency and redundancy check

Before accepting the Figure Plan, verify:

- The three mandatory figures are present.
- Every additional figure has a unique communication purpose.
- The same module is not copied wholesale across multiple figures.
- Background figure focuses on motivation/gap/problem.
- Framework figure focuses on conceptual research structure.
- Technical route focuses on execution sequence and validation.
- Additional figures fill a genuine information gap.
- Every substantive claim can be traced to the proposal.

Write the complete result to:

`${PROJECT_DIR}/figures/figure-plan.md`

The Figure Plan must also include a final **Figure Inventory** section listing all selected figures in execution order, for example:

```text
F01 | 研究背景图 | MANDATORY | P0 | prompts/01-research-background.md
F02 | 总体研究框架图 | MANDATORY | P0 | prompts/02-overall-framework.md
F03 | 技术路线图 | MANDATORY | P0 | prompts/03-technical-route.md
F04 | <推荐图名称> | RECOMMENDED | P1 | prompts/04-<slug>.md
```

### Review mode

If the user's request explicitly says to confirm/review the Figure Plan before continuing, STOP here and wait for confirmation.

If the user asks for an end-to-end / one-shot pipeline, save and report the Figure Plan, then continue automatically.

---

## Stage 3 — Unified visual logic

Read and strictly follow:

`/home/yanfeng/.agents/skills/academic-figure-color-expert/SKILL.md`

Authoritative inputs:

1. Final proposal PDF
2. `${PROJECT_DIR}/figures/figure-plan.md`

The output is not merely a palette. Build a reusable **Visual Logic** for the complete selected figure set.

For Chinese research-grant applications, default to a classic academic family unless the user explicitly requests another style:

- white or near-white background
- restrained dark navy as primary color
- limited cyan/teal/blue accent
- dark gray connectors and body text
- flat 2D vector infographic
- clear border hierarchy
- sparse fills; color encodes semantics rather than decoration
- print-friendly and grayscale-aware
- no large gradients
- no glow
- no glassmorphism
- no 3D
- no commercial poster aesthetics
- no excessive shadows

Define at minimum:

- visual style family
- background
- primary / secondary / accent palette with HEX values
- semantic color mapping
- text hierarchy
- border hierarchy
- connector hierarchy
- arrow semantics
- container hierarchy
- emphasis rules
- icon rules
- typography
- line weights
- corner radius policy
- whitespace policy
- grayscale / accessibility considerations
- shared rules across all selected figures
- figure-specific exceptions where scientifically justified

Write to:

`${PROJECT_DIR}/figures/visual-logic.md`

---

## Stage 4 — Academic figure prompts

Read and strictly follow:

`/home/yanfeng/.agents/skills/academic-figure-prompt/SKILL.md`

Authoritative inputs:

1. Final proposal PDF
2. Figure Plan
3. Visual Logic

Generate one self-contained prompt package for **EVERY figure listed in the Figure Inventory**, not only the three mandatory figures.

The downstream image model must NOT be assumed to have access to the proposal PDF, Figure Plan, or Visual Logic. Therefore each prompt must explicitly carry the content required to render the figure correctly.

For each figure, include the outputs required by the upstream prompt skill, plus:

- diagram purpose
- exact figure type
- layout and reading direction
- module names and internal labels
- module hierarchy
- arrow/connector relationships
- formulas/symbols only when present and necessary in the proposal
- visual hierarchy
- palette and semantic color rules
- typography
- stroke hierarchy
- whitespace
- target aspect ratio
- academic style constraints
- negative constraints

Write each prompt to the exact filename declared in the Figure Inventory.

### Prompt grounding rule

The prompt-generation stage may compress, reorganize, and visually encode proposal content, but must not introduce new:

- methods
- datasets
- mechanisms
- experiments
- metrics
- claims
- conclusions
- research tasks

that are absent from the proposal or explicitly approved Figure Plan.

---

## Stage 5 — Cross-prompt QA

Before completion, check the entire prompt set together:

1. Scientific grounding: all major content comes from the proposal.
2. Core coverage: the three mandatory figures exist and are complete.
3. Additional figure justification: every extra figure still adds distinct value.
4. Role separation: no two figures are near-duplicates.
5. Terminology consistency: the same research object and method use the same wording across figures.
6. Visual consistency: shared palette, typography, border and arrow conventions are preserved.
7. Prompt independence: each prompt can be copied to an image model by itself.
8. Inventory consistency: every Figure Inventory entry has exactly one prompt file.
9. No rendering instructions invoke tools in the current workflow.

If issues are found, revise the plan/visual logic/prompts before finalizing.

---

## Stage 6 — Summary and STOP

Write `${PROJECT_DIR}/figures/pipeline-summary.md` containing:

- source PDF path
- PDF freshness status
- mandatory figure count
- additional recommended figure count
- complete Figure Inventory
- Figure Plan path
- Visual Logic path
- all prompt paths
- rejected figure ideas and why they were rejected
- unresolved scientific ambiguities
- unresolved visual ambiguities
- explicit status: `PROMPT_ONLY_COMPLETE`

Final user-facing report should be concise and list the artifact paths.

## Hard stop rule

After all prompt files in the Figure Inventory and the summary are complete, STOP.

Never in this skill:

- call image generation
- run gpt-image-generation
- invoke NanoBanana / Gemini / Midjourney
- invoke sensenova image generation
- create PNG/JPG/WebP/SVG/PDF figure assets
- continue into rendering merely because an image backend is available

Image generation belongs to a separate workflow.
