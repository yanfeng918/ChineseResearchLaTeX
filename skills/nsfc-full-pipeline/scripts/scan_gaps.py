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
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
UNFINISHED_MARKERS = ("\\NSFCBlankPara", "待填写", "现有材料未列", "项目编号未知")

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


def collect_known_ids(project_dir: Path) -> tuple[set[str], list[str], list[str]]:
    """从事实库收集已登记的事实 ID，并报告声明但无法读取的文件。"""
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
    missing: list[str] = []
    for path in candidates:
        if not path.is_file():
            missing.append(str(path))
            continue
        seen.append(str(path))
        for token in ID_RE.findall(read_text(path)):
            ids.add(token)
    return ids, seen, missing


def resolve_active_tex_files(
    project_dir: Path,
    body_dir: str,
    include_all: bool = False,
) -> tuple[list[Path], list[str]]:
    """解析真正参与编译的正文文件；默认不扫描孤儿或注释态文件。"""
    body_root = (project_dir / body_dir).resolve()
    if include_all:
        return (
            [path for path in sorted(body_root.rglob("*.tex")) if not path.name.startswith("@")],
            [],
        )

    main_tex = project_dir / "main.tex"
    if not main_tex.is_file():
        return [], [f"缺少主入口文件：{main_tex}"]

    active: list[Path] = []
    problems: list[str] = []
    seen: set[Path] = set()
    clean_main = "\n".join(strip_comments(line) for line in read_text(main_tex).splitlines())
    for match in INPUT_RE.finditer(clean_main):
        raw = match.group(1).strip()
        rel = Path(raw if raw.endswith(".tex") else f"{raw}.tex")
        path = (project_dir / rel).resolve()
        try:
            path.relative_to(body_root)
        except ValueError:
            continue
        if path.name.startswith("@"):
            continue
        if not path.is_file():
            problems.append(f"main.tex 引用的正文文件不存在：{rel.as_posix()}")
            continue
        if path not in seen:
            active.append(path)
            seen.add(path)

    if not active and not problems:
        problems.append(f"未从 main.tex 解析到 {body_dir}/ 下的活动正文文件")
    return active, problems


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


def scan(project_dir: Path, body_dir: str = "extraTex", include_all: bool = False) -> dict:
    known_ids, fact_files, missing_fact_files = collect_known_ids(project_dir)
    tex_files, scope_problems = resolve_active_tex_files(project_dir, body_dir, include_all)

    findings: list[dict] = []
    unfinished_placeholders: list[str] = []
    for tex in tex_files:
        lines = read_text(tex).splitlines()
        for lineno, raw in enumerate(lines):
            line = strip_comments(raw)
            for marker in UNFINISHED_MARKERS:
                if marker in line:
                    unfinished_placeholders.append(
                        f"{tex.relative_to(project_dir)}:{lineno + 1} {marker}"
                    )
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

    problems: list[str] = list(scope_problems)
    hard_findings = [finding for finding in findings if finding["kind"] == "待补"]
    if hard_findings and not fact_files:
        problems.append("发现硬事实缺口，但未加载到事实库；不得把这些 ID 视为已登记")
    for path in missing_fact_files:
        problems.append(f"断点声明的事实库文件不存在：{path}")
    for f in findings:
        if f["kind"] != "待补":
            continue
        if not f["id"]:
            problems.append(f"{f['file']}:{f['line']} 待补标记缺少事实 ID")
        elif not ID_RE.fullmatch(f["id"]):
            problems.append(f"{f['file']}:{f['line']} 事实 ID 格式无效：{f['id']}")
        elif f["id"] not in known_ids:
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
        "scan_scope": "all_body_files" if include_all else "active_main_inputs",
        "scanned_files": [str(path.relative_to(project_dir)) for path in tex_files],
        "fact_files": fact_files,
        "missing_fact_files": missing_fact_files,
        "known_id_count": len(known_ids),
        "findings": findings,
        "problems": problems,
        "open_hard_gaps": sorted({f["id"] for f in findings if f["kind"] == "待补" and f["id"]}),
        "tentative_count": sum(1 for f in findings if f["kind"] == "暂定"),
        "unfinished_placeholders": unfinished_placeholders,
        "hard_gaps_clear": not hard_findings,
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
        if result["hard_gaps_clear"]:
            print("未发现硬事实缺口；这只表示缺口已清空，不代表整份申请书可提交。")
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
    ap.add_argument(
        "--all-body-files",
        action="store_true",
        help="诊断模式：扫描正文目录全部 tex；默认只扫描 main.tex 的活动输入",
    )
    args = ap.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        print(f"错误：项目目录不存在：{project_dir}", file=sys.stderr)
        return 2
    if not (project_dir / args.body_dir).is_dir():
        print(f"错误：正文目录不存在：{project_dir / args.body_dir}", file=sys.stderr)
        return 2

    result = scan(project_dir, args.body_dir, include_all=args.all_body_files)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result["problems"] else 0
    return render(result, args.only_id)


if __name__ == "__main__":
    raise SystemExit(main())
