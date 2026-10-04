# projects 目录导览

`projects/` 目录存放的是各条产品线的示例项目与最薄的一层项目入口。它们面向的用户群体并不相同，建议先按你的写作场景选择版块，再进入具体项目。

补充说明：

- 每个示例项目都应自带一个与目录同名的 `*.code-workspace` 和 `.vscode/settings.json`
- 本地使用 VS Code 时，建议直接打开该 `*.code-workspace`，让 LaTeX Workshop 自动走项目内置的构建 wrapper，而不是手工拼 `xelatex`
- 当前固定配置默认通过 `texlua + scripts/latex_workshop_build.lua` 转调项目级 Python wrapper，按同一套模板兼容 macOS / Linux / Windows
- 无标准目录名前缀的项目可在 `template.json` 中声明 `build_profile`，同步脚本会采用已有类型的固定配置。
- 打开整个仓库时，根目录的受管配置也会按当前主文件路由到所属项目 wrapper；请打开所需项目的 `main.tex` 再构建，避免在多个项目间误选主文件。

`NSFC_2026_XJ-PVCast_final` 为中国沙漠气象科学研究基金申请项目，显式使用 `bensz-thesis` 的 `xj-desert-fund-2026` profile；可编辑13页空白稿与正式工作稿见 [项目说明](NSFC_2026_XJ-PVCast_final/README.md)。

## 实验室开放基金

[`NSFC_2026_CIESM-STSR_final/`](./NSFC_2026_CIESM-STSR_final/README.md) 提供地球系统数值模拟教育部重点实验室开放基金四页空白申请书，封面和表格可填写，正文可自动续页。模板由 `bensz-thesis` 的独立 `ciesm-open-fund` profile/style 承载；官方入口为 `thesis_project_tool.py build --project-dir projects/NSFC_2026_CIESM-STSR_final`。

## 国自然（NSFC）

适合人群：

- 正在撰写国家自然科学基金申请书正文的教师、医生、科研人员
- 需要在本地或 Overleaf 上快速得到与官方 Word 模板对齐 PDF 的用户

说明：

- 这一组项目共享 [`packages/bensz-nsfc/`](../packages/bensz-nsfc/) 公共包
- 三个项目的区别主要在于**申报类型不同**，不是写作工具链不同

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`NSFC_General/`](./NSFC_General/) | 面上项目正文模板 | 已有一定研究基础，准备申报国自然面上项目 |
| [`NSFC_Local/`](./NSFC_Local/) | 地区科学基金项目正文模板 | 面向地区科学基金项目申报 |
| [`NSFC_Young/`](./NSFC_Young/) | 青年科学基金项目正文模板 | 面向青年科学基金项目申报 |

如果你是第一次接触本仓库，且当前任务是写国自然标书，通常从与你申报类型一致的 `NSFC_*` 项目进入即可。

## 广东省自然科学基金（GDNSF）

适合人群：

- 正在准备广东省自然科学基金面上项目报告正文的科研人员
- 需要将广东省基金 Word 提纲迁移到可维护 LaTeX 项目的用户

说明：

- 当前 `GDNSF_*` 是项目层独立模板，优先复用共享字体资源，但不修改 `packages/bensz-nsfc/`
- 构建入口为项目内 `python scripts/gdnsf_build.py build --project-dir .`

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`GDNSF_General/`](./GDNSF_General/) | 广东省自然科学基金面上项目报告正文模板 | 准备广东省自然科学基金面上项目正文上传材料 |
| [`GDNSF_Regional_Young/`](./GDNSF_Regional_Young/) | 广东省基础与应用基础研究基金区域联合基金青年基金报告正文模板 | 准备区域联合青年基金项目正文上传材料 |

## 广西自然科学基金（GXNSF）

适合人群：

- 正在准备广西自然科学基金面上项目报告正文的科研人员
- 需要将广西基金 Word 提纲迁移到可维护 LaTeX 项目的用户

说明：

- 当前 `GXNSF_General/` 是项目层独立模板，复用共享字体资源，但不修改或依赖 `packages/bensz-nsfc/`
- 构建入口为项目内 `python scripts/gxnsf_build.py build --project-dir .`
- 模板只覆盖 issue #52 提供的精简报告正文提纲；正式申报前仍需核对当年度申报须知与系统附件要求

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`GXNSF_General/`](./GXNSF_General/) | 广西自然科学基金面上项目报告正文模板 | 准备广西自然科学基金面上项目正文上传材料 |

## 华中师范大学实验室开放课题

[`Huazhong_template/`](./Huazhong_template/README.md) 提供 2026 版开放课题项目申请书，包含封面、承诺、信息表、横向成员表及五个章节。稳定版式由 `bensz-thesis` 的 `ccnu-open-fund-2026` profile 承载，项目使用 `build_profile=thesis` 接入统一 VS Code 配置。

[`NSFC_2026_CCNU-EduAgentTrust_final/`](./NSFC_2026_CCNU-EduAgentTrust_final/README.md) 按同一官方 PDF 新建七页可编辑空白项目，复用上述公共样式；`template.json` 显式指定 thesis 构建链路，覆盖目录名前缀推断。

## 测绘科学与工程实验室开放基金

[NSFC_2027_Mapping_final](NSFC_2027_Mapping_final/README.md) 按官方 2026 版 PDF 提供 10 页可编辑空白申请书，含横向成员表、预算和自动续页正文；通过 `template.json` 显式选择 `thesis` 构建链路。

## SCI 论文

适合人群：

- 正在撰写英文期刊论文的科研人员
- 希望维护一份 LaTeX 正文源文件，同时导出 PDF 和 Word 的用户

说明：

- 这一组项目共享 [`packages/bensz-paper/`](../packages/bensz-paper/) 公共包
- 当前已落地论文正文与投稿信两条可验证示例链路，重点展示“`extraTex/**/*.tex` 单一正文来源 + PDF/DOCX 双输出”

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`paper-sci-01/`](./paper-sci-01/) | SCI 论文示例项目 | 写英文论文、投稿前排版、需要同时交付 `main.pdf` 与 `main.docx` |
| [`paper-coverletter-01/`](./paper-coverletter-01/) | 投稿信示例项目 | 已有 cover letter Word 稿件，想迁移到可维护的 LaTeX + DOCX 双输出模板 |

如果你的目标是期刊论文正文或投稿信，而不是基金申请书，请直接从对应的 `paper-*` 项目开始，不必进入 NSFC 项目。

## 学位论文与博士后研究报告

适合人群：

- 正在撰写硕士、博士学位论文的学生
- 需要提交博士后出站研究报告、并希望直接使用 LaTeX 维护封面、题名页、摘要、目录和正文的研究人员
- 需要在统一构建链路内维护学位论文或博士后长文档的模板维护者

说明：

- 这一组项目统一共享 [`packages/bensz-thesis/`](../packages/bensz-thesis/) 公共包
- `thesis-*` 项目的 `template.json` 当前可用 `bachelor / master / doctor / postdoc` 四种类型，分别对应学士、硕士、博士和博士后研究报告
- 每个 `thesis-*` 项目都应在 `packages/bensz-thesis/` 中拥有独立的 `template/profile/style` 身份，避免项目之间互相借用模板 ID
- 通用构建入口支持 `docx` 子命令，可从 LaTeX 源导出可编辑 Word draft；复杂对象会在 `.latex-cache/docx/` 的质量报告中提示人工复核

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`thesis-smu-master/`](./thesis-smu-master/) | 南方医科大学硕士论文示例项目 | 需要 SMU 硕士论文版式模板 |
| [`thesis-nju-master/`](./thesis-nju-master/) | 南京大学工程管理硕士论文示例项目 | 需要 NJU 工程管理硕士论文版式模板，且希望默认 `main.tex` 就是可编辑入口，同时保留公开基线验收文件 |
| [`thesis-just-bachelor/`](./thesis-just-bachelor/) | 江苏科技大学本科毕业设计（论文）示例项目 | 需要 JUST 本科毕业设计（论文）版式模板 |
| [`thesis-jxust-bachelor/`](./thesis-jxust-bachelor/) | 江西理工大学本科毕业论文 / 毕业设计示例项目 | 需要 JXUST 本科毕业论文 / 毕业设计版式模板，并希望在 `main.tex` 中切换论文 / 设计页眉 |
| [`thesis-ahnu-master/`](./thesis-ahnu-master/) | 安徽师范大学硕士论文示例项目 | 需要 AHNU 硕士论文版式模板 |
| [`thesis-cas-postdoc/`](./thesis-cas-postdoc/) | 中国科学院博士后出站研究报告示例项目 | 需要按中国科学院博士后出站报告场景组织封面、题名页、中英文摘要、目录、图表清单、正文与后置材料 |
| [`thesis-hit-doctor/`](./thesis-hit-doctor/) | 哈尔滨工业大学博士论文示例项目 | 需要 HIT 博士论文版式模板 |
| [`thesis-jlau-doctor/`](./thesis-jlau-doctor/) | 吉林农业大学博士论文示例项目 | 需要 JLAU 博士论文版式模板 |
| [`thesis-jlau-master/`](./thesis-jlau-master/) | 吉林农业大学硕士论文示例项目 | 需要 JLAU 硕士论文版式模板 |
| [`thesis-nwu-doctor/`](./thesis-nwu-doctor/) | 西北大学博士论文示例项目 | 需要 NWU 博士论文版式模板 |
| [`thesis-sysu-doctor/`](./thesis-sysu-doctor/) | 中山大学博士论文示例项目 | 需要 SYSU 博士论文版式模板 |
| [`thesis-ucas-doctor/`](./thesis-ucas-doctor/) | 中国科学院大学博士论文示例项目 | 需要 UCAS 博士论文版式模板 |
| [`thesis-smu-postdoc/`](./thesis-smu-postdoc/) | 南方医科大学博士后研究报告示例项目 | 需要按博士后研究报告规范组织封面、题名页、中英文摘要、正文与后置材料 |

如果你的目标是博士后出站研究报告，请优先进入 `thesis-cas-postdoc/` 或 `thesis-smu-postdoc/`；如果你的目标是学位论文，请进入学校和类型最接近的其他 `thesis-*` 项目。

## 简历（CV）

适合人群：

- 需要维护一份中英文双语学术简历的研究者、医生、学生或实验室成员
- 希望先用私有简历完成版式验收，再替换为公开演示内容的模板维护者

说明：

- 这一组项目共享 [`packages/bensz-cv/`](../packages/bensz-cv/) 公共包
- 当前示例项目重点展示“只读源样式复刻 → 像素级验收 → 去隐私公开示例”的完整链路

| 项目 | 用途 | 适用场景 |
|------|------|----------|
| [`cv-01/`](./cv-01/) | 中英文简历示例项目 | 写学术简历、个人资料页、媒体包式履历，或维护公开 CV 模板 |

如果你的目标是简历或个人资料页模板，请直接从 `cv-01/` 开始。

## 选型建议

- 写国自然标书：进入 `NSFC_General/`、`NSFC_Local/` 或 `NSFC_Young/`
- 写广东省自然科学基金面上项目报告正文：进入 `GDNSF_General/`
- 写广东省基础与应用基础研究基金区域联合基金青年基金报告正文：进入 `GDNSF_Regional_Young/`
- 写广西自然科学基金面上项目报告正文：进入 `GXNSF_General/`
- 写 SCI 论文正文：进入 `paper-sci-01/`
- 写投稿 cover letter：进入 `paper-coverletter-01/`
- 写毕业论文：进入与你学校和类型最接近的 `thesis-*` 项目（如 `thesis-smu-master/`、`thesis-nju-master/`、`thesis-nwu-doctor/`、`thesis-sysu-doctor/`、`thesis-ucas-doctor/`）
- 写博士后研究报告：进入 `thesis-cas-postdoc/` 或 `thesis-smu-postdoc/`
- 写中英文简历：进入 `cv-01/`

若你的问题涉及共享样式、公共宏、构建脚本或安装逻辑，再回到 `packages/` 目录定位对应公共包。

## 中南大学实验室开放基金

[NSFC_2026_MineChangeTrust_final](NSFC_2026_MineChangeTrust_final/README.md) 保留官方 2026 版申请书的 13 页空白结构与十四个栏目。采用 `bensz-thesis` 的 `csu-open-fund-2026` profile，支持研究正文续页及固定栏位溢出检查；项目显式声明 `build_profile=thesis`。
