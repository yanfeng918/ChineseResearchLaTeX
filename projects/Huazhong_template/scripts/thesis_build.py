#!/usr/bin/env python3
"""定位 bensz-thesis 官方构建入口；支持完整仓库和单项目目录。"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]


def find_build_tool() -> Path:
    for parent in PROJECT_DIR.parents:
        candidate = parent / "packages/bensz-thesis/scripts/thesis_project_tool.py"
        if candidate.is_file():
            return candidate
    kpsewhich = shutil.which("kpsewhich")
    if kpsewhich:
        result = subprocess.run(
            [kpsewhich, "bensz-thesis.sty"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0 and result.stdout.strip():
            candidate = Path(result.stdout.strip()).resolve().parent / "scripts/thesis_project_tool.py"
            if candidate.is_file():
                return candidate
    raise FileNotFoundError("未找到 bensz-thesis 构建入口。请使用完整仓库，或安装含 ccnu-open-fund-2026 profile 的 bensz-thesis 与 bensz-fonts。")


def main() -> int:
    try:
        tool = find_build_tool()
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    args = sys.argv[1:] or ["build"]
    if "--project-dir" not in args and not any(arg.startswith("--project-dir=") for arg in args):
        args += ["--project-dir", str(PROJECT_DIR)]
    return subprocess.run([sys.executable, str(tool), *args], cwd=PROJECT_DIR).returncode


if __name__ == "__main__":
    raise SystemExit(main())
