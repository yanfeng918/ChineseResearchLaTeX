#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _yaml_utils import extract_yaml_list_under_block, extract_yaml_value_under_block
from grant_profile_reader import load_profile, resolve_role_file

DEFAULT_RISK_PHRASES = ["首次", "领先", "填补空白", "突破性", "国际领先", "世界领先"]
DEFAULT_SUBGOAL_MARKERS_MIN = 3
DEFAULT_DURATION_YEARS = 3

# config.yaml 的 targets 字段 -> 画像角色 -> 内容检查类型
TARGET_ROLES: tuple[tuple[str, str, str], ...] = (
    ("research_content_tex", "research_content", "research"),
    ("innovation_tex", "innovation", "innovation"),
    ("yearly_plan_tex", "yearly_plan", "yearly"),
)


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def _read_targets_from_config(config_yaml: Path) -> dict[str, str]:
    lines = config_yaml.read_text(encoding="utf-8").splitlines()
    research = extract_yaml_value_under_block(lines, "targets", "research_content_tex")
    innovation = extract_yaml_value_under_block(lines, "targets", "innovation_tex")
    yearly = extract_yaml_value_under_block(lines, "targets", "yearly_plan_tex")
    if not research or not innovation or not yearly:
        raise ValueError("config.yaml missing targets.*_tex")
    return {
        "research_content_tex": research,
        "innovation_tex": innovation,
        "yearly_plan_tex": yearly,
    }


def _resolve_plan(project_root: Path, config_targets: dict[str, str]) -> tuple[list[tuple[str, str]], list[str], int]:
    """确定要检查哪些文件、每个文件按什么类型检查。

    有基金画像时按角色解析：``merged_into`` 的角色不会被跳过，而是把它的内容
    检查转到宿主文件上——广东省基金要求把"特色与创新""年度研究计划"写进
    "研究内容"，跳过就等于默许这两块内容缺失。

    没有画像时维持原有的三文件固定检查，既有 NSFC 项目行为不变。
    """
    profile = load_profile(project_root)
    if profile is None:
        plan = [(config_targets[key], kind) for key, _, kind in TARGET_ROLES]
        return plan, [], DEFAULT_DURATION_YEARS

    notes: list[str] = []
    plan: list[tuple[str, str]] = []
    for key, role, kind in TARGET_ROLES:
        rel, state, host = resolve_role_file(profile, role)
        if state in ("absent", "unknown"):
            notes.append(f"角色 {role} 在本基金模板中不存在，已跳过 {kind} 检查")
            continue
        if state == "unresolved" or not rel:
            notes.append(f"角色 {role} 画像未裁决（unresolved），请先补全 grant-profile.yaml")
            continue
        if host:
            notes.append(f"角色 {role} 并入 {host}，改为在 {rel} 内检查 {kind} 内容")
        plan.append((rel, kind))

    grant = profile.get("grant") or {}
    try:
        years = int(grant.get("duration_years") or DEFAULT_DURATION_YEARS)
    except (TypeError, ValueError):
        years = DEFAULT_DURATION_YEARS
    return plan, notes, max(1, years)


def _read_checks_from_config(config_yaml: Path) -> tuple[list[str], int]:
    lines = config_yaml.read_text(encoding="utf-8").splitlines()

    risk_phrases = extract_yaml_list_under_block(lines, "checks", "risk_phrases") or DEFAULT_RISK_PHRASES
    raw_min = extract_yaml_value_under_block(lines, "checks", "subgoal_markers_min")
    try:
        subgoal_markers_min = int(raw_min) if raw_min is not None else DEFAULT_SUBGOAL_MARKERS_MIN
    except ValueError:
        subgoal_markers_min = DEFAULT_SUBGOAL_MARKERS_MIN

    subgoal_markers_min = max(1, subgoal_markers_min)
    return risk_phrases, subgoal_markers_min


def _check_file_exists(project_root: Path, relpath: str) -> str | None:
    path = project_root / relpath
    if not path.exists():
        return f"missing file: {path}"
    if not path.is_file():
        return f"not a file: {path}"
    return None


_CN_DIGITS = "〇一二三四五六七八九十"


def _year_patterns(years: int) -> dict[str, list[str]]:
    """按资助年限生成年度小标题的匹配模式。

    年限不是常数：NSFC 面上 4 年、青年 3 年、省基金多为 3 年，
    写死"第1/2/3年"会让 4 年期项目误报缺失第 4 年、3 年期项目被要求写第 4 年。
    """
    patterns: dict[str, list[str]] = {}
    for n in range(1, years + 1):
        cn = _CN_DIGITS[n] if n < len(_CN_DIGITS) else str(n)
        patterns[f"第{n}年/第{cn}年"] = [rf"第\s*{n}\s*年", rf"第{cn}年"]
    return patterns


def _check_minimal_content(
    path: Path, *, kind: str, subgoal_markers_min: int, duration_years: int = DEFAULT_DURATION_YEARS
) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []

    if kind == "research":
        markers = {int(m.group(1)) for m in re.finditer(r"\bS(\d+)\b", text)}
        if len(markers) < subgoal_markers_min:
            problems.append(
                f"{path}: not enough subgoal markers like S1/S2/... (found={len(markers)} min={subgoal_markers_min})"
            )
    elif kind == "innovation":
        if not re.search(r"对应\s*S\d+", text):
            problems.append(f"{path}: missing backreference marker like '对应 S1'")
    elif kind == "yearly":
        for label, patterns in _year_patterns(duration_years).items():
            if not any(re.search(p, text) for p in patterns):
                problems.append(f"{path}: missing yearly header ({label})")
        if not re.search(r"对应\s*S\d+", text) and not re.search(r"\bS\d+\b", text):
            problems.append(f"{path}: missing subgoal backreference like '对应 S1'")
    else:
        problems.append(f"{path}: unknown kind {kind}")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lightweight checker for nsfc-research-content-writer outputs under a given project_root.",
    )
    parser.add_argument(
        "--project-root",
        required=True,
        help="NSFC LaTeX project root (must contain extraTex/).",
    )
    parser.add_argument(
        "--no-content-check",
        action="store_true",
        help="Only check that target files exist (skip content heuristics).",
    )
    parser.add_argument(
        "--no-risk-scan",
        action="store_true",
        help="Skip scanning for risk phrases like '首次/领先' (default: scan and warn).",
    )
    parser.add_argument(
        "--fail-on-risk-phrases",
        action="store_true",
        help="Treat risk phrases as errors (default: warnings).",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    config_yaml = skill_root / "config.yaml"
    if not config_yaml.exists():
        return _err(f"missing config.yaml: {config_yaml}")

    project_root = Path(args.project_root).expanduser().resolve()
    if not project_root.exists() or not project_root.is_dir():
        return _err(f"project_root does not exist or is not a directory: {project_root}")
    if not (project_root / "extraTex").exists():
        return _err(f"project_root missing extraTex/: {project_root}")

    try:
        targets = _read_targets_from_config(config_yaml)
    except ValueError as exc:
        return _err(str(exc))

    risk_phrases, subgoal_markers_min = _read_checks_from_config(config_yaml)

    plan, profile_notes, duration_years = _resolve_plan(project_root, targets)
    for note in profile_notes:
        print(f"INFO: {note}")
    if not plan:
        return _err("基金画像未解析出任何可检查的章节，请先补全 grant-profile.yaml")

    errors: list[str] = []
    errors.extend(e for e in (_check_file_exists(project_root, rel) for rel, _ in plan) if e)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if not args.no_content_check:
        for relpath, kind in plan:
            errors.extend(
                _check_minimal_content(
                    project_root / relpath,
                    kind=kind,
                    subgoal_markers_min=subgoal_markers_min,
                    duration_years=duration_years,
                )
            )

    warnings: list[str] = []
    if not args.no_risk_scan:
        # 角色合并后多个角色可能指向同一文件，去重避免重复告警
        for relpath in dict.fromkeys(rel for rel, _ in plan):
            path = project_root / relpath
            text = path.read_text(encoding="utf-8", errors="replace")
            for phrase in risk_phrases:
                if phrase in text:
                    msg = f"{path}: contains risk phrase '{phrase}'"
                    if args.fail_on_risk_phrases:
                        errors.append(msg)
                    else:
                        warnings.append(msg)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)

    print("OK: project outputs check passed")
    print(f"- project_root: {project_root}")
    print(f"- duration_years: {duration_years}")
    print("- targets:")
    for relpath, kind in plan:
        print(f"  - {relpath}  ({kind})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
