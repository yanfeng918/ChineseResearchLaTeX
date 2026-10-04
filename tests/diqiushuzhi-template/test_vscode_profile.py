"""非标准目录名的配置发现回归；所有临时写入限制在测试目录。"""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("syncer", ROOT / "scripts/sync_vscode_configs.py")
syncer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(syncer)


def test_custom_name_uses_metadata(tmp_path):
    (tmp_path / "template.json").write_text('{"build_profile":"thesis"}')
    assert syncer.resolve_project_profile(tmp_path) == "thesis"


@pytest.mark.parametrize("metadata", ['[]', '{bad', '{"build_profile":"../../bad"}', '{"build_profile":[]}'])
def test_invalid_metadata_fails(tmp_path, metadata):
    (tmp_path / "template.json").write_text(metadata)
    with pytest.raises(ValueError):
        syncer.resolve_project_profile(tmp_path)


def test_explicit_profile_overrides_legacy_prefix(tmp_path):
    project = tmp_path / "NSFC_Example"
    project.mkdir()
    (project / "template.json").write_text('{"build_profile":"thesis"}')
    assert syncer.resolve_project_profile(project) == "thesis"


def test_legacy_prefix_without_override(tmp_path):
    project = tmp_path / "NSFC_Example"
    project.mkdir()
    assert syncer.resolve_project_profile(project) == "nsfc"
    (project / "template.json").write_text('{"edition":"2026"}')
    assert syncer.resolve_project_profile(project) == "nsfc"


def test_unknown_directory_without_metadata_stays_skipped(tmp_path):
    assert syncer.resolve_project_profile(tmp_path) is None
