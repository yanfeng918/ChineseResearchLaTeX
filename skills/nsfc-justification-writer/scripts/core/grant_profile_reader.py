#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""读取项目级基金画像（grant-profile.yaml），把章节角色解析成实际文件路径。

各类基金申请书的章节切分互不兼容：同一个"立项依据"在广东省基金里叫
"立论依据"，在广西基金里"研究内容"与"关键科学问题"合在一个文件。本 skill
原先按固定路径寻址（``extraTex/1.1.立项依据.tex``），换基金即失效。

有画像就按画像走，没有就回退到 config.yaml 里的原有默认值——因此对既有
NSFC 项目完全无感。

本文件是 ``scripts/grant_profile.py`` 的精简只读版，随 skill 分发；
角色词表、推断与校验逻辑只在仓库根的那份维护，改动请优先改那边。
"""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Tuple


PROFILE_FILENAME = "grant-profile.yaml"

# \newcommand{\Name}、\newcommand*{\Name}、\renewcommand{\Name} 三种写法
_MACRO_DEF_RE_TEMPLATE = r"\\(?:re)?newcommand\*?\s*\{\s*\\%s\s*\}"
# 宏名与参数声明之间可能有 [n][default]
_MACRO_ARGS_RE = re.compile(r"\s*(?:\[[^\]]*\]\s*)*")


def _match_closing_brace(text: str, open_index: int) -> Optional[int]:
    """从 ``text[open_index]`` 的 ``{`` 出发找配对的 ``}``，返回其下标。

    正文里嵌套花括号很常见（``\\textbf{...}``、``$\\geq 99\\%$`` 等），
    只找下一个 ``}`` 会截断宏体。这里逐字符配对，并跳过：
    - 被反斜杠转义的 ``\\{`` ``\\}``
    - ``%`` 起始到行尾的 TeX 注释（注释里的花括号不参与配对）
    """
    if open_index >= len(text) or text[open_index] != "{":
        return None

    depth = 0
    i = open_index
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == "\\":
            i += 2  # 跳过转义序列整体，\{ \} \\ 都不参与配对
            continue
        if ch == "%":
            newline = text.find("\n", i)
            i = n if newline == -1 else newline + 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return None


def find_macro_body_span(text: str, macro_name: str) -> Optional[Tuple[int, int]]:
    """定位宏体在 ``text`` 中的区间 ``[start, end)``（不含两侧花括号）。

    找不到定义或花括号不配对时返回 None——调用方必须据此报错，
    不能当作"宏体为空"继续写入。
    """
    pattern = re.compile(_MACRO_DEF_RE_TEMPLATE % re.escape(macro_name))
    match = pattern.search(text)
    if not match:
        return None

    cursor = _MACRO_ARGS_RE.match(text, match.end()).end()
    if cursor >= len(text) or text[cursor] != "{":
        return None

    close = _match_closing_brace(text, cursor)
    if close is None:
        return None
    return (cursor + 1, close)


def read_macro_body(text: str, macro_name: str) -> Optional[str]:
    """取出宏体原文；宏不存在返回 None。"""
    span = find_macro_body_span(text, macro_name)
    return text[span[0]:span[1]] if span else None


def replace_macro_body(text: str, macro_name: str, new_body: str) -> Tuple[str, bool]:
    """只替换指定宏的宏体，返回 ``(新全文, 是否替换成功)``。

    同一个 ``macro_file`` 通常并存二十多个角色的正文，整文件重写会把它们
    全部冲掉，因此写入必须走这个函数。
    """
    span = find_macro_body_span(text, macro_name)
    if span is None:
        return (text, False)
    return (text[: span[0]] + new_body + text[span[1] :], True)


def load_profile(project_root: Path | str) -> Optional[Dict[str, Any]]:
    """读取画像；不存在或不可解析时返回 None，由调用方回退到默认配置。"""
    path = Path(project_root) / PROFILE_FILENAME
    if not path.is_file():
        return None
    try:
        import yaml  # type: ignore
    except (ModuleNotFoundError, ImportError):
        return None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8", errors="ignore")) or {}
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def resolve_role(profile: Dict[str, Any], role: str) -> Tuple[str, Any]:
    """把角色解析成 ``(state, value)``。

    state ∈ {file, merged_into, absent, unresolved, unknown}。
    """
    spec = (profile.get("roles") or {}).get(role)
    if not isinstance(spec, dict):
        return ("unknown", None)
    if spec.get("file"):
        return ("file", spec["file"])
    # 一个角色可跨多个文件（如"立项依据"拆成国外现状+国内现状两节）
    if isinstance(spec.get("files"), list) and spec["files"]:
        return ("files", list(spec["files"]))
    # 宏级寻址：正文存在 \newcommand 宏里，写入目标是 macro_file 中的指定宏体
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


def resolve_role_files(
    profile: Dict[str, Any], role: str
) -> Tuple[List[str], str, Optional[str]]:
    """解析角色对应的全部文件，返回 ``(相对路径列表, state, 宿主角色)``。

    ``merged_into`` 会跟随到宿主角色的文件：该角色的内容必须写进宿主文件，
    而不是被跳过。跟随深度限制为 3 层，避免画像里出现环。
    """
    macro_file = str(profile.get("macro_file") or "").strip()
    seen: List[str] = []
    current = role
    for _ in range(3):
        state, value = resolve_role(profile, current)
        if state in ("file", "files"):
            rels = [str(value)] if state == "file" else [str(v) for v in value]
            host = current if current != role else None
            return (rels, "merged_into" if host else state, host)
        if state in ("macro", "macros"):
            # 宏级寻址：可写文件只有一个（macro_file），真正的定位靠宏名。
            # 调用方必须用 resolve_role_macros 拿到宏名并只改写对应宏体，
            # 整文件覆盖会冲掉同一文件里其它角色的正文。
            host = current if current != role else None
            return ([macro_file] if macro_file else [], "merged_into" if host else state, host)
        if state != "merged_into":
            return ([], state, None)
        if value in seen:
            return ([], "unresolved", None)
        seen.append(current)
        current = str(value)
    return ([], "unresolved", None)


def resolve_role_file(
    profile: Dict[str, Any], role: str
) -> Tuple[Optional[str], str, Optional[str]]:
    """解析角色的**主**写入文件，返回 ``(相对路径, state, 宿主角色)``。

    角色跨多个文件时返回第一个；需要全部文件请用 ``resolve_role_files``。
    宏级寻址下返回的是 ``macro_file``，还须配合 ``resolve_role_macros``。
    """
    rels, state, host = resolve_role_files(profile, role)
    return (rels[0] if rels else None, state, host)


def is_macro_addressing(profile: Dict[str, Any]) -> bool:
    """该项目是否用 \\newcommand 宏承载正文，而不是一节一文件。"""
    return str(profile.get("addressing") or "file").strip() == "macro"


def resolve_role_macros(profile: Dict[str, Any], role: str) -> List[str]:
    """取角色对应的宏名列表；非宏级寻址返回空列表。

    写作时必须只替换这些宏的宏体，不能整文件重写——同一个 ``macro_file``
    里通常并存二十多个角色的正文。
    """
    if not is_macro_addressing(profile):
        return []
    current = role
    for _ in range(3):
        state, value = resolve_role(profile, current)
        if state == "macro":
            return [str(value)]
        if state == "macros":
            return [str(v) for v in value]
        if state != "merged_into":
            return []
        current = str(value)
    return []


def _set_dotted(container: Dict[str, Any], dotted_key: str, value: Any) -> Any:
    """按 ``a.b`` 形式的键写入嵌套 mapping，返回原值。"""
    parts = dotted_key.split(".")
    node = container
    for part in parts[:-1]:
        child = node.get(part)
        if not isinstance(child, dict):
            child = {}
            node[part] = child
        node = child
    previous = node.get(parts[-1])
    node[parts[-1]] = value
    return previous


def _pop_dotted(container: Dict[str, Any], dotted_key: str) -> None:
    parts = dotted_key.split(".")
    node = container
    for part in parts[:-1]:
        child = node.get(part)
        if not isinstance(child, dict):
            return
        node = child
    node.pop(parts[-1], None)


def apply_to_config(
    config: Dict[str, Any],
    project_root: Path | str | None,
    role_map: Dict[str, str],
    readonly_role_map: Optional[Dict[str, str]] = None,
) -> List[str]:
    """按画像重写 ``config['targets']``，返回给用户看的说明列表。

    - ``role_map``：可写目标。解析出的路径会追加进 ``guardrails.allowed_write_files``。
    - ``readonly_role_map``：只读引用（如术语一致性要对照的邻近章节）。
      **不会**进写入白名单——否则立项依据 writer 就能改研究内容文件了。

    两者的键都是 ``targets`` 下的字段名，支持 ``related_tex.research_content``
    这种点号嵌套；值是画像里的角色名。

    空列表表示没有画像、维持原有默认值。
    """
    notes: List[str] = []
    if not project_root:
        return notes

    profile = load_profile(project_root)
    if profile is None:
        return notes

    grant_name = ((profile.get("grant") or {}).get("name") or "").strip()
    targets = config.setdefault("targets", {})
    guard = config.setdefault("guardrails", {})
    allowed = guard.get("allowed_write_files")
    if not isinstance(allowed, list):
        allowed = []
        guard["allowed_write_files"] = allowed

    for writable, mapping in ((True, role_map), (False, readonly_role_map or {})):
        for target_key, role in mapping.items():
            rels, state, host = resolve_role_files(profile, role)
            rel = rels[0] if rels else None

            if state in ("macro", "macros") and writable:
                macros = resolve_role_macros(profile, role)
                notes.append(
                    f"角色 {role} 为宏级寻址：改写 {rel} 中的 "
                    f"{', '.join('\\\\' + m for m in macros)} 宏体，"
                    f"严禁整文件覆盖（该文件还承载其它角色的正文）"
                )

            if state == "files" and writable:
                # 角色跨多个文件：主目标取第一个，其余也放行写入，
                # 否则 writer 只能写一半内容却不报错
                notes.append(
                    f"角色 {role} 跨 {len(rels)} 个文件：{', '.join(rels)}；"
                    f"主写入目标为 {rel}，请按各文件的小节主题分配内容"
                )
                for extra in rels[1:]:
                    if extra not in allowed:
                        allowed.append(extra)

            if state in ("absent", "unknown"):
                # 本模板不要求该角色：清空目标，避免误写到不存在的默认路径。
                _pop_dotted(targets, target_key)
                if writable:
                    notes.append(f"角色 {role} 在本基金模板中不存在，已跳过")
                continue

            if state == "unresolved" or not rel:
                notes.append(
                    f"角色 {role} 在 {PROFILE_FILENAME} 中仍是 unresolved，"
                    f"请先补全画像（改成 merged_into: <角色> 或 absent: true）再运行"
                )
                continue

            previous = _set_dotted(targets, target_key, rel)
            if writable and rel not in allowed:
                allowed.append(rel)

            if host and writable:
                # 关键提示：该角色没有独立文件，内容要写进宿主文件的对应小节，
                # 不能整文件覆盖，否则会冲掉宿主角色已有的正文。
                notes.append(
                    f"角色 {role} 在本模板中并入 {host}，目标文件 {rel}；"
                    f"请只改写该角色对应的小节，不要整文件替换"
                )
            elif previous and previous != rel:
                notes.append(f"角色 {role} 按画像重定向：{previous} -> {rel}")

    if notes and grant_name:
        notes.insert(0, f"已加载基金画像：{grant_name}")
    return notes
