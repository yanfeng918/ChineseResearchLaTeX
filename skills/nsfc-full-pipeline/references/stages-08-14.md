# Stage 08–14：核查、评审、修复与编译

执行 08–14 任一阶段前必须完整读取本文件。

## Stage 08：引用一致性核查

调用 `nsfc-ref-alignment`，只读检查正文引用与 `references/myexample.bib`：

- bibkey 是否存在；
- BibTeX 字段、DOI 和元数据是否异常；
- 引用是否真正支持相邻主张；
- 是否存在一条文献支撑过多异质结论或堆砌引用。

输出 `review/引用一致性审核报告.md`。若需要改正文或 BibTeX，修改后重跑本阶段。不得自动编造或替换为未经核验的条目。

## Stage 09：篇幅对齐

调用 `nsfc-length-aligner`，按项目级 `AGENTS.md` 的预算检查，不使用跨项目通用页数猜测。输出 `review/篇幅控制报告.md`。

若仍有 `【待补 …】`，篇幅结论必须标“暂定”：补入论文、项目和平台信息后页数可能增加。压缩或扩写时逐字保护 `【待补 …】`、`【暂定 …】`、引用命令、数值和事实。

## Stage 10：去 AI 味

调用 `nsfc-humanization`，输出 `review/去AI味修改报告.md`。重点处理模板化转折、伪对立、抽象名词堆叠、边界声明过重和研究动作不清。

不得新增事实、方法、指标或结论；不得删除或改写两类缺口标记；不得为了“自然”牺牲术语精度和章节职责。

## Stage 11：质量控制

调用 `nsfc-qc`，输出 `review/质量控制报告.md`。检查结构、逻辑、文风、引用、篇幅、未写作占位、编译风险与缺口。

- `\NSFCBlankPara`、`待填写` 等未写作占位属于 P0；
- 合法 `【待补 ID：说明】` 单列为提交前缺口，不当作正文未写，也不自动升级为 P0/P1；
- 非法/未登记 ID、整段只有占位、事实来源缺失属于结构错误。

## Stage 12：模拟专家评审

调用 `nsfc-reviewers`，项目类型必须取 stage 00 解析结果。默认 3 组、最多 5 组评审，输出 `review/模拟专家评审_全稿.md`。

评审应区分：科学性问题、表达问题、证据问题、资助额度下的合理妥协、待补事实。不得把待补 ID 猜成具体值后再评价。

## Stage 13：P0/P1 定点修复

读取最新 QC 和模拟评审，建立 `docs/评审意见修复清单.md`，至少包含：问题 ID、等级、证据、分类、落点、动作、复核阶段和状态。

分类：

- `auto_fix`：证据充分且边界明确，直接定点修；
- `needs_user_fact`：保留或插入已登记事实 ID，继续修其他问题；
- `defer_or_reject`：超出项目边界、资助额度或用户目标，记录理由。

只改命中的句段，不重写无关章节。每轮修复后按触及范围重跑：

- 正文主张或 BibTeX → stage 08；
- 第一部分长度 → stage 09；
- 实质文本 → stage 10/11；
- 科学方案或创新发生实质变化 → stage 12。

若仍有可安全自动修复的 P0/P1，继续下一轮；当剩余问题都需要用户事实/选择或已明确拒绝时结束。输出 `review/P0P1定点修复报告.md`，记录已修、未修及理由。stage 13 不运行编译，避免和 stage 14 重复。

## Stage 14：编译

从仓库根目录运行：

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build \
  --project-dir <project-dir>
```

若只打开单个项目，则运行项目 wrapper：

```bash
python scripts/nsfc_build.py build --project-dir .
```

输出 `main.pdf` 与 `review/编译检查报告.md`。报告包括命令、退出码、错误数、warning 摘要、页数、硬事实 ID、暂定项数量，并区分已有和新增 warning。

编译零错误是底线；带合法硬事实缺口可以编译，但不能宣告提交就绪。

## 最终校验

依次运行：

```bash
python skills/nsfc-full-pipeline/scripts/scan_gaps.py \
  --project-dir <project-dir> --json
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> reconcile --apply
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> readiness
```

最终汇报包括：

- 15 个阶段的状态与跳过理由；
- 主要正文和报告路径；
- 编译结果与 PDF；
- 剩余硬事实 ID 和暂定项；
- `body_pipeline_ready`；
- `submission_ready` 与尚缺组件。

