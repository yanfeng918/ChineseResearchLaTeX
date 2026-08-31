#!/usr/bin/env python3
"""Lightweight, read-only checker for nsfc-research-content-writer outputs.

Write targets are resolved from the project's own ``main.tex`` by role, never by
chapter number: NSFC templates do not share one numbering scheme and the numbers
overlap (``2.1`` is 研究内容 in three-part layouts but 研究基础 in five-part ones),
so a numeric glob silently selects the wrong chapter.

Only deterministic properties are checked here. Whether the technical route
actually corresponds to the research contents is a semantic judgement and is
left to the host AI, per the skill's DoD checklist.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _yaml_utils import extract_yaml_list_under_block, extract_yaml_value_under_block

DEFAULT_RISK_PHRASES = ["首次", "领先", "填补空白", "突破性", "国际领先", "世界领先"]

# 角色关键词：与 SKILL.md「落点解析」和 config.yaml 的 layout_resolution 保持一致。
# 顺序敏感——先匹配更具体的角色，避免"年度研究计划"被"研究内容"之外的规则抢走。
ROLE_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("innovation", ("特色与创新",)),
    ("scheme", ("方案及可行性",)),
    ("yearly_plan", ("年度研究计划", "研究计划")),
    ("research_content", ("研究内容", "内容目标问题")),
]

INPUT_RE = re.compile(r"\\input\{(extraTex/[^}]+)\}")


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def _read_risk_phrases(config_yaml: Path) -> list[str]:
    lines = config_yaml.read_text(encoding="utf-8").splitlines()
    return extract_yaml_list_under_block(lines, "checks", "risk_phrases") or DEFAULT_RISK_PHRASES


def _read_known_layout(config_yaml: Path, block: str) -> dict[str, str]:
    """Read one of the ``targets_three_part`` / ``targets_five_part`` sanity tables."""
    lines = config_yaml.read_text(encoding="utf-8").splitlines()
    out: dict[str, str] = {}
    for role, key in (
        ("research_content", "research_content_tex"),
        ("innovation", "innovation_tex"),
        ("yearly_plan", "yearly_plan_tex"),
        ("scheme", "scheme_tex"),
    ):
        value = extract_yaml_value_under_block(lines, block, key)
        if value:
            out[role] = value
    return out


def parse_active_inputs(main_tex: Path) -> list[str]:
    """Collect active ``\\input{extraTex/...}`` targets in document order.

    Commented-out lines and ``@config.tex`` are ignored; duplicates are collapsed
    while preserving first-seen order (some templates ship a file both commented
    and active).
    """
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
    """Map writing roles to the single file that owns each role."""
    roles: dict[str, str] = {}
    for rel in files:
        for role, keywords in ROLE_KEYWORDS:
            if any(k in rel for k in keywords) and role not in roles:
                roles[role] = rel
                break
    return roles


def detect_layout(roles: dict[str, str]) -> str:
    if "scheme" in roles:
        return "five-part"
    return "three-part"


def _check_yearly_plan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []
    for label, patterns in {
        "第1年/第一年": (r"第\s*1\s*年", r"第一年"),
        "第2年/第二年": (r"第\s*2\s*年", r"第二年"),
        "第3年/第三年": (r"第\s*3\s*年", r"第三年"),
    }.items():
        if not any(re.search(p, text) for p in patterns):
            problems.append(f"{path}: missing yearly header ({label})")
    return problems


def _check_no_internal_markers(path: Path) -> list[str]:
    """Internal planning markers (S1/T2/V3) must never reach the submitted body."""
    text = path.read_text(encoding="utf-8", errors="replace")
    found = sorted({m.group(0) for m in re.finditer(r"\b[STV]\d+\b", text)})
    if found:
        return [f"{path}: internal planning markers leaked into body text: {', '.join(found)}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only checker for nsfc-research-content-writer outputs under a given project_root.",
    )
    parser.add_argument("--project-root", required=True, help="NSFC LaTeX project root (must contain main.tex and extraTex/).")
    parser.add_argument("--no-content-check", action="store_true", help="Only check that target files exist.")
    parser.add_argument("--no-risk-scan", action="store_true", help="Skip scanning for risk phrases like '首次/领先'.")
    parser.add_argument("--fail-on-risk-phrases", action="store_true", help="Treat risk phrases as errors (default: warnings).")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    config_yaml = skill_root / "config.yaml"
    if not config_yaml.exists():
        return _err(f"missing config.yaml: {config_yaml}")

    project_root = Path(args.project_root).expanduser().resolve()
    if not project_root.is_dir():
        return _err(f"project_root does not exist or is not a directory: {project_root}")
    if not (project_root / "extraTex").exists():
        return _err(f"project_root missing extraTex/: {project_root}")

    main_tex = project_root / "main.tex"
    if not main_tex.exists():
        return _err(f"project_root missing main.tex (write targets are resolved from it): {project_root}")

    active = parse_active_inputs(main_tex)
    if not active:
        return _err(f"no active \\input{{extraTex/...}} resolved from {main_tex}; refusing to guess chapter numbers")

    roles = classify_roles(active)
    missing_roles = [r for r in ("research_content", "innovation", "yearly_plan") if r not in roles]
    if missing_roles:
        return _err(
            f"could not resolve required role(s) {missing_roles} from {main_tex}; "
            f"active files were: {active}"
        )

    layout = detect_layout(roles)
    known = _read_known_layout(config_yaml, f"targets_{layout.replace('-', '_')}")

    errors: list[str] = []
    warnings: list[str] = []

    # 与 config.yaml 的已知布局表做合理性校验（不替代 main.tex 解析结果）
    for role, resolved in roles.items():
        expected = known.get(role)
        if expected and expected != resolved:
            warnings.append(
                f"resolved {role}={resolved} differs from known {layout} table ({expected}); "
                "custom template? verify before writing"
            )

    for role, rel in sorted(roles.items()):
        path = project_root / rel
        if not path.is_file():
            errors.append(f"missing file for role {role}: {path}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if not args.no_content_check:
        errors.extend(_check_yearly_plan(project_root / roles["yearly_plan"]))
        for rel in roles.values():
            errors.extend(_check_no_internal_markers(project_root / rel))

    if not args.no_risk_scan:
        risk_phrases = _read_risk_phrases(config_yaml)
        for rel in roles.values():
            text = (project_root / rel).read_text(encoding="utf-8", errors="replace")
            for phrase in risk_phrases:
                if phrase in text:
                    msg = f"{project_root / rel}: contains risk phrase '{phrase}'"
                    (errors if args.fail_on_risk_phrases else warnings).append(msg)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)

    print("OK: project outputs check passed")
    print(f"- project_root: {project_root}")
    print(f"- layout: {layout} (resolved from main.tex)")
    print("- resolved roles:")
    for role, rel in sorted(roles.items()):
        print(f"  - {role}: {rel}")
    if layout == "three-part":
        print("- note: no separate 方案及可行性 file; technical route belongs inside the 研究内容 file")
    else:
        print("- note: technical route belongs in the 方案及可行性 file, not the 研究内容 file")
    print("- not checked here (semantic, see references/dod_checklist.md):")
    print("  技术路线是否为总分两层、分路线条数/序号是否与研究内容逐项对应")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
