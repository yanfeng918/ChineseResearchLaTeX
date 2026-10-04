"""在本目录运行：核验空白模板、真实排版、长正文和固定表格溢出。"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

import pymupdf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PROJECT = REPO / "projects/NSFC_2026_CCNU-EduAgentTrust_final"
TOOL = REPO / "packages/bensz-thesis/scripts/thesis_project_tool.py"


def compact(text):
    return re.sub(r"\s+", "", text)


def build(project, label, *, expected=0):
    command = [sys.executable, str(TOOL), "build", "--project-dir", str(project)]
    process = subprocess.run(command, cwd=HERE, capture_output=True, text=True)
    (HERE / f"{label}.log").write_text(process.stdout + process.stderr, encoding="utf-8")
    log = (project / ".latex-cache/main.log").read_text(errors="replace")
    issues = [line for line in log.splitlines()
              if re.search(r"Warning|Error:|Overfull|Underfull|Missing character|^!", line)]
    assert (process.returncode == 0) == (expected == 0), (label, process.returncode, issues)
    if expected == 0:
        assert not issues, (label, issues)
        assert (project / ".latex-cache/main.fls").is_file()
    return {"label": label, "exit_code": process.returncode, "issues": issues}


def fixture(name):
    target = HERE / "fixtures" / name
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROJECT / "main.tex", target / "main.tex")
    shutil.copytree(PROJECT / "extraTex", target / "extraTex", dirs_exist_ok=True)
    return target


def lines(page):
    return [(drawing["width"], *[coordinate for point in item[1:] for coordinate in point])
            for drawing in page.get_drawings() for item in drawing["items"] if item[0] == "l"]


def label_origins(page):
    return [(character["c"], character["origin"]) for block in page.get_text("rawdict")["blocks"]
            for line in block.get("lines", []) for span in line["spans"]
            if 500 < span["origin"][1] < 520
            for character in span["chars"] if not character["c"].isspace()]


def main():
    result = {"builds": [build(PROJECT, "build-blank")], "pages": []}
    metadata = json.loads((PROJECT / "template.json").read_text())
    baseline = PROJECT / metadata["baseline_pdf"]
    result["baseline_sha256"] = hashlib.sha256(baseline.read_bytes()).hexdigest()
    with pymupdf.open(baseline) as reference, pymupdf.open(PROJECT / "main.pdf") as current:
        assert len(reference) == len(current) == 7
        for index, (a, b) in enumerate(zip(reference, current)):
            assert a.rect == b.rect, index + 1
            assert Counter(compact(a.get_text())) == Counter(compact(b.get_text())), index + 1
            assert not b.get_images(), index + 1
            page = {"page": index + 1, "size_bp": list(b.rect)[2:],
                    "visible_character_counts_match": True, "embedded_images": 0}
            if index in (0, 2, 3, 6):
                original, rendered = lines(a), lines(b)
                assert len(original) == len(rendered), index + 1
                error = max(min(max(abs(x-y) for x, y in zip(s, t)) for t in rendered)
                            for s in original)
                assert error < .01, (index + 1, error)
                page.update(line_count=len(original), max_line_error_bp=error)
            result["pages"].append(page)
        original, rendered = label_origins(reference[0]), label_origins(current[0])
        assert "".join(c for c, _ in original) == "".join(c for c, _ in rendered) == "课题负责人"
        error = max(abs(x-y) for (_, a), (_, b) in zip(original, rendered) for x, y in zip(a, b))
        assert error < .01, error
        result["cover_label_max_origin_error_bp"] = error

    filled = fixture("filled")
    (filled / "extraTex/metadata.tex").write_text(r"""\HuazhongSetup{
title={教育智能体可信协同与学习反馈机制研究},applicant={测试甲},organization={测试大学教育研究中心},
category={B},year={2026},month={9},day={15},edition={2026 年9 月},
sex={女},ethnicity={汉},birth={1990.01},major={教育学},degree={博士},position={教师},
professional-title={副教授},phone={027-00000000},keywords={教育智能体；可信协同},funding={5},period={2026.10--2027.09}}
""", encoding="utf-8")
    (filled / "extraTex/abstract.tex").write_text("本段仅用于模板填写验收。围绕教育智能体的可信协同与学习反馈，核验简介、申请字段及表格排版。", encoding="utf-8")
    (filled / "extraTex/members.tex").write_text(
        r"\HuazhongMember{1}{测试乙}{男}{1991.02}{博士}{讲师}{测试大学}{研究设计与分析}" + "\n" +
        r"\HuazhongMember{12}{测试丙}{女}{1992.03}{硕士}{助理}{测试大学}{资料整理}", encoding="utf-8")
    (filled / "extraTex/budget.tex").write_text("\n".join([
        r"\HuazhongBudgetRow{1}{5}{——}", r"\HuazhongBudgetRow{2}{3}{——}",
        r"\HuazhongBudgetRow{3}{2}{资料整理和测试费用}", r"\HuazhongBudgetRow{4}{1}{研究辅助人员劳务}",
        r"\HuazhongBudgetRow{5}{0}{无设备购置}", r"\HuazhongBudgetRow{6}{2}{间接费用}"]), encoding="utf-8")
    (filled / "extraTex/organization.tex").write_text("已审核申请材料。本段仅用于模板填写测试。", encoding="utf-8")
    result["builds"].append(build(filled, "build-filled"))
    with pymupdf.open(filled / "main.pdf") as document:
        assert len(document) == 7
        text = compact("".join(p.get_text() for p in document))
        for word in ("测试甲", "测试乙", "测试丙", "已审核申请材料", "无设备购置"):
            assert word in text, word
        assert text.count("教育智能体可信协同与学习反馈机制研究") == 2
        assert any(item[0] == "c" for d in document[2].get_drawings() for item in d["items"])
    result["filled"] = {"pages": 7, "baseline_present": False, "cover_and_information_title_match": True,
                        "first_and_last_member_present": True, "category_circle_present": True}

    long = fixture("long-content")
    text = "续页验收：围绕教育智能体的可信协同与学习反馈，分析研究问题、方法与适用范围，核对自动换页后的标题、版框和正文。"
    for section, count, marker in (("foundation", 24, "基础末尾标记"), ("proposal", 36, "申请内容末尾标记")):
        (long / f"extraTex/{section}.tex").write_text(
            "\n\n".join(f"{i+1}．{text * 3}" for i in range(count)) + f"\n\n{marker}。", encoding="utf-8")
    result["builds"].append(build(long, "build-long-content"))
    with pymupdf.open(long / "main.pdf") as document:
        assert len(document) > 7
        text = "".join(p.get_text() for p in document)
        assert "基础末尾标记" in text and "申请内容末尾标记" in text
        for index in range(4, len(document)-1):
            page = document[index]
            assert "二、研究基础" in page.get_text() or "三、项目申请内容" in page.get_text()
            assert page.get_drawings()
            assert page.get_text(clip=pymupdf.Rect(290, 776, 330, 800)).strip() == str(index)
            for word in page.get_text("words"):
                if word[1] > 100 and word[3] < 780:
                    assert 64 <= word[0] and word[2] <= 546 and word[3] <= 744.7, word
        assert "四、经费预算" in document[-1].get_text()
        result["pagination"] = {"pages": len(document), "both_end_markers_present": True,
                                "frames_headings_page_numbers_match": True, "body_inside_frames": True}

    overflow = fixture("overflow")
    (overflow / "extraTex/metadata.tex").write_text(r"\HuazhongSetup{title={" + "超长字段"*70 + "}}", encoding="utf-8")
    failure = build(overflow, "reject-overflow", expected=1)
    assert any("Fixed form cell overflow" in issue for issue in failure["issues"])
    result["builds"].append(failure)
    (HERE / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
