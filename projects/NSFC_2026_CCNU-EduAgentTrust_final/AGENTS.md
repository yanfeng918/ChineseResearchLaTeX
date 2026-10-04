# CCNU 教育智能体开放课题申请书

- 本项目是华中师范大学实验室 2026 版开放课题申请书。`NSFC_` 是项目目录命名；构建使用 `bensz-thesis` 的 `ccnu-open-fund-2026` profile。
- 正文和申请字段维护在 [extraTex/metadata.tex](extraTex/metadata.tex#L1) 及 [README.md](README.md#L25) 列出的文件；没有用户事实时保持空白。
- 稳定版式维护在公共包的 [profile](../../packages/bensz-thesis/profiles/bthesis-profile-ccnu-open-fund-2026.def#L1) 和 [style](../../packages/bensz-thesis/styles/bthesis-style-ccnu-open-fund-2026.tex#L1)，与 `Huazhong_template` 共用；修改共享样式须先规划回归。
- 保留官方提纲、承诺、横向成员表和签章区域。参考 PDF 只作基线，不能作为构建结果直通复制或整页嵌入。
- 用 `python3 scripts/thesis_build.py` 或官方 `thesis_project_tool.py build` 构建；交付文件为 `main.pdf`，中间文件位于 `.latex-cache/`。
- [main.tex](main.tex#L1) 是按篇幅整理的正式入口，[full.tex](full.tex#L1) 是未删节迁移审阅入口，[blank.tex](blank.tex#L1) 是独立七页空白入口。同项目入口必须顺序构建，避免共用缓存清理冲突。
- 封面、简表与简历引用同一份元数据；公开来源状态及缺项维护在[填写说明](docs/填写说明.md#L1)。原图 PDF、图注、标签与引用句由两份正文共用，不删图或擅自重绘。
- 一般课题按已核对的2026年度指南申请5万元、研究1年；[预算测算](docs/预算测算.md#L1)记录拟编分项及审核边界。`blank.tex`不得读取已填写预算或单位意见。民族等稳定事实可沿用本人既有确认，跨项目成员与授权不能自动沿用。2026-09-19用户已指定[参与者资料](../../docs/applicants/00_参与者信息.md#L1)用于本课题，七名成员及拟定分工已写入[members.tex](extraTex/members.tex#L1)；教学复核、实验室合作和课程授权仍需分别落实。
- 正式提纲用 `section`，内部用 `subsection`，按所属提纲连续编号。官方研究栏目标题只出现在首页，续页仅保留版框、正文及连续页码；参考文献零条目/段间额外间距由模板专属公共样式统一维护。
- [template.json](template.json#L1) 必须保持目录同名的 `project_name`、`document_type=open-fund-application` 和 `build_profile=thesis`；不使用学位 `degree`。
- 工作区和 VS Code 配置通过根级 `scripts/sync_vscode_configs.py --project NSFC_2026_CCNU-EduAgentTrust_final` 生成；验收记录、临时填写副本和差异图放在仓库 `tests/ccnu-eduagenttrust-template/`。
