# NSFC_2026_CIESM-STSR_final 项目说明

- 本项目为开放基金申请书，采用 [main.tex](main.tex#L1) 和 [template.json](template.json#L1) 指定的 `ciesm-open-fund` 模板，不是 NSFC 正文或学位论文。
- 可编辑内容位于 [metadata.tex](extraTex/metadata.tex#L1)、[abstract.tex](extraTex/abstract.tex#L1)、[report.tex](extraTex/report.tex#L1) 引入的六份正文和 [budget.tex](extraTex/budget.tex#L1)。`main.tex` 为填写审阅稿，`blank.tex` 为独立四页空白入口；保留已确认内容与事实状态，不编造缺失事实。
- 官方标题、提示语和预算科目应保留。字体、框线、页脚和可复用宏维护在 [公共样式](../../packages/bensz-thesis/styles/bthesis-style-ciesm-open-fund.tex#L1)，项目中不复制共享字体或样式实现。
- 用 `python3 scripts/thesis_build.py` 构建；VS Code 打开 [NSFC_2026_CIESM-STSR_final.code-workspace](NSFC_2026_CIESM-STSR_final.code-workspace#L1)。wrapper 转调官方 `thesis_project_tool.py`，中间文件位于 `.latex-cache/`。
- 排版验证和测试产物放在仓库 `tests/ciesm-application-20260910/`，官方 PDF 作为只读基线，不得用于替代可编辑 LaTeX 输出。操作说明见 [README.md](README.md#L1)。
