from __future__ import annotations

from pathlib import Path
import sys

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts import create_project as creator


def make_template(projects_dir: Path, name: str = "NSFC_Local") -> Path:
    template_dir = projects_dir / name
    (template_dir / ".latex-cache").mkdir(parents=True)
    (template_dir / ".vscode").mkdir()
    (template_dir / "extraTex").mkdir()
    (template_dir / "template").mkdir()

    (template_dir / "main.tex").write_text("template body\n", encoding="utf-8")
    (template_dir / "main.pdf").write_bytes(b"generated pdf")
    (template_dir / "main.aux").write_text("generated aux\n", encoding="utf-8")
    (template_dir / ".latex-cache" / "main.log").write_text(
        "generated log\n", encoding="utf-8"
    )
    (template_dir / "extraTex" / "content.tex").write_text(
        "content\n", encoding="utf-8"
    )
    (template_dir / "template" / "official.docx").write_bytes(b"official docx")
    (template_dir / "template" / "official.pdf").write_bytes(b"official pdf")
    (template_dir / ".vscode" / "settings.json").write_text(
        "{}\n", encoding="utf-8"
    )
    (template_dir / f"{name}.code-workspace").write_text(
        "old workspace\n", encoding="utf-8"
    )
    return template_dir


def write_new_workspace(project_dir: Path, *, check_only: bool) -> list[str]:
    assert check_only is False
    workspace = project_dir / f"{project_dir.name}.code-workspace"
    workspace.write_text("new workspace\n", encoding="utf-8")
    return [f"UPDATED {workspace.name}"]


def test_create_project_copies_clean_source_and_generates_named_workspace(tmp_path: Path):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)

    created = creator.create_project(
        template_name="NSFC_Local",
        project_name="NSFC_MyProject",
        projects_dir=projects_dir,
        sync_project_func=write_new_workspace,
    )

    assert created == projects_dir / "NSFC_MyProject"
    assert (created / "main.tex").read_text(encoding="utf-8") == "template body\n"
    assert (created / "extraTex" / "content.tex").is_file()
    assert (created / "template" / "official.docx").is_file()
    assert (created / ".vscode" / "settings.json").is_file()
    assert not (created / ".latex-cache").exists()
    assert not (created / "main.pdf").exists()
    assert not (created / "main.aux").exists()
    assert not (created / "template" / "official.pdf").exists()
    assert not (created / "NSFC_Local.code-workspace").exists()
    assert (created / "NSFC_MyProject.code-workspace").is_file()


@pytest.mark.parametrize(
    "project_name",
    ["MyProject", "../NSFC_Escape", "NSFC_Project/child", "NSFC_Project name"],
)
def test_create_project_rejects_unsafe_or_unrecognized_project_names(
    tmp_path: Path, project_name: str
):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)

    with pytest.raises(ValueError):
        creator.create_project(
            template_name="NSFC_Local",
            project_name=project_name,
            projects_dir=projects_dir,
            sync_project_func=write_new_workspace,
        )


@pytest.mark.parametrize(
    ("template_name", "project_name"),
    [
        ("GDNSF_General", "GDNSF_MyProject"),
        ("GXNSF_General", "GXNSF_MyProject"),
    ],
)
def test_create_project_supports_provincial_grant_families(
    tmp_path: Path, template_name: str, project_name: str
):
    """省级基金产品线此前被 ^NSFC_ 硬校验挡住，完全建不出项目。"""
    projects_dir = tmp_path / "projects"
    make_template(projects_dir, name=template_name)

    created = creator.create_project(
        template_name=template_name,
        project_name=project_name,
        projects_dir=projects_dir,
        sync_project_func=write_new_workspace,
    )

    assert created == projects_dir / project_name
    assert (created / "main.tex").read_text(encoding="utf-8") == "template body\n"
    assert (created / f"{project_name}.code-workspace").is_file()
    assert not (created / f"{template_name}.code-workspace").exists()


def test_create_project_rejects_cross_family_copy(tmp_path: Path):
    """跨产品线复制会让同步器写入错族的 settings.json，产出编译不了的项目。"""
    projects_dir = tmp_path / "projects"
    make_template(projects_dir, name="GDNSF_General")

    with pytest.raises(ValueError, match="同一产品线"):
        creator.create_project(
            template_name="GDNSF_General",
            project_name="NSFC_Mixed",
            projects_dir=projects_dir,
            sync_project_func=write_new_workspace,
        )

    assert not (projects_dir / "NSFC_Mixed").exists()


def test_create_project_rejects_families_needing_extra_metadata(tmp_path: Path):
    """thesis 项目还需同步维护 template.json，直接复制会产出坏项目。"""
    projects_dir = tmp_path / "projects"
    make_template(projects_dir, name="thesis-smu-master")

    with pytest.raises(ValueError, match="template.json"):
        creator.create_project(
            template_name="thesis-smu-master",
            project_name="thesis-foo-master",
            projects_dir=projects_dir,
            sync_project_func=write_new_workspace,
        )


def test_validate_project_name_returns_detected_profile():
    assert creator.validate_project_name("NSFC_Foo", label="新项目名") == "nsfc"
    assert creator.validate_project_name("GDNSF_Foo", label="新项目名") == "gdnsf"
    assert creator.validate_project_name("GXNSF_Foo", label="新项目名") == "gxnsf"


def test_main_reports_family_specific_build_command(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """各产品线的构建 wrapper 不同，不能一律提示 NSFC 的命令。"""
    projects_dir = tmp_path / "projects"
    make_template(projects_dir, name="GXNSF_General")
    monkeypatch.setattr(creator, "PROJECTS_DIR", projects_dir)
    monkeypatch.setattr(creator.sync_vscode_configs, "sync_project", write_new_workspace)

    exit_code = creator.main(["--template", "GXNSF_General", "--name", "GXNSF_FromCli"])

    assert exit_code == 0
    assert "scripts/gxnsf_build.py" in capsys.readouterr().out


def test_create_project_preserves_existing_destination(tmp_path: Path):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)
    destination = projects_dir / "NSFC_Existing"
    destination.mkdir()
    sentinel = destination / "keep.txt"
    sentinel.write_text("user data\n", encoding="utf-8")

    with pytest.raises(FileExistsError):
        creator.create_project(
            template_name="NSFC_Local",
            project_name="NSFC_Existing",
            projects_dir=projects_dir,
            sync_project_func=write_new_workspace,
        )

    assert sentinel.read_text(encoding="utf-8") == "user data\n"


def test_create_project_rejects_missing_template(tmp_path: Path):
    projects_dir = tmp_path / "projects"
    projects_dir.mkdir()

    with pytest.raises(FileNotFoundError):
        creator.create_project(
            template_name="NSFC_Missing",
            project_name="NSFC_New",
            projects_dir=projects_dir,
            sync_project_func=write_new_workspace,
        )


def test_create_project_rolls_back_new_directory_when_vscode_sync_fails(tmp_path: Path):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)

    def fail_sync(project_dir: Path, *, check_only: bool) -> list[str]:
        raise RuntimeError("sync failed")

    with pytest.raises(RuntimeError, match="sync failed"):
        creator.create_project(
            template_name="NSFC_Local",
            project_name="NSFC_Rollback",
            projects_dir=projects_dir,
            sync_project_func=fail_sync,
        )

    assert not (projects_dir / "NSFC_Rollback").exists()


def test_main_creates_project_from_cli_arguments(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)
    monkeypatch.setattr(creator, "PROJECTS_DIR", projects_dir)
    monkeypatch.setattr(creator.sync_vscode_configs, "sync_project", write_new_workspace)

    exit_code = creator.main(
        ["--template", "NSFC_Local", "--name", "NSFC_FromCli"]
    )

    assert exit_code == 0
    assert (projects_dir / "NSFC_FromCli" / "main.tex").is_file()
    assert "projects/NSFC_FromCli" in capsys.readouterr().out


def test_cli_defaults_to_clean_local_template():
    args = creator.build_parser().parse_args(["--name", "NSFC_FromClean"])

    assert args.template == "NSFC_Local_Clean"


def test_main_reports_existing_destination_without_overwriting(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    projects_dir = tmp_path / "projects"
    make_template(projects_dir)
    destination = projects_dir / "NSFC_Existing"
    destination.mkdir()
    sentinel = destination / "keep.txt"
    sentinel.write_text("user data\n", encoding="utf-8")
    monkeypatch.setattr(creator, "PROJECTS_DIR", projects_dir)

    exit_code = creator.main(
        ["--template", "NSFC_Local", "--name", "NSFC_Existing"]
    )

    assert exit_code == 1
    assert sentinel.read_text(encoding="utf-8") == "user data\n"
    assert "不会覆盖" in capsys.readouterr().err
