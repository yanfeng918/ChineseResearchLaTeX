#!/usr/bin/env python3
"""基金画像（grant-profile.yaml）的推断、校验与查询入口。

各类基金申请书的章节切分互不兼容：同一个"立项依据"在不同模板里可能叫
"立论依据"，可能独立成文件，也可能与"研究内容"合并。写作类 skill 如果继续
按固定路径（如 ``extraTex/1.1.立项依据.tex``）寻址，换一个基金就会失效。

本模块把"章节角色 -> 实际文件"的映射抽成项目级的 ``grant-profile.yaml``，
让 skill 只认角色（role），不认路径。

角色有三种状态，缺一不可：

- ``file``：本模板有独立文件承载该角色
- ``merged_into``：本模板没有独立文件，该角色的内容必须写进另一个角色里
- ``absent``：本模板确实不要求该角色

``merged_into`` 是关键。以广东省基金为例，它没有"特色与创新""年度研究计划"
的独立文件；若把这两个角色简单标成 absent，写作 skill 会静默丢掉这两块内容，
而模板本身仍然要求在"研究内容"里写到。

用法::

    python scripts/grant_profile.py infer    --project-dir projects/GDNSF_General
    python scripts/grant_profile.py validate --project-dir projects/GDNSF_General
    python scripts/grant_profile.py show     --project-dir projects/GDNSF_General --role justification
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import Any


PROFILE_FILENAME = "grant-profile.yaml"

# 角色词表：role -> 文件名关键词。顺序即优先级，靠前的关键词匹配得分更高。
# 新增基金模板时优先在此扩充别名，不要在各 skill 里另立一套判断。
ROLE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "justification": ("立项依据", "立论依据", "立项论据", "项目的立项依据"),
    "research_content": ("研究内容", "研究目标", "内容目标"),
    "key_questions": ("关键科学问题", "科学问题"),
    "research_scheme": ("研究方案", "可行性", "技术路线"),
    "innovation": ("特色与创新", "创新点", "特色", "创新"),
    "yearly_plan": ("年度研究计划", "年度计划", "研究计划"),
    "expected_results": ("预期研究结果", "预期成果", "预期结果"),
    "research_foundation": ("研究工作基础", "研究基础", "工作基础"),
    "work_conditions": ("实验条件", "工作条件"),
    "team_members": ("项目组人员", "申请人简介", "人员简介", "研究队伍"),
    "ongoing_projects": ("申请或承担科研项目", "承担项目", "在研项目"),
    # "项目情况" 放在 ongoing_projects 之后，"承担项目情况"会先被前者认领。
    "completed_projects": ("项目完成情况", "完成情况", "结题情况", "项目情况"),
    "ai_disclosure": ("生成式人工智能", "生成式AI", "人工智能使用"),
    "budget_plan": ("经费分配", "预算说明", "经费预算"),
    "management": ("组织实施", "组织管理", "管理措施"),
    "site_scale": ("实施地点", "实施规模"),
    "attachments": ("附件清单", "其他附件"),
    # 以下角色在 NSFC 模板中并入其它章节，但在产业/重点研发类基金里独立成节
    "guideline_alignment": ("指南方向", "关联关系", "指南匹配"),
    "assessment_indicators": ("考核指标", "评测方式", "考核方式"),
    "economic_benefits": ("经济社会效益", "社会效益", "经济效益"),
    "partners": ("协作单位", "参与单位", "合作单位"),
    "task_division": ("任务分工", "单位分工", "分工"),
    "intl_cooperation": ("国际合作", "对外交流"),
    "safeguards": ("保障措施", "支撑条件"),
    "ip_strategy": ("知识产权", "成果管理", "权益分配"),
    "risk_analysis": ("风险分析", "风险及对策", "风险"),
    "other": ("其他", "其它"),
}

# 写作主链路角色：推断不到时必须由人确认，不允许静默判为 absent。
CORE_WRITING_ROLES: tuple[str, ...] = (
    "justification",
    "research_content",
    "innovation",
    "yearly_plan",
    "research_foundation",
)

# 每个角色的中文名，用于报告与生成的注释。
ROLE_LABELS: dict[str, str] = {
    "justification": "立项依据",
    "research_content": "研究内容",
    "key_questions": "关键科学问题",
    "research_scheme": "研究方案与可行性",
    "innovation": "特色与创新",
    "yearly_plan": "年度研究计划",
    "expected_results": "预期研究结果",
    "research_foundation": "研究基础",
    "work_conditions": "工作条件",
    "team_members": "项目组人员",
    "ongoing_projects": "申请或承担科研项目",
    "completed_projects": "项目完成情况",
    "ai_disclosure": "生成式人工智能声明",
    "budget_plan": "经费与预算",
    "management": "组织实施与管理",
    "site_scale": "实施地点及规模",
    "attachments": "附件清单",
    "guideline_alignment": "与指南方向的关联",
    "assessment_indicators": "考核指标与评测方式",
    "economic_benefits": "预期经济社会效益",
    "partners": "协作单位",
    "task_division": "任务分工",
    "intl_cooperation": "国际合作与交流",
    "safeguards": "保障措施",
    "ip_strategy": "知识产权与成果管理",
    "risk_analysis": "风险分析及对策",
    "other": "其他",
}

# 宏级寻址的角色词表：role -> 宏名关键词（英文，大小写不敏感）。
# 部分模板不用"一节一文件"，而是把正文存成 \newcommand 宏、再由版式文件
# 按固定坐标渲染（见 projects/NSFC_2027_Silk_Road_Smart_Logistic_v2）。
MACRO_KEYWORDS: dict[str, tuple[str, ...]] = {
    "justification": ("foreignresearch", "domesticresearch", "background", "justification"),
    "guideline_alignment": ("guidealignment", "guidelinealignment"),
    "assessment_indicators": ("objectives", "indicators", "assessment"),
    "expected_results": ("outcomeforms", "expectedresults", "deliverables"),
    "research_content": ("researchcontent",),
    "research_scheme": ("researchmethods", "methodfeasibility", "technicalroute"),
    "innovation": ("innovation",),
    "economic_benefits": ("benefits",),
    "research_foundation": ("priorwork", "foundation"),
    "team_members": ("teamachievements", "team", "members"),
    "work_conditions": ("researchconditions", "conditions"),
    "partners": ("partneradvantages", "partner"),
    "task_division": ("taskdivision",),
    "intl_cooperation": ("internationalcooperation",),
    "yearly_plan": ("schedule", "yearlyplan", "timeline"),
    "management": ("organization",),
    "safeguards": ("safeguards",),
    "ip_strategy": ("intellectualproperty",),
    "risk_analysis": ("risk",),
}

_INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
_NEWCOMMAND_RE = re.compile(r"\\newcommand\s*\{\s*\\([A-Za-z]+)\s*\}")

# 天然不承载正文角色的 include，不必提示"未匹配到角色"。
_NON_CONTENT_INPUTS = ("@config", "references/", "reference.tex")


class ProfileError(Exception):
    """画像文件缺失、结构非法或与项目实际文件不一致。"""


def _strip_tex_comment(line: str) -> str:
    """去掉 TeX 行注释，保留被转义的 ``\\%``。"""
    out: list[str] = []
    escaped = False
    for ch in line:
        if escaped:
            out.append(ch)
            escaped = False
            continue
        if ch == "\\":
            out.append(ch)
            escaped = True
            continue
        if ch == "%":
            break
        out.append(ch)
    return "".join(out)


def parse_input_chain(main_tex: Path) -> list[str]:
    """按出现顺序取出 main.tex 中未被注释的 ``\\input``/``\\include`` 路径。

    被注释掉的章节代表该模板当前不启用，必须排除；否则篇幅统计和写作目标
    都会把不会编译进 PDF 的文件算进来。
    """
    if not main_tex.is_file():
        raise ProfileError(f"未找到 main.tex：{main_tex}")

    paths: list[str] = []
    for raw in main_tex.read_text(encoding="utf-8", errors="ignore").splitlines():
        for match in _INPUT_RE.finditer(_strip_tex_comment(raw)):
            target = match.group(1).strip()
            if target:
                paths.append(target)
    return paths


def _matches_role(stem: str, role: str) -> bool:
    """判断文件名是否命中某个角色的任一别名。"""
    return any(keyword in stem for keyword in ROLE_KEYWORDS[role])


def detect_macro_file(project_dir: Path) -> Path | None:
    """找出以 ``\\newcommand`` 承载正文的文件。

    判据是"定义了足够多正文宏"，而不是文件名：宏定义零星出现属于普通样式代码，
    成批出现（>=8 个且多数命中角色词表）才是正文载体。
    """
    best: tuple[int, Path] | None = None
    for candidate in sorted(project_dir.rglob("*.tex")):
        if any(part.startswith(".") for part in candidate.parts):
            continue
        names = _NEWCOMMAND_RE.findall(
            candidate.read_text(encoding="utf-8", errors="ignore")
        )
        if len(names) < 8:
            continue
        hits = sum(1 for n in names if _match_macro_role(n))
        if hits >= max(5, len(names) // 2) and (best is None or hits > best[0]):
            best = (hits, candidate)
    return best[1] if best else None


def _match_macro_role(macro_name: str) -> str | None:
    """把宏名匹配到角色；按 MACRO_KEYWORDS 的声明顺序取第一个命中。"""
    lowered = macro_name.lower()
    for role, keywords in MACRO_KEYWORDS.items():
        if any(kw in lowered for kw in keywords):
            return role
    return None


def infer_macro_roles(macro_file: Path) -> tuple[dict[str, dict[str, Any]], list[str], list[str]]:
    """从宏定义文件推断角色映射。

    同一角色可能对应多个宏（如"立项依据"拆成国外/国内现状两个宏），
    按定义顺序聚合到 ``macros`` 列表。
    """
    names = _NEWCOMMAND_RE.findall(macro_file.read_text(encoding="utf-8", errors="ignore"))

    grouped: dict[str, list[str]] = {}
    unmatched: list[str] = []
    for name in names:
        role = _match_macro_role(name)
        if role:
            grouped.setdefault(role, []).append(name)
        else:
            unmatched.append(name)

    roles: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []
    for role in ROLE_KEYWORDS:
        macros = grouped.get(role)
        if macros:
            roles[role] = {"macro": macros[0]} if len(macros) == 1 else {"macros": macros}
        elif role in CORE_WRITING_ROLES:
            roles[role] = {"unresolved": True}
            warnings.append(
                f"核心写作角色 {role}（{ROLE_LABELS[role]}）未匹配到任何宏，已标为 unresolved。"
                f"请人工确认：是并入了其它角色（merged_into），本模板不要求（absent），"
                f"还是需要在 MACRO_KEYWORDS 里补充宏名别名"
            )
        else:
            roles[role] = {"absent": True}

    notes = [f"宏未匹配到任何角色，写作类 skill 不会寻址它：\\{n}" for n in unmatched]
    return roles, warnings, notes


def infer_roles(project_dir: Path) -> tuple[dict[str, dict[str, Any]], list[str], list[str]]:
    """从 main.tex 的 input 链推断角色映射。

    返回 ``(roles, warnings, notes)``。warnings 是必须人工处理的待办
    （核心写作角色未解析）；notes 只是提示（文件不承载任何角色）。
    """
    inputs = [
        p
        for p in parse_input_chain(project_dir / "main.tex")
        if not any(marker in p for marker in _NON_CONTENT_INPUTS)
    ]

    # 每个文件归给命中的、声明顺序最靠前的角色。
    # 不能按关键词长度打分：广西的"研究内容目标与关键科学问题"里
    # "关键科学问题"比"研究内容"长，会把主角色错判成 key_questions。
    # ROLE_KEYWORDS 的声明顺序即角色优先级，核心写作角色排在细分角色之前。
    assigned: dict[str, str] = {}
    matches: dict[str, set[str]] = {}
    for rel in inputs:
        stem = Path(rel).stem
        hit = [role for role in ROLE_KEYWORDS if _matches_role(stem, role)]
        if not hit:
            continue
        matches[rel] = set(hit)
        # 一个角色只认领一个文件；重复命中的留给后续 merged_into 处理。
        primary = next((role for role in hit if role not in assigned), None)
        if primary:
            assigned[primary] = rel

    roles: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []
    for role in ROLE_KEYWORDS:
        if role in assigned:
            roles[role] = {"file": assigned[role]}
            continue

        # 该角色没有独立文件：若它的关键词命中了别人的文件，视为合并。
        host = next(
            (
                owner_role
                for rel, hit_roles in matches.items()
                if role in hit_roles
                for owner_role, owner_rel in assigned.items()
                if owner_rel == rel
            ),
            None,
        )
        if host:
            roles[role] = {"merged_into": host}
        elif role in CORE_WRITING_ROLES:
            # 核心写作角色绝不能默认 absent：多数模板（如广东省基金）并非
            # 不要求"特色与创新""年度计划"，而是要求写进"研究内容"里。
            # 默认 absent 会让 writer 静默丢掉这部分内容，所以留成待裁决状态，
            # 由 validate 拦下，强制人工在 merged_into / absent 之间选。
            roles[role] = {"unresolved": True}
            warnings.append(
                f"核心写作角色 {role}（{ROLE_LABELS[role]}）未匹配到独立文件，"
                f"已标为 unresolved。请人工确认：是并入了其它章节（改成 merged_into），"
                f"还是本模板确实不要求（改成 absent）"
            )
        else:
            roles[role] = {"absent": True}

    # 无角色文件多为承诺性说明章节（如"不同类型国基情况"），写作类 skill 本就不碰它们，
    # 只作提示，不作待办；核心角色未解析才是必须处理的。
    notes = [
        f"文件未匹配到任何角色，写作类 skill 不会寻址它：{rel}"
        for rel in inputs
        if rel not in matches
    ]

    return roles, warnings, notes


def _quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_profile(
    project_dir: Path,
    roles: dict[str, dict[str, Any]],
    *,
    macro_file: Path | None = None,
) -> str:
    """生成带注释的 grant-profile.yaml 文本。

    手写而非 yaml.dump，是为了保留角色顺序和中文注释——这份文件要给人读和改。
    """
    lines = [
        "# 基金画像（grant-profile.yaml）",
        "# 由 `python scripts/grant_profile.py infer` 生成，请人工复核后使用。",
        "# 规范见 docs/grant-profile-spec.md。",
        "#",
        "# roles 的三种状态：",
        "#   file/files:  本模板有独立文件承载该角色",
        "#   macro/macros: 正文存在 \\newcommand 宏里（宏级寻址）",
        "#   merged_into: 本模板无独立文件，内容须写进目标角色（不可当作不用写）",
        "#   absent:      本模板确实不要求该角色",
        "",
    ]
    if macro_file is not None:
        rel_macro = macro_file.relative_to(project_dir).as_posix()
        lines += [
            "# 宏级寻址：正文不是一节一文件，而是集中定义在下面这个文件的",
            "# \\newcommand 宏里，再由版式文件按固定坐标渲染。写作时改写宏体，",
            "# 不要新建 extraTex 文件。",
            "addressing: macro",
            f"macro_file: {_quote(rel_macro)}",
            "",
        ]
    lines += [
        "grant:",
        f"  name: {_quote(project_dir.name)}   # TODO 改成基金全称，如“广东省自然科学基金-面上项目”",
        "  agency: \"\"           # TODO 资助机构",
        "  duration_years: 3    # TODO 资助年限，决定年度计划写几年",
        "  source: \"\"           # TODO 依据的官方模板版本，如“2024年度申请书模板”",
        "",
        "roles:",
    ]

    for role, spec in roles.items():
        label = ROLE_LABELS.get(role, role)
        lines.append(f"  {role}:   # {label}")
        if "file" in spec:
            lines.append(f"    file: {_quote(spec['file'])}")
        elif "files" in spec:
            lines.append("    files:")
            lines.extend(f"      - {_quote(f)}" for f in spec["files"])
        elif "macro" in spec:
            lines.append(f"    macro: {spec['macro']}")
        elif "macros" in spec:
            lines.append("    macros:")
            lines.extend(f"      - {m}" for m in spec["macros"])
        elif "merged_into" in spec:
            host = spec["merged_into"]
            lines.append(f"    merged_into: {host}   # 无独立文件，须写进{ROLE_LABELS.get(host, host)}")
        elif "unresolved" in spec:
            lines.append("    unresolved: true   # TODO 必填：改成 merged_into: <角色> 或 absent: true")
        else:
            lines.append("    absent: true")

    lines += [
        "",
        "# 篇幅预算：不同基金差异极大，务必按当年指南校对后再用。",
        "length_budget:",
        "  unit: cjk_chars",
        "  pages:",
        "    max: null        # TODO 建议上限（留缓冲）",
        "    hard_max: null   # TODO 指南硬上限",
        "  by_role: {}        # TODO 形如 justification: [8000, 10000]",
        "",
        "# 模拟评审口径，供 nsfc-reviewers 使用。",
        "review:",
        "  grant_type: \"\"   # TODO 如“省级面上项目”",
        "  criteria: []     # TODO 该基金公开的评审要点",
        "",
    ]
    return "\n".join(lines)


def load_profile(project_dir: Path) -> dict[str, Any] | None:
    """读取项目画像；不存在返回 None（调用方据此回退到旧的硬编码默认值）。"""
    path = Path(project_dir) / PROFILE_FILENAME
    if not path.is_file():
        return None

    import yaml

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8", errors="ignore")) or {}
    except yaml.YAMLError as exc:
        raise ProfileError(f"{path} 解析失败：{exc}") from exc
    if not isinstance(data, dict):
        raise ProfileError(f"{path} 顶层必须是 mapping")
    return data


def resolve_role(profile: dict[str, Any], role: str) -> tuple[str, Any]:
    """把角色解析成 ``(state, value)``。

    state 为 ``file`` / ``merged_into`` / ``absent`` / ``unresolved`` / ``unknown``。
    调用方必须显式处理 ``merged_into``，否则会丢内容；遇到 ``unresolved``
    应停下来要求用户补全画像，不要擅自当成 absent。
    """
    spec = (profile.get("roles") or {}).get(role)
    if not isinstance(spec, dict):
        return ("unknown", None)
    if spec.get("file"):
        return ("file", spec["file"])
    # 一个角色可以跨多个文件：广西重点研发把"立项依据"拆成
    # "国外研究现状"+"国内研究现状"两节。第一个是主写入目标，其余一并返回。
    if isinstance(spec.get("files"), list) and spec["files"]:
        return ("files", list(spec["files"]))
    if spec.get("macro"):
        return ("macro", spec["macro"])
    if isinstance(spec.get("macros"), list) and spec["macros"]:
        return ("macros", list(spec["macros"]))
    if spec.get("merged_into"):
        return ("merged_into", spec["merged_into"])
    if spec.get("unresolved"):
        return ("unresolved", None)
    if spec.get("absent"):
        return ("absent", None)
    return ("unknown", None)


def validate_profile(project_dir: Path) -> list[str]:
    """校验画像与项目实际文件一致，返回问题列表（空列表表示通过）。"""
    project_dir = Path(project_dir)
    profile = load_profile(project_dir)
    if profile is None:
        return [f"缺少 {PROFILE_FILENAME}"]

    problems: list[str] = []
    roles = profile.get("roles")
    if not isinstance(roles, dict) or not roles:
        return ["roles 缺失或为空"]

    is_macro_mode = str(profile.get("addressing") or "file").strip() == "macro"
    defined_macros: set[str] = set()
    if is_macro_mode:
        rel_macro = str(profile.get("macro_file") or "").strip()
        if not rel_macro:
            return ["addressing: macro 时必须声明 macro_file"]
        macro_path = project_dir / rel_macro
        if not macro_path.is_file():
            return [f"macro_file 不存在：{rel_macro}"]
        defined_macros = set(
            _NEWCOMMAND_RE.findall(macro_path.read_text(encoding="utf-8", errors="ignore"))
        )

    try:
        chain = set(parse_input_chain(project_dir / "main.tex"))
    except ProfileError as exc:
        problems.append(str(exc))
        chain = set()

    for role, spec in roles.items():
        if not isinstance(spec, dict):
            problems.append(f"{role}: 取值必须是 mapping")
            continue

        if spec.get("unresolved"):
            problems.append(
                f"{role}（{ROLE_LABELS.get(role, role)}）: 仍是 unresolved，"
                f"请改成 merged_into: <角色> 或 absent: true 后再使用"
            )
            continue

        states = [k for k in ("file", "files", "macro", "macros", "merged_into", "absent") if spec.get(k)]
        if len(states) != 1:
            problems.append(
                f"{role}: 必须且只能声明 file / files / macro / macros / merged_into / absent 之一，"
                f"当前为 {states or '空'}"
            )
            continue

        if "macro" in states or "macros" in states:
            if not is_macro_mode:
                problems.append(f"{role}: 使用了 macro/macros，但顶层未声明 addressing: macro")
                continue
            names = [spec["macro"]] if "macro" in states else list(spec["macros"])
            for name in names:
                if name not in defined_macros:
                    problems.append(f"{role}: 宏 \\{name} 未在 macro_file 中定义")
        elif "file" in states or "files" in states:
            rels = [spec["file"]] if "file" in states else list(spec["files"])
            if "files" in states and not all(isinstance(r, str) for r in rels):
                problems.append(f"{role}: files 必须是字符串列表")
                continue
            for rel in rels:
                if not (project_dir / rel).is_file():
                    problems.append(f"{role}: 文件不存在 {rel}")
                elif chain and rel not in chain:
                    problems.append(f"{role}: {rel} 不在 main.tex 的 input 链里（不会编译进 PDF）")
        elif "merged_into" in states:
            host = spec["merged_into"]
            if host not in roles:
                problems.append(f"{role}: merged_into 指向未定义的角色 {host}")
            elif not any(
                (roles[host] or {}).get(k) for k in ("file", "files", "macro", "macros")
            ):
                problems.append(f"{role}: merged_into 的目标 {host} 自身没有可写目标，无处承载")

    for role in CORE_WRITING_ROLES:
        if role not in roles:
            problems.append(f"缺少核心写作角色定义：{role}（{ROLE_LABELS[role]}）")

    return problems


def _cmd_infer(args: argparse.Namespace) -> int:
    project_dir = Path(args.project_dir).resolve()

    # 先判断寻址方式：正文集中在 \newcommand 宏里的项目，按文件名推断只会得到
    # 一份几乎全 absent 的错误画像。
    macro_file = detect_macro_file(project_dir)
    if macro_file is not None:
        print(f"[识别] 宏级寻址，正文载体：{macro_file.relative_to(project_dir).as_posix()}")
        roles, warnings, notes = infer_macro_roles(macro_file)
    else:
        roles, warnings, notes = infer_roles(project_dir)
    target = project_dir / PROFILE_FILENAME

    if target.exists() and not args.force:
        print(f"[跳过] 已存在 {target}，如需覆盖请加 --force", file=sys.stderr)
        return 1

    text = render_profile(project_dir, roles, macro_file=macro_file)
    if args.dry_run:
        print(text)
    else:
        target.write_text(text, encoding="utf-8")
        print(f"[写入] {target}")

    for role, spec in roles.items():
        state = next(iter(spec))
        raw = spec[state] if state in ("file", "files", "macro", "macros", "merged_into") else ""
        value = ", ".join(raw) if isinstance(raw, list) else raw
        print(f"  {role:22s} {state:12s} {value}")

    for note in notes:
        print(f"[提示] {note}", file=sys.stderr)
    for warning in warnings:
        print(f"[需确认] {warning}", file=sys.stderr)
    return 0


def _cmd_validate(args: argparse.Namespace) -> int:
    problems = validate_profile(Path(args.project_dir))
    if not problems:
        print(f"[通过] {args.project_dir}")
        return 0
    print(f"[失败] {args.project_dir}", file=sys.stderr)
    for problem in problems:
        print(f"  - {problem}", file=sys.stderr)
    return 1


def _cmd_show(args: argparse.Namespace) -> int:
    profile = load_profile(Path(args.project_dir))
    if profile is None:
        print(f"[缺失] 未找到 {PROFILE_FILENAME}", file=sys.stderr)
        return 1
    state, value = resolve_role(profile, args.role)
    print(f"{args.role}\t{state}\t{value if value is not None else ''}")
    return 0 if state != "unknown" else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="基金画像的推断、校验与查询")
    sub = parser.add_subparsers(dest="command", required=True)

    p_infer = sub.add_parser("infer", help="从 main.tex 推断并生成 grant-profile.yaml")
    p_infer.add_argument("--project-dir", required=True)
    p_infer.add_argument("--force", action="store_true", help="覆盖已存在的画像")
    p_infer.add_argument("--dry-run", action="store_true", help="只打印不写文件")
    p_infer.set_defaults(func=_cmd_infer)

    p_validate = sub.add_parser("validate", help="校验画像与项目实际文件是否一致")
    p_validate.add_argument("--project-dir", required=True)
    p_validate.set_defaults(func=_cmd_validate)

    p_show = sub.add_parser("show", help="查询单个角色的解析结果")
    p_show.add_argument("--project-dir", required=True)
    p_show.add_argument("--role", required=True)
    p_show.set_defaults(func=_cmd_show)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ProfileError as exc:
        print(f"[错误] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
