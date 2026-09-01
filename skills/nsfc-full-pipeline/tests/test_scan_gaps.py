from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_gaps.py"
SPEC = importlib.util.spec_from_file_location("scan_gaps", SCRIPT)
assert SPEC and SPEC.loader
scan_gaps = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scan_gaps)


class ScanGapsTests(unittest.TestCase):
    def make_project(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp_dir = tempfile.TemporaryDirectory()
        project = Path(temp_dir.name)
        (project / "extraTex").mkdir()
        (project / "docs").mkdir()
        return temp_dir, project

    def write_status(self, project: Path, fact_file: str = "docs/00_项目事实库.md") -> None:
        (project / "docs" / "workflow_status.yaml").write_text(
            "schema_version: 2\n"
            "project:\n"
            "  body_dir: extraTex\n"
            f"  project_fact_file: {fact_file}\n",
            encoding="utf-8",
        )

    def test_scans_only_active_main_tex_inputs(self) -> None:
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        self.write_status(project)
        (project / "docs" / "00_项目事实库.md").write_text(
            "| F-ACT-01 | 已确认 |\n| F-ORPHAN-01 | 已确认 |\n",
            encoding="utf-8",
        )
        (project / "main.tex").write_text(
            "\\input{extraTex/active}\n% \\input{extraTex/orphan}\n",
            encoding="utf-8",
        )
        (project / "extraTex" / "active.tex").write_text(
            "申请信息为\\textbf{【待补 F-ACT-01：批准号】}，用于说明基础。\n",
            encoding="utf-8",
        )
        (project / "extraTex" / "orphan.tex").write_text(
            "孤儿文件包含\\textbf{【待补 F-ORPHAN-01：批准号】}。\n",
            encoding="utf-8",
        )

        result = scan_gaps.scan(project)

        self.assertEqual([item["id"] for item in result["findings"]], ["F-ACT-01"])
        self.assertEqual(result["scanned_files"], ["extraTex/active.tex"])

    def test_hard_gap_fails_when_no_fact_source_can_be_loaded(self) -> None:
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        (project / "main.tex").write_text("\\input{extraTex/body}\n", encoding="utf-8")
        (project / "extraTex" / "body.tex").write_text(
            "项目号为\\textbf{【待补 F-MISSING-01：批准号】}，其余论证完整。\n",
            encoding="utf-8",
        )

        result = scan_gaps.scan(project)

        self.assertTrue(any("未加载到事实库" in problem for problem in result["problems"]))
        self.assertFalse(result["hard_gaps_clear"])

    def test_unregistered_id_is_reported(self) -> None:
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        self.write_status(project)
        (project / "docs" / "00_项目事实库.md").write_text(
            "| F-KNOWN-01 | 已确认 |\n",
            encoding="utf-8",
        )
        (project / "main.tex").write_text("\\input{extraTex/body}\n", encoding="utf-8")
        (project / "extraTex" / "body.tex").write_text(
            "项目号为\\textbf{【待补 F-UNKNOWN-01：批准号】}，其余论证完整。\n",
            encoding="utf-8",
        )

        result = scan_gaps.scan(project)

        self.assertTrue(any("F-UNKNOWN-01 未登记" in problem for problem in result["problems"]))

    def test_result_reports_gap_clearance_not_submission_readiness(self) -> None:
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        self.write_status(project)
        (project / "docs" / "00_项目事实库.md").write_text("", encoding="utf-8")
        (project / "main.tex").write_text("\\input{extraTex/body}\n", encoding="utf-8")
        (project / "extraTex" / "body.tex").write_text(
            "\\NSFCBlankPara\n",
            encoding="utf-8",
        )

        result = scan_gaps.scan(project)

        self.assertNotIn("submittable", result)
        self.assertTrue(result["hard_gaps_clear"])
        self.assertEqual(result["unfinished_placeholders"], ["extraTex/body.tex:1 \\NSFCBlankPara"])

    def test_latex_comments_do_not_create_findings(self) -> None:
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        self.write_status(project)
        (project / "docs" / "00_项目事实库.md").write_text(
            "| F-COMMENT-01 | 已确认 |\n",
            encoding="utf-8",
        )
        (project / "main.tex").write_text("\\input{extraTex/body}\n", encoding="utf-8")
        (project / "extraTex" / "body.tex").write_text(
            "% 【待补 F-COMMENT-01：注释中的旧标记】\n正文完整。\n",
            encoding="utf-8",
        )

        result = scan_gaps.scan(project)

        self.assertEqual(result["findings"], [])


if __name__ == "__main__":
    unittest.main()
