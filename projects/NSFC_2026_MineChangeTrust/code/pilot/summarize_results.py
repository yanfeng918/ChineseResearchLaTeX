"""Recompute saved confusion counts and create publication figures and portable evidence."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import ndimage

ARMS = ['none', 'full', 'background']
NAMES = ['No consistency', 'Full region', 'Background only']
COLORS = ['#64748b', '#d88736', '#168b86']


def read(path):
    return json.loads(path.read_text())


def save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cache-dir', type=Path, required=True)
    ap.add_argument('--run-dir', type=Path, required=True)
    ap.add_argument('--output-dir', type=Path, required=True)
    args = ap.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    aggregate = {x['arm']: x for x in read(args.run_dir / 'aggregate_metrics.json')}
    counts = read(args.run_dir / 'per_site_metrics.json')
    contrasts = read(args.run_dir / 'paired_site_contrasts.json')
    with np.load(args.cache_dir / 'val.npz') as f:
        data = {k: f[k] for k in f.files}
    y = data['label'].astype(bool)
    # Independent small-component implementation; do not reuse training helper.
    sm = np.zeros_like(y)
    cfg = read(args.run_dir / 'frozen_protocol.json')['protocol']
    for index, label in enumerate(y):
        components, n = ndimage.label(label, structure=np.ones((3, 3)))
        for k, slices in enumerate(ndimage.find_objects(components), 1):
            if slices is None:
                continue
            if any(s.start == 0 or s.stop == 256 for s in slices):
                continue
            candidate = components[slices] == k
            if candidate.sum() <= cfg['small_component_max_pixels']:
                sm[index][slices] |= candidate
    audits = []
    for seed in cfg['seeds']:
        initial_hashes = []
        for arm in ARMS:
            run = args.run_dir / f'{arm}_seed{seed}'
            summary = read(run / 'training_summary.json')
            initial_hashes.append(summary['initial_state_sha256'])
            assert hashlib.sha256((run / 'model.pt').read_bytes()).hexdigest() == summary['checkpoint_sha256']
            assert summary['epochs'] == 12 and not summary['validation_used_for_selection']
            with np.load(run / 'validation_predictions.npz') as f:
                pred = f['prediction']
                assert np.array_equal(pred, f['probability'] >= cfg['threshold'])
                assert np.array_equal(f['row_index'], data['row_index'])
                assert np.array_equal(f['domain'], data['domain'])
            for row in counts:
                if row['arm'] != arm or row['seed'] != seed:
                    continue
                idx = data['domain'] == row['domain']
                gt, pr = y[idx], pred[idx]
                # Integer encoding independently reconstructs TN, FP, FN, TP.
                matrix = np.bincount((gt.astype(np.uint8) * 2 + pr).ravel(), minlength=4)
                assert matrix.tolist() == [row['TN'], row['FP'], row['FN'], row['TP']]
                assert int(sm[idx].sum()) == row['small_total']
                assert int((sm[idx] & pr).sum()) == row['small_TP']
            audits.append(summary)
        assert len(set(initial_hashes)) == 1
    save(out / 'recomputation_audit.json', {'runs_checked': len(audits), 'site_rows_checked': len(counts), 'confusion_counts_match': True, 'small_component_counts_match': True, 'prediction_threshold_exact_match': True, 'same_seed_initialization_match': True, 'checkpoint_hashes_match': True})
    for name in ['aggregate_metrics.json', 'paired_site_contrasts.json', 'seed_macro_metrics.json', 'per_site_metrics.json', 'per_site_metrics.csv', 'frozen_protocol.json']:
        shutil.copy2(args.run_dir / name, out / name)
    for name in ['audit.json', 'selection.json', 'sample_manifest.jsonl', 'qualitative_selection.json']:
        shutil.copy2(args.cache_dir / name, out / name)
    save(out / 'training_summaries.json', audits)
    save(out / 'training_curves.json', {f'{a}_seed{s}': read(args.run_dir / f'{a}_seed{s}/training_curve.json') for s in cfg['seeds'] for a in ARMS})
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False, 'pdf.fonttype': 42})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.0), layout='constrained')
    for ax, metric, title in zip(axes, ['IoU', 'FPR', 'small_recall'], ['Change IoU (higher better)', 'Background FPR (lower better)', 'Small-change recall (higher better)']):
        if any(aggregate[a][metric]['mean'] is None for a in ARMS):
            ax.set_title(title, fontsize=10)
            ax.text(.5, .5, 'NA: no eligible\nsmall components', ha='center', va='center', transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            continue
        means = [aggregate[a][metric]['mean'] * 100 for a in ARMS]
        stds = [aggregate[a][metric]['seed_std'] * 100 for a in ARMS]
        ax.bar(range(3), means, yerr=stds, color=COLORS, capsize=4, width=.6)
        ax.set_xticks(range(3), ['None', 'Full', 'Background'])
        ax.set_ylabel('Site-macro score (%)')
        ax.set_title(title, fontsize=10)
        ax.set_ylim(bottom=0)
        ax.grid(axis='y', alpha=.15)
    fig.suptitle('MineNetCD256 pilot | 10 validation mines | mean ± SD across 3 seeds', fontsize=11)
    for ext in ['pdf', 'png']:
        fig.savefig(out / f'pilot_metrics.{ext}', dpi=220)
    plt.close(fig)
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.5), layout='constrained')
    for ax, metric in zip(axes, ['IoU', 'FPR', 'small_recall']):
        row = next(x for x in contrasts if x['contrast'] == 'background - full' and x['metric'] == metric)
        if row['n'] == 0:
            ax.set_title(metric + ': Background − Full')
            ax.text(.5, .5, 'NA: no eligible\nsmall components', ha='center', va='center', transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            continue
        values = np.array(row['site_differences']) * 100
        ax.scatter(values, np.arange(len(values)), color=COLORS[2], s=22)
        ax.axvline(0, color='#888888', linewidth=.8)
        ax.errorbar(row['mean_difference'] * 100, -1.5, xerr=np.array([[row['mean_difference'] - row['ci_low']], [row['ci_high'] - row['mean_difference']]]) * 100, fmt='D', color='#0f172a', capsize=4)
        ax.set_yticks([-1.5] + list(range(len(values))), ['Mean / 95% CI'] + [f'M{i+1:02d}' for i in range(len(values))])
        ax.set_xlabel('Difference (percentage points)')
        ax.set_title(metric + ': Background − Full')
        ax.grid(axis='x', alpha=.15)
    fig.suptitle('Exploratory paired-mine bootstrap; seeds averaged within each mine', fontsize=11)
    for ext in ['pdf', 'png']:
        fig.savefig(out / f'pilot_paired_effects.{ext}', dpi=220)
    plt.close(fig)
    selected = read(args.cache_dir / 'qualitative_selection.json')['cases']
    predictions = {}
    for arm in ARMS:
        with np.load(args.run_dir / f'{arm}_seed{cfg["seeds"][0]}/validation_predictions.npz') as f:
            predictions[arm] = f['prediction'][[c['index'] for c in selected]]
    fig, axes = plt.subplots(len(selected), 6, figsize=(12, 6), layout='constrained')
    for r, case in enumerate(selected):
        i = case['index']
        ims = [data['imageA'][i], data['imageB'][i], data['label'][i]] + [predictions[a][r] for a in ARMS]
        for c, im in enumerate(ims):
            axes[r, c].imshow(im, cmap='gray', vmin=0, vmax=1 if c >= 2 else 255)
            axes[r, c].set_xticks([])
            axes[r, c].set_yticks([])
            if r == 0:
                axes[r, c].set_title(['Time A', 'Time B', 'Change label', *NAMES][c], fontsize=9)
        axes[r, 0].set_ylabel(f"{case['domain']}\nrow {case['row_index']}", fontsize=7)
    fig.suptitle('Prespecified validation examples | seed 17 | white = change\nSource: Yu et al., MineNetCD / HZDR-FWGEL (CC BY 4.0); predictions generated in this pilot', fontsize=10)
    for ext in ['pdf', 'png']:
        fig.savefig(out / f'pilot_examples.{ext}', dpi=180)
    plt.close(fig)
    print(json.dumps({'verified_runs': len(audits), 'output_dir': str(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
