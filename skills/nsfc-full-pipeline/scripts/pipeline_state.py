#!/usr/bin/env python3
"""维护 nsfc-full-pipeline 的可迁移、可校准断点状态。

脚本把确定性状态操作从提示词中下沉：旧断点迁移、阶段开始/完成、
中断后按产物恢复、正文缺口与 YAML 对账、main.tex 变更失效，以及
“正文流程完成”与“整份申请书可提交”的分离判断。
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


SCHEMA_VERSION = 2
STAGE_NAMES = {
    "00_layout_resolution": "布局与项目类型解析",
    "01_topic_extraction": "选题与研究主题",
    "02_literature_review": "文献调研",
    "03_scientific_questions": "科学问题与创新点",
    "04_research_plan": "研究方案与技术路线",
    "05_part_one_writing": "第一部分正文",
    "06_research_foundation": "研究基础与工作条件",
    "07_other_statements": "其他说明",
    "08_reference_alignment": "引用一致性核查",
    "09_length_control": "篇幅对齐",
    "10_humanization": "去 AI 味润色",
    "11_qc": "质量控制",
    "12_simulated_review": "模拟专家评审",
    "13_targeted_repair": "P0/P1 定点修复",
    "14_compile": "编译",
}
STAGE_ORDER = list(STAGE_NAMES)
ROLE_STAGE = {
    "part_one": "05_part_one_writing",
    "foundation": "06_research_foundation",
    "statements": "07_other_statements",
}
STAGE_INPUTS = {
    "00_layout_resolution": ["main.tex", "AGENTS.md", "README.md"],
    "01_topic_extraction": ["AGENTS.md", "README.md", "main.tex", "docs/00_项目基本信息.md", "@applicant_profile", "@project_fact"],
    "02_literature_review": ["AGENTS.md", "docs/01_选题与研究主题.md"],
    "03_scientific_questions": ["AGENTS.md", "docs/01_选题与研究主题.md", "docs/02_文献调研"],
    "04_research_plan": ["AGENTS.md", "docs/03_科学问题与创新点.md"],
    "05_part_one_writing": ["AGENTS.md", "docs/03_科学问题与创新点.md", "docs/04_研究方案与技术路线.md", "references/myexample.bib", "@applicant_profile", "@project_fact"],
    "06_research_foundation": ["AGENTS.md", "docs/05_研究基础素材.md", "@applicant_profile", "@project_fact"],
    "07_other_statements": ["@applicant_profile", "@project_fact"],
    "08_reference_alignment": ["@part_one", "@foundation", "@statements", "references/myexample.bib"],
    "09_length_control": ["@part_one", "@foundation", "@statements", "AGENTS.md"],
    "10_humanization": ["@part_one", "@foundation", "@statements"],
    "11_qc": ["@part_one", "@foundation", "@statements", "references/myexample.bib", "AGENTS.md"],
    "12_simulated_review": ["@part_one", "@foundation", "@statements", "references/myexample.bib", "AGENTS.md"],
    "13_targeted_repair": ["review/质量控制报告.md", "review/模拟专家评审_全稿.md"],
    "14_compile": ["main.tex", "@part_one", "@foundation", "@statements", "references/myexample.bib"],
}
STAGE_OUTPUTS = {
    "01_topic_extraction": ["docs/01_选题与研究主题.md"],
    "02_literature_review": ["docs/02_文献调研", "references/myexample.bib"],
    "03_scientific_questions": ["docs/03_科学问题与创新点.md"],
    "04_research_plan": ["docs/04_研究方案与技术路线.md"],
    "05_part_one_writing": ["@part_one"],
    "06_research_foundation": ["@foundation"],
    "07_other_statements": ["@statements", "docs/其他说明检查报告.md"],
    "08_reference_alignment": ["review/引用一致性审核报告.md"],
    "09_length_control": ["review/篇幅控制报告.md"],
    "10_humanization": ["review/去AI味修改报告.md"],
    "11_qc": ["review/质量控制报告.md"],
    "12_simulated_review": ["review/模拟专家评审_全稿.md"],
    "13_targeted_repair": ["review/P0P1定点修复报告.md", "docs/评审意见修复清单.md"],
    "14_compile": ["main.pdf", "review/编译检查报告.md"],
}
PLACEHOLDERS = ("\\NSFCBlankPara", "待填写", "现有材料未列", "项目编号未知")
SUBMISSION_ITEMS = ("abstract", "application_code", "budget", "declarations", "attachments")


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _mapping(parent: dict[str, Any], key: str) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        value = {}
        parent[key] = value
    return value


def _list(parent: dict[str, Any], key: str) -> list[Any]:
    value = parent.get(key)
    if not isinstance(value, list):
        value = []
        parent[key] = value
    return value


def migrate_state(state: dict[str, Any] | None) -> tuple[dict[str, Any], bool]:
    """把 v0.1/v0.3 断点幂等升级到 schema v2。"""
    migrated = copy.deepcopy(state) if isinstance(state, dict) else {}
    before = copy.deepcopy(migrated)
    source_schema = migrated.get("schema_version")
    migrated["schema_version"] = SCHEMA_VERSION

    project = _mapping(migrated, "project")
    defaults = {
        "proposal_path": ".",
        "body_dir": "extraTex",
        "bib_file": "references/myexample.bib",
        "guide_file": "AGENTS.md",
        "project_fact_file": "docs/00_项目事实库.md",
        "stage_output_dir": "docs",
        "review_output_dir": "review",
        "main_tex_sha256": "",
    }
    for key, value in defaults.items():
        project.setdefault(key, value)
    body_files = _mapping(project, "body_files")
    for role in ROLE_STAGE:
        _list(body_files, role)

    run = _mapping(migrated, "run")
    run.setdefault("current_mode", "resume")
    run.setdefault("fill_policy", "draft_first")
    run.setdefault("last_started", None)
    run.setdefault("last_finished", None)
    run.setdefault("last_summary", None)
    run.setdefault("next_stage", "00_layout_resolution")

    stages = _mapping(migrated, "stages")
    for stage_id, name in STAGE_NAMES.items():
        stage = stages.get(stage_id)
        if not isinstance(stage, dict):
            stage = {}
            stages[stage_id] = stage
        stage.setdefault("name", name)
        stage.setdefault("status", "pending")
        if source_schema != SCHEMA_VERSION:
            stage["inputs"] = list(STAGE_INPUTS.get(stage_id, []))
            stage["outputs"] = list(STAGE_OUTPUTS.get(stage_id, []))
        else:
            stage.setdefault("inputs", list(STAGE_INPUTS.get(stage_id, [])))
            stage.setdefault("outputs", list(STAGE_OUTPUTS.get(stage_id, [])))
        stage.setdefault("last_updated", None)
        stage.setdefault("notes", None)
        _list(stage, "blockers")
        _list(stage, "gaps")
        stage.setdefault("input_sha256", "")
        stage.setdefault("output_sha256_before", "")
        stage.setdefault("output_sha256", "")
        if stage["status"] == "completed" and stage["gaps"]:
            stage["status"] = "drafted_with_gaps"

    submission = _mapping(migrated, "submission")
    for item in SUBMISSION_ITEMS:
        submission.setdefault(item, "pending")

    return migrated, migrated != before


def _normalize_rel(path: str) -> str:
    rel = Path(path if path.endswith(".tex") else f"{path}.tex")
    return rel.as_posix().lstrip("./")


def _expand_declared_paths(
    project_dir: Path,
    state: dict[str, Any],
    declared: list[Any],
) -> list[Path]:
    project = state["project"]
    expanded: list[str] = []
    for item in declared:
        if item == "@part_one":
            expanded.extend(project["body_files"]["part_one"])
        elif item == "@foundation":
            expanded.extend(project["body_files"]["foundation"])
        elif item == "@statements":
            expanded.extend(project["body_files"]["statements"])
        elif item == "@applicant_profile":
            value = project.get("applicant_profile_file")
            if value:
                expanded.append(value)
        elif item == "@project_fact":
            value = project.get("project_fact_file")
            if value:
                expanded.append(value)
        elif isinstance(item, str) and not item.startswith("docs/workflow_status.yaml#"):
            expanded.append(item)
    return [(project_dir / item).resolve() for item in expanded]


def expand_stage_inputs(project_dir: Path, state: dict[str, Any], stage_id: str) -> list[Path]:
    declared = state["stages"][stage_id].get("inputs") or STAGE_INPUTS.get(stage_id, [])
    return _expand_declared_paths(project_dir, state, declared)


def expand_stage_outputs(project_dir: Path, state: dict[str, Any], stage_id: str) -> list[Path]:
    declared = state["stages"][stage_id].get("outputs") or STAGE_OUTPUTS.get(stage_id, [])
    return _expand_declared_paths(project_dir, state, declared)


def _fingerprint_paths(project_dir: Path, paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda item: str(item)):
        if path.is_dir():
            files = [item for item in sorted(path.rglob("*")) if item.is_file()]
        elif path.is_file():
            files = [path]
        else:
            files = []
        try:
            label = str(path.relative_to(project_dir))
        except ValueError:
            label = str(path)
        digest.update(label.encode("utf-8", errors="replace"))
        for file_path in files:
            try:
                file_label = str(file_path.relative_to(project_dir))
            except ValueError:
                file_label = str(file_path)
            digest.update(file_label.encode("utf-8", errors="replace"))
            digest.update(file_sha256(file_path).encode("ascii"))
    return digest.hexdigest()


def _text_output_ready(path: Path, body_output: bool) -> bool:
    if not path.is_file() or path.stat().st_size == 0:
        return False
    if path.suffix.lower() not in {".tex", ".md", ".yaml", ".yml"}:
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    if body_output and any(marker in text for marker in PLACEHOLDERS):
        return False
    return bool(text.strip())


def outputs_ready(project_dir: Path, state: dict[str, Any], stage_id: str) -> bool:
    if stage_id == "00_layout_resolution":
        project = state["project"]
        return bool(
            project.get("type")
            and project.get("grant_type")
            and project.get("layout")
            and project.get("length_budget")
            and any(project.get("body_files", {}).values())
        )
    paths = expand_stage_outputs(project_dir, state, stage_id)
    if not paths:
        return False
    body_output = stage_id in ROLE_STAGE.values()
    for path in paths:
        if path.is_dir():
            if not any(item.is_file() and item.stat().st_size for item in path.rglob("*")):
                return False
        elif not _text_output_ready(path, body_output):
            return False
    return True


def _load_scan_module():
    script = Path(__file__).with_name("scan_gaps.py")
    spec = importlib.util.spec_from_file_location("nsfc_full_pipeline_scan_gaps", script)
    if not spec or not spec.loader:
        raise RuntimeError(f"无法加载 {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def scan_project(project_dir: Path, state: dict[str, Any]) -> dict[str, Any]:
    module = _load_scan_module()
    body_dir = str(state.get("project", {}).get("body_dir") or "extraTex")
    return module.scan(project_dir, body_dir=body_dir)


def next_stage(state: dict[str, Any]) -> str | None:
    terminal = {"completed", "skipped", "drafted_with_gaps"}
    for stage_id in STAGE_ORDER:
        if state["stages"][stage_id].get("status") not in terminal:
            return stage_id
    return None


def begin_stage(
    project_dir: Path,
    state: dict[str, Any],
    stage_id: str,
    now: str | None = None,
) -> dict[str, Any]:
    state, _ = migrate_state(state)
    if stage_id not in STAGE_ORDER:
        raise ValueError(f"未知阶段：{stage_id}")
    stamp = now or now_iso()
    stage = state["stages"][stage_id]
    stage["input_sha256"] = _fingerprint_paths(
        project_dir, expand_stage_inputs(project_dir, state, stage_id)
    )
    paths = expand_stage_outputs(project_dir, state, stage_id)
    stage["output_sha256_before"] = _fingerprint_paths(project_dir, paths)
    stage["status"] = "in_progress"
    stage["last_updated"] = stamp
    state["run"]["last_started"] = stamp
    state["run"]["next_stage"] = stage_id
    return state


def _gaps_by_role(state: dict[str, Any], scan_result: dict[str, Any]) -> dict[str, list[str]]:
    file_roles: dict[str, str] = {}
    for role, files in state["project"]["body_files"].items():
        for path in files:
            file_roles[_normalize_rel(str(path))] = role
    result = {role: [] for role in ROLE_STAGE}
    for finding in scan_result["findings"]:
        if finding["kind"] != "待补" or not finding["id"]:
            continue
        role = file_roles.get(_normalize_rel(finding["file"]))
        if role and finding["id"] not in result[role]:
            result[role].append(finding["id"])
    for values in result.values():
        values.sort()
    return result


def reconcile_state(
    project_dir: Path,
    state: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    state, migrated = migrate_state(state)
    report: dict[str, Any] = {
        "migrated": migrated,
        "layout_invalidated": False,
        "invalidated_stages": [],
        "recovered_stages": [],
        "scan_problems": [],
    }

    main_tex = project_dir / "main.tex"
    stored_main_hash = state["project"].get("main_tex_sha256") or ""
    if main_tex.is_file() and stored_main_hash and file_sha256(main_tex) != stored_main_hash:
        stage00 = state["stages"]["00_layout_resolution"]
        stage00["status"] = "pending"
        stage00["notes"] = "main.tex 已变化，必须重新解析正文布局、项目类型和篇幅预算。"
        report["layout_invalidated"] = True

    scan_result = scan_project(project_dir, state)
    report["scan_problems"] = scan_result["problems"]

    for stage_id in STAGE_ORDER:
        stage = state["stages"][stage_id]
        stored_input = stage.get("input_sha256") or ""
        if stage.get("status") != "completed" or not stored_input:
            continue
        current_input = _fingerprint_paths(
            project_dir, expand_stage_inputs(project_dir, state, stage_id)
        )
        if current_input == stored_input:
            continue
        stage["status"] = "pending"
        stage["notes"] = "阶段输入已变化，需定点复核后重新完成；不得无关重写。"
        report["invalidated_stages"].append(stage_id)

    gaps_by_role = _gaps_by_role(state, scan_result)
    for role, stage_id in ROLE_STAGE.items():
        stage = state["stages"][stage_id]
        stage["gaps"] = gaps_by_role[role]
        if (
            stage["status"] == "need_user_input"
            and stage["gaps"]
            and not scan_result["problems"]
            and outputs_ready(project_dir, state, stage_id)
        ):
            stage["status"] = "drafted_with_gaps"
            stage["notes"] = "旧版事实阻塞已迁为 draft-first 缺口稿；按 ID 定点回填。"
            report["recovered_stages"].append(stage_id)
        if stage["status"] == "drafted_with_gaps" and not stage["gaps"] and outputs_ready(project_dir, state, stage_id):
            stage["status"] = "completed"
            report["recovered_stages"].append(stage_id)

    if not scan_result["problems"]:
        for stage_id in STAGE_ORDER:
            stage = state["stages"][stage_id]
            if stage["status"] != "in_progress" or not outputs_ready(project_dir, state, stage_id):
                continue
            paths = expand_stage_outputs(project_dir, state, stage_id)
            current = _fingerprint_paths(project_dir, paths)
            before = stage.get("output_sha256_before") or ""
            if not before or current == before:
                continue
            stage["output_sha256"] = current
            stage["input_sha256"] = _fingerprint_paths(
                project_dir, expand_stage_inputs(project_dir, state, stage_id)
            )
            stage["status"] = "drafted_with_gaps" if stage.get("gaps") else "completed"
            report["recovered_stages"].append(stage_id)

    state["run"]["next_stage"] = "00_layout_resolution" if report["layout_invalidated"] else next_stage(state)
    return state, report


def finish_stage(
    project_dir: Path,
    state: dict[str, Any],
    stage_id: str,
    now: str | None = None,
) -> dict[str, Any]:
    state, _ = migrate_state(state)
    if stage_id not in STAGE_ORDER:
        raise ValueError(f"未知阶段：{stage_id}")
    if not outputs_ready(project_dir, state, stage_id):
        raise ValueError(f"阶段产物尚未齐全或仍是未写作占位：{stage_id}")
    stamp = now or now_iso()
    if stage_id == "00_layout_resolution":
        main_tex = project_dir / "main.tex"
        state["project"]["main_tex_sha256"] = file_sha256(main_tex)
    reconciled, report = reconcile_state(project_dir, state)
    if report["scan_problems"] and stage_id in ROLE_STAGE.values():
        raise ValueError("正文缺口扫描存在结构问题，不能完成阶段：" + "; ".join(report["scan_problems"]))
    stage = reconciled["stages"][stage_id]
    stage["status"] = "drafted_with_gaps" if stage.get("gaps") else "completed"
    stage["last_updated"] = stamp
    stage["input_sha256"] = _fingerprint_paths(
        project_dir, expand_stage_inputs(project_dir, reconciled, stage_id)
    )
    stage["output_sha256"] = _fingerprint_paths(
        project_dir, expand_stage_outputs(project_dir, reconciled, stage_id)
    )
    reconciled["run"]["last_finished"] = stamp
    reconciled["run"]["next_stage"] = next_stage(reconciled)
    return reconciled


def evaluate_readiness(project_dir: Path, state: dict[str, Any]) -> dict[str, Any]:
    state, report = reconcile_state(project_dir, state)
    scan_result = scan_project(project_dir, state)
    stage_ready = all(
        state["stages"][stage_id].get("status") in {"completed", "skipped"}
        for stage_id in STAGE_ORDER
    )
    pdf_ready = (project_dir / "main.pdf").is_file() and (project_dir / "main.pdf").stat().st_size > 0
    body_pipeline_ready = bool(
        stage_ready
        and pdf_ready
        and scan_result["hard_gaps_clear"]
        and not scan_result["unfinished_placeholders"]
        and not scan_result["problems"]
    )
    pending_submission_items = [
        key
        for key in SUBMISSION_ITEMS
        if state["submission"].get(key) not in {"completed", "not_applicable"}
    ]
    return {
        "body_pipeline_ready": body_pipeline_ready,
        "submission_ready": body_pipeline_ready and not pending_submission_items,
        "pending_submission_items": pending_submission_items,
        "open_hard_gaps": scan_result["open_hard_gaps"],
        "tentative_count": scan_result["tentative_count"],
        "unfinished_placeholders": scan_result["unfinished_placeholders"],
        "scan_problems": scan_result["problems"],
        "layout_invalidated": report["layout_invalidated"],
    }


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError(f"断点文件根节点必须是 mapping：{path}")
    return value


def atomic_write_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            yaml.safe_dump(state, handle, allow_unicode=True, sort_keys=False)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def _print(value: Any, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(value, ensure_ascii=False, indent=2))
    else:
        print(yaml.safe_dump(value, allow_unicode=True, sort_keys=False).rstrip())


def main() -> int:
    parser = argparse.ArgumentParser(description="维护 nsfc-full-pipeline 断点状态")
    parser.add_argument("--project-dir", required=True, help="标书项目根目录")
    subparsers = parser.add_subparsers(dest="command", required=True)

    migrate_parser = subparsers.add_parser("migrate", help="把旧断点升级到当前 schema")
    migrate_parser.add_argument("--apply", action="store_true", help="写回；默认仅预览")

    begin_parser = subparsers.add_parser("begin", help="原子记录阶段开始")
    begin_parser.add_argument("--stage", required=True, choices=STAGE_ORDER)

    finish_parser = subparsers.add_parser("finish", help="核验产物并原子记录阶段完成")
    finish_parser.add_argument("--stage", required=True, choices=STAGE_ORDER)

    reconcile_parser = subparsers.add_parser("reconcile", help="对照实际产物、缺口与断点")
    reconcile_parser.add_argument("--apply", action="store_true", help="写回；默认仅预览")

    subparsers.add_parser("next", help="输出下一阶段")
    subparsers.add_parser("readiness", help="区分正文流程完成与整份申请书可提交")
    args = parser.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        parser.error(f"项目目录不存在：{project_dir}")
    status_path = project_dir / "docs" / "workflow_status.yaml"
    state = load_state(status_path)

    try:
        if args.command == "migrate":
            state, changed = migrate_state(state)
            if args.apply:
                atomic_write_state(status_path, state)
            _print({"changed": changed, "applied": bool(args.apply), "state": state}, as_json=True)
        elif args.command == "begin":
            state = begin_stage(project_dir, state, args.stage)
            atomic_write_state(status_path, state)
            _print({"stage": args.stage, "status": "in_progress"}, as_json=True)
        elif args.command == "finish":
            state = finish_stage(project_dir, state, args.stage)
            atomic_write_state(status_path, state)
            _print({"stage": args.stage, "status": state["stages"][args.stage]["status"]}, as_json=True)
        elif args.command == "reconcile":
            state, report = reconcile_state(project_dir, state)
            if args.apply:
                atomic_write_state(status_path, state)
            _print({"applied": bool(args.apply), "report": report, "state": state}, as_json=True)
        elif args.command == "next":
            state, _ = migrate_state(state)
            _print({"next_stage": next_stage(state)}, as_json=True)
        elif args.command == "readiness":
            _print(evaluate_readiness(project_dir, state), as_json=True)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"错误：{exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
