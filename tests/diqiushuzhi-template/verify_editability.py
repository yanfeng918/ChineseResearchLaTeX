"""用隔离项目验证数字、斜杠、长正文、预算换行与填写框溢出。

运行：在本测试目录执行 python3 verify_editability.py。
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys

import pymupdf

TEST_DIR = Path(__file__).resolve().parent
ROOT = TEST_DIR.parents[1]
SOURCE = ROOT / "projects/diQiuShuzhi"
TOOL = ROOT / "packages/bensz-thesis/scripts/thesis_project_tool.py"


def build(project, log_name):
    result = subprocess.run(
        [sys.executable, str(TOOL), "build", "--project-dir", str(project)],
        cwd=TEST_DIR, capture_output=True, text=True,
    )
    (TEST_DIR / log_name).write_text(result.stdout + result.stderr, encoding="utf-8")
    return result


def main():
    filled = TEST_DIR / "_artifacts/filled"
    if filled.exists():
        shutil.rmtree(filled)
    shutil.copytree(SOURCE, filled, ignore=shutil.ignore_patterns("*.pdf", ".latex-cache", "*.md", ".vscode"))
    meta = filled / "extraTex/metadata.tex"
    content = meta.read_text(encoding="utf-8")
    fields = {
        "special-name": "测试专项A01", "title": "地球系统模拟测试",
        "applicant": "测试申请人", "institution": "测试大学",
        "unit-count": "2", "sex": "女", "professional-title": "副教授",
        "degree": "博士", "total-budget": "10.50",
        "expected-results": "形成测试数据集V2及可复现实验报告。",
        "keywords": "模拟；测试；评估",
    }
    for key, value in fields.items():
        content = re.sub(r"(?<![\w-])" + re.escape(key) + r"=\{\}",
                         lambda match: f"{key}={{{value}}}", content)
    meta.write_text(content, encoding="utf-8")
    (filled / "extraTex/abstract.tex").write_text("摘要测试起点。" + "检验地球系统模拟结果的一致性。" * 22 + "摘要测试终点。", encoding="utf-8")
    body = filled / "extraTex/1.2.研究内容.tex"
    body.write_text("\n\n".join(
        f"续页测试段落{i}。" + "本段仅用于验证模板的连续排版和页码更新，检查每段文字可见且不超出版心。" * 5
        for i in range(1, 25)
    ) + "\n\n续页测试终点。", encoding="utf-8")
    budget = filled / "extraTex/budget.tex"
    budget.write_text(budget.read_text(encoding="utf-8").replace(
        r"\CiesmBudgetRow{1}{设备费}{}{}",
        r"\CiesmBudgetRow{1}{设备费}{10.50}{用于测试设备配置、计算资源接入与实验环境验证。}"
    ), encoding="utf-8")
    result = build(filled, "filled-build.log")
    assert result.returncode == 0, result.stdout + result.stderr
    pdf = pymupdf.open(filled / "main.pdf")
    texts = [re.sub(r"\s+", "", page.get_text()) for page in pdf]
    assert len(pdf) > 4
    assert "测试专项A01" in texts[0]
    assert all("地球系统模拟测试" in t for t in texts[:2])
    assert "形成测试数据集V2" in texts[1]
    assert "副教授" in texts[1]
    assert "摘要测试终点" in texts[1]
    assert "续页测试终点" in "".join(texts[2:-1])
    for i in range(1, 25):
        assert f"续页测试段落{i}。" in "".join(texts[2:-1])
    assert "10.50" in texts[1] and texts[-1].count("10.50") == 2
    assert "出版/文献/信息传播/知识产权事务费" in texts[-1]
    for i, text in enumerate(texts, 1):
        assert f"第{i}页共{len(pdf)}页" in text
    log = (filled / ".latex-cache/main.log").read_text(encoding="utf-8")
    warnings = [line for line in log.splitlines() if any(s in line for s in ("Warning", "Overfull", "Underfull", "Missing character"))]
    assert not warnings, warnings
    for i in (0, 1, len(pdf)-1):
        pdf[i].get_pixmap().save(str(TEST_DIR / f"filled-page-{i+1}.png"))
    page_count = len(pdf)
    pdf.close()

    # 故意超出单行填写框，要求官方工具返回失败，不能静默裁掉。
    overflow = TEST_DIR / "_artifacts/overflow"
    if overflow.exists():
        shutil.rmtree(overflow)
    shutil.copytree(filled, overflow, ignore=shutil.ignore_patterns("*.pdf", ".latex-cache"))
    bad_meta = overflow / "extraTex/metadata.tex"
    bad_meta.write_text(content.replace("title={地球系统模拟测试}", "title={" + "超长测试" * 25 + "}"), encoding="utf-8")
    failure = build(overflow, "overflow-build.log")
    assert failure.returncode != 0
    assert "too long" in failure.stdout + failure.stderr
    assert not (overflow / "main.pdf").exists()
    report = {"filled_build": "passed", "filled_pages": page_count,
              "warnings": warnings, "metadata_and_numeric_text": "passed",
              "body_continuation_and_total_pages": "passed", "budget_wrapping": "passed",
              "overflow_rejected": True, "official_pdf_needed_for_build": False}
    (TEST_DIR / "editability-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
