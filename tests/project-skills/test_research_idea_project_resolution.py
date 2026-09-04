from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_find_skill_prefers_repository_canonical_source_from_nested_project(tmp_path: Path):
    module = _load_module(
        "research_idea_init_workspace",
        REPO_ROOT / "skills" / "research-idea" / "scripts" / "init_workspace.py",
    )
    repo = tmp_path / "repo"
    canonical = repo / "skills" / "alpha" / "SKILL.md"
    canonical.parent.mkdir(parents=True)
    canonical.write_text("---\nname: alpha\ndescription: test\n---\n", encoding="utf-8")
    nested_project = repo / "projects" / "example"
    nested_project.mkdir(parents=True)

    found = module.find_skill("alpha", ["."], nested_project)

    assert found == canonical.resolve()


def test_project_search_does_not_escape_repository_root(tmp_path: Path):
    module = _load_module(
        "research_idea_init_workspace_no_escape",
        REPO_ROOT / "skills" / "research-idea" / "scripts" / "init_workspace.py",
    )
    home = tmp_path / "home"
    repo = home / "work" / "repo"
    (repo / "skills").mkdir(parents=True)
    nested_project = repo / "projects" / "example"
    nested_project.mkdir(parents=True)
    user_level = home / ".claude" / "skills" / "alpha" / "SKILL.md"
    user_level.parent.mkdir(parents=True)
    user_level.write_text("---\nname: alpha\ndescription: global\n---\n", encoding="utf-8")

    found = module.find_skill("alpha", ["."], nested_project)

    assert found is None


def test_dependency_check_warns_when_using_user_level_fallback(tmp_path: Path, capsys):
    module = _load_module(
        "research_idea_init_workspace_fallback_warning",
        REPO_ROOT / "skills" / "research-idea" / "scripts" / "init_workspace.py",
    )
    repo = tmp_path / "repo"
    (repo / "skills").mkdir(parents=True)
    global_root = tmp_path / "user-skills"
    fallback = global_root / "parallel-vibe" / "SKILL.md"
    fallback.parent.mkdir(parents=True)
    fallback.write_text(
        "---\nname: parallel-vibe\ndescription: external\n---\n",
        encoding="utf-8",
    )
    config = {
        "dependencies": {
            "required_skills": ["parallel-vibe"],
            "legacy_skill_aliases": {},
            "search_roots": [".", str(global_root)],
        }
    }

    found = module.check_dependencies(config, repo)

    captured = capsys.readouterr()
    assert found["parallel-vibe"] == str(fallback.parent)
    assert "用户级兼容回退" in captured.err
