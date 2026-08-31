#!/usr/bin/env python3
"""Read-only checker for nsfc-research-foundation-writer outputs.

Write targets are resolved from the project's own ``main.tex`` by role, never by
chapter number: NSFC templates do not share one numbering scheme and the numbers
overlap. ``3.1`` is 研究基础 in three-part layouts but 不同类型国基情况 (a
declaration section) in five-part ones, so a numeric glob silently selects the
wrong chapter.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _yaml_utils import extract_yaml_value_under_block

RISK_PHRASES = [
    "首次",
    "领先",
    "国际领先",
    "国内领先",
    "唯一",
    "填补空白",
    "世界领先",
    "国内首创",
]

# 角色关键词：与 SKILL.md「落点解析」和 config.yaml 的 layout_resolution 保持一致
ROLE_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("work_conditions", ("工作条件",)),
    ("foundation", ("研究基础",)),
]

# 同属"研究基础"大节但不由本技能撰写，必须排除，避免误判为落点
EXCLUDE_KEYWORDS = ("承担项目", "完成国基项目", "项目完成情况")

INPUT_RE = re.compile(r"\\input\{(extraTex/[^}]+)\}")


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def _warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def parse_active_inputs(main_tex: Path) -> list[str]:
    """Collect active ``\\input{extraTex/...}`` targets in document order."""
    files: list[str] = []
    seen: set[str] = set()
    for raw in main_tex.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("%"):
            continue
        match = INPUT_RE.search(line)
        if not match:
            continue
        rel = match.group(1)
        if rel == "extraTex/@config.tex" or rel in seen:
            continue
        seen.add(rel)
        files.append(rel)
    return files


def classify_roles(files: list[str]) -> dict[str, str]:
    roles: dict[str, str] = {}
    for rel in files:
        if any(k in rel for k in EXCLUDE_KEYWORDS):
            continue
        for role, keywords in ROLE_KEYWORDS:
            if any(k in rel for k in keywords) and role not in roles:
                roles[role] = rel
                break
    return roles


def detect_layout(roles: dict[str, str]) -> str:
    """Five-part templates put 研究基础 in chapter 2, three-part ones in chapter 3."""
    foundation = roles.get("foundation", "")
    if foundation.startswith("extraTex/2."):
        return "five-part"
    if foundation.startswith("extraTex/3."):
        return "three-part"
    return "custom"


def _read_known_layout(config_yaml: Path, block: str) -> dict[str, str]:
    lines = config_yaml.read_text(encoding="utf-8").splitlines()
    out: dict[str, str] = {}
    for role, key in (("foundation", "foundation_tex"), ("work_conditions", "conditions_tex")):
        value = extract_yaml_value_under_block(lines, block, key)
        if value:
            out[role] = value
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check nsfc-research-foundation-writer outputs under a LaTeX project root (existence + light heuristics)."
    )
    parser.add_argument("--project-root", required=True, help="LaTeX project root (must contain main.tex and extraTex/).")
    parser.add_argument("--no-content-check", action="store_true", help="Only check that target files exist.")
    parser.add_argument("--no-risk-scan", action="store_true", help="Skip scanning for risk phrases like '首次/领先'.")
    parser.add_argument("--fail-on-risk-phrases", action="store_true", help="Treat risk phrases as errors (default: warnings).")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    config_yaml = skill_root / "config.yaml"
    if not config_yaml.exists():
        return _err(f"missing config.yaml: {config_yaml}")

    project_root = Path(args.project_root).expanduser().resolve()
    extra_tex = project_root / "extraTex"
    if not extra_tex.is_dir():
        return _err(f"missing extraTex/ under project root: {extra_tex}")

    main_tex = project_root / "main.tex"
    if not main_tex.exists():
        return _err(f"project_root missing main.tex (write targets are resolved from it): {project_root}")

    active = parse_active_inputs(main_tex)
    if not active:
        return _err(f"no active \\input{{extraTex/...}} resolved from {main_tex}; refusing to guess chapter numbers")

    roles = classify_roles(active)
    missing = [r for r in ("foundation", "work_conditions") if r not in roles]
    if missing:
        return _err(f"could not resolve required role(s) {missing} from {main_tex}; active files were: {active}")

    layout = detect_layout(roles)
    if layout == "custom":
        _warn(f"layout does not match either known NSFC layout; resolved roles: {roles}")
    else:
        known = _read_known_layout(config_yaml, f"targets_{layout.replace('-', '_')}")
        for role, resolved in roles.items():
            expected = known.get(role)
            if expected and expected != resolved:
                _warn(
                    f"resolved {role}={resolved} differs from known {layout} table ({expected}); "
                    "custom template? verify before writing"
                )

    foundation_path = project_root / roles["foundation"]
    conditions_path = project_root / roles["work_conditions"]
    for p in [foundation_path, conditions_path]:
        if not p.is_file():
            return _err(f"missing target file: {p}")

    print(f"- layout: {layout} (resolved from main.tex)")
    print(f"- foundation: {roles['foundation']}")
    print(f"- work_conditions: {roles['work_conditions']}")

    if args.no_content_check:
        print("OK: target files exist (content checks skipped)", flush=True)
        return 0

    foundation_text = foundation_path.read_text(encoding="utf-8", errors="replace")
    conditions_text = conditions_path.read_text(encoding="utf-8", errors="replace")

    # Foundation must include explicit risk responses; require >=3 risk items.
    if "风险" not in foundation_text:
        return _err(f"{foundation_path} does not contain '风险' (risk section missing?)")
    if not (("应对" in foundation_text) or ("预案" in foundation_text) or ("替代" in foundation_text)):
        _warn(f"{foundation_path} has '风险' but lacks common response keywords (应对/预案/替代); please confirm risk responses are explicit")

    risk_items: list[str] = []
    risk_items += re.findall(r"\\subsubsubsection\{[^}]*风险[^}]*\}", foundation_text)
    risk_items += re.findall(r"\\subsubsection\{[^}]*风险[^}]*\}", foundation_text)
    risk_items += re.findall(r"(?m)^\s*#+\s*.*风险.*$", foundation_text)
    risk_items += re.findall(r"风险\s*(?:\d+|[一二三四五六七八九十])", foundation_text)

    risk_items = list(dict.fromkeys(risk_items))
    if len(risk_items) < 3:
        return _err(f"{foundation_path} seems to contain < 3 risk items (found {len(risk_items)})")

    # Conditions should reflect "have" and "lack + plan" structure.
    if not (("已具备" in conditions_text) or ("具备" in conditions_text)):
        _warn(f"{conditions_path} does not mention '已具备/具备' explicitly; please confirm it lists existing conditions")
    if not (("尚缺" in conditions_text) or ("缺少" in conditions_text) or ("不足" in conditions_text)):
        _warn(f"{conditions_path} does not mention '尚缺/缺少/不足' explicitly; please confirm it covers missing conditions + plan")

    if any(m in foundation_text or m in conditions_text for m in ("[请补充：", "[需补充：")):
        _warn("found placeholder markers like '[请补充：...]' in outputs; confirm this is intentional and consistent with provided info")

    if not args.no_risk_scan:
        combined = f"{foundation_text}\n{conditions_text}"
        hits = [p for p in RISK_PHRASES if p in combined]
        if hits:
            msg = "risk phrases present: " + ", ".join(hits)
            if args.fail_on_risk_phrases:
                return _err(msg)
            _warn(msg)

    print("OK: output checks passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
