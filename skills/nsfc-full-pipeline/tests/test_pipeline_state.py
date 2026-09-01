from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pipeline_state.py"


def load_module():
    spec = importlib.util.spec_from_file_location("pipeline_state", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PipelineStateTests(unittest.TestCase):
    def make_project(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp_dir = tempfile.TemporaryDirectory()
        project = Path(temp_dir.name)
        (project / "extraTex").mkdir()
        (project / "docs").mkdir()
        (project / "review").mkdir()
        return temp_dir, project

    def test_migrates_legacy_checkpoint_to_schema_v2(self) -> None:
        pipeline_state = load_module()
        legacy = {
            "project": {"proposal_path": ".", "body_dir": "extraTex"},
            "run": {"current_mode": "resume"},
            "stages": {
                "06_research_foundation": {
                    "name": "Research Foundation",
                    "status": "need_user_input",
                    "inputs": ["docs/05_研究基础素材.md", "docs/研究基础信息补充问卷.md"],
                    "outputs": ["@foundation", "docs/05_研究基础素材.md"],
                }
            },
        }

        migrated, changed = pipeline_state.migrate_state(legacy)

        self.assertTrue(changed)
        self.assertEqual(migrated["schema_version"], 2)
        self.assertEqual(migrated["run"]["fill_policy"], "draft_first")
        self.assertEqual(migrated["project"]["project_fact_file"], "docs/00_项目事实库.md")
        self.assertIn("gaps", migrated["stages"]["06_research_foundation"])
        self.assertIn("@project_fact", migrated["stages"]["06_research_foundation"]["inputs"])
        self.assertEqual(migrated["stages"]["06_research_foundation"]["outputs"], ["@foundation"])
        self.assertEqual(migrated["submission"]["abstract"], "pending")
        self.assertEqual(len(migrated["stages"]), 15)

    def test_reconcile_recovers_interrupted_stage_from_changed_output(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        (project / "main.tex").write_text("\\input{extraTex/part-one}\n", encoding="utf-8")
        body = project / "extraTex" / "part-one.tex"
        body.write_text("\\NSFCBlankPara\n", encoding="utf-8")
        (project / "docs" / "00_项目事实库.md").write_text(
            "| F-GEN-03 | 待补 | 批准号 |\n",
            encoding="utf-8",
        )
        state, _ = pipeline_state.migrate_state(
            {
                "project": {
                    "proposal_path": ".",
                    "body_dir": "extraTex",
                    "project_fact_file": "docs/00_项目事实库.md",
                    "body_files": {
                        "part_one": ["extraTex/part-one.tex"],
                        "foundation": [],
                        "statements": [],
                    },
                }
            }
        )
        for stage_id in pipeline_state.STAGE_ORDER[:5]:
            state["stages"][stage_id]["status"] = "completed"
        state = pipeline_state.begin_stage(project, state, "05_part_one_writing", now="2026-09-01T10:00:00+08:00")
        self.assertTrue(state["stages"]["05_part_one_writing"]["input_sha256"])
        body.write_text(
            "申请人主持项目\\textbf{【待补 F-GEN-03：批准号】}，已有研究形成了可复核的方法基础。\n",
            encoding="utf-8",
        )

        reconciled, report = pipeline_state.reconcile_state(project, state)

        stage = reconciled["stages"]["05_part_one_writing"]
        self.assertEqual(stage["status"], "drafted_with_gaps")
        self.assertEqual(stage["gaps"], ["F-GEN-03"])
        self.assertIn("05_part_one_writing", report["recovered_stages"])
        self.assertEqual(reconciled["run"]["next_stage"], "06_research_foundation")

    def test_reconcile_converts_legacy_fact_block_to_drafted_gap(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        (project / "main.tex").write_text("\\input{extraTex/foundation}\n", encoding="utf-8")
        (project / "extraTex" / "foundation.tex").write_text(
            "申请人主持项目\\textbf{【待补 F-GEN-03：批准号】}，已有工作支撑本项目。\n",
            encoding="utf-8",
        )
        (project / "docs" / "00_项目事实库.md").write_text(
            "| F-GEN-03 | 待本人确认 | 批准号 |\n",
            encoding="utf-8",
        )
        state, _ = pipeline_state.migrate_state(
            {
                "project": {
                    "project_fact_file": "docs/00_项目事实库.md",
                    "body_files": {
                        "part_one": [],
                        "foundation": ["extraTex/foundation.tex"],
                        "statements": [],
                    },
                },
                "stages": {
                    "06_research_foundation": {
                        "status": "need_user_input",
                    }
                },
            }
        )

        reconciled, report = pipeline_state.reconcile_state(project, state)

        self.assertEqual(
            reconciled["stages"]["06_research_foundation"]["status"],
            "drafted_with_gaps",
        )
        self.assertEqual(
            reconciled["stages"]["06_research_foundation"]["gaps"],
            ["F-GEN-03"],
        )
        self.assertIn("06_research_foundation", report["recovered_stages"])

    def test_reconcile_invalidates_layout_when_main_tex_changes(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        main_tex = project / "main.tex"
        main_tex.write_text("\\input{extraTex/a}\n", encoding="utf-8")
        (project / "extraTex" / "a.tex").write_text("正文已经完成。\n", encoding="utf-8")
        state, _ = pipeline_state.migrate_state({})
        state["stages"]["00_layout_resolution"]["status"] = "completed"
        state["project"]["main_tex_sha256"] = pipeline_state.file_sha256(main_tex)
        main_tex.write_text("\\input{extraTex/a}\n% layout changed\n", encoding="utf-8")

        reconciled, report = pipeline_state.reconcile_state(project, state)

        self.assertTrue(report["layout_invalidated"])
        self.assertEqual(reconciled["stages"]["00_layout_resolution"]["status"], "pending")
        self.assertEqual(reconciled["run"]["next_stage"], "00_layout_resolution")

    def test_readiness_distinguishes_body_pipeline_from_submission(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        (project / "main.tex").write_text("\\input{extraTex/body}\n", encoding="utf-8")
        (project / "extraTex" / "body.tex").write_text("正文已经完成。\n", encoding="utf-8")
        (project / "docs" / "00_项目事实库.md").write_text("", encoding="utf-8")
        (project / "main.pdf").write_bytes(b"%PDF-1.4\n")
        state, _ = pipeline_state.migrate_state(
            {
                "project": {
                    "body_files": {
                        "part_one": ["extraTex/body.tex"],
                        "foundation": [],
                        "statements": [],
                    }
                }
            }
        )
        for stage in state["stages"].values():
            stage["status"] = "completed"
        state["stages"]["legacy_removed_stage"] = {"status": "failed"}

        readiness = pipeline_state.evaluate_readiness(project, state)

        self.assertTrue(readiness["body_pipeline_ready"])
        self.assertFalse(readiness["submission_ready"])
        self.assertIn("abstract", readiness["pending_submission_items"])

    def test_stage_input_fingerprint_tracks_external_applicant_profile(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        applicant = project.parent / f"{project.name}-applicant.md"
        self.addCleanup(lambda: applicant.unlink(missing_ok=True))
        applicant.write_text("| F-GEN-03 | 待本人确认 | 批准号 |\n", encoding="utf-8")
        (project / "docs" / "00_项目事实库.md").write_text("", encoding="utf-8")
        state, _ = pipeline_state.migrate_state(
            {
                "project": {
                    "applicant_profile_file": f"../{applicant.name}",
                    "project_fact_file": "docs/00_项目事实库.md",
                }
            }
        )

        first = pipeline_state.begin_stage(project, state, "06_research_foundation")
        first_hash = first["stages"]["06_research_foundation"]["input_sha256"]
        applicant.write_text("| F-GEN-03 | 已确认 | NSFC-123 |\n", encoding="utf-8")
        second = pipeline_state.begin_stage(project, first, "06_research_foundation")

        self.assertNotEqual(
            first_hash,
            second["stages"]["06_research_foundation"]["input_sha256"],
        )

    def test_reconcile_invalidates_completed_stage_when_fact_input_changes(self) -> None:
        pipeline_state = load_module()
        temp_dir, project = self.make_project()
        self.addCleanup(temp_dir.cleanup)
        (project / "main.tex").write_text("\\input{extraTex/foundation}\n", encoding="utf-8")
        body = project / "extraTex" / "foundation.tex"
        body.write_text("已有研究形成了可复核的方法基础。\n", encoding="utf-8")
        fact_file = project / "docs" / "00_项目事实库.md"
        fact_file.write_text("| F-PROJ-01 | 待本人确认 | 平台条件 |\n", encoding="utf-8")
        state, _ = pipeline_state.migrate_state(
            {
                "project": {
                    "project_fact_file": "docs/00_项目事实库.md",
                    "body_files": {
                        "part_one": [],
                        "foundation": ["extraTex/foundation.tex"],
                        "statements": [],
                    },
                }
            }
        )
        state = pipeline_state.begin_stage(project, state, "06_research_foundation")
        state = pipeline_state.finish_stage(project, state, "06_research_foundation")
        fact_file.write_text("| F-PROJ-01 | 已确认 | GPU 集群 |\n", encoding="utf-8")

        reconciled, report = pipeline_state.reconcile_state(project, state)

        self.assertEqual(reconciled["stages"]["06_research_foundation"]["status"], "pending")
        self.assertIn("06_research_foundation", report["invalidated_stages"])


if __name__ == "__main__":
    unittest.main()
