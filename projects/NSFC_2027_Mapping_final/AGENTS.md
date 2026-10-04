# 测绘实验室开放基金申请书项目指令

- 本项目使用 [template.json](template.json#L1) 声明的 `casm-open-fund-2026` / `build_profile=thesis`，即使目录名以 `NSFC_` 开头，也不得切换至 NSFC 构建器。
- 优先编辑 [extraTex/](extraTex/metadata.tex#L1) 内的字段和正文；稳定样式修改到 [公共 style](../../packages/bensz-thesis/styles/bthesis-style-casm-open-fund-2026.tex#L1)，固定表格标签与矢量线位于同目录 artwork。
- 通过 `python3 scripts/thesis_build.py` 构建，或在仓库中调用 `thesis_project_tool.py build --project-dir`；缓存放 `.latex-cache/`，验收放 `tests/` 子目录。
- 原始参考 PDF 是 2026 版；不因目录名中的 2027 自动替换年度、期限或官方措辞。
- 未给申请事实时保持字段留空；成员、预算及审核意见不得虚构。
- 固定表格的超长文字需精简；研究正文按普通 LaTeX 段落续页，禁止将整页 PDF 或截图嵌入以冒充可编辑模板。
