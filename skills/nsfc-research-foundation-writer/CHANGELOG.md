# 变更记录

## [0.2.0] - 2026-08-31

### Fixed

- **按编号 glob 定位写入目标，会在地区基金项目上静默写错章节**：`SKILL.md` 原写死 `extraTex/3.1.研究基础.tex` / `extraTex/3.2.工作条件.tex`，并指示"仅编辑两份 `extraTex/3.*.tex` 文件"。但 NSFC 模板不共用一套章节编号且互相重叠——三段式（`NSFC_General`/`NSFC_Young`）的 `3.1` 是「研究基础」，五段式（`NSFC_Local`/`NSFC_Local_Clean`）的 `3.1` 却是「不同类型国基情况」，属于「其他说明」里的声明章节；地区基金的研究基础与工作条件实际在 `2.1` / `2.2`。在地区基金项目上运行会把研究基础与工作条件写进声明章节，且编译不报错。现新增「落点解析（写作前必做）」章节：从 `main.tex` 未注释的 `\input{extraTex/...}` 按 `foundation` / `work_conditions` 两个角色解析，解析失败或角色缺失即停下询问，禁止回退到任一布局的硬编码文件名。
- **跨章节引用同样写死编号**：一致性校验原按 `2.1`（研究内容）与 `2.3`（年度研究计划）定位，而这两章在五段式为 `1.2.内容目标问题` / `1.5.研究计划`。现全部改为按角色引用。
- **误写风险**：承担项目 / 完成国基项目 / 项目完成情况与研究基础同属一个大节，且都在 `extraTex/3.*.tex`（三段式）或 `extraTex/2.*.tex`（五段式）的 glob 范围内。现在落点解析中显式排除，避免本技能写入这些必须按真实信息填写的文件。
- **版本号双真相来源**：`SKILL.md` frontmatter 的 `version` 与 `config.yaml` 各存一份，且 `version` 并非宿主支持的 frontmatter 字段。现移除 frontmatter 的 `version`，校验器改为"存在则必须与 `config.yaml` 一致"。

### Changed

- `config.yaml`：`targets`（写死文件名）改为 `layout_resolution` + `targets_three_part` / `targets_five_part` 两张已知布局表；`guardrails.allowed_write_files` 改为 `allowed_write_roles`（角色白名单），新增 `forbid_numeric_glob_targeting`。
- `scripts/check_project_outputs.py`：改为自行解析 `main.tex` 按角色定位、自动判定 `three-part` / `five-part` 布局，并与 `config.yaml` 的已知布局表做合理性校验；原有的风险条目数、已具备/尚缺结构、绝对化措辞等内容检查全部保留。
- `scripts/validate_skill.py`：新增回归护栏——两张布局表必须存在且互不相同、必须声明 `layout_resolution.resolve_from`、`allowed_write_roles` 必须含两个角色，且 `SKILL.md` 一旦提到编号 glob 就必须同时带有禁令文本。
- `SKILL.md` / `README.md` / `references/dod_checklist.md` 同步按角色改写；技能版本 `0.1.2` → `0.2.0`。

### Verified

- `validate_skill.py` 通过；`check_project_outputs.py` 在 `NSFC_Young` / `NSFC_General` 解析为 three-part（`3.1`/`3.2`），在 `NSFC_Local` 解析为 five-part（`2.1`/`2.2`），落点全部正确。

## [0.1.2] - 2026-04-24

### Fixed
- 修复 `SKILL.md` frontmatter 中混入 Markdown 正文导致技能加载器 YAML 解析失败的问题。

### Changed
- 将 `bensz-collect-bugs` 协作约定移出 YAML frontmatter，保留为正文执行规则。
- 增强 `scripts/validate_skill.py`，在 PyYAML 可用时对 `SKILL.md` frontmatter 执行严格 YAML 解析。

## [0.1.1] - 2026-02-16

### Added
- 新增只读自检脚本：`scripts/validate_skill.py`、`scripts/check_project_outputs.py`、`scripts/run_checks.py`

### Changed
- 强化 SKILL.md 的写入安全约束与参数说明，降低误改 LaTeX 结构风险
- 信息表与文档表述去年份化，提升通用性
- README 增加 `output_mode` 用法与可选自检入口

## [0.1.0] - 2026-01-14

### Added
- 初始版本发布
- 支持为 NSFC 标书正文"（三）研究基础"写作/重构
- 支持同步编排"工作条件"和"研究风险应对"
- 支持证据链验证、可行性四维分析、风险预案生成

### Changed
- 增强 SKILL.md 工作流步骤的详细指导
- 增加 config.yaml 的注释说明
- 增强 README.md 的用户引导

### Fixed
- 修复 quality_contract 配置未在工作流中引用的问题
- 修复工作流步骤缺少路径验证说明的问题
- 修复边缘情况处理说明缺失的问题
