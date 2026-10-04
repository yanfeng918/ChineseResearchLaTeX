# 华中师范大学开放课题申请书项目

- 本项目是 2026 版实验室开放课题申请书，复用 bensz-thesis 构建链路。
- 内容填写入口见 [README.md](README.md#L23)，固定版式在公共包的 [style](../../packages/bensz-thesis/styles/bthesis-style-ccnu-open-fund-2026.tex#L1) 与 [profile](../../packages/bensz-thesis/profiles/bthesis-profile-ccnu-open-fund-2026.def#L1)。不要把整套样式复制回项目。
- 保持官方原文、五个章节、横向成员表及签章区域；没有用户事实时保留空白。
- 通过 `python3 scripts/thesis_build.py` 或仓库官方 `thesis_project_tool.py build` 构建。最终 PDF 为 `main.pdf`，缓存为 `.latex-cache/`。
- 参考 PDF 只作版式基线，禁止将其直通复制或整页嵌入作为可编辑模板的构建结果。
- 测试夹具和差异图只写入仓库 `tests/` 子目录；本目录保留最终可交付 PDF。
