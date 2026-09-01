from __future__ import annotations

import json
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPO_ROOT / "skills" / "nsfc-full-pipeline"


class SkillConsistencyTests(unittest.TestCase):
    def test_full_pipeline_metadata_and_docs_use_draft_first(self) -> None:
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        catalog_text = (REPO_ROOT / "skills" / "README.md").read_text(encoding="utf-8")
        evals = json.loads((SKILL_ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        eval_text = "\n".join(item["expected_output"] for item in evals["evals"])

        stale_phrases = (
            "缺真实信息时生成问卷并阻塞",
            "缺真实情况时生成 docs/其他说明信息补充问卷.md 并标记 need_user_input",
            "把阶段 06 标记为 need_user_input 并停下等待用户补充事实",
        )
        for phrase in stale_phrases:
            self.assertNotIn(phrase, skill_text)
            self.assertNotIn(phrase, catalog_text)
            self.assertNotIn(phrase, eval_text)

    def test_full_pipeline_skill_is_compact_and_counts_all_stages(self) -> None:
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme_text = (SKILL_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertLessEqual(len(skill_text.splitlines()), 500)
        self.assertIn("15 个阶段", readme_text)
        self.assertNotIn("## 14 个阶段", readme_text)

    def test_versions_are_bumped_for_behavior_changes(self) -> None:
        expected = {
            "nsfc-full-pipeline": "0.4.0",
            "nsfc-qc": "1.2.2",
            "nsfc-length-aligner": "0.3.2",
            "nsfc-humanization": "1.2.1",
        }
        for skill_name, version in expected.items():
            config = yaml.safe_load(
                (REPO_ROOT / "skills" / skill_name / "config.yaml").read_text(encoding="utf-8")
            )
            self.assertEqual(str(config["skill_info"]["version"]), version)

    def test_full_pipeline_references_and_state_tool_are_documented(self) -> None:
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        config_text = (SKILL_ROOT / "config.yaml").read_text(encoding="utf-8")

        for filename in (
            "references/checkpoint-and-gap-policy.md",
            "references/stages-00-07.md",
            "references/stages-08-14.md",
        ):
            self.assertTrue((SKILL_ROOT / filename).is_file(), filename)
            self.assertIn(filename, skill_text)
        self.assertIn("pipeline_state.py", skill_text)
        self.assertIn("pipeline_state.py", config_text)


if __name__ == "__main__":
    unittest.main()
