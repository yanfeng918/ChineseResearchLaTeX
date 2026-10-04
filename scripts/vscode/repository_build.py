#!/usr/bin/env python3
"""从仓库工作区将当前主文件交给所属项目的官方构建 wrapper。"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from sync_vscode_configs import PROJECTS_DIR, resolve_project_profile


def build_document(tex_file: Path) -> int:
    tex_file = tex_file.expanduser().resolve()
    project_dir = tex_file.parent
    if project_dir.parent != PROJECTS_DIR or not tex_file.is_file() or tex_file.suffix != ".tex":
        raise ValueError("请选择 projects/<项目>/ 下的主 TeX 文件，再执行构建。")
    profile = resolve_project_profile(project_dir)
    if profile is None:
        raise ValueError(f"无法识别 {project_dir.name} 的构建类型，请检查 template.json。")
    wrapper = project_dir / "scripts" / f"{profile}_build.py"
    if not wrapper.is_file():
        raise FileNotFoundError(f"缺少项目构建入口：{wrapper}")
    print(f"构建 {project_dir.name}/{tex_file.name}，使用 {profile} wrapper", flush=True)
    return subprocess.run(
        [sys.executable, str(wrapper), "build", "--project-dir", str(project_dir),
         "--tex-file", tex_file.name],
        cwd=project_dir,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex_file", type=Path, help="LaTeX Workshop 识别的主 TeX 文件路径")
    args = parser.parse_args()
    try:
        return build_document(args.tex_file)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
