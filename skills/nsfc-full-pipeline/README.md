# nsfc-full-pipeline — NSFC 标书全流程编排器

**版本**：v0.1.0（开发中，版本号以 [config.yaml](config.yaml) 为准）
**类型**：📝 日常

把"选题 → 文献 → 科学问题 → 研究方案 → 正文写作 → 核查 → 评审 → 修复 → 编译"串成一条可断点续跑的流水线，自动调用仓库内已有的 NSFC / research 系列 skill，而不是让你逐个手动触发。

---

## 什么时候用

- 你有一个 NSFC 标书 LaTeX 项目（`main.tex` + `extraTex/` + `references/`），想从头跑完整流程
- 上次跑到一半中断了，想接着跑而不是推倒重来
- QC 或模拟评审出了报告，想让 AI **直接改稿**而不是只给建议

**不适用**：只想写某一个章节（直接用对应的 `nsfc-*-writer`）；只想做一次只读体检（直接用 `nsfc-qc`）。

---

## 快速开始

在标书项目目录下：

```text
请使用 nsfc-full-pipeline 处理 projects/NSFC_2026_Education，从头跑全流程。
```

续跑：

```text
继续
```

评审后自动修复：

```text
根据模拟评审报告修复 P0/P1 问题
```

---

## 14 个阶段

| 阶段 | 调用的 skill | 产出 |
|---|---|---|
| 00 布局解析 | —（内置） | 断点文件的 `project.body_files` |
| 01 选题 | `research-topic-extractor` + `research-guide-updater` | `docs/01_选题与研究主题.md` |
| 02 文献调研 | `research-literature-review` | `docs/02_文献调研/` + `.bib` |
| 03 科学问题 | `research-idea` | `docs/03_科学问题与创新点.md` |
| 04 研究方案 | `research-plan` | `docs/04_研究方案与技术路线.md` |
| 05 第一部分正文 | `nsfc-justification-writer`、`nsfc-research-content-writer` | `part_one` 角色对应的 `.tex` |
| 06 研究基础 | `nsfc-research-foundation-writer` | `foundation` 角色对应的 `.tex` |
| 07 其他说明 | —（人工确认） | `statements` 角色对应的 `.tex` |
| 08 引用核查 | `nsfc-ref-alignment` | `review/引用一致性审核报告.md` |
| 09 篇幅对齐 | `nsfc-length-aligner` | `review/篇幅控制报告.md` |
| 10 去 AI 味 | `nsfc-humanization` | `review/去AI味修改报告.md` |
| 11 质控 | `nsfc-qc` | `review/质量控制报告.md` |
| 12 模拟评审 | `nsfc-reviewers`（默认 3 组） | `review/模拟专家评审_全稿.md` |
| 13 定点修复 | —（内置） | `review/P0P1定点修复报告.md` |
| 14 编译 | `nsfc_project_tool.py` | `main.pdf` |

---

## 三个关键机制

### 1. 布局解析（stage 00）

仓库里的 NSFC 模板**不共用一套章节编号**，而且编号互相重叠：

| 布局 | 项目 | 第一部分 | 研究基础 | 其他说明 |
|---|---|---|---|---|
| `five-part` | `NSFC_Local`、`NSFC_2026_Education` | `1.1`–`1.5` | `2.1`–`2.4` | `3.1`–`3.5` |
| `three-part` | `NSFC_General`、`NSFC_Young` | `1.1`、`2.1`–`2.3` | `3.1`–`3.4` | `4.1`–`4.4`、`4.6` |

如果按固定编号写，在面上项目上会把"研究基础"写进"研究内容"的位置**且不报错**。所以 stage 00 强制先读 `main.tex` 里未被注释的 `\input{extraTex/...}`，解析出真实文件集合并按角色归类，解析不出来就停下来问你。

### 2. 断点续跑

状态记在 `docs/workflow_status.yaml`。判定阶段是否完成时**不只看文件是否存在**——模板自带 `\NSFCBlankPara` 占位，文件本来就在。必须同时确认内容非占位态。

### 3. 不编造事实

遇到需要真实项目号、经费、论文、奖项、平台、团队信息时，会在 `docs/` 下生成问卷、把阶段标成 `need_user_input` 然后停住，等你填完再继续。

---

## 本编排器不管的事

需要时请单独调用：

| 环节 | skill |
|---|---|
| 中英文摘要 | `nsfc-abstract` |
| 申请代码推荐 | `nsfc-code` |
| 预算说明书 | `nsfc-budget` |
| 配图规划与 prompt | `nsfc-proposal-figure-pipeline` |

摘要是申请书必填项，跑完本流程后别忘了补。

---

## 输出去哪

`docs/` 与 `review/` 直接写在标书项目里，**不进** `.bensz-api/` 任务工作区——按 [WORKSPACE.md](../WORKSPACE.md) 的定义它们属于正式交付物。只有检索缓存、中间 JSON、命令日志才进任务工作区。

---

## 已知限制

- `SKILL.md` 当前 617 行，仍超出项目规范的 500 行上限
- 阶段 07「其他说明」高度依赖人工确认，自动化程度低于其他阶段
- 若 `main.tex` 里某个声明章节是注释态（如部分模板的生成式人工智能声明），本流程不会写入，只会在检查报告里提示你决定是否启用

---

## 相关文档

- [SKILL.md](SKILL.md) — AI 执行规范
- [config.yaml](config.yaml) — 参数与版本号唯一真相来源
- [CHANGELOG.md](CHANGELOG.md) — 变更记录
