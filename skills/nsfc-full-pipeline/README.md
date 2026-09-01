# nsfc-full-pipeline — NSFC 标书正文全流程

**版本**：v0.4.0（以 [config.yaml](config.yaml) 为准）
**状态**：🚧 开发中

把选题、文献、科学问题、研究方案、正文写作、核查、评审、定点修复和编译串成可可靠续跑的 15 阶段流程。默认采用 draft-first：硬事实不足时保留可见、可追踪的事实 ID 缺口，先完成可安全完成的正文，不因一条批准号或设备型号反复中断。

## 适用场景

- 从头写一份 NSFC 面上、青年或地区项目正文；
- 上次运行中断，需要从真实进度继续；
- 根据 QC 或模拟评审结果自动修复 P0/P1；
- 需要统一管理事实缺口、编译和提交前检查。

支持 `NSFC_General`、`NSFC_General_Clean`、`NSFC_Young`、`NSFC_Local`、`NSFC_Local_Clean` 及其派生项目。

不适用：单章节写作、一次性只读 QC、省级/地方自然科学基金项目。摘要、申请代码、预算说明、附件和配图不属于正文 15 阶段，需另行完成。

## 快速开始

```text
请使用 nsfc-full-pipeline 处理 projects/NSFC_Local，从头跑全流程。
```

续跑：

```text
继续上次 NSFC 标书写作流程，不要从头开始。
```

评审后修复：

```text
根据模拟专家评审和 QC 报告修复 P0/P1，并重新核查。
```

## 15 个阶段

| ID | 阶段 | 主要产物 |
|---|---|---|
| 00 | 布局与项目类型解析 | 正文角色、资助类别、篇幅预算 |
| 01 | 选题与研究主题 | `docs/01_选题与研究主题.md` |
| 02 | 文献调研 | `docs/02_文献调研/`、真实 BibTeX |
| 03 | 科学问题与创新点 | `docs/03_科学问题与创新点.md` |
| 04 | 研究方案与技术路线 | `docs/04_研究方案与技术路线.md` |
| 05 | 第一部分正文 | stage 00 解析出的 `part_one` 文件 |
| 06 | 研究基础与工作条件 | `foundation` 文件 |
| 07 | 其他说明 | `statements` 文件与检查报告 |
| 08 | 引用一致性核查 | `review/引用一致性审核报告.md` |
| 09 | 篇幅对齐 | `review/篇幅控制报告.md` |
| 10 | 去 AI 味 | `review/去AI味修改报告.md` |
| 11 | QC | `review/质量控制报告.md` |
| 12 | 模拟专家评审 | `review/模拟专家评审_全稿.md` |
| 13 | P0/P1 定点修复 | 修复清单与修复报告 |
| 14 | 编译 | `main.pdf`、编译检查报告 |

## 为什么续跑更可靠

状态保存在 `docs/workflow_status.yaml`，schema v2 不只记录阶段名，还记录：

- `main.tex`、阶段输入和输出指纹；
- `in_progress` 中断恢复依据；
- 正文真实缺口与 stage 05–07 的反向对账；
- 摘要、申请代码、预算、声明和附件的独立提交清单。

手工诊断命令：

```bash
python3 skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <项目路径> migrate --apply
python3 skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <项目路径> reconcile --apply
python3 skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <项目路径> next
```

旧断点会幂等迁移；`main.tex` 改变会让 stage 00 失效；遗留 `in_progress` 只有在产物有效且确实发生变化时才恢复。

## Draft-first 如何工作

- 可推定项：给保守草稿值并标 `【暂定 …】`；
- 硬事实：把句子写完整，只挖掉名词短语，例如 `\textbf{【待补 F-GEN-03：批准号与起止年份】}`。

事实 ID 必须已登记在申请人事实文件或项目事实库。缺硬事实时集中更新问卷，stage 05–07 标为 `drafted_with_gaps` 并继续；只有布局、项目类型或选题无法确定时才暂停。

扫描活动正文中的缺口：

```bash
python3 skills/nsfc-full-pipeline/scripts/scan_gaps.py \
  --project-dir <项目路径> --json
```

默认只扫描 `main.tex` 实际引用的正文；`--all-body-files` 仅用于诊断孤儿文件。补事实后按 ID 定点回填，不重写整节。

## 正文完成不等于可以提交

```bash
python3 skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <项目路径> readiness
```

- `body_pipeline_ready`：15 阶段完成、PDF 存在、无硬事实缺口和未写作占位；
- `submission_ready`：还要求摘要、申请代码、预算、声明和附件全部完成或明确不适用。

只要仍有 `【待补 …】`，或提交清单仍有 `pending`，就不会宣告整份申请书可提交。

## 常见问题

**会编造批准号、经费或论文吗？** 不会。draft-first 只改变何时停，不改变事实标准。

**为什么磁盘上的某个 `.tex` 没有被写？** `main.tex` 的活动 `\input` / `\include` 是唯一正文清单；注释态和孤儿文件不会进入正式流程。

**可以恢复旧的阻塞模式吗？** 兼容旧断点中的 `blocking` 值，但推荐保留 `draft_first`；无论哪种模式都不能编造事实。

**文献必须固定 25 条吗？** 不是。所有领域必须满足论断覆盖和语义匹配；25/30–50 是 CS/AI 的默认量化参考，其他领域按证据传统调整并说明理由。

## 相关文件

- [SKILL.md](SKILL.md)：AI 执行入口
- [checkpoint-and-gap-policy.md](references/checkpoint-and-gap-policy.md)：断点、缺口与两级就绪度
- [stages-00-07.md](references/stages-00-07.md)：前半流程细则
- [stages-08-14.md](references/stages-08-14.md)：检查、修复与编译细则
- [CHANGELOG.md](CHANGELOG.md)：版本记录
