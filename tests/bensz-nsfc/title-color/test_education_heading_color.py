from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "projects" / "NSFC_2026_Education"
BLACK_SUBSUBSECTION_FORMAT = (
    r"\newcommand{\NSFCProjectSubsubsectionFormat}"
    r"{\color{black} \subsubsectionzihao \templatefont \bfseries}"
)
BLACK_REFERENCE_HEADING = (
    r"\newcommand{\NSFCProjectReferenceHeading}"
    r"{\color{black} \sihao \templatefont \bfseries \leftline{参考文献}}"
)


@pytest.mark.parametrize("project_name", ["NSFC_Local_Clean", "NSFC_2026_Education"])
def test_clean_template_and_derived_project_subsubsection_headings_are_black(
    project_name: str,
):
    config = (
        REPO_ROOT / "projects" / project_name / "extraTex" / "@config.tex"
    ).read_text(encoding="utf-8")

    assert BLACK_SUBSUBSECTION_FORMAT in config


@pytest.mark.parametrize("project_name", ["NSFC_Local_Clean", "NSFC_2026_Education"])
def test_clean_template_and_derived_project_reference_heading_are_black(
    project_name: str,
):
    config = (
        REPO_ROOT / "projects" / project_name / "extraTex" / "@config.tex"
    ).read_text(encoding="utf-8")

    assert BLACK_REFERENCE_HEADING in config


def test_education_justification_uses_subsubsection_for_expected_headings():
    content = (PROJECT_DIR / "extraTex" / "1.1.立项依据.tex").read_text(
        encoding="utf-8"
    )

    for heading in (
        "研究背景与意义",
        "国内外研究现状及发展动态分析",
        "现有研究不足",
        "本项目的研究切入点",
    ):
        assert rf"\subsubsection{{{heading}}}" in content
