# bensz-thesis

`bensz-thesis` 是本仓库中面向毕业论文、博士后报告与特定申请表模板的公共包源码目录。

README 只描述公共包本身的职责、稳定入口和目录结构；具体学校、学位、示例正文与演示资产，应维护在各自的项目目录中。

## 包职责

- `xj-desert-fund-2026`：中国沙漠气象科学研究基金 2026 版申请书，项目见 [NSFC_2026_XJ-PVCast_final](../../projects/NSFC_2026_XJ-PVCast_final/README.md)。原生文字与矢量表框重建 13 页空白稿（含横向成员表）；正式稿按栏目自动续页、连续页码，固定字段检查溢出，文献条目间不附加空白，并防止条目首尾孤行跨页。成员表支持按需追加第8行，保留原行高及签名列，空白稿仍为官方7行。申请字段由项目元数据统一提供。

- `casm-open-fund-2026`：测绘科学与工程自然资源部重点实验室 2026 版开放基金申请书，见 [NSFC_2027_Mapping_final](../../projects/NSFC_2027_Mapping_final/README.md)。专属 profile/style/artwork 重建 10 页空白模板，含横向成员表、预算表、流式正文及固定区域溢出检查。栏目标题按实际标题与提示高度预留正文空间，避免长提示与正文分离；`\CasmBibliographyStylePath` 复用 `bensz-nsfc` 的 `gbt7714-nsfc.bst`，使用该文献样式的独立项目需同时安装 `bensz-nsfc`。

- `csu-open-fund-2026`：中南大学有色金属成矿预测教育部重点实验室 2026 版开放基金申请书，项目见 [`NSFC_2026_MineChangeTrust_final`](../../projects/NSFC_2026_MineChangeTrust_final/README.md)。原生文字与矢量表格重建 13 页空白表，研究正文可自动续页，栏目标题仅在首页显示，续页保留版框；正文 `\subsection` 按栏目自动编号为 `1.1`、`1.2` 等，填写数据留在项目 `extraTex/`。固定填写值与同行标签对齐基线，成员表单行及双行字段统一对齐，保留字段溢出检查。文献使用小五号字（9pt）、14bp 行距及零条目间距，`\CSUBibliographyStylePath` 复用 `bensz-nsfc` 中的 `gbt7714-nsfc.bst`；使用此文献样式的独立项目需同时安装 `bensz-nsfc`。
  固定表单的西文片段局部关闭 xeCJK 自动切换，以保留 Times New Roman 引号及其字宽；中文段落的标点规则不受影响。
  研究栏目和拆分栏目均只为空内容插入占位，非空正文结束不追加空行，避免接近满页时额外生成空白续页。

- 提供毕业论文模板的公共入口包、profile 与样式装配逻辑
- 提供 PDF 构建、DOCX 初稿导出、缓存清理与像素级比较脚本入口
- 依赖 `bensz-fonts` 统一管理共享字体资源
- `ciesm-open-fund`：开放基金申请书专属 profile，项目入口见 [`NSFC_2026_CIESM-STSR_final`](../../projects/NSFC_2026_CIESM-STSR_final/README.md)。封面、信息表、页脚、预算表、填写稿标题层级、图注分页与文献间距集中维护在独立 style；项目提供填写稿 `main.tex` 与四页空白 `blank.tex`，填写稿使用 Biber。该文档不使用学位枚举。
- 当前已注册独立模板：`thesis-smu-master`、`thesis-nju-master`、`thesis-just-bachelor`、`thesis-jxust-bachelor`、`thesis-ahnu-master`、`thesis-hit-doctor`、`thesis-jlau-doctor`、`thesis-jlau-master`、`thesis-nwu-doctor`、`thesis-cas-postdoc`、`thesis-smu-postdoc`、`thesis-sysu-doctor`、`thesis-ucas-doctor`

开放课题申请表另有独立 profile `ccnu-open-fund-2026`，由 [`projects/Huazhong_template`](../../projects/Huazhong_template/README.md) 与 [`projects/NSFC_2026_CCNU-EduAgentTrust_final`](../../projects/NSFC_2026_CCNU-EduAgentTrust_final/README.md) 共用。它复用本包 PDF 构建与 compare 入口，不使用学位元数据；封面、固定表格与研究章节续页样式在包内统一维护。研究栏目标题仅首页显示，正式提纲使用真正标题命令，文献取消条目与段间额外留白，原图与图注共同分页；长单位和专业字段局部适配并保留溢出检查。CCNU 项目提供正式、未删节审阅及独立七页空白入口，各入口须顺序构建。

构建器启用 `-recorder` 供 `bensz-fonts` 解析共享字体路径，并检查最后一趟 XeLaTeX 的退出码；在原有三遍编译后，若日志仍提示交叉引用需要重跑，最多追加两遍，并在 `.latex-cache/` 保留逐遍日志与输出。最后一遍失败或仍未收敛时，即使已产生 PDF，也不复制到项目根目录，构建命令返回失败。

## 目录说明

- `bensz-thesis.sty`：公共入口包
- `bthesis-core.sty`：profile 与样式装配入口
- `profiles/`：不同论文模板的 profile
- `styles/`：不同论文模板的稳定样式实现
- `../bensz-fonts/`：共享字体基础包；`bensz-thesis` 安装时会作为强制依赖一并安装
- `scripts/thesis_project_tool.py`：PDF 构建 / DOCX 导出 / 清理 / 像素级比较入口
- `scripts/thesis_docx_tool.py`：LaTeX 源到可编辑 Word 初稿的通用导出实现
- `scripts/package/install.py`：本地安装脚本
- `scripts/package/build_tds_zip.py`：TDS ZIP 打包脚本

## 使用方式

在仓库中开发时，优先直接调用：

```bash
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir <project-dir>
```

如需从同一份 LaTeX 源导出可编辑 Word 初稿：

```bash
python packages/bensz-thesis/scripts/thesis_project_tool.py docx --project-dir <project-dir>
```

DOCX 导出默认生成 `<project-dir>/main.docx`，中间 Markdown 与质量报告保存在 `<project-dir>/.latex-cache/docx/`。该功能定位为“可编辑 Word draft”：标题、正文、列表、图片、基础公式和基础引用会尽量保留；复杂表格、算法、代码块、TikZ 或 PDF 专属构造会写入占位符，并在质量报告中提示人工复核。若学校提供官方 Word 模板，建议显式传入：

```bash
python packages/bensz-thesis/scripts/thesis_project_tool.py docx \
  --project-dir <project-dir> \
  --reference-doc <path-to-reference.docx>
```

如需安装到本地 `TEXMFHOME`：

```bash
python packages/bensz-thesis/scripts/package/install.py
python packages/bensz-thesis/scripts/package/install.py install --ref main
python packages/bensz-thesis/scripts/package/install.py rollback
python packages/bensz-thesis/scripts/package/install.py check
```
