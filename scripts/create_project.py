#!/usr/bin/env python3
"""从现有 NSFC 模板创建干净的项目副本。"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import re
import shutil
import sys

if __package__:
    from . import sync_vscode_configs
else:
    import sync_vscode_configs


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = REPO_ROOT / "projects"

PROJECT_NAME_PATTERN = re.compile(r"^NSFC_[A-Za-z0-9][A-Za-z0-9_-]*$")
IGNORED_DIRECTORY_NAMES = {
    ".latex-cache",
    ".pytest_cache",
    "__pycache__",
}
IGNORED_FILE_ENDINGS = (
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".lof",
    ".log",
    ".lot",
    ".nav",
    ".out",
    ".pdf",
    ".run.xml",
    ".snm",
    ".synctex.gz",
    ".toc",
    ".vrb",
)

SyncProject = Callable[..., list[str]]


def validate_project_name(name: str, *, label: str) -> None:
    """校验名称为安全且能被现有 VS Code 同步器识别的 NSFC 目录名。"""
    if not PROJECT_NAME_PATTERN.fullmatch(name):
        raise ValueError(
            f"{label}必须以 NSFC_ 开头，且只能包含英文字母、数字、下划线或连字符：{name}"
        )


def ignore_generated_files(_directory: str, names: list[str]) -> set[str]:
    """返回复制模板时应忽略的缓存、构建产物和旧工作区文件。"""
    ignored: set[str] = set()
    for name in names:
        lowered = name.casefold()
        if name in IGNORED_DIRECTORY_NAMES:
            ignored.add(name)
            continue
        if lowered.endswith(".code-workspace"):
            ignored.add(name)
            continue
        if lowered.endswith(IGNORED_FILE_ENDINGS):
            ignored.add(name)
    return ignored


def create_project(
    *,
    template_name: str,
    project_name: str,
    projects_dir: Path | None = None,
    sync_project_func: SyncProject | None = None,
) -> Path:
    """复制 NSFC 模板、过滤构建产物并生成与目标同名的 VS Code 配置。"""
    validate_project_name(template_name, label="模板名")
    validate_project_name(project_name, label="新项目名")

    selected_projects_dir = (projects_dir or PROJECTS_DIR).resolve()
    template_dir = selected_projects_dir / template_name
    destination = selected_projects_dir / project_name

    if not template_dir.is_dir():
        raise FileNotFoundError(f"未找到模板目录：{template_dir}")
    if destination.exists():
        raise FileExistsError(f"目标项目已存在，不会覆盖：{destination}")

    selected_projects_dir.mkdir(parents=True, exist_ok=True)
    try:
        destination.mkdir()
    except FileExistsError as exc:
        raise FileExistsError(f"目标项目已存在，不会覆盖：{destination}") from exc

    sync = sync_project_func or sync_vscode_configs.sync_project
    try:
        shutil.copytree(
            template_dir,
            destination,
            dirs_exist_ok=True,
            ignore=ignore_generated_files,
        )
        sync(destination, check_only=False)
    except Exception:
        shutil.rmtree(destination)
        raise

    return destination


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="在 projects/ 下从现有 NSFC 模板创建一个干净的新项目。"
    )
    parser.add_argument(
        "--template",
        default="NSFC_Local_Clean",
        help="projects/ 下的源模板目录名（默认：NSFC_Local_Clean）。",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="新项目目录名；必须以 NSFC_ 开头。",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        created = create_project(
            template_name=args.template,
            project_name=args.name,
        )
    except (FileExistsError, FileNotFoundError, OSError, ValueError) as exc:
        print(f"创建失败：{exc}", file=sys.stderr)
        return 1

    print(f"已创建项目：projects/{created.name}")
    print(
        "构建命令：python packages/bensz-nsfc/scripts/nsfc_project_tool.py "
        f"build --project-dir projects/{created.name}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
