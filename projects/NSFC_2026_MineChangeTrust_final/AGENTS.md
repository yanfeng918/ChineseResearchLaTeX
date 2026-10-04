# 中南大学实验室开放基金申请书

- 本项目是 2026 版开放基金申请书，使用 `build_profile=thesis`；不能按目录名前缀切换到 NSFC 模板。
- 正文及申请信息维护在 [extraTex/metadata.tex](extraTex/metadata.tex#L1) 与相应章节文件，入口为 [main.tex](main.tex#L1)。用户未提供的信息保持空白，不编造经历、成果、资助金额或签署意见。
- 稳定版式维护在 [csu-open-fund-2026 style](../../packages/bensz-thesis/styles/bthesis-style-csu-open-fund-2026.tex#L1)，不把样式或共享字体复制回本项目。
- 官方构建：`python3 scripts/thesis_build.py`；缓存保存在 `.latex-cache/`。
- [blank.tex](blank.tex#L1) 为 13 页空白验收入口；使用 `python3 scripts/thesis_build.py build --tex-file blank.tex`。同一项目的不同入口应顺序构建，避免官方构建器清理共享缓存时冲突。
- 参考 PDF 仅用于验收，不得用 PDF 直通或截图替代可编辑模板。
- 研究正文允许续页；固定信息表、成员表及意见栏超高时须缩短内容或补充附件，不得静默裁切。
- 签章由本人、所在单位或实验室按原模板要求完成，封面项目编号不由申请者填写。
- 模板说明与填写入口见 [README.md](README.md#L1)。
