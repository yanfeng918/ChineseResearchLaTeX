#!/usr/bin/env python3
"""Export the editable six-figure deck to native vector PDF and SVG files."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

import pymupdf


FIGURES = [
    "F01_research_background",
    "F02_overall_framework",
    "F03_route_diagnosis",
    "F04_route_constraint",
    "F05_route_reliability",
    "F14_pilot_workflow",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", required=True, type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    deck = project / "figures/NSFC-Figures-vector.pptx"
    output = project / "figures/vector"
    executable = shutil.which("soffice") or shutil.which("libreoffice")
    if not executable or not deck.is_file():
        parser.error("需要 LibreOffice 和 figures/NSFC-Figures-vector.pptx")
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="vector-export-", dir=work) as temp:
        temporary = Path(temp)
        subprocess.run(
            [executable, "-env:UserInstallation=" + (temporary / "profile").as_uri(),
             "--headless", "--convert-to", "pdf", "--outdir", str(temporary), str(deck)],
            check=True, timeout=180,
        )
        exported = temporary / (deck.stem + ".pdf")
        with pymupdf.open(exported) as source:
            if len(source) != len(FIGURES):
                raise ValueError("图件PPT必须恰好为6页，且与FIGURES顺序一致")
            report = []
            for index, name in enumerate(FIGURES):
                page = source[index]
                if page.get_images(full=True):
                    raise ValueError(f"{name}仍含位图，不能作为全矢量图交付")
                # Preserve the original figure canvas and the existing 12 mm top trim.
                with pymupdf.open(project / "figures" / (name + ".pdf")) as original:
                    rectangle = original[0].rect
                result = pymupdf.open()
                target = result.new_page(width=rectangle.width, height=rectangle.height)
                target.show_pdf_page(target.rect, source, index)
                result.save(output / (name + ".pdf"), garbage=4, deflate=True)
                # Outlined glyphs keep SVG portable; the PPT preserves editable text.
                (output / (name + ".svg")).write_text(target.get_svg_image(text_as_path=True))
                report.append({"figure": name, "slide": index + 1,
                               "raster_images": len(target.get_images(full=True)),
                               "text_characters": len(target.get_text()),
                               "vector_paths": len(target.get_drawings())})
                result.close()
            (work / "vector-export.json").write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"已导出6幅矢量 PDF 和 SVG：{output}")


if __name__ == "__main__":
    main()
