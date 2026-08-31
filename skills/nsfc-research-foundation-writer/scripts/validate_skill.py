#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

from _yaml_utils import extract_yaml_list_under_block, extract_yaml_value_under_block


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def _warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def _extract_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return ""
    return parts[0]


def _parse_frontmatter_yaml(frontmatter: str) -> dict[str, Any] | None:
    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        _warn("PyYAML is not installed; skipping strict frontmatter YAML parsing")
        return None

    try:
        parsed = yaml.safe_load(frontmatter) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"SKILL.md frontmatter is invalid YAML: {exc}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("SKILL.md frontmatter must parse to a YAML mapping")
    return parsed


def _extract_frontmatter_field(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    repo_root = skill_root.parents[1]
    skill_md = skill_root / "SKILL.md"
    config_yaml = skill_root / "config.yaml"

    required_files = [
        skill_md,
        config_yaml,
        skill_root / "README.md",
        skill_root / "CHANGELOG.md",
        skill_root / "references" / "info_form.md",
        skill_root / "references" / "dod_checklist.md",
        skill_root / "references" / "example_output.md",
        skill_root / "scripts" / "_yaml_utils.py",
    ]
    for path in required_files:
        if not path.exists():
            return _err(f"missing required file: {path}")

    skill_text = skill_md.read_text(encoding="utf-8")
    frontmatter = _extract_frontmatter(skill_text)
    if not frontmatter:
        return _err("SKILL.md missing YAML frontmatter block")
    try:
        _parse_frontmatter_yaml(frontmatter)
    except ValueError as exc:
        return _err(str(exc))

    fm_name = _extract_frontmatter_field(frontmatter, "name")
    fm_config = _extract_frontmatter_field(frontmatter, "config")
    fm_references = _extract_frontmatter_field(frontmatter, "references")
    if not fm_name or not fm_config or not fm_references:
        return _err("SKILL.md frontmatter missing required fields: name/config/references")

    # 版本号只认 config.yaml（单一真相来源），且 `version` 不是宿主支持的 frontmatter 字段；
    # 若 SKILL.md 里仍残留 version，必须与 config.yaml 一致，否则就是漂移。
    fm_version = _extract_frontmatter_field(frontmatter, "version")

    fm_config_path = Path(fm_config)
    resolved_config_path = (
        (repo_root / fm_config_path) if str(fm_config_path).startswith("skills/") else (skill_root / fm_config_path)
    ).resolve()
    if resolved_config_path != config_yaml.resolve():
        return _err(f"config path mismatch: SKILL.md={resolved_config_path} expected={config_yaml.resolve()}")

    fm_refs_path = Path(fm_references)
    resolved_refs_path = (
        (repo_root / fm_refs_path) if str(fm_refs_path).startswith("skills/") else (skill_root / fm_refs_path)
    ).resolve()
    if not resolved_refs_path.exists() or not resolved_refs_path.is_dir():
        return _err(f"references path invalid: {resolved_refs_path}")

    config_lines = config_yaml.read_text(encoding="utf-8").splitlines()
    cfg_name = extract_yaml_value_under_block(config_lines, "skill_info", "name")
    cfg_version = extract_yaml_value_under_block(config_lines, "skill_info", "version")
    if not cfg_name or not cfg_version:
        return _err("config.yaml missing skill_info.name or skill_info.version")
    if cfg_name != fm_name:
        return _err(f"skill name mismatch: SKILL.md={fm_name} config.yaml={cfg_name}")
    if fm_version is not None and cfg_version != fm_version:
        return _err(f"skill version mismatch: SKILL.md={fm_version} config.yaml={cfg_version}")

    # 两张已知布局表都必须完整；它们只用于对 main.tex 解析结果做合理性校验。
    layout_tables = {}
    for block in ("targets_three_part", "targets_five_part"):
        table = {
            key: extract_yaml_value_under_block(config_lines, block, key)
            for key in ("foundation_tex", "conditions_tex")
        }
        missing = [k for k, v in table.items() if not v]
        if missing:
            return _err(f"config.yaml {block} missing: {missing}")
        layout_tables[block] = table

    # 两种布局必须给出不同的落点，否则说明编号硬编码问题没有真正修掉
    if layout_tables["targets_three_part"] == layout_tables["targets_five_part"]:
        return _err("config.yaml: targets_three_part and targets_five_part must differ")

    allowed_roles = extract_yaml_list_under_block(config_lines, "guardrails", "allowed_write_roles") or []
    for role in ("foundation", "work_conditions"):
        if role not in allowed_roles:
            return _err(f"config.yaml guardrails.allowed_write_roles missing role: {role}")

    if not extract_yaml_value_under_block(config_lines, "layout_resolution", "resolve_from"):
        return _err("config.yaml missing layout_resolution.resolve_from (write targets must be resolved from main.tex)")

    # 回归护栏：SKILL.md 不得再把编号 glob 当作写入目标的选择方式。
    # 允许在解释"为什么不能这么做"时出现该字符串，因此只在缺少禁令时报错。
    if "extraTex/3.*.tex" in skill_text and "严禁用 `extraTex/3.*.tex`" not in skill_text:
        return _err("SKILL.md mentions the numeric glob extraTex/3.*.tex without the accompanying prohibition")

    # Heuristic checks: keep them lightweight; warn rather than fail when ambiguous.
    for needle in ["落点解析", "main.tex", "extraTex/@config.tex"]:
        if needle not in skill_text:
            _warn(f"SKILL.md does not mention expected guardrail/target string: {needle}")

    info_form = (skill_root / "references" / "info_form.md").read_text(encoding="utf-8")
    if re.search(r"(?i)\bNSFC\s*20\d{2}\b", info_form):
        _warn("references/info_form.md contains a year-like token (e.g., 'NSFC 2026'); consider keeping it year-agnostic")

    print("OK: skill validation passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
