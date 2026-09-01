# 断点、缺口与续跑策略

本文件定义 `nsfc-full-pipeline` 的确定性状态协议。每次运行本技能时必须完整读取。

## 断点 schema

断点固定为项目内 `docs/workflow_status.yaml`，当前 `schema_version: 2`。核心节点：

- `project`：项目类型、资助类别、布局、篇幅预算、正文角色映射、事实文件路径、`main.tex` 指纹；
- `run`：运行模式、`fill_policy: draft_first`、最近开始/完成时间与下一阶段；
- `stages`：00–14 共 15 个阶段；
- `submission`：`abstract`、`application_code`、`budget`、`declarations`、`attachments` 的完成状态。

阶段状态只允许：

- `pending`：尚未执行；
- `in_progress`：已原子记录开始，尚未核验产物；
- `completed`：产物有效且无该阶段硬事实缺口；
- `drafted_with_gaps`：正文已写，仍有硬事实 ID 待回填；
- `skipped`：有明确理由不适用；
- `need_user_input`：真正无法安全推进；
- `failed`：工具或产物失败，需修复后重试。

禁止只因文件存在就标完成。正文含 `\NSFCBlankPara`、`待填写`、`现有材料未列` 或 `项目编号未知` 时仍属未写作。

## 状态脚本

脚本路径：`skills/nsfc-full-pipeline/scripts/pipeline_state.py`。

```bash
# 幂等迁移旧断点；默认预览，加 --apply 才写回
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> migrate --apply

# 按真实文件、缺口与指纹校准状态
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> reconcile --apply

# 原子记录阶段开始/完成
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> begin --stage 05_part_one_writing
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> finish --stage 05_part_one_writing

# 查看下一阶段与两级就绪度
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> next
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> readiness
```

写回使用同目录临时文件、`fsync` 与原子替换，避免中断留下半份 YAML。

## 中断恢复

续跑固定顺序是 `migrate --apply → reconcile --apply → next`。

`reconcile` 执行以下工作：

1. 若 `main.tex` 指纹变化，把 stage 00 置回 `pending`，重新解析正文角色；
2. 从正文真实标记重建 stage 05–07 的 `gaps`，不依赖人工维护的清单；
3. 若 `drafted_with_gaps` 的缺口已清空且产物有效，转为 `completed`；
4. 旧版因事实不足停在 `need_user_input`、但正文已经形成合法 ID 缺口稿的 stage 05–07，迁为 `drafted_with_gaps` 后继续；
5. 已完成阶段的输入指纹发生变化时，置回 `pending` 并要求定点复核；申请人事实文件即使位于项目目录外也纳入指纹；
6. 对遗留 `in_progress`，只有输出有效且输出指纹相对阶段开始时发生变化，才恢复为 `completed` 或 `drafted_with_gaps`；
7. 未变化、缺失或仍是未写作占位的产物不得自动恢复。

## 缺口分类

### 可推定项

年度计划月份、预期成果数量口径、实验规模、指标阈值和 baseline 等可以先给保守、合理的草稿值，标为 `【暂定 …】`。这些标记不属于硬事实缺口，但最终报告必须统计并请用户确认。

### 硬事实

批准号、经费、论文、奖项、设备型号、平台保障、团队成员、前期结果和声明必须来自：

- 断点中的 `applicant_profile_file`，通常是 `docs/applicants/<slug>.md`；
- 断点中的 `project_fact_file`，通常是 `docs/00_项目事实库.md`。

未知时使用普通 LaTeX 文本标记：

```tex
\textbf{【待补 F-GEN-03：批准号与起止年份】}
```

要求：

- ID 必须已经登记；不得由模型临时创造；
- 只挖掉名词短语，不得整段只有占位；
- 同一事实统一使用同一 ID；
- 不新增自定义宏，确保独立项目与 Overleaf 可编译；
- 缺事实时集中更新问卷，但 stage 05–07 继续推进。

## 扫描与回填

扫描器默认只检查 `main.tex` 实际引用的正文文件：

```bash
python skills/nsfc-full-pipeline/scripts/scan_gaps.py \
  --project-dir <project-dir> --json
```

`--all-body-files` 仅用于诊断磁盘上的孤儿文件，不用于正式就绪判定。扫描结果中的 `hard_gaps_clear` 只表示硬事实标记已清空，不等于整份申请书可提交。

扫描器必须报错的情况：

- 有硬事实缺口但没有可读取的事实来源；
- ID 格式非法或未登记；
- 一个段落基本只有待补标记；
- 仍存在未写作占位。

用户补事实后：

1. 重读两层事实文件，确认事实状态为“已确认”或“明确暂无”；
2. 按 ID 定位所有命中处，只替换相关句子；
3. “明确暂无”要改成真实否定句，不换成另一个占位；
4. 运行 `reconcile --apply`；
5. 按实际变更重跑引用、篇幅、QC 或评审阶段。

## 停止条件

硬停止仅限：

- stage 00 无法确定布局、项目类型、篇幅规则或安全写入路径；
- stage 01 无法确定研究主题；
- 资料相互冲突，无法判断哪一份是真实来源；
- 工具失败或权限/路径问题使继续执行不安全。

普通事实缺失、参考文献需要补充、篇幅尚未最终确定均不应逐项打断用户。

## 就绪度

`body_pipeline_ready` 需要：15 阶段均 `completed`/`skipped`、`main.pdf` 存在、无硬事实缺口、无未写作占位、无扫描结构错误。

`submission_ready` 还需要 `submission` 五项均为 `completed` 或 `not_applicable`。只要任一项为 `pending`，不得声称整份申请书可以提交。
