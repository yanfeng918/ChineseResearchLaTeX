#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _yaml_utils import extract_yaml_value_under_block
from grant_profile_reader import load_profile, resolve_role_file

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


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def _warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def _resolve_targets(project_root: Path, fallback: tuple[str, str]) -> tuple[str, str | None, list[str]]:
    """按基金画像解析研究基础/工作条件的实际路径。

    没有画像时返回 config.yaml 的 NSFC 默认值，既有项目行为不变。
    工作条件在个别模板中可能并入研究基础或不存在，因此允许为 None。
    """
    profile = load_profile(project_root)
    if profile is None:
        return fallback[0], fallback[1], []

    notes: list[str] = []

    def _one(role: str, default: str) -> str | None:
        rel, state, host = resolve_role_file(profile, role)
        if state in ("absent", "unknown"):
            notes.append(f"角色 {role} 在本基金模板中不存在，已跳过相关检查")
            return None
        if state == "unresolved" or not rel:
            notes.append(f"角色 {role} 画像未裁决（unresolved），请先补全 grant-profile.yaml")
            return None
        if host:
            notes.append(f"角色 {role} 并入 {host}，改为在 {rel} 内检查")
        elif rel != default:
            notes.append(f"角色 {role} 按画像重定向：{default} -> {rel}")
        return rel

    foundation = _one("research_foundation", fallback[0])
    conditions = _one("work_conditions", fallback[1])
    if not foundation:
        # 研究基础是本 skill 的主目标，缺了没法工作，退回默认值让后续报错更直白
        foundation = fallback[0]
    return foundation, conditions, notes


def _load_targets(config_yaml: Path) -> tuple[str, str]:
    lines = config_yaml.read_text(encoding="utf-8").splitlines()
    foundation = extract_yaml_value_under_block(lines, "targets", "foundation_tex") or ""
    conditions = extract_yaml_value_under_block(lines, "targets", "conditions_tex") or ""
    if not foundation or not conditions:
        raise ValueError("missing targets.foundation_tex / targets.conditions_tex in config.yaml")
    return foundation, conditions


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check nsfc-research-foundation-writer outputs under a LaTeX project root (existence + light heuristics)."
    )
    parser.add_argument("--project-root", required=True, help="LaTeX project root (must contain extraTex/).")
    parser.add_argument(
        "--no-content-check",
        action="store_true",
        help="Only check that target files exist (skip content heuristics).",
    )
    parser.add_argument(
        "--no-risk-scan",
        action="store_true",
        help="Skip scanning for risk phrases like '首次/领先'.",
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

    try:
        target_foundation, target_conditions = _load_targets(config_yaml)
    except ValueError as exc:
        return _err(str(exc))

    project_root = Path(args.project_root).expanduser().resolve()
    extra_tex = project_root / "extraTex"
    if not extra_tex.exists() or not extra_tex.is_dir():
        return _err(f"missing extraTex/ under project root: {extra_tex}")

    target_foundation, target_conditions, profile_notes = _resolve_targets(
        project_root, (target_foundation, target_conditions)
    )
    for note in profile_notes:
        print(f"INFO: {note}", flush=True)

    foundation_path = project_root / target_foundation
    conditions_path = (project_root / target_conditions) if target_conditions else None
    for p in [foundation_path] + ([conditions_path] if conditions_path else []):
        if not p.exists() or not p.is_file():
            return _err(f"missing target file: {p}")

    if args.no_content_check:
        print("OK: target files exist (content checks skipped)", flush=True)
        return 0

    foundation_text = foundation_path.read_text(encoding="utf-8", errors="replace")
    # 工作条件若并入研究基础或本模板不要求，就在研究基础正文里查条件相关表述
    conditions_text = (
        conditions_path.read_text(encoding="utf-8", errors="replace")
        if conditions_path
        else foundation_text
    )

    # Foundation must include explicit risk responses; require >=3 risk items.
    if "风险" not in foundation_text:
        return _err(f"{foundation_path} does not contain '风险' (risk section missing?)")
    if not (("应对" in foundation_text) or ("预案" in foundation_text) or ("替代" in foundation_text)):
        _warn(f"{foundation_path} has '风险' but lacks common response keywords (应对/预案/替代); please confirm risk responses are explicit")

    # Try to count "risk items" from common LaTeX heading patterns.
    risk_items: list[str] = []
    risk_items += re.findall(r"\\subsubsubsection\{[^}]*风险[^}]*\}", foundation_text)
    risk_items += re.findall(r"\\subsubsection\{[^}]*风险[^}]*\}", foundation_text)
    risk_items += re.findall(r"(?m)^\\s*#+\\s*.*风险.*$", foundation_text)  # markdown-like headings (rare)
    risk_items += re.findall(r"风险\\s*(?:\\d+|[一二三四五六七八九十])", foundation_text)

    # Deduplicate near-identical hits.
    risk_items = list(dict.fromkeys(risk_items))
    if len(risk_items) < 3:
        return _err(f"{foundation_path} seems to contain < 3 risk items (found {len(risk_items)})")

    # Conditions should reflect "have" and "lack + plan" structure.
    conditions_label = conditions_path if conditions_path else f"{foundation_path} (工作条件并入研究基础)"
    if not (("已具备" in conditions_text) or ("具备" in conditions_text)):
        _warn(f"{conditions_label} does not mention '已具备/具备' explicitly; please confirm it lists existing conditions")
    if not (("尚缺" in conditions_text) or ("缺少" in conditions_text) or ("不足" in conditions_text)):
        _warn(f"{conditions_label} does not mention '尚缺/缺少/不足' explicitly; please confirm it covers missing conditions + plan")

    # Placeholders are allowed in preview / when info is missing; warn for apply-mode outputs.
    if "[请补充：" in foundation_text or "[需补充：" in foundation_text or "[请补充：" in conditions_text or "[需补充：" in conditions_text:
        _warn("found placeholder markers like '[请补充：...]' in outputs; confirm this is intentional and consistent with provided info")

    if not args.no_risk_scan:
        hits: list[tuple[str, str]] = []
        combined = f"{foundation_text}\n{conditions_text}"
        for phrase in RISK_PHRASES:
            if phrase in combined:
                hits.append((phrase, "found"))
        if hits:
            msg = "risk phrases present: " + ", ".join(p for p, _ in hits)
            if args.fail_on_risk_phrases:
                return _err(msg)
            _warn(msg)

    print("OK: output checks passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
