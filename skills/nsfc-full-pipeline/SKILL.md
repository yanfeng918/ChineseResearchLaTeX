---
name: nsfc-full-pipeline
description: Use this skill whenever the user wants to automatically write, resume, revise, quality-control, review, repair after reviewer feedback, or compile a National Natural Science Foundation of China (NSFC) Regional Science Fund proposal in a ChineseResearchLaTeX project. This skill orchestrates the full proposal workflow with checkpoints and reuses NSFC/research sub-skills. It must be used for end-to-end NSFC proposal generation, for resuming a stalled pipeline, and for automatically applying P0/P1 fixes after QC or simulated review when the fixes can be made from available evidence.
---

# NSFC Full Pipeline

## Workspace Convention

This skill deliberately writes to the proposal project itself rather than to a `.bensz-api/` task workspace. `docs/workflow_status.yaml` is the resume checkpoint, `docs/*.md` are stage records the user reads and edits, and `review/*.md` are deliverable reports. Under `skills/WORKSPACE.md` these count as formal deliverables, which are excluded from the task workspace.

Scratch artifacts that are not deliverables — retrieval caches, intermediate JSON, command logs — still follow the standard convention and go to `./.bensz-api/task-{yyyymmdd-hhmm}-{简短描述}/nsfc-full-pipeline/input|output|log/`. Sub-skills invoked by this pipeline keep their own workspace behavior; share one task root across the run rather than creating one per sub-skill.

## Purpose

This skill controls a recoverable full-process writing pipeline for NSFC Regional Science Fund proposals based on ChineseResearchLaTeX.

It coordinates topic extraction, literature review, scientific question refinement, research plan design, proposal writing, research foundation writing, citation alignment, length control, humanization, QC, simulated review, targeted repair, and final compilation.

## Core Principles

- Work in checkpoint/resume mode. Never restart from the beginning when previous outputs already exist.
- Read before writing. Inspect existing files, checkpoints, and generated artifacts before deciding the next stage.
- Do not fabricate papers, projects, data, awards, platforms, team achievements, prior experiments, funding information, or personal declarations.
- If required real information is missing, create a questionnaire in `docs/` and mark the stage as `need_user_input`.
- Prefer incremental updates over wholesale rewriting unless the user explicitly requests full regeneration.
- Keep the project aligned with `AGENTS.md`; do not drift from the stable research scope.
- Only modify proposal content files, docs, references, review reports, workflow status, and generated artifacts unless the user explicitly authorizes template changes.
- Do not modify `extraTex/@config.tex` or layout/template files unless the user explicitly requests template changes.
- After QC or simulated review, do not stop at advice when the user asks to continue, repair, fix, or automatically modify. Convert actionable findings into concrete edits, apply them, and rerun the relevant checks.

## CS/AI/Agent/Time-Series Proposal Defaults

When `AGENTS.md`, `docs/00_项目基本信息.md`, or the user request indicates a computer science direction such as 人工智能, 多模态, 大模型, 智能体/Agent, 信息检索, 推荐, 生成式检索, 时间序列, 时空预测, 异常检测, or related machine learning topics, apply these additional defaults:

- Treat the proposal as a computational-method NSFC application, not only a narrative writing task.
- The research scheme text resolved in stage 00, whether a dedicated 方案及可行性 file or the scheme part of the 研究内容 file, must contain formal problem definition, notation, model/input-output mapping, objective or loss functions, and evaluation/constraint definitions. Aim for 4-8 meaningful formula blocks across representation learning, model optimization, inference/decoding, and evaluation. Each formula must be followed by a short variable explanation and a sentence linking it to an experiment or metric.
- Avoid decorative math. Do not add formulas that merely restate text without supporting a trainable model, optimization objective, inference rule, evaluation metric, or falsification path.
- For agent-oriented topics, include state/action/memory/tool-use or planning equations when appropriate.
- For time-series topics, include temporal input window, forecasting/anomaly target, temporal dependency modeling, prediction loss, uncertainty or robustness metric when appropriate.
- For retrieval/recommendation/multimodal topics, include query-item scoring, representation alignment, ranking/generation objective, constrained decoding, Recall@K/NDCG/MRR or constraint satisfaction definitions when appropriate.

## Reference Sufficiency Gate

Reference quantity and coverage are part of proposal quality, not a final formatting detail.

- For CS/AI/Agent/Time-Series NSFC proposals, the proposal bibliography should normally contain 30-50 verifiable BibTeX entries, unless the user explicitly requests a shorter reference list. Do not leave a full proposal with fewer than 25 references after the literature stage.
- Ensure coverage across: seminal foundations, recent 3-5 year advances, representative methods, datasets/benchmarks, evaluation metrics, domain applications, and known limitations or failure modes.
- For fast-moving AI fields, prefer at least 60% of references from the last 5 years while retaining a small number of unavoidable seminal older works.
- The 立项依据 file should normally cite 20-35 references, with citations close to the claims they support rather than piled at paragraph ends.
- Before completing stage 05, check that `references/myexample.bib` has enough entries and that Part One cites a meaningful subset. If the bibliography is too thin, run additional literature review or create `docs/参考文献补充清单.md` with missing reference groups and mark the relevant stage as `need_user_input`.
- Never invent references. Add or cite only entries that are verifiable from user-provided materials, project literature-review artifacts, official metadata, DOI/Crossref/OpenAlex/Semantic Scholar records, or other reliable bibliographic sources.

## Review-Driven Auto-Repair Policy

When the user says `得到评审后`, `根据评审修改`, `自动修改`, `继续修复`, `P0/P1修复`, `按模拟评审修改`, or similar, treat this as permission to edit proposal content files directly after reading the latest QC and simulated review outputs.

The default repair loop is:

1. Read the latest `review/质量控制报告.md`, `review/模拟专家评审_全稿.md`, `review/引用一致性审核报告.md`, `review/篇幅控制报告.md`, `review/最终核查摘要.md`, and `docs/workflow_status.yaml` if they exist.
2. Extract findings into an explicit repair matrix with: source report, severity, issue, affected section/file, proposed edit, evidence basis, and status.
3. Classify each finding:
   - `auto_fix`: can be fixed from existing proposal text, verified references, local docs, or harmless structural/wording edits.
   - `needs_user_fact`: requires real personal, project, funding, platform, award, team, prior-result, or unpublished experimental information not present locally.
   - `defer_or_reject`: low-value P2/P3 suggestion, reviewer preference that conflicts with project scope, or change that would introduce unverifiable claims.
4. Apply `auto_fix` items directly with minimal scoped edits. Update `extraTex/*.tex`, `references/myexample.bib`, `docs/*.md`, and `review/*.md` only as needed.
5. For `needs_user_fact` items, create or update a concise questionnaire in `docs/`, keep the proposal truthful, and mark the stage `need_user_input` only if the missing facts block a P0/P1 issue.
6. Record every applied, deferred, and blocked item in `review/P0P1定点修复报告.md`.
7. Rerun checks based on touched files:
   - If citations or BibTeX changed, rerun `nsfc-ref-alignment`.
   - If Part One changed, rerun length control.
   - If substantive text changed, rerun QC and simulated review or a focused reviewer pass.
   - If no P0 blocker remains, compile.
8. Update `docs/workflow_status.yaml` with the repair summary, current stage, blockers, and next stage.

Auto-repair should focus on P0/P1 first: missing citations, reference mismatch, overlong Part One, weak 立项依据 or research-scheme evidence chain, missing formulas for CS/AI proposals, unclear evaluation protocol, chapter inconsistency, unresolved placeholders, and review comments that can be addressed without inventing facts. P2/P3 polishing is optional and should be limited unless the user asks for a full refinement pass.

## Required Initial Reads

Before any writing or repair, read:

- `AGENTS.md`
- `README.md` or `README` if present
- `main.tex`
- `docs/00_项目基本信息.md` if present
- `docs/workflow_status.yaml` if present
- Existing `docs/` stage outputs
- Existing `extraTex/*.tex`
- `references/myexample.bib`
- Existing `review/*.md` reports if present

If `docs/workflow_status.yaml` does not exist, create it.

## Stage 00: Proposal Layout Resolution

Grant templates in this repository do not share one chapter numbering scheme, and the numbers overlap. Writing Part One content into a project that uses the other scheme silently overwrites the wrong chapter instead of failing. Resolve the layout before any writing, repair, or QC stage.

**Prefer the grant profile.** If the project root contains `grant-profile.yaml` (spec: `docs/grant-profile-spec.md`), use it as the authoritative role-to-file map and skip the filename heuristics below. It is the only mechanism that works for non-NSFC funds, whose chapter names differ (Guangdong writes 立**论**依据, not 立**项**依据):

- `roles.<role>.file` — the role has its own file; write there.
- `roles.<role>.merged_into: <host>` — the role has **no** separate file, but the template still requires the content. Write it into the host role's file as a dedicated subsection. Never skip a merged role: Guangdong's official outline demands 特色与创新点 and 年度研究计划 inside 研究内容, so skipping silently drops required content.
- `roles.<role>.absent: true` — the template genuinely does not ask for it; skip the corresponding stage.
- `roles.<role>.unresolved: true` — the profile is incomplete. Stop and ask the user to decide `merged_into` vs `absent` before writing.
- `grant.duration_years` — how many years the yearly plan must cover. Do not assume three.
- `review.grant_type` — overrides `simulated_review.grant_type` for stage 12.

If no profile exists, generate one with `python scripts/grant_profile.py infer --project-dir <project-dir>`, have the user confirm it, then proceed. Falling back to the heuristics below is only appropriate for the four known NSFC layouts.

Fallback (no profile): do not hardcode `extraTex/*.tex` filenames. Derive the real file set from `main.tex`:

1. Read `main.tex` and collect every **active** `\input{extraTex/...}` in document order. Ignore lines whose `\input` is commented out with `%`, and ignore `extraTex/@config.tex`.
2. Ignore `extraTex/*.tex` files that exist on disk but are not reachable from `main.tex`. They are disabled or orphaned sections; do not write to them and do not treat them as missing work.
3. Classify each active file into a role by its chapter heading in `main.tex` and its filename:
   - `part_one`: 立项依据 / 内容目标问题 / 方案及可行性 / 特色与创新 / 研究计划 / 研究内容 / 年度研究计划
   - `foundation`: 研究基础 / 工作条件 / 承担项目 / 完成国基项目 / 项目完成情况
   - `statements`: 不同类型国基情况 / 同年单位不一致 / 承担中单位不一致 / 不同专业技术职务的申请 / 生成式人工智能 / 其他 / 其它
4. Record the resolved layout and the ordered role-to-file map into `project.layout` and `project.body_files` in the checkpoint.

Two **NSFC** layouts are known. Use them to sanity-check the resolved map, not as a substitute for reading `main.tex`. Non-NSFC templates will match neither, which is expected — that is what the profile is for, so do not treat a mismatch as an error when a profile exists:

| Layout | Example projects | Part One | Foundation | Statements |
|---|---|---|---|---|
| `five-part` | `NSFC_Local`, `NSFC_2026_Education` | `1.1`–`1.5` | `2.1`–`2.4` | `3.1`–`3.5` |
| `three-part` | `NSFC_General`, `NSFC_Young` | `1.1`, `2.1`–`2.3` | `3.1`–`3.4` | `4.1`–`4.4`, `4.6` |

Stop and ask the user when:

- no `\input{extraTex/...}` can be resolved from `main.tex`;
- an active file cannot be classified into any role;
- the resolved map contradicts both known layouts, no `grant-profile.yaml` exists, and the user has not confirmed a custom template. The fix is to generate a profile, not to add another layout to `known`.

If the user later enables a section that is currently commented out in `main.tex`, such as an AIGC usage declaration, re-run this stage so the new file enters the role map before it is written.

## Checkpoint File

Use `docs/workflow_status.yaml` as the single workflow checkpoint.

If `docs/workflow_status.yaml` does not exist, create it before running any pipeline stage.

The checkpoint file must use the following standard structure:

```yaml
project:
  type: NSFC_Regional          # resolved by stage 00
  layout: five-part            # five-part | three-part | custom, resolved by stage 00
  proposal_path: "."
  body_dir: "extraTex"
  bib_file: "references/myexample.bib"
  guide_file: "AGENTS.md"
  stage_output_dir: "docs"
  review_output_dir: "review"
  body_files:                  # role -> ordered active files, resolved by stage 00
    part_one: []
    foundation: []
    statements: []

run:
  current_mode: resume
  last_started:
  last_finished:
  last_summary:
  next_stage:

# Every stage uses the same field set:
#   name, status, inputs, outputs, last_updated, notes, blockers
# status: pending | in_progress | completed | skipped | need_user_input | failed
# In stages 05-07, `@part_one` / `@foundation` / `@statements` expand to the
# corresponding project.body_files entry. Never write literal filenames here
# before stage 00 has resolved the layout.
stages:
  "00_layout_resolution":
    name: "Proposal Layout Resolution"
    status: pending
    inputs: ["main.tex", "extraTex/"]
    outputs: ["docs/workflow_status.yaml#project.body_files"]
    last_updated:
    notes:
    blockers:

  "01_topic_extraction":
    name: "Topic Extraction"
    status: pending
    inputs: ["AGENTS.md", "README.md", "main.tex", "docs/00_项目基本信息.md"]
    outputs: ["docs/01_选题与研究主题.md"]
    last_updated:
    notes:
    blockers:

  "02_literature_review":
    name: "Literature Review"
    status: pending
    inputs: ["AGENTS.md", "docs/01_选题与研究主题.md", "references/myexample.bib"]
    outputs: ["docs/02_文献调研/"]
    last_updated:
    notes:
    blockers:

  "03_scientific_questions":
    name: "Scientific Questions and Innovation"
    status: pending
    inputs: ["AGENTS.md", "docs/01_选题与研究主题.md", "docs/02_文献调研/"]
    outputs: ["docs/03_科学问题与创新点.md"]
    last_updated:
    notes:
    blockers:

  "04_research_plan":
    name: "Research Plan"
    status: pending
    inputs: ["AGENTS.md", "docs/03_科学问题与创新点.md"]
    outputs: ["docs/04_研究方案与技术路线.md"]
    last_updated:
    notes:
    blockers:

  "05_part_one_writing":
    name: "NSFC Part One Writing"
    status: pending
    inputs: ["AGENTS.md", "docs/04_研究方案与技术路线.md", "references/myexample.bib"]
    outputs: ["@part_one"]
    last_updated:
    notes:
    blockers:

  "06_research_foundation":
    name: "Research Foundation and Work Conditions"
    status: pending
    inputs: ["AGENTS.md", "docs/05_研究基础素材.md", "docs/研究基础信息补充问卷.md"]
    outputs: ["@foundation"]
    last_updated:
    notes:
    blockers:

  "07_other_statements":
    name: "Other Statements"
    status: pending
    inputs: ["docs/其他说明信息补充问卷.md"]
    outputs: ["@statements", "docs/其他说明检查报告.md"]
    last_updated:
    notes:
    blockers:

  "08_reference_alignment":
    name: "Reference Alignment"
    status: pending
    inputs: ["extraTex/", "references/myexample.bib"]
    outputs: ["review/引用一致性审核报告.md"]
    last_updated:
    notes:
    blockers:

  "09_length_control":
    name: "Length Control"
    status: pending
    inputs: ["extraTex/", "AGENTS.md"]
    outputs: ["review/篇幅控制报告.md"]
    last_updated:
    notes:
    blockers:

  "10_humanization":
    name: "Humanization"
    status: pending
    inputs: ["extraTex/"]
    outputs: ["review/去AI味修改报告.md"]
    last_updated:
    notes:
    blockers:

  "11_qc":
    name: "Quality Control"
    status: pending
    inputs: ["extraTex/", "references/myexample.bib", "AGENTS.md"]
    outputs: ["review/质量控制报告.md"]
    last_updated:
    notes:
    blockers:

  "12_simulated_review":
    name: "Simulated Review"
    status: pending
    inputs: ["extraTex/", "references/myexample.bib", "AGENTS.md"]
    outputs: ["review/模拟专家评审_全稿.md"]
    last_updated:
    notes:
    blockers:

  "13_targeted_repair":
    name: "P0/P1 Targeted Repair"
    status: pending
    inputs: ["review/质量控制报告.md", "review/模拟专家评审_全稿.md"]
    outputs: ["review/P0P1定点修复报告.md", "docs/评审意见修复清单.md"]
    last_updated:
    notes:
    blockers:

  "14_compile":
    name: "Compile"
    status: pending
    inputs: ["main.tex", "extraTex/", "references/myexample.bib"]
    outputs: ["main.pdf", "review/编译检查报告.md"]
    last_updated:
    notes:
    blockers:
```

## Pipeline Stages

### 1. Topic Extraction

Use `research-topic-extractor`.

Inputs:

- `AGENTS.md`
- project background
- `docs/00_项目基本信息.md` if present

Outputs:

- `docs/01_选题与研究主题.md`

Then use `research-guide-updater` to synchronize stable topic scope, terms, research boundaries, and writing rules into `AGENTS.md`.

Mark this stage `need_user_input` if the project topic, funding type, or application field is unclear.

### 2. Literature Review

Use `research-literature-review`.

Default scope:

- 2022 to current year unless the user specifies otherwise.
- English literature first, Chinese literature as supplement.
- Use the project scope in `AGENTS.md` as the retrieval boundary.
- For CS/AI/Agent/Time-Series projects, use multiple query groups rather than a single broad query:
  - core method keywords;
  - agent/LLM/tool-use/planning keywords when relevant;
  - time-series/temporal modeling/forecasting/anomaly keywords when relevant;
  - multimodal/retrieval/recommendation keywords when relevant;
  - datasets, benchmarks, and evaluation metric keywords.

Outputs should normally include:

- review markdown or LaTeX
- BibTeX file
- validation report
- PDF and Word when requested by the user or project convention

Default output directory:

- `docs/02_文献调研/`

After completion, use `research-guide-updater` to synchronize stable literature groups, terminology, and technical boundaries into `AGENTS.md`.

### 3. Scientific Questions and Innovation

Use `research-idea`.

Inputs:

- `AGENTS.md`
- `docs/01_选题与研究主题.md`
- `docs/02_文献调研/`

Output:

- `docs/03_科学问题与创新点.md`

The report must include:

- core contradiction and research gap
- 2 to 3 key scientific questions
- falsifiable hypotheses
- innovation points
- relationship to existing paradigms
- likely reviewer challenges and the intended response line

Then use `research-guide-updater` to synchronize stable scientific questions, hypotheses, and term boundaries into `AGENTS.md`.

### 4. Research Plan

Use `research-plan`.

Inputs:

- `AGENTS.md`
- `docs/01_选题与研究主题.md`
- `docs/02_文献调研/`
- `docs/03_科学问题与创新点.md`

Output:

- `docs/04_研究方案与技术路线.md`

The research plan should map each scientific question to a research content, method, experiment, and falsification path.

For CS/AI/Agent/Time-Series topics, the research plan must also include a compact formalization section covering inputs, outputs, notation, optimization objective, inference rule, evaluation metrics, and failure/falsification criteria. This section is later reused when drafting the research scheme text in stage 05.

### 5. NSFC Part One Writing

Write only the files listed under `project.body_files.part_one`. Map skills to files by role, not by number:

- `nsfc-justification-writer` for the 立项依据 file.
- `nsfc-research-content-writer` for the 研究内容 / 内容目标问题, 特色与创新, and 研究计划 / 年度研究计划 files.
- `research-plan` outputs for the 方案及可行性 file when the layout has one.

In `three-part` layouts there is no separate 方案及可行性 file. Fold the research scheme, technical route, and feasibility analysis into the 研究内容 file instead of creating a new file or writing into an inactive one.

Requirements:

- Keep Part One under the project word/page budget in `AGENTS.md`.
- Maintain one-to-one consistency among research contents, scientific questions, and research schemes.
- Use only BibTeX keys that exist in `references/myexample.bib`.
- Do not turn the proposal into a generic AI, recommendation, ranking, or LLM-agent project when `AGENTS.md` defines a narrower scope.
- For CS/AI/Agent/Time-Series projects, do not leave the research scheme text as a plain prose workflow, whether it lives in its own 方案及可行性 file or inside the 研究内容 file. It must include domain-appropriate formulas for representation/modeling, optimization, inference/decoding, and evaluation, plus variable explanations.
- Before marking this stage complete, verify that Part One has enough cited references for the topic and that `references/myexample.bib` passes the Reference Sufficiency Gate.

### 6. Research Foundation and Work Conditions

Use `nsfc-research-foundation-writer`.

Inputs:

- `docs/05_研究基础素材.md` if present. This is the collected-facts file for this stage; create it from user-supplied CV, project, and platform materials before writing, so the stage has a source of record separate from its own output.
- `docs/研究基础信息补充问卷.md` if a previous run produced one and the user has filled it in.
- applicant CV/project information if present.
- latest `review/模拟专家评审_全稿.md` if present.

Outputs:

- the files listed under `project.body_files.foundation`.

Read the current content of those files before writing, but do not treat their existence as evidence that this stage is done. Template files ship pre-populated with `\NSFCBlankPara` placeholders.

If real project numbers, funding amounts, publications, awards, platforms, team member roles, prior results, or completion status are missing, stop this stage and create:

- `docs/研究基础信息补充问卷.md`

Mark the stage as `need_user_input`.

When writing the 承担项目 file, do not leave internal placeholders such as `待填写`, `现有材料未列`, `--`, or `项目编号未知` in the final text. If a project genuinely has no NSFC-style approval number, state the formal reason based on user-provided facts.

### 7. Other Statements

Check every file listed under `project.body_files.statements`. The count and numbering differ by layout, and some templates ship additional declaration sections that are commented out in `main.tex`.

If the project has an active 生成式人工智能 declaration file, treat it as mandatory for this stage and fill it from the user's actual AIGC usage during drafting. If that section exists on disk but is commented out in `main.tex`, do not write to it; instead note in `docs/其他说明检查报告.md` that the declaration is disabled, so the user can decide whether to enable it before submission.

Do not fabricate declarations. If the true situation is unknown, create `docs/其他说明信息补充问卷.md` and mark this stage as `need_user_input`.

If the user confirms no relevant situation exists, use formal wording such as `无相关情况。` rather than draft-like placeholders.

### 8. Reference Alignment

Use `nsfc-ref-alignment`.

Check:

- all `\cite{}` keys exist in `references/myexample.bib`
- suspicious 2025 to 2026 references
- URL/DOI/title risks
- citation-to-claim alignment

Default output:

- `review/引用一致性审核报告.md`

Do not modify references unless the user asks for repair. If repair is requested, only change entries that can be verified or are supported by the project literature review artifacts.

### 9. Length Control

Use `nsfc-length-aligner`.

Focus:

- Part One under the `AGENTS.md` budget, normally 8000 Chinese characters or less for regional fund drafts.
- full proposal under the project page budget.
- compress `1.1` and `1.3` first if overlong.

Do not remove scientific questions, falsification paths, or required NSFC headings merely to shorten text.

### 10. Humanization

Use `nsfc-humanization`.

Focus:

- repeated sentences
- slogan-like transitions
- excessive `不是...而是...` structures
- over-abstract AI-style wording
- chapter-to-chapter phrasing duplication

Do not expand. Preserve technical meaning and citation links.

### 11. QC

Use `nsfc-qc`.

Default output:

- `review/质量控制报告.md`

Check:

- research content, scientific question, and research scheme consistency
- length
- AI-style residue
- citation risk
- regional fund fit
- missing real information
- unresolved placeholders

### 12. Simulated Review

Use `nsfc-reviewers`.

Default parameters:

- `proposal_path=.`
- `grant_type=地区基金`, or the grant type resolved in stage 00
- `panel_count=3`, matching the tuned default of `nsfc-reviewers`. Raise it to at most 5 when the user asks for a stricter pass and accepts the added cost.
- `output_path=review/模拟专家评审_全稿.md`
- `focus=创新性、科学问题、研究方案可行性、研究基础支撑、地区基金适配性、函评/会评风险`

Do not modify proposal body text during simulated review.

### 13. P0/P1 Targeted Repair

Read the latest QC and simulated review reports, then run the Review-Driven Auto-Repair Policy.

Do not merely tell the user how to revise when the issue is auto-fixable. Apply the edit, keep the change minimal, and record it.

Required outputs:

- `docs/评审意见修复清单.md`: a repair matrix extracted from QC/reviewer findings.
- `review/P0P1定点修复报告.md`: what was changed, what was deferred, what still needs user-confirmed facts, and which checks were rerun.

Repair only P0/P1 issues unless the user asks for deeper polishing. Typical auto-fixable repairs include:

- unresolved placeholders or draft-like wording
- citation/BibTeX mismatch or missing citation support
- chapter inconsistency among 1.1, 1.2, 1.3, 1.4, and 1.5
- overlong sections, especially Part One
- weak 1.1 literature chain or missing benchmark/dataset/method references
- plain-prose 1.3 for CS/AI/Agent/Time-Series topics that lacks formulas, metrics, or protocol definitions
- unclear data/evaluation protocol
- weak research foundation bridge when existing local evidence can support it
- overly broad innovation claims that can be narrowed without changing the project truth

Do not auto-fill real project numbers, funding amounts, unpublished results, awards, personnel declarations, or prior-experiment metrics. If these are needed, create or update the relevant questionnaire in `docs/`, mark the item `needs_user_fact`, and leave a truthful non-fabricated text state.

After repairs, rerun all relevant downstream checks:

- `nsfc-ref-alignment` after citation or BibTeX changes.
- `nsfc-length-aligner` after Part One changes.
- `nsfc-qc` after any substantive proposal text changes.
- `nsfc-reviewers` after P0/P1 substantive repairs, unless the user asks to skip review for speed.
- Compile after P0 issues are resolved.

Update `docs/workflow_status.yaml` after each repair loop. If the rerun reports still contain P0/P1 auto-fixable findings, perform one additional repair loop before stopping. Stop only when all remaining P0/P1 items require user facts, conflict with the scope, or the user has asked for review-only mode.

### 14. Compile

Compile only after P0 issues are resolved, or when the user explicitly asks to compile despite known issues.

Preferred command, run from the repository root:

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir <project-dir>
```

When the working directory is the proposal project itself, or the project was distributed as a standalone zip, use its own wrapper instead:

```bash
python scripts/nsfc_build.py build --project-dir .
```

`scripts/nsfc_build.py` only exists inside each project directory. There is no such script at the repository root, so do not run the wrapper form from the repo root.

Fallback:

```bash
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

Output:

- `main.pdf`

Record compile status in `docs/workflow_status.yaml`, including whether bibliography rendered and whether page budget appears acceptable.

## Final Deliverables

At the end of a successful run, provide:

- generated/updated `extraTex/*.tex`
- updated `references/myexample.bib` if modified
- `main.pdf`
- QC report
- simulated review report
- remaining human verification checklist
- workflow status summary

## Resume Behavior

When the user says `继续`, `resume`, `接着写`, `继续全流程`, or similar:

1. Read `docs/workflow_status.yaml`.
2. Re-run stage 00 if `project.body_files` is empty or if `main.tex` changed since `last_updated`.
3. Verify whether declared outputs are actually present **and populated**. For `extraTex/*.tex` outputs, existence is not evidence of completion: template files ship with `\NSFCBlankPara` placeholders already in place. Treat a stage as incomplete when its output files still consist only of placeholders, questionnaire stubs, or draft markers such as `待填写`.
4. Continue from the earliest stage with status other than `completed` or `skipped`.
5. If all stages are completed, run a final QC/review summary rather than regenerating content.

## Stop Conditions

Stop and ask for user input when:

- a stage requires real personal, funding, project, team, award, platform, or data information that is not present locally.
- a required file is missing and cannot be safely recreated.
- QC or review identifies a P0 issue that cannot be fixed without user-confirmed facts.
- the user requests a decision that affects truthfulness, compliance, or personal declaration.

When stopping, create a concise questionnaire in `docs/` and mark the relevant stage `need_user_input`.
