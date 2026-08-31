#!/usr/bin/env python3
"""扫描标书正文中的缺口标记，产出「事实 ID → 出现位置」反向索引。

用于 nsfc-full-pipeline 的 draft-first 缺口策略：
- `【待补 ID：说明】` 硬事实缺口，必须带事实库中已存在的 ID，未清空前不得声称定稿
- `【暂定 …】`        可推定草稿值，不阻塞提交，但需用户确认

除标准库外无依赖。

用法：
    python3 scan_gaps.py --project-dir projects/NSFC_General_Clean
    python3 scan_gaps.py --project-dir <dir> --id F-GEN-03    # 只看某个 ID
    python3 scan_gaps.py --project-dir <dir> --json           # 供上游程序消费
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TBD_RE = re.compile(r"【待补\s*([^：:】]*?)\s*[：:]\s*([^】]*)】")
TBD_NO_DESC_RE = re.compile(r"【待补\s*([^：:】]+?)\s*】")
TENTATIVE_RE = re.compile(r"【暂定\s*([^】]*)】")
ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b")

# 判断「整段只有占位」时先剥掉的 LaTeX 噪声
LATEX_CMD_RE = re.compile(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?")
LATEX_PUNCT_RE = re.compile(r"[{}$&#_^~\\%\s，。、；：？！（）()\[\]—－\-]+")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def strip_comments(line: str) -> str:
    """去掉 LaTeX 行注释，保留 \\% 转义。"""
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line):
            out.append(line[i : i + 2])
            i += 2
            continue
        if ch == "%":
            break
        out.append(ch)
        i += 1
    return "".join(out)


def yaml_scalar(text: str, key: str) -> str | None:
    """从 workflow_status.yaml 取一个标量值，顺带剥掉行内注释。

    仓库内的 YAML 解析器不剥行内注释，这里只取两个路径字段，自己处理更省事。
    """
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*(.*)$", text, re.MULTILINE)
    if not m:
        return None
    value = m.group(1)
    if not value.lstrip().startswith(("'", '"')):
        value = value.split("#", 1)[0]
    value = value.strip().strip("'\"")
    return value or None


def collect_known_ids(project_dir: Path) -> tuple[set[str], list[str]]:
    """从事实库收集已登记的事实 ID。返回 (ID 集合, 实际读到的文件列表)。"""
    status_file = project_dir / "docs" / "workflow_status.yaml"
    candidates: list[Path] = []
    if status_file.is_file():
        text = read_text(status_file)
        for key in ("applicant_profile_file", "project_fact_file"):
            rel = yaml_scalar(text, key)
            if rel:
                candidates.append((project_dir / rel).resolve())
    fallback = project_dir / "docs" / "00_项目事实库.md"
    if fallback.is_file() and fallback.resolve() not in candidates:
        candidates.append(fallback.resolve())

    ids: set[str] = set()
    seen: list[str] = []
    for path in candidates:
        if not path.is_file():
            continue
        seen.append(str(path))
        for token in ID_RE.findall(read_text(path)):
            ids.add(token)
    return ids, seen


def paragraph_is_placeholder_only(lines: list[str], index: int) -> bool:
    """判断该行所在段落是否只有占位——挖空写法禁止整段皆占位。"""
    start = index
    while start > 0 and strip_comments(lines[start - 1]).strip():
        start -= 1
    end = index
    while end + 1 < len(lines) and strip_comments(lines[end + 1]).strip():
        end += 1

    body = " ".join(strip_comments(l) for l in lines[start : end + 1])
    body = TBD_RE.sub("", body)
    body = TBD_NO_DESC_RE.sub("", body)
    body = TENTATIVE_RE.sub("", body)
    body = LATEX_CMD_RE.sub("", body)
    body = LATEX_PUNCT_RE.sub("", body)
    return len(body) < 15


def scan(project_dir: Path, body_dir: str = "extraTex") -> dict:
    known_ids, fact_files = collect_known_ids(project_dir)
    tex_root = project_dir / body_dir

    findings: list[dict] = []
    for tex in sorted(tex_root.glob("*.tex")):
        if tex.name.startswith("@"):
            continue
        lines = read_text(tex).splitlines()
        for lineno, raw in enumerate(lines):
            line = strip_comments(raw)
            if "【" not in line:
                continue
            for m in TBD_RE.finditer(line):
                findings.append(
                    {
                        "kind": "待补",
                        "id": m.group(1).strip(),
                        "desc": m.group(2).strip(),
                        "file": str(tex.relative_to(project_dir)),
                        "line": lineno + 1,
                        "paragraph_only": paragraph_is_placeholder_only(lines, lineno),
                    }
                )
            for m in TBD_NO_DESC_RE.finditer(line):
                if TBD_RE.search(m.group(0)):
                    continue
                findings.append(
                    {
                        "kind": "待补",
                        "id": m.group(1).strip(),
                        "desc": "",
                        "file": str(tex.relative_to(project_dir)),
                        "line": lineno + 1,
                        "paragraph_only": paragraph_is_placeholder_only(lines, lineno),
                    }
                )
            for m in TENTATIVE_RE.finditer(line):
                findings.append(
                    {
                        "kind": "暂定",
                        "id": "",
                        "desc": m.group(1).strip(),
                        "file": str(tex.relative_to(project_dir)),
                        "line": lineno + 1,
                        "paragraph_only": False,
                    }
                )

    problems: list[str] = []
    for f in findings:
        if f["kind"] != "待补":
            continue
        if not f["id"]:
            problems.append(f"{f['file']}:{f['line']} 待补标记缺少事实 ID")
        elif known_ids and f["id"] not in known_ids:
            problems.append(
                f"{f['file']}:{f['line']} 事实 ID {f['id']} 未登记在事实库，"
                f"应先在事实库建行再引用"
            )
        if f["paragraph_only"]:
            problems.append(
                f"{f['file']}:{f['line']} 整段只有占位——挖空的应是名词短语，不是整段"
            )

    return {
        "project_dir": str(project_dir),
        "fact_files": fact_files,
        "known_id_count": len(known_ids),
        "findings": findings,
        "problems": problems,
        "open_hard_gaps": sorted({f["id"] for f in findings if f["kind"] == "待补" and f["id"]}),
        "tentative_count": sum(1 for f in findings if f["kind"] == "暂定"),
        "submittable": not any(f["kind"] == "待补" for f in findings),
    }


def render(result: dict, only_id: str | None) -> int:
    findings = result["findings"]
    if only_id:
        findings = [f for f in findings if f["id"] == only_id]

    hard = [f for f in findings if f["kind"] == "待补"]
    soft = [f for f in findings if f["kind"] == "暂定"]

    if not findings:
        print("未发现缺口标记。" if not only_id else f"未发现 {only_id} 的缺口标记。")
    if hard:
        print(f"待补（硬事实，阻塞定稿）：{len(hard)} 处")
        by_id: dict[str, list[dict]] = {}
        for f in hard:
            by_id.setdefault(f["id"] or "<无ID>", []).append(f)
        for fid in sorted(by_id):
            print(f"  {fid}")
            for f in by_id[fid]:
                desc = f"  — {f['desc']}" if f["desc"] else ""
                print(f"      {f['file']}:{f['line']}{desc}")
    if soft:
        print(f"\n暂定（草稿值，需用户确认，不阻塞定稿）：{len(soft)} 处")
        for f in soft:
            print(f"      {f['file']}:{f['line']}  — {f['desc']}")

    if result["problems"]:
        print(f"\n结构问题：{len(result['problems'])} 项")
        for p in result["problems"]:
            print(f"      {p}")

    if not only_id:
        print()
        if result["submittable"]:
            print("无待补事实：正文缺口已清空。")
        else:
            print(
                f"仍有 {len(result['open_hard_gaps'])} 个待补事实 ID，"
                f"不得声称定稿或可提交。"
            )
    return 1 if result["problems"] else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="扫描 NSFC 标书正文的缺口标记")
    ap.add_argument("--project-dir", required=True, help="标书项目根目录")
    ap.add_argument("--body-dir", default="extraTex", help="正文目录，默认 extraTex")
    ap.add_argument("--id", dest="only_id", help="只列出指定事实 ID 的出现位置")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        print(f"错误：项目目录不存在：{project_dir}", file=sys.stderr)
        return 2
    if not (project_dir / args.body_dir).is_dir():
        print(f"错误：正文目录不存在：{project_dir / args.body_dir}", file=sys.stderr)
        return 2

    result = scan(project_dir, args.body_dir)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result["problems"] else 0
    return render(result, args.only_id)


if __name__ == "__main__":
    raise SystemExit(main())
