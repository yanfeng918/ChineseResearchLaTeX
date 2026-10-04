# 测绘科学与工程自然资源部重点实验室开放基金申请书

基于同目录 2026 版官方 PDF 填写的开放基金申请书。当前包含申请信息、研究正文、预算、成员表、48 条参考文献及 12 幅插图；第 4 页为横向成员表。原始空白表为 10 页，填写稿随正文自动续页。文字、表格和固定标签均可编辑，插图为 PNG，构建不依赖参考 PDF。

## 构建与打开

建议用 [NSFC_2027_Mapping_final.code-workspace](NSFC_2027_Mapping_final.code-workspace) 打开 VS Code。LaTeX Workshop 通过 `texlua` 和项目 wrapper 调用 thesis 官方构建器。

在仓库根目录执行：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2027_Mapping_final
```

在项目目录执行：

```bash
python3 scripts/thesis_build.py
```

产物为 [main.pdf](main.pdf)，中间文件与 SyncTeX 位于 `.latex-cache/`。需要 XeLaTeX、BibTeX、Python，以及包含 `casm-open-fund-2026` profile 的 `bensz-thesis`、`bensz-fonts` 和提供文献样式的 `bensz-nsfc`。完整仓库直接使用本地公共包源码；单独复制项目时，需先安装相应公共包。

文献目录引起分页变化后，固定表格的 TikZ 定位可能需要额外一遍编译。官方构建器在常规三遍后按日志最多补两遍，位置和标签未收敛则返回失败；不要将尚有重跑提示的中间 PDF 当作交付稿。

## 填写入口

| 文件 | 内容 |
|---|---|
| [extraTex/metadata.tex](extraTex/metadata.tex) | 课题名称、申请人、依托单位及基本信息；封面和信息表共用字段 |
| [extraTex/abstract.tex](extraTex/abstract.tex) | 400 字以内摘要，替换蓝色说明 |
| [extraTex/members.tex](extraTex/members.tex) | 10 行成员与 7 项人数汇总；不含负责人 |
| [extraTex/budget.tex](extraTex/budget.tex) | 3 项合计、15 项预算金额，单位万元、保留两位小数 |
| [extraTex/budget-basis.tex](extraTex/budget-basis.tex) | 预算测算依据 |
| [extraTex/proposal.tex](extraTex/proposal.tex) | 立项依据、研究内容、研究方案、创新点、年度计划 |
| [extraTex/foundation.tex](extraTex/foundation.tex) | 工作基础、条件、成员简介、承担项目情况 |
| [extraTex/commitment.tex](extraTex/commitment.tex) | 官方申请人承诺 |
| [extraTex/organization.tex](extraTex/organization.tex) | 官方依托单位意见 |
| [extraTex/committee.tex](extraTex/committee.tex)、[extraTex/director.tex](extraTex/director.tex) | 审核意见留白 |
| [extraTex/attachments.tex](extraTex/attachments.tex) | 推荐意见等附件 |
| [references/myexample.bib](references/myexample.bib) | 文献题录唯一来源，构建时经 BibTeX 自动生成文献目录 |

文献目录仍位于立项依据末尾，`main.tex` 中的 `\MappingBibliography` 为显式构建入口；修改 `.bib` 后通过官方构建器重建即可。题录来源和关键论证核验范围见 [docs/literature-notes.md](docs/literature-notes.md)。

`direction`、`period`、`category`、`funding` 留空时显示原稿蓝色示例，填写后自动替换。当前填写稿已填入已确认字段，签字盖章及审核栏仍须按实际手续完成。尚缺的成员履历、论文全文等事实材料见 [docs/pending-information.md](docs/pending-information.md)。

研究正文直接写在每个 `\CasmTopic` 后面，使用宋体、Times New Roman、小四号及对应的 1.25 倍行距；长正文自动续页，保留版框和连续页码。“四、立项依据与研究内容”和“五、研究基础与工作条件”仅在各自部分首页显示，由本项目的 [extraTex/@config.tex](extraTex/@config.tex) 配置。蓝色提示可在填写时修改或删除。摘要、成员和预算等固定区域不自动扩页；文字超出可用高度时构建报错，需要精简内容。金额合计与人数由填写人核对，模板不代算。

## 分层与参考版本

稳定版式由公共包的 `casm-open-fund-2026` profile、style 及 artwork 承载；项目仅保留正文、字段、薄入口、元数据和 VS Code 配置。`template.json` 明确声明 `document_type=open-fund-application`、`build_profile=thesis`，不设置学位 `degree`；构建类型不由 `NSFC_` 目录前缀决定。

参考文件是 **2026 版**，封面“二〇二六年制”、2026 年度说明和研究期限“2026 年 11 月 1 日—2027 年 10 月 31 日”均按原稿保留。目录名中的 2027 不代表已取得 2027 版官方文件。原稿成员表第 9 行编号重复为“8”，末尾两节均编号“七”；本模板保留原样，未自行修订。

## 验证

官方比对命令（从仓库根目录执行）：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py compare \
  --project-dir projects/NSFC_2027_Mapping_final \
  --baseline-pdf projects/NSFC_2027_Mapping_final/测绘科学与工程自然资源部重点实验室.pdf \
  --output-dir tests/mapping-template/official-compare
```

上述 compare 适用于空白模板基线；当前填写稿与 10 页空白参考页数不同，不应以逐页像素相同比较验收正文。历史空白模板验收见 [tests/mapping-template/REPORT.md](../../tests/mapping-template/REPORT.md)；本轮填写稿修订、图文检查与构建结果见 [tests/mapping-fixes-20260921/REPORT.md](../../tests/mapping-fixes-20260921/REPORT.md)。共享字体与 WPS 原稿字体有字形差异，段落重排及抗锯齿也会带来像素差异。
