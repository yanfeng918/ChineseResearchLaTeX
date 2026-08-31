# Changelog — nsfc-research-content-writer

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

（暂无）

## [1.1.0] - 2026-08-31

### Fixed（修复，高优先）

- **按编号 glob 定位写入目标，会在地区基金项目上静默写错章节**：`SKILL.md` 两处指示"仅编辑三份 `extraTex/2.*.tex` 文件"，但 NSFC 模板不共用一套章节编号且互相重叠——三段式的 `2.1` 是「研究内容」，五段式（`NSFC_Local`/`NSFC_Local_Clean`）的 `2.1` 却是「研究基础」。该 glob 在 `NSFC_Local` 上匹配到的是 `2.1.研究基础.tex` / `2.2.工作条件.tex` / `2.3.承担项目.tex`，会把研究内容、特色与创新、年度计划写进研究基础那三个文件，且编译不报错。现新增 `SKILL.md`「落点解析（写作前必做）」章节：从 `main.tex` 未注释的 `\input{extraTex/...}` 解析真实文件，按 `research_content` / `innovation` / `yearly_plan` / `scheme` 四个角色归类，解析失败或角色缺失即停下询问，禁止回退到任一布局的硬编码文件名。
- **技术路线在五段式项目上落错文件**：五段式有独立的 `1.3.方案及可行性.tex`，技术路线应写在那里而非并入研究内容。现已在 SKILL、README、`technical_route_structure.md`、DoD 四处按布局分别说明落点，两种布局的"总—分"结构要求保持一致。
- **自检链路整条失效**：`validate_skill.py` 硬性要求 `plans/` 目录，但该目录从未提交过，导致校验恒失败；`check_project_outputs.py` 又要求正文中出现 `S1`/`对应 S1` 等内部规划编号，而 `SKILL.md` 与 DoD 明令禁止这些编号进入正文——按规范写出的稿子跑检查必然报错。现修复：`plans/` 与 `tests/` 改为可选（仅在存在且非目录时报错）；`check_project_outputs.py` 删除 `S\d+` 强制要求，反过来改为**检测内部编号泄漏到正文**（`[STV]\d+` 出现即报错），与写作规范同向。
- **`check_project_outputs.py` 无法在五段式项目上工作**：原实现从 `config.yaml` 读死 `targets.*_tex`。现改为自行解析 `main.tex` 按角色定位、自动判定 `three-part` / `five-part` 布局，并与 `config.yaml` 的已知布局表做合理性校验（不一致时 WARN 提示可能是自定义模板）。已在 `NSFC_Young`/`NSFC_General`（三段式）与 `NSFC_Local`（五段式）上验证解析正确。
- **`validate_skill.py` 要求 frontmatter 必须有 `version` 且与 config 一致**：但宿主不支持 `version` 作为 frontmatter 字段（IDE 明确提示），且 `AGENTS.md` 规定 `config.yaml` 为版本号唯一真相来源。现改为：frontmatter 的 `version` 可选，若存在则必须与 `config.yaml` 一致（防漂移），校验输出统一打印 `config.yaml` 的版本号。

### Added（新增）

- 新增 [references/technical_route_structure.md](references/technical_route_structure.md)：技术路线"总—分"结构规范。包含总体路线四问（起点/主链/落位/闭合）、分项路线五要素（输入/方法与关键步骤/输出/验证口径/衔接）、"研究内容 ↔ 分路线"对应关系映射表与四项自检（数量一致/序号一致/术语一致/依赖闭合），以及 8 条技术路线专项反模式。
- `SKILL.md` 工作流新增独立步骤「写技术路线（"总—分"结构，强制）」，并在一致性校验步骤中新增「技术路线 ↔ 研究内容对应检查（必做）」与技术路线图图文一致性检查。
- `config.yaml` 新增 `technical_route` 节，固化总分结构、两层必需、分路线条数与序号须匹配研究内容、分路线五要素与总体路线五要素等约束。
- `config.yaml` 新增 `layout_resolution` 节（解析来源与角色关键词）与 `targets_three_part` / `targets_five_part` 两张已知布局表；`guardrails.allowed_write_files`（写死文件名）改为 `allowed_write_roles`（角色白名单）并新增 `forbid_numeric_glob_targeting`。
- `validate_skill.py` 新增回归护栏：两张布局表必须存在、必须互不相同、五段式必须给出 `scheme_tex`、必须声明 `layout_resolution.resolve_from`，且 `SKILL.md` 一旦提到编号 glob 就必须同时带有禁令文本——防止编号硬编码悄悄回潮。
- `references/dod_checklist.md` 新增 B2 节「技术路线"总—分"结构」共 8 条验收项；快速自检新增第 0 步（先填映射表）。
- `references/anti_patterns.md` 新增 6b/6c/6d 三组反模式：技术路线与研究内容不对应（缺口/孤儿/序号错位）、缺"总"或缺"分"、分路线只有方法和验证而无上下游接口。
- `references/output_skeletons.md` 的技术路线骨架由一行注释扩展为完整的总分两层骨架。

### Fixed（修复）

- **技术路线与研究内容脱节缺乏任何约束**：此前技术路线在 `SKILL.md` 中仅为一条 bullet（"技术路线与验证口径（对照/消融/外部验证/泄漏防控/统计方法，融入叙述而非单独罗列）"），既未要求总分结构，也未要求与研究内容逐项对应，`output_skeletons.md` 中只有 `% 技术路线与验证口径（可按子目标分组写）` 一行注释。实际写作中容易退化成与研究内容各说各话的方法罗列，是评审高频扣分点。现已在 SKILL、config、骨架、DoD、反模式五处建立完整约束。
- **版本号双真相来源**：`SKILL.md` frontmatter 写 `version: 0.2.3`，`config.yaml` 写 `1.0.0`，二者长期不一致。现移除 frontmatter 中的 `version` 字段，统一以 `config.yaml` 为唯一真相来源。

### Changed（变更）

- 技能版本 `1.0.0` → `1.1.0`；`SKILL.md` 与 `config.yaml` 的 `description` 均补充"技术路线按总—分两层结构编排并与研究内容逐项对应"。
- 明确"研究内容一/技术路线一"这类中文序号属于正文正常表述，**不在** `S1/T1/V1` 内部编号净化范围内，避免误删正文中的正常对应表述。

## [1.0.0] - 2026-02-24

### Changed

- `config.yaml`：版本号 `0.2.3 → 1.0.0`，标记为正式稳定版本
