# XJ-PVCast 开放基金申请书项目约定

本目录属于中国沙漠气象科学研究基金开放课题申请书，实际构建产品线为 `thesis`。以 [template.json](template.json#L1) 和 [extraTex/@config.tex](extraTex/@config.tex#L1) 为准，不按 `NSFC_` 目录前缀选择构建器。

- [main.tex](main.tex#L1) 是填写后的申请书入口；[blank.tex](blank.tex#L1) 是与官方13页空白表比较的独立入口。正文允许自然续页，不强制与空白版页数相同。
- 原生LaTeX文字、表格、表框和签章区域必须保持可编辑，不得改为整页截图或直接插入官方PDF。
- 项目层维护正文、摘要、图片、BibTeX和申请字段。稳定的表格、字体、标题、参考文献间距、页码及分页规则维护在 `packages/bensz-thesis/` 本模板专属profile/style/artwork。
- 修改公共包前先生成回归计划，按实际包引用发现全部直接消费者，包括不以 `thesis-` 开头的开放基金项目；修改后用官方入口验证目标和其他直接消费者。
- 所有重复基本信息从 [extraTex/metadata.tex](extraTex/metadata.tex#L1) 的 `\XJField{key}` 引用。保留既有已确认资料；公开来源待终核和未确认字段不得升级为确认事实。
- 事实优先级及原始来源见 [docs/00_项目事实库.md](docs/00_项目事实库.md#L1)，实际缺口见 [docs/填写说明与待补清单.md](docs/填写说明与待补清单.md#L1)。F-XJ-01至F-XJ-08来自原项目事实库，不新增同义缺口编号。
- 不改写研究结论，不把拟开展工作当已完成成果。迁移或排版修复后核对原段落、公式、引用及资源清单；原项目只读。
- 官方栏目标题每栏只出现一次。内部使用真正的 `\subsection` / `\subsubsection`，按栏目自动编号；续页不重复官方完整标题。
- 图1按用户明确要求改为 `figures/background-significance.tex` 原生TikZ背景意义图，沿用 `fig:xj-f01`；原 `F01.pdf` 保留作迁移原件，不再参与正文。图2使用 `figures/research-content-framework.tex`，标签为 `fig:xj-content-framework`。图3、4、6继续调用原字节的 `F02.pdf`、`F03.pdf`、`F05.pdf`；图5按本次方案确定要求调用 `F04-confirmed.pdf`，仅删除原生文字“( 暂定)”，原 `F04.pdf` 保留。标签保持，全稿6图自动编号。除已明确授权的图1替换和图5文字更新外，后续不得擅自重绘替代原图或裁切内容。
- 使用 `python3 scripts/thesis_build.py build --tex-file blank.tex` 和 `python3 scripts/thesis_build.py build --tex-file main.tex` 顺序构建；该wrapper转调 `packages/bensz-thesis/scripts/thesis_project_tool.py`。同一项目不同入口不得并行，避免共享缓存被清理。
- 使用同名 `.code-workspace` 打开项目；编辑器必须沿 `texlua` launcher和Python wrapper调用官方构建器。中间文件放 `.latex-cache/`，所有测试与比较材料放仓库 `tests/` 专用子目录。
- 编译错误必须解决；警告区分已有和新增。最终同时检查空白版式、正式长字段、标题、参考文献实际间距和个人信息一致性。日志与公开报告不复述电话或证件号码。
- 成员使用 `extraTex/team-metadata.tex` 统一字段：本次指定的7名新疆大学研究生全部回填，分工为授权拟定；连同申请人共8人。性别和年龄据所给证件编码整理后待本人核对，职称与已获最高学历未确认不推定，签名留空。第8行仅在正式成员表按需追加，空白模板保持官方7行。
- 本次授权已确定研究设计和3万元申请预算，以正式正文及项目事实库为准；申请预算不代表获批，成员实际投入及流程签章保留真实状态；模板交付完成与正式提交材料齐备分别陈述，不代签或推定审批通过。
