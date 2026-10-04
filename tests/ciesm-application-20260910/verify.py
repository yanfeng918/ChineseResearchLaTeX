"""Acceptance checks against actual PDFs, source dependencies and final build log."""
import collections
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pymupdf as fitz
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
P = ROOT / 'projects/NSFC_2026_CIESM-STSR_final'
S = ROOT / 'projects/NSFC_2026_CIESM-STSR'
OUT = HERE / 'rendered'
OUT.mkdir(exist_ok=True)

def norm(s):
    return re.sub(r'\s+', '', s)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def uncomment(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

main = fitz.open(P / 'main.pdf')
blank = fitz.open(P / 'blank.pdf')
official = fitz.open(P / '地球系统数值模拟教育部重点实验室开放基金.pdf')
assert len(blank) == len(official) == 4
metrics = []
for i, (a, b) in enumerate(zip(blank, official)):
    assert abs(a.rect.width - b.rect.width) < .1
    assert abs(a.rect.height - b.rect.height) < .1
    assert collections.Counter(norm(a.get_text())) == collections.Counter(norm(b.get_text())), ('blank text', i + 1)
    assert not a.get_images() and not a.get_xobjects(), 'Blank must be native text/table'
    aa, bb = [np.frombuffer(p.get_pixmap(matrix=fitz.Matrix(2, 2)).samples, dtype=np.uint8).reshape(-1, 3)
              for p in (a, b)]
    metrics.append({'page': i + 1, 'different_pixels_percent': round(float(np.any(aa != bb, axis=1).mean() * 100), 4),
                    'mean_absolute_channel_difference': round(float(np.abs(aa.astype(float) - bb).mean()), 4)})
    a.get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(OUT / f'blank-{i+1:02}.png')
    b.get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(OUT / f'official-{i+1:02}.png')

# Primary pixel metric uses the official compare command's pdftoppm rasters.
# MuPDF above is an independent text/geometry check; DeviceGray conversion can
# differ from the official RGB gray by one channel level over a large table area.
official_metrics = []
for i in range(1, 5):
    a = np.asarray(Image.open(HERE / f'blank-compare/project/project-{i}.png').convert('RGB'))
    b = np.asarray(Image.open(HERE / f'blank-compare/baseline/baseline-{i}.png').convert('RGB'))
    delta = np.abs(a.astype(int) - b)
    official_metrics.append({'page': i, 'different_pixels_percent': round(float(np.any(delta > 0, axis=2).mean() * 100), 4),
                            'mean_absolute_channel_difference': round(float(delta.mean()), 4)})

texts = [norm(p.get_text()) for p in main]
alltext = ''.join(texts)
headings = ['一、基本信息表', '二、报告正文', '（一）立项依据与研究内容',
 '1．课题的立项依据', '2．课题的研究内容及拟解决的关键科学问题',
 '3．课题的特色与创新之处', '4．年度研究计划及预期研究结果',
 '（二）研究基础与工作条件', '1．工作基础（', '2．申请人简介（', '三、课题经费预算表']
assert all(alltext.count(h) == 1 for h in headings), {h: alltext.count(h) for h in headings}
assert '本次未迁移图片' not in alltext and '??' not in alltext and '\ufffd' not in alltext
for i, text in enumerate(texts):
    assert f'第{i+1}页共{len(main)}页' in text

aux = (P / '.latex-cache/main.aux').read_text()
part = column = sub = para = 0
heading_rows = []
for line in aux.splitlines():
    m = re.search(r'\\contentsline \{(section|subsection|subsubsection|paragraph)\}\{\\numberline \{([^}]*)\}', line)
    if not m:
        continue
    kind, number = m.groups()
    if kind == 'section':
        part += 1
        column = 0
    elif kind == 'subsection':
        column += 1
        sub = 0
    elif kind == 'subsubsection':
        sub += 1
        para = 0
        assert number == f'{column}.{sub}', line
    else:
        para += 1
        assert number == f'{column}.{sub}.{para}', line
    heading_rows.append({'part': part, 'column': column, 'kind': kind, 'number': number})

inventory = json.loads((HERE / 'resource-inventory-before.json').read_text())
source_keys = {key.strip() for row in inventory['inputs'] for call in row['citations'] for key in call.split(',')}
bbl = (P / '.latex-cache/main.bbl').read_text()
bibkeys = set(re.findall(r'\\entry\{([^}]+)\}', bbl))
assert source_keys == bibkeys and len(bibkeys) == 25, (source_keys - bibkeys, bibkeys - source_keys)
assert sha(P / 'references/myexample.bib') == sha(S / 'references/myexample.bib')
figures = []
figure_tex = '\n'.join(p.read_text() for p in (P / 'extraTex').glob('*.tex'))
assert figure_tex.count('\\CiesmFigure{') == 7
for number, row in enumerate(inventory['figures'], 1):
    assert sha(P / row['path']) == row['sha256'] == sha(S / row['path'])
    match = re.search(r'\\CiesmFigure\{' + re.escape(row['path']) + r'\}\{([^}]+)\}\{([^}]+)\}', figure_tex)
    assert match
    caption, label = match.groups()
    m = re.search(r'\\newlabel\{' + re.escape(label) + r'\}\{\{(\d+)\}\{(\d+)\}', aux)
    assert m and int(m[1]) == number
    page = main[int(m[2]) - 1]
    assert norm(caption) in norm(page.get_text())
    assert f'图{number}' in norm(page.get_text())
    assert len(page.get_xobjects()) == 1, (number, 'missing original PDF form')
    assert not page.get_images(), 'Original vector figure must remain vector'
    paths = page.get_drawings()
    bounds = fitz.Rect(paths[0]['rect'])
    for path in paths[1:]:
        bounds |= path['rect']
    assert bounds.x0 >= 89 and bounds.x1 <= 506.3 and bounds.y0 >= 79 and bounds.y1 <= 762, (number, bounds)
    figures.append({'number': number, 'label': label, 'page': int(m[2]), 'file': row['path'],
                    'sha256': row['sha256'], 'vector_bounds': list(bounds)})

# Compare line baselines before every new bibliography item against the preceding
# line on that page. This measures rendered item gaps, including continuation pages.
item_gaps, inner_gaps = [], []
ref_pages = []
for i, page in enumerate(main):
    lines = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            spans = line['spans']
            if any('TimesNewRoman' in s['font'] and 10 < s['size'] < 13 for s in spans):
                lines.append((round(spans[0]['origin'][1], 3), ''.join(s['text'] for s in spans)))
    # A rendered numeric bibliography label distinguishes bibliography from CV.
    if not any(re.match(r'^\[\d+\]', text) for _, text in lines):
        continue
    ref_pages.append(i + 1)
    ys = sorted({y for y, _ in lines})
    starts = {y for y, t in lines if re.match(r'^\[\d+\]', t)}
    for previous, current in zip(ys, ys[1:]):
        gap = round(current - previous, 3)
        (item_gaps if current in starts else inner_gaps).append(gap)
assert len(item_gaps) >= 18 and max(abs(g - 22) for g in item_gaps) < .05, item_gaps
assert inner_gaps and max(abs(g - 22) for g in inner_gaps) < .05, inner_gaps

metadata = (P / 'extraTex/metadata.tex').read_text()
title = re.search(r'title=\{([^}]+)\}', metadata)[1]
for value in [title, '颜丰', '新疆大学']:
    assert norm(value) in texts[0] and norm(value) in texts[1]
address = re.search(r'address=\{([^}]+)\}', metadata)[1]
assert norm(address) in alltext
for key in ['phone', 'email']:
    assert norm(re.search(key + r'=\{([^}]+)\}', metadata)[1]) in alltext, key
assert '出生日期' in texts[1] and '1990年11月4日' in texts[1]
assert '2027年1月1日' in texts[1] and '2027年12月31日' in texts[1]
abstract = uncomment((P / 'extraTex/abstract.tex').read_text()).strip()
assert len(norm(abstract)) <= 400 and norm(abstract) in texts[1]
keywords = re.search(r'keywords=\{([^}]+)\}', metadata)[1].split('；')
assert len(keywords) <= 5 and all(norm(k) in texts[1] for k in keywords)

def field_bounds(page, value):
    chars = [c for b in page.get_text('rawdict')['blocks'] for line in b.get('lines', [])
             for span in line['spans'] for c in span['chars'] if not c['c'].isspace()]
    start = ''.join(c['c'] for c in chars).index(norm(value))
    boxes = [fitz.Rect(c['bbox']) for c in chars[start:start + len(norm(value))]]
    bounds = boxes[0]
    for box in boxes[1:]:
        bounds |= box
    return bounds

fixed_fields = []
for page, key, value, allowed in [
    (0, 'cover-title', title, (198, 321.94, 495, 371.79)),
    (1, 'information-title', title, (182.15, 103.92, 423.15, 124.91)),
    (1, 'keywords', '；'.join(keywords), (234.55, 588.43, 528.2, 610.12)),
    (1, 'birth-date', '1990年11月4日', (182.15, 166.86, 289.05, 187.46))]:
    rect = field_bounds(main[page], value)
    assert fitz.Rect(allowed).contains(rect), (key, rect)
    fixed_fields.append({'field': key, 'page': page + 1, 'glyph_bounds': list(rect), 'allowed_bounds': list(allowed)})
guard = HERE / 'fixtures/overflow-guard'
guard.mkdir(parents=True, exist_ok=True)
shutil.copytree(P / 'extraTex', guard / 'extraTex', dirs_exist_ok=True)
guard_source = (P / 'blank.tex').read_text().replace(r'\begin{document}',
    '\\CiesmSetup{title={' + '完整信息不可裁切' * 30 + '}}\n\\begin{document}')
(guard / 'main.tex').write_text(guard_source)
guard_run = subprocess.run([sys.executable, str(ROOT / 'packages/bensz-thesis/scripts/thesis_project_tool.py'),
    'build', '--project-dir', str(guard)], cwd=HERE, capture_output=True, text=True)
assert guard_run.returncode != 0, 'Oversized fields must fail the official build'
overflow_log = guard_run.stdout + guard_run.stderr
(HERE / 'overflow-guard.log').write_text(overflow_log)
assert 'Cover field' in overflow_log and 'Information field exceeds its box' in overflow_log and 'BuildError' in overflow_log

log = (P / '.latex-cache/main.log').read_text()
for marker in ['LaTeX Error', 'Package ciesm-open-fund Error', 'Overfull', 'Missing character', 'undefined', 'Font Warning']:
    assert marker not in log, marker
fls = (P / '.latex-cache/main.fls').read_text()
assert 'styles/bthesis-style-ciesm-open-fund.tex' in fls
assert '地球系统数值模拟教育部重点实验室开放基金.pdf' not in fls
assert all(row['path'] in fls for row in inventory['figures'])
overflow_spans = []
for i, page in enumerate(main):
    if i < 2 or i == len(main) - 1:
        continue
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                x0, y0, x1, y1 = span['bbox']
                if span['text'].strip() and y0 < 770 and (x0 < 88 or x1 > 507.3):
                    overflow_spans.append({'page': i + 1, 'bbox': span['bbox']})
assert not overflow_spans, overflow_spans

first_part = ''.join(uncomment((P / 'extraTex' / name).read_text()) for name in
 ['1.1.立项依据.tex', '1.2.研究内容.tex', '1.3.特色与创新.tex', '1.4.年度计划.tex'])
han_count = len(re.findall(r'[\u4e00-\u9fff]', first_part))
for stale in OUT.glob('main-*.png'):
    stale.unlink()
for i, page in enumerate(main):
    page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(OUT / f'main-{i+1:02}.png')
report = {'main_pages': len(main), 'blank_pages': len(blank), 'blank_comparison_pdftoppm_144dpi': official_metrics,
 'blank_comparison_mupdf_144dpi': metrics,
 'official_headings_each_once': headings, 'numbered_headings': heading_rows,
 'figures': figures, 'bibliography_keys': sorted(bibkeys), 'bibliography_pages': ref_pages,
 'bibliography_between_item_baselines_bp': item_gaps, 'bibliography_within_item_baselines_bp': sorted(set(inner_gaps)),
 'abstract_characters_including_punctuation': len(norm(abstract)), 'keywords': len(keywords),
 'first_part_han_count_including_headings_captions_excluding_bibliography': han_count,
 'first_part_3000_limit_met': han_count <= 3000,
 'full_address_and_contact_verified': True, 'fixed_field_bounds': fixed_fields,
 'oversized_field_guard_rejects': True, 'body_overflow_spans': overflow_spans,
 'underfull_boxes': re.findall(r'Underfull \\hbox \(badness \d+\)', log),
 'main_pdf_sha256': sha(P / 'main.pdf'), 'style_sha256': sha(ROOT / 'packages/bensz-thesis/styles/bthesis-style-ciesm-open-fund.tex')}
(HERE / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ['main_pages','blank_pages','abstract_characters_including_punctuation',
 'first_part_han_count_including_headings_captions_excluding_bibliography','underfull_boxes']}, ensure_ascii=False))
