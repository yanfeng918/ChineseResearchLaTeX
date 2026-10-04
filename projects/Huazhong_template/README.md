# 华中师范大学实验室开放课题申请书（2026 版）

基于本目录的官方参考 PDF 重建的可编辑 LaTeX 项目，默认生成 7 页空白申请书：封面、申请人承诺、简要信息表、横向成员表、研究基础、项目申请内容、预算与单位意见。

## 构建

在完整 ChineseResearchLaTeX 仓库中：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/Huazhong_template
```

只打开本项目时：

```bash
python3 scripts/thesis_build.py
```

需要 XeLaTeX、Python 3，以及包含 `ccnu-open-fund-2026` profile 的 `bensz-thesis`（`p_v20260906` 或更新版本）与 `bensz-fonts`。完整仓库的官方构建入口会直接使用本地公共包源码；单项目 wrapper 会通过 `kpsewhich bensz-thesis.sty` 定位已安装公共包。输出为 `main.pdf`，中间文件和 SyncTeX 位于 `.latex-cache/`。

VS Code 请打开 `Huazhong_template.code-workspace`。LaTeX Workshop 使用仓库统一的 `texlua → thesis_build.py → thesis_project_tool.py` 构建配置。

## 填写位置

| 文件 | 内容 |
|---|---|
| `extraTex/metadata.tex` | 名称、申请人、单位、申请日期、类别、简要个人信息、关键词、申请经费和起止年月 |
| `extraTex/abstract.tex` | 中文简介，300 字以内 |
| `extraTex/members.tex` | 最多 12 名成员，不包括申请人；签字留白 |
| `extraTex/foundation.tex` | 研究基础、代表作、承担项目 |
| `extraTex/proposal.tex` | 立项依据、研究内容、方案、创新、计划及成果，不超过 7000 字 |
| `extraTex/budget.tex` | 六行预算金额及用途，单位为万元 |
| `extraTex/organization.tex` | 所在单位（部门）意见 |
| `extraTex/commitment.tex` | 官方承诺原文及固定换行 |

`metadata.tex` 的 `category` 填 `A`、`B` 或 `C`，对应重大、重点、一般课题；留空输出空白表。封面和信息表共用名称、申请人、单位字段。`edition` 保留原表的“2026 年9 月”；实际申请日期填写 `year/month/day`。

例如：

```latex
\HuazhongSetup{title={教育智能体评价研究}, applicant={张三},
  organization={华中师范大学}, category={C}, funding={5},
  year={2026}, month={9}, day={15}}
```

研究基础和申请内容可以自动续页，续页保留对应章节标题、版框和连续页码。可在条目下直接写段落、公式和表格；参考文献可使用 `thebibliography` 环境。固定信息表、成员表和预算单元格按原表尺寸排版，超高内容会使构建失败并标出单元格坐标，需要缩短填写内容。金额、字数和成员事实由填写者核对，不自动生成或计算。

## 分层与版式验收

- 稳定版式位于 `packages/bensz-thesis/profiles/bthesis-profile-ccnu-open-fund-2026.def` 和对应 `styles/bthesis-style-ccnu-open-fund-2026.tex`，项目只维护内容与薄入口。
- 本项目是开放课题申请书；`template.json` 用 `document_type=open-fund-application` 标识，`build_profile=thesis` 仅表示复用构建链路，不设置学位 `degree`。
- 参考 PDF 仅用于验收，生成 PDF 不读取、嵌入或复制参考 PDF；所有文字与表格线均由 LaTeX 重建。
- 保留原文，包括预算备注中的“项总预算”。承诺、金额比例等文字按用户提供的版本复现，未作政策解释。
- 使用共享包中的宋体、楷体、Adobe 黑体和 Adobe 仿宋。参考 PDF 的封面嵌入字体 `WPSEMBED2` 未提供完整字体，使用宋体加粗近似；黑体、仿宋也存在字形差异。因此不宣称逐像素完全一致。

复核命令（在仓库的 `tests/huazhong-template/` 下执行）：

```bash
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py compare \
  --project-dir ../../projects/Huazhong_template \
  --baseline-pdf '../../projects/Huazhong_template/华中师范大学人工智能与教育新形态实验室开放课题项目申请书（2026版）.pdf' \
  --output-dir ./compare --keep-rasters
```

官方 compare 采用严格逐像素判定，字体或渲染差异会返回非零；应结合差异图和验收报告阅读。完整验证记录见仓库的 `tests/huazhong-template/REPORT.md`。
