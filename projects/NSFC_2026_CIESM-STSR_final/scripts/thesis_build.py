#!/usr/bin/env python3
"""定位仓库或已安装的 bensz-thesis，转调官方入口。"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys

PROJECT_DIR = Path(__file__).resolve().parents[1]


def find_tool() -> Path | None:
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
            candidate = Path(result.stdout.strip()).parent / "scripts/thesis_project_tool.py"
            if candidate.is_file():
                return candidate
    texmf_roots = [Path.home() / "texmf", Path.home() / "Library/texmf"]
    if os.environ.get("TEXMFHOME"):
        texmf_roots.insert(0, Path(os.environ["TEXMFHOME"]).expanduser())
    for root in texmf_roots:
        candidate = root / "tex/latex/bensz-thesis/scripts/thesis_project_tool.py"
        if candidate.is_file():
            return candidate
    return None


def main() -> int:
    tool = find_tool()
    if tool is None:
        print("未找到 bensz-thesis；请使用完整仓库，或先安装含 ciesm-open-fund 的 bensz-thesis 和 bensz-fonts。", file=sys.stderr)
        return 1
    args = sys.argv[1:] or ["build"]
    if "--project-dir" not in args and not any(arg.startswith("--project-dir=") for arg in args):
        args += ["--project-dir", str(PROJECT_DIR)]
    return subprocess.run([sys.executable, str(tool), *args]).returncode


if __name__ == "__main__":
    raise SystemExit(main())
