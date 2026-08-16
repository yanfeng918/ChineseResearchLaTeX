#!/usr/bin/env python3
"""定宽框溢出检查：核对宏体正文是否被静默截断。

表单式模板（``addressing: macro``）用 ``\\parbox[t][高度][t]{宽度}`` 把正文钉在
固定坐标框里。内容超过框高时，**LaTeX 不报错、不裁剪提示、页数也不变**，
超出部分直接从 PDF 里消失。

实测（projects/NSFC_2027_Silk_Road_Smart_Logistic_v2，把一节灌到 4 倍）：

- ``Overfull \\vbox`` 警告数：0
- 注入 28 个重复段落，PDF 中只剩 12 个
- 页数保持 14 页不变

所以基于编译日志或 bbox 的检查会漏报，唯一可靠的手段是**回读 PDF 文本、
核对每个宏的尾句是否还在**。字数预算只是代理指标：真实上限取"模板标注字数"
与"框高容量"的较小者，而框高容量只能这样实测。

用法::

    python check_box_overflow.py --project-dir <项目目录>
    python check_box_overflow.py --project-dir <项目目录> --build
    python check_box_overflow.py --project-dir <项目目录> --pdf <指定PDF>
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grant_profile_reader import (  # noqa: E402
    is_macro_addressing,
    load_profile,
    read_macro_body,
    resolve_role_macros,
)


DEFAULT_TAIL_CHARS = 12

_RE_MATH = re.compile(r"\$[^$]*\$")
_RE_COMMAND = re.compile(r"\\[A-Za-z@]+\*?")


def _err(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 2


def normalize(text: str) -> str:
    """两侧统一的归一化：只保留汉字与字母数字。

    标点、斜杠、空白必须一起去掉。PDF 抽取会重排换行、把 ``2G/3G`` 原样保留，
    而源文里的标点在版式中未必逐字对应；只对一侧做剥离会产生假截断
    （开发时就因此误判过一次）。
    """
    return re.sub(r"[^\u4e00-\u9fff0-9A-Za-z]", "", text)


def visible_text(body: str) -> str:
    """把宏体源码转成"渲染后大致可见"的文本。"""
    text = _RE_MATH.sub(" ", body)
    text = _RE_COMMAND.sub(" ", text)
    return re.sub(r"[{}\[\]]", " ", text)


def extract_pdf_text(pdf_path: Path) -> str:
    """抽取 PDF 全文；优先 pdftotext，回退 pypdf。"""
    if shutil.which("pdftotext"):
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            errors="replace",
        )
        if result.returncode == 0:
            return result.stdout

    try:
        import pypdf  # type: ignore

        reader = pypdf.PdfReader(str(pdf_path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except ImportError:
        pass

    raise RuntimeError("需要 pdftotext（poppler-utils）或 pypdf 才能读取 PDF 文本")


def matched_prefix_len(needle: str, haystack: str) -> int:
    """二分求 needle 在 haystack 中还能匹配上的最长前缀长度。

    用于定位截断点：整段找不到时，前缀长度即"实际渲染出来的字数"。
    """
    lo, hi = 0, len(needle)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if needle[:mid] in haystack:
            lo = mid
        else:
            hi = mid - 1
    return lo


def resolve_pdf(project_dir: Path, explicit: str | None, build: bool) -> Path | None:
    """定位待核对的 PDF。

    取最新的一份，而不是固定优先 ``.latex-cache/``：两处 PDF 常常不同步，
    对着过期 PDF 核对会两个方向都出错——旧内容长会虚报截断，旧内容短会漏报。
    """
    if explicit:
        path = Path(explicit).expanduser()
        return path if path.is_file() else None

    if build:
        (project_dir / ".latex-cache").mkdir(exist_ok=True)
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory=.latex-cache", "main.tex"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )

    candidates = [
        p
        for p in (project_dir / ".latex-cache" / "main.pdf", project_dir / "main.pdf")
        if p.is_file()
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="核对宏体正文是否因定宽框溢出而被静默截断"
    )
    parser.add_argument("--project-dir", required=True)
    parser.add_argument("--pdf", default="", help="指定 PDF；默认用 .latex-cache/main.pdf 或 main.pdf")
    parser.add_argument("--build", action="store_true", help="检查前先跑一次 xelatex")
    parser.add_argument(
        "--tail-chars",
        type=int,
        default=DEFAULT_TAIL_CHARS,
        help=f"用于判定的尾句长度（默认 {DEFAULT_TAIL_CHARS}）",
    )
    args = parser.parse_args(argv)

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        return _err(f"项目目录不存在：{project_dir}")

    profile = load_profile(project_dir)
    if profile is None:
        return _err(f"未找到 grant-profile.yaml：{project_dir}")
    if not is_macro_addressing(profile):
        print("SKIP: 该项目不是宏级寻址（addressing: macro），没有定宽框，无需本检查")
        return 0

    macro_rel = str(profile.get("macro_file") or "").strip()
    macro_path = project_dir / macro_rel
    if not macro_path.is_file():
        return _err(f"macro_file 不可读：{macro_rel}")

    pdf_path = resolve_pdf(project_dir, args.pdf or None, args.build)
    if pdf_path is None:
        return _err("未找到 PDF；请先编译，或加 --build，或用 --pdf 指定")

    try:
        pdf_text = normalize(extract_pdf_text(pdf_path))
    except RuntimeError as exc:
        return _err(str(exc))
    if not pdf_text:
        return _err(f"PDF 文本为空，无法核对：{pdf_path}")

    source = macro_path.read_text(encoding="utf-8", errors="replace")

    print(f"PDF：{pdf_path}")
    print(f"正文载体：{macro_rel}")

    # PDF 比正文旧 = 在核对一份不存在的稿子，结论无效。
    # 这比漏报更危险：用户会以为"没问题"而直接提交。
    stale = pdf_path.stat().st_mtime < macro_path.stat().st_mtime
    if stale:
        print()
        print(
            f"WARN: PDF 比 {macro_rel} 旧，本次结论反映的是编译时的旧正文。"
            f"请先重新编译，或加 --build 后重跑。",
            file=sys.stderr,
        )
    print()

    truncated: list[tuple[str, str, int, int]] = []
    missing: list[tuple[str, str]] = []
    checked = 0

    for role in (profile.get("roles") or {}):
        for name in resolve_role_macros(profile, role):
            body = read_macro_body(source, name)
            if body is None:
                missing.append((role, name))
                continue

            content = normalize(visible_text(body))
            if not content:
                continue
            checked += 1

            tail = content[-args.tail_chars :]
            if tail in pdf_text:
                continue

            rendered = matched_prefix_len(content, pdf_text)
            truncated.append((role, name, rendered, len(content)))

    for role, name in missing:
        print(f"WARN: 角色 {role} 的宏 \\{name} 未在 {macro_rel} 中定义，已跳过", file=sys.stderr)

    if not truncated:
        print(f"OK: {checked} 个宏的尾句均在 PDF 中，未发现定宽框截断")
        return 0

    print(f"发现 {len(truncated)} 处定宽框截断（内容已丢失且 LaTeX 不会报错）：")
    print()
    for role, name, rendered, total in truncated:
        lost = total - rendered
        pct = (rendered * 100 // total) if total else 0
        print(f"  角色 {role}  \\{name}")
        print(f"    可见字数 {total}，PDF 中只渲染出 {rendered}（{pct}%），丢失 {lost} 字")
    print()
    print("处理方式：压缩该角色正文，或在 sections/ 版式文件里加大对应框的高度。")
    print("不要只看字数预算——框高容量与模板标注字数取较小者才是真实上限。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
