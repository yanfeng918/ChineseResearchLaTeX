from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_syncer():
    script = REPO_ROOT / "scripts" / "sync_project_skills.py"
    spec = importlib.util.spec_from_file_location("sync_project_skills", script)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _write_skill(
    repo: Path,
    directory_name: str,
    *,
    frontmatter_name: str | None = None,
    config_name: str | None = None,
    description: str = "测试项目级 Skill。",
    extra_frontmatter: str = "",
) -> Path:
    skill_dir = repo / "skills" / directory_name
    skill_dir.mkdir(parents=True)
    name = frontmatter_name or directory_name
    configured_name = config_name or directory_name
    (skill_dir / "SKILL.md").write_text(
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "metadata:\n"
        "  author: Test\n"
        f"{extra_frontmatter}"
        "---\n\n"
        "# Canonical instructions\n\n"
        "Read references/example.md before acting.\n",
        encoding="utf-8",
    )
    (skill_dir / "config.yaml").write_text(
        "skill_info:\n"
        f"  name: {configured_name}\n"
        '  version: "1.2.3"\n'
        '  description: "测试项目级 Skill。"\n'
        '  category: "testing"\n',
        encoding="utf-8",
    )
    return skill_dir


@pytest.fixture
def syncer():
    return _load_syncer()


def test_build_entrypoint_preserves_frontmatter_and_references_canonical_skill(
    syncer, tmp_path: Path
):
    repo = tmp_path / "repo with spaces"
    _write_skill(repo, "alpha", extra_frontmatter="config:\n  source: config.yaml\n")
    skill = syncer.discover_source_skills(repo)["alpha"]
    target = repo / ".agents" / "skills" / "alpha" / "SKILL.md"

    content = syncer.build_entrypoint(skill, target)

    generated_frontmatter = content.split("\n\n", 1)[0]
    assert "metadata:\n  author: Test" in generated_frontmatter
    assert "config:" not in generated_frontmatter
    assert "name: alpha" in content
    assert "description: 测试项目级 Skill。" in content
    assert "../../../skills/alpha/SKILL.md" in content
    assert syncer.MANAGED_MARKER in content
    assert "# Canonical instructions" not in content


def test_sync_creates_both_host_entrypoints_and_check_reports_no_drift(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    _write_skill(repo, "beta")

    changed = syncer.sync_project_skills(repo, check_only=False)
    checked = syncer.sync_project_skills(repo, check_only=True)

    assert any(message.startswith("UPDATED ") for message in changed)
    assert not syncer.has_mismatch(checked)
    for host_root in (repo / ".agents" / "skills", repo / ".claude" / "skills"):
        assert (host_root / "alpha" / "SKILL.md").is_file()
        assert (host_root / "beta" / "SKILL.md").is_file()


def test_check_detects_missing_and_modified_entrypoints(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")

    missing = syncer.sync_project_skills(repo, check_only=True)
    syncer.sync_project_skills(repo, check_only=False)
    target = repo / ".agents" / "skills" / "alpha" / "SKILL.md"
    target.write_text(target.read_text(encoding="utf-8") + "manual drift\n", encoding="utf-8")
    modified = syncer.sync_project_skills(repo, check_only=True)

    assert syncer.has_mismatch(missing)
    assert any(message.startswith("MISMATCH ") for message in modified)


def test_sync_removes_only_stale_managed_entrypoints(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    syncer.sync_project_skills(repo, check_only=False)

    stale = repo / ".agents" / "skills" / "stale" / "SKILL.md"
    stale.parent.mkdir(parents=True)
    stale.write_text(syncer.MANAGED_MARKER + "\n", encoding="utf-8")
    unmanaged = repo / ".agents" / "skills" / "custom" / "SKILL.md"
    unmanaged.parent.mkdir(parents=True)
    unmanaged.write_text("---\nname: custom\ndescription: custom\n---\n", encoding="utf-8")

    syncer.sync_project_skills(repo, check_only=False)

    assert not stale.exists()
    assert unmanaged.exists()


def test_sync_refuses_host_directory_that_escapes_through_symlink(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    outside = tmp_path / "outside"
    outside.mkdir()
    (repo / ".agents").symlink_to(outside, target_is_directory=True)

    with pytest.raises(syncer.SkillConfigError, match="符号链接"):
        syncer.sync_project_skills(repo, check_only=False)

    assert not (outside / "skills" / "alpha" / "SKILL.md").exists()


@pytest.mark.parametrize(
    ("frontmatter_name", "config_name"),
    [("wrong", "alpha"), ("alpha", "wrong")],
)
def test_discovery_rejects_name_mismatches(
    syncer, tmp_path: Path, frontmatter_name: str, config_name: str
):
    repo = tmp_path / "repo"
    _write_skill(
        repo,
        "alpha",
        frontmatter_name=frontmatter_name,
        config_name=config_name,
    )

    with pytest.raises(syncer.SkillConfigError, match="alpha"):
        syncer.discover_source_skills(repo)


def test_discovery_rejects_invalid_skill_directory_name(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "Bad Name")

    with pytest.raises(syncer.SkillConfigError, match="lowercase"):
        syncer.discover_source_skills(repo)


def test_discovery_allows_skill_without_optional_config(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    skill_dir = _write_skill(repo, "alpha")
    (skill_dir / "config.yaml").unlink()

    skills = syncer.discover_source_skills(repo)

    assert skills["alpha"].version is None


def test_discovery_rejects_missing_frontmatter_description(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    skill_dir = _write_skill(repo, "alpha")
    source = skill_dir / "SKILL.md"
    source.write_text(
        source.read_text(encoding="utf-8").replace("description: 测试项目级 Skill。\n", ""),
        encoding="utf-8",
    )

    with pytest.raises(syncer.SkillConfigError, match="description"):
        syncer.discover_source_skills(repo)


def test_audit_global_reports_only_project_owned_names(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    roots = {
        "agents": tmp_path / "home" / ".agents" / "skills",
        "legacy-codex": tmp_path / "home" / ".codex" / "skills",
        "claude": tmp_path / "home" / ".claude" / "skills",
    }
    for root in roots.values():
        (root / "alpha").mkdir(parents=True, exist_ok=True)
        (root / "alpha" / "SKILL.md").write_text("---\nname: alpha\ndescription: old\n---\n", encoding="utf-8")
    unrelated = roots["agents"] / "third-party" / "SKILL.md"
    unrelated.parent.mkdir(parents=True)
    unrelated.write_text("---\nname: third-party\ndescription: keep\n---\n", encoding="utf-8")

    collisions = syncer.audit_global_skills(repo, roots)

    assert [(item.host, item.name) for item in collisions] == [
        ("agents", "alpha"),
        ("claude", "alpha"),
        ("legacy-codex", "alpha"),
    ]
    assert unrelated.exists()


def test_archive_and_restore_are_exact_and_recoverable(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    roots = {
        "agents": tmp_path / "home" / ".agents" / "skills",
        "legacy-codex": tmp_path / "home" / ".codex" / "skills",
        "claude": tmp_path / "home" / ".claude" / "skills",
    }
    owned = roots["agents"] / "alpha"
    owned.mkdir(parents=True)
    (owned / "SKILL.md").write_text("old global copy\n", encoding="utf-8")
    unrelated = roots["agents"] / "third-party"
    unrelated.mkdir()
    (unrelated / "SKILL.md").write_text("keep me\n", encoding="utf-8")

    manifest_path = syncer.archive_global_skills(
        repo,
        roots,
        backup_root=tmp_path / "backups",
        archive_id="20260904-120000",
    )

    assert manifest_path is not None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len(manifest["entries"]) == 1
    assert manifest["entries"][0]["name"] == "alpha"
    assert not owned.exists()
    assert unrelated.exists()

    restored = syncer.restore_global_skills(manifest_path, roots, owned_names={"alpha"})

    assert restored == [owned]
    assert owned.is_dir()
    assert (owned / "SKILL.md").read_text(encoding="utf-8") == "old global copy\n"
    assert unrelated.exists()


def test_restore_refuses_destination_outside_approved_roots(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    roots = {"agents": tmp_path / "home" / ".agents" / "skills"}
    archive = tmp_path / "backups" / "run" / "agents" / "alpha"
    archive.mkdir(parents=True)
    manifest = archive.parents[1] / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema": syncer.ARCHIVE_SCHEMA,
                "entries": [
                    {
                        "host": "agents",
                        "name": "alpha",
                        "original": str(tmp_path / "outside" / "alpha"),
                        "archived": str(archive),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(syncer.ArchiveSafetyError, match="approved global root"):
        syncer.restore_global_skills(manifest, roots, owned_names={"alpha"})


def test_archive_refuses_regular_files_at_skill_paths(syncer, tmp_path: Path):
    repo = tmp_path / "repo"
    _write_skill(repo, "alpha")
    roots = {"agents": tmp_path / "home" / ".agents" / "skills"}
    collision = roots["agents"] / "alpha"
    collision.parent.mkdir(parents=True)
    collision.write_text("not a skill directory\n", encoding="utf-8")

    with pytest.raises(syncer.ArchiveSafetyError, match="目录或符号链接"):
        syncer.archive_global_skills(
            repo,
            roots,
            backup_root=tmp_path / "backups",
            archive_id="20260904-130000",
        )

    assert collision.read_text(encoding="utf-8") == "not a skill directory\n"


def test_restore_refuses_skill_name_not_owned_by_project(syncer, tmp_path: Path):
    roots = {"agents": tmp_path / "home" / ".agents" / "skills"}
    archive = tmp_path / "backups" / "run" / "agents" / "third-party"
    archive.mkdir(parents=True)
    manifest = archive.parents[1] / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema": syncer.ARCHIVE_SCHEMA,
                "entries": [
                    {
                        "host": "agents",
                        "name": "third-party",
                        "original": str(roots["agents"] / "third-party"),
                        "archived": str(archive),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(syncer.ArchiveSafetyError, match="不属于当前项目"):
        syncer.restore_global_skills(manifest, roots, owned_names={"alpha"})


def test_restore_rejects_malformed_entries(syncer, tmp_path: Path):
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps({"schema": syncer.ARCHIVE_SCHEMA, "entries": {"alpha": "bad"}}),
        encoding="utf-8",
    )

    with pytest.raises(syncer.ArchiveSafetyError, match="entries"):
        syncer.restore_global_skills(manifest, {"agents": tmp_path}, owned_names={"alpha"})


def test_external_dependency_manifest_declares_parallel_vibe():
    manifest = REPO_ROOT / "skills" / "external-dependencies.yaml"

    content = manifest.read_text(encoding="utf-8")

    assert "name: parallel-vibe" in content
    assert "bundled: false" in content
    assert "research-idea" in content


def test_repository_contract_has_synced_entrypoint_for_every_skill(syncer):
    skills = syncer.discover_source_skills(REPO_ROOT)

    assert len(skills) == 25
    messages = syncer.sync_project_skills(REPO_ROOT, check_only=True)
    assert not syncer.has_mismatch(messages), "\n".join(messages)
