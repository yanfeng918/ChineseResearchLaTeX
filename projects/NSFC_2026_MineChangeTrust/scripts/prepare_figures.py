#!/usr/bin/env python3
"""Prepare the seven selected figures, preserving source pixels and measured data."""

from pathlib import Path
import hashlib
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pymupdf


PROJECT = Path(__file__).resolve().parents[1]
FIGURES = PROJECT / "figures"
RESULTS = PROJECT / "code" / "pilot" / "results"
NAMES = [
    "F01_research_background",
    "F02_overall_framework",
    "F03_route_diagnosis",
    "F04_route_constraint",
    "F05_route_reliability",
    "F14_pilot_workflow",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wrap_png(source, output):
    """Embed the decoded image without resampling or JPEG recompression."""
    image = pymupdf.Pixmap(str(source))
    width = 183 / 25.4 * 72
    doc = pymupdf.open()
    page = doc.new_page(width=width, height=width * image.height / image.width)
    page.insert_image(page.rect, filename=str(source))
    doc.set_metadata({"title": output.stem, "subject": "Lossless raster wrapper; source: " + source.name})
    doc.save(str(output), garbage=4, deflate=True)
    doc.close()
    with pymupdf.open(output) as check:
        embedded = pymupdf.Pixmap(check, check[0].get_images()[0][0])
        assert (embedded.width, embedded.height, embedded.samples) == (image.width, image.height, image.samples)


def prepare_result_plot():
    for font in font_manager.findSystemFonts():
        if Path(font).name in {"NotoSansCJK-Regular.ttc", "SourceHanSansSC-Regular.otf"}:
            font_manager.fontManager.addfont(font)
            family = font_manager.FontProperties(fname=font).get_name()
            break
    else:
        raise RuntimeError("Install Noto Sans CJK or Source Han Sans before rendering Chinese labels.")
    plt.rcParams.update({
        "font.family": family,
        "font.size": 9,
        "axes.unicode_minus": False,
        # CJK TTC subsetting through Type 42 mis-maps glyphs in this renderer.
        # Type 3 embeds the original glyph outlines as vector content.
        "pdf.fonttype": 3,
        "ps.fonttype": 42,
        "axes.labelcolor": "#333333",
        "text.color": "#333333",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "axes.edgecolor": "#616161",
        "axes.linewidth": 0.8,
        "savefig.facecolor": "white",
    })
    aggregate_path = RESULTS / "aggregate_metrics.json"
    contrasts_path = RESULTS / "paired_site_contrasts.json"
    aggregate = {row["arm"]: row for row in json.loads(aggregate_path.read_text())}
    contrasts = {(row["contrast"], row["metric"]): row for row in json.loads(contrasts_path.read_text())}
    arms = ["none", "full", "background"]
    metrics = ["IoU", "FPR", "recall"]
    colors = ["#616161", "#2E6B9E", "#1B3A5C"]
    markers = ["s", "o", "^"]
    titles = ["变化 IoU", "背景误报率", "总体召回率"]
    pairs = ["background - full", "background - none"]
    fig, axes = plt.subplots(2, 3, figsize=(183 / 25.4, 137.25 / 25.4))
    # Reserve a separate heading band above the panel titles and between rows.
    fig.subplots_adjust(left=0.14, right=0.98, top=0.87, bottom=0.17, hspace=0.85, wspace=0.40)
    plotted = {"top": [], "bottom": []}
    for c, metric in enumerate(metrics):
        ax = axes[0, c]
        for x, arm in enumerate(arms):
            values = aggregate[arm][metric]
            mean, sd = 100 * values["mean"], 100 * values["seed_std"]
            assert np.isfinite(mean) and np.isfinite(sd) and sd >= 0
            ax.errorbar(x, mean, yerr=sd, fmt=markers[x], color=colors[x], markersize=6,
                        capsize=3, elinewidth=1.2, markeredgewidth=1.1, zorder=3)
            plotted["top"].append({"arm": arm, "metric": metric, "mean_percent": mean, "seed_sd_percent": sd})
        ax.set_title(f"({chr(97 + c)}) {titles[c]}", fontsize=10, fontweight="bold", color="#1B3A5C", pad=10)
        ax.set_xticks(range(3), ["无一致性", "全区域", "背景位置"], fontsize=8)
        ax.set_xlim(-0.55, 2.55)
        ax.set_ylim(0, [30, 40, 100][c])
        ax.set_yticks(np.arange(0, [31, 41, 101][c], [10, 10, 20][c]))
        if c == 0:
            ax.set_ylabel("指标（%）", fontsize=9)
        for r, contrast in enumerate(pairs):
            row = contrasts[(contrast, metric)]
            mean, low, high = [100 * row[key] for key in ("mean_difference", "ci_low", "ci_high")]
            assert -7 <= low <= mean <= high <= 3
            axes[1, c].errorbar(mean, 1 - r, xerr=[[mean - low], [high - mean]], fmt=markers[r + 1],
                               color=colors[r + 1], markersize=6, capsize=3, elinewidth=1.2, zorder=3)
            plotted["bottom"].append({"contrast": contrast, "metric": metric, "difference_pp": mean, "ci95_pp": [low, high]})
        ax = axes[1, c]
        ax.axvline(0, color="#888888", linewidth=0.9, linestyle="--", zorder=1)
        ax.set_title(f"({chr(100 + c)}) {['IoU差', '误报率差', '总体召回差'][c]}",
                     fontsize=10, fontweight="bold", color="#1B3A5C", pad=10)
        ax.set_xlim(-7, 3)
        ax.set_xticks([-6, -3, 0, 3])
        ax.set_ylim(-0.45, 1.45)
        ax.set_yticks([1, 0], ["背景减全区域", "背景减无约束"] if c == 0 else ["", ""], fontsize=8)
        ax.tick_params(axis="y", length=0)
        ax.set_xlabel("差异（百分点）", fontsize=8.5)
    for ax in axes.ravel():
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#E6E6E6", linewidth=0.5)
        ax.set_axisbelow(True)
        ax.tick_params(axis="both", labelsize=8)
    fig.text(0.56, 0.988, "预实验结果：三组均值与种子标准差", ha="center", va="top", fontsize=10, color="#1B3A5C")
    fig.text(0.56, 0.535, "矿区配对差异与95%区间", ha="center", va="center", fontsize=10, color="#1B3A5C")
    fig.text(0.56, 0.042, "小变化召回：NA（验证子样本中无合格对象）", ha="center", fontsize=9)
    output = FIGURES / "F15_F16_pilot_results.pdf"
    fig.savefig(output, metadata={"Title": "MCT-P01: measured performance and paired mine effects", "Subject": "Coordinates derived from archived JSON; no simulated measurements."})
    plt.close(fig)
    return output, {
        "display_number": 7,
        "figure_id": "F15_F16",
        "pdf": output.name,
        "kind": "vector plot from archived measurements",
        "data_sources": {str(path.relative_to(PROJECT)): digest(path) for path in (aggregate_path, contrasts_path)},
        "plotted_values": plotted,
        "note": "The supplied seventh PNG has mismatched values and is preserved but not used as scientific evidence.",
    }


def main():
    records = []
    for n, name in enumerate(NAMES, 1):
        matches = list(FIGURES.glob(f"ChatGPT Image * ({n}).png"))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one source image for figure {n}, found {len(matches)}")
        source = matches[0]
        output = FIGURES / (name + ".pdf")
        before = digest(source)
        wrap_png(source, output)
        assert digest(source) == before
        records.append({"display_number": n, "figure_id": "F14" if n == 6 else f"F{n:02}",
                        "png": source.name, "png_sha256": before, "pdf": output.name,
                        "kind": "lossless raster PDF", "latex_top_trim_mm": 12,
                        "note": "Full original retained in the PDF; LaTeX clips only its embedded heading for automatic caption numbering."})
    _, result = prepare_result_plot()
    records.append(result)
    (FIGURES / "inserted_figures.json").write_text(json.dumps({"figure_count": 7, "items": records}, ensure_ascii=False, indent=2) + "\n")
    print("Prepared six lossless raster PDFs and one measured vector result plot.")


if __name__ == "__main__":
    main()
