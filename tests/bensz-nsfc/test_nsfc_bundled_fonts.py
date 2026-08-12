from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = REPO_ROOT / "packages" / "bensz-nsfc" / "templates"


def _bundled_fonts_branch(template_name: str) -> str:
    content = (TEMPLATE_DIR / template_name).read_text(encoding="utf-8")
    branch_start = content.index(r"\ifNSFCHasBundledFonts")
    branch_end = content.index(r"\else", branch_start)
    return content[branch_start:branch_end]


def test_nsfc_templates_use_bundled_times_new_roman_file() -> None:
    expected = (
        r"\setmainfont[Path={\NSFCResolvedFontsDir}, Extension=.ttf, "
        r"AutoFakeBold=5, AutoFakeSlant=0.2]{TimesNewRoman}"
    )

    for profile in ("general", "local", "young"):
        bundled_branch = _bundled_fonts_branch(f"bensz-nsfc-{profile}.tex")
        assert expected in bundled_branch, (
            f"{profile} 模板在随包字体分支中没有使用 TimesNewRoman.ttf"
        )
        assert "BoldFont=Times New Roman" not in bundled_branch
