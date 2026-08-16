#!/usr/bin/env python3
"""从现有申报书模板创建干净的项目副本。

支持 NSFC 与省级基金（GDNSF / GXNSF）三条产品线；项目族由目录名前缀决定，
识别逻辑复用 ``sync_vscode_configs.infer_project_profile``。
"""

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

# 目录名安全字符集：禁止路径分隔符、点号与空格，避免越界写入。
# 项目族的识别是另一件事，交给 sync_vscode_configs.infer_project_profile 判断，
# 以免这里的前缀清单与同步器再次漂移（此前写死 ^NSFC_，导致 GDNSF/GXNSF 建不出来）。
PROJECT_NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")

# 本脚本支持的项目族。thesis / paper / cv 虽然也被同步器识别，但另有
# template.json 等需要随目录名同步维护的元数据，直接复制会产出坏项目，
# 因此在这里显式拒绝并给出指引。
SUPPORTED_PROFILES = ("nsfc", "gdnsf", "gxnsf")
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


def validate_project_name(name: str, *, label: str) -> str:
    """校验目录名安全且属于本脚本支持的项目族，返回识别出的族名。

    前缀无法被 VS Code 同步器识别的项目会被同步流程跳过，最终缺少
    ``.vscode/settings.json`` 与 ``*.code-workspace``，因此这里直接拒绝。
    """
    if not PROJECT_NAME_PATTERN.fullmatch(name):
        raise ValueError(
            f"{label}只能包含英文字母、数字、下划线或连字符，且需以字母或数字开头：{name}"
        )

    profile = sync_vscode_configs.infer_project_profile(name)
    if profile is None:
        supported = "、".join(f"{p.upper()}_" for p in SUPPORTED_PROFILES)
        raise ValueError(
            f"{label}前缀无法被 VS Code 同步器识别，将导致项目缺少工作区配置："
            f"{name}（当前支持：{supported}）"
        )
    if profile not in SUPPORTED_PROFILES:
        raise ValueError(
            f"{label}属于 {profile} 产品线，本脚本不支持：{name}。"
            f"该产品线的项目还需同步维护 template.json 等元数据，"
            f"请改用对应产品线的新建流程"
        )
    return profile


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
    """复制申报书模板、过滤构建产物并生成与目标同名的 VS Code 配置。"""
    template_profile = validate_project_name(template_name, label="模板名")
    project_profile = validate_project_name(project_name, label="新项目名")

    # 跨产品线复制会让同步器按新名字的族写入 settings.json，
    # 而目录内是另一族的样式与构建 wrapper，产出的项目编译不了。
    if template_profile != project_profile:
        raise ValueError(
            f"模板与新项目不属于同一产品线（{template_profile} -> {project_profile}）："
            f"{template_name} -> {project_name}。请让新项目名沿用模板的前缀"
        )

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
        description="在 projects/ 下从现有申报书模板创建一个干净的新项目。"
    )
    parser.add_argument(
        "--template",
        default="NSFC_Local_Clean",
        help="projects/ 下的源模板目录名（默认：NSFC_Local_Clean）。",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="新项目目录名；前缀需与模板同族（NSFC_ / GDNSF_ / GXNSF_）。",
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
    # 各产品线的构建 wrapper 不同（nsfc_build.py / gdnsf_build.py / gxnsf_build.py），
    # 不能一律提示 NSFC 的命令。
    profile = sync_vscode_configs.infer_project_profile(created.name) or "nsfc"
    print(
        f"构建命令：python projects/{created.name}/scripts/{profile}_build.py "
        f"build --project-dir projects/{created.name}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
