"""Check rendered cover rules, justified bibliography and proposed budget."""
import collections
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import pymupdf as fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = ROOT / 'projects/NSFC_2026_CIESM-STSR_final'
main = fitz.open(P / 'main.pdf')
blank = fitz.open(P / 'blank.pdf')
metadata = (P / 'extraTex/metadata.tex').read_text()
norm = lambda s: re.sub(r'\s+', '', s)
title = re.search(r'title=\{([^}]+)\}', metadata)[1]

chars = [(c, span['size']) for b in main[0].get_text('rawdict')['blocks']
         for line in b.get('lines', []) for span in line['spans']
         for c in span['chars'] if not c['c'].isspace()]
start = ''.join(c['c'] for c, _ in chars).index(norm(title))
title_chars = chars[start:start + len(norm(title))]
baselines = sorted({round(c['origin'][1], 2) for c, _ in title_chars})
assert len(baselines) == 2
assert all(abs(size - 15.95) < .01 for _, size in title_chars)
rules = []
for baseline in baselines:
    matching = [list(p['rect']) for p in main[0].get_drawings()
                if abs(p['rect'].x0 - 198) < .01 and abs(p['rect'].x1 - 495) < .01
                and abs(p['rect'].y0 - baseline - 3.2) < .02
                and p['rect'].height < .01]
    assert len(matching) == 1
    rules += matching

full = json.loads((HERE.parent / 'verification.json').read_text())
lines = []
for n in full['bibliography_pages']:
    groups = collections.defaultdict(list)
    for b in main[n-1].get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for span in line['spans']:
                if 10 < span['size'] < 13:
                    groups[round(span['origin'][1], 2)].append(span)
    for baseline, spans in sorted(groups.items()):
        if any('TimesNewRoman' in span['font'] for span in spans):
            lines.append({'page': n, 'baseline': baseline,
                          'text': ''.join(s['text'] for s in spans),
                          'right': max(s['bbox'][2] for s in spans)})
assert sum(bool(re.match(r'^\[\d+\]', row['text'])) for row in lines) == 25
nonfinal = [row for row, following in zip(lines, lines[1:])
            if not re.match(r'^\[\d+\]', following['text'])]
assert len(nonfinal) > 60
# Slanted glyph ink can extend slightly beyond its typographic advance width.
assert all(abs(row['right'] - 505.3) < 2 for row in nonfinal), nonfinal

budget = (P / 'extraTex/budget.tex').read_text()
items = re.findall(r'\\CiesmBudgetRow\{(\d+)\}\{([^}]+)\}\{([\d.]+)\}\{([^}]+)\}', budget)
assert len(items) == 8
total = re.search(r'total-budget=\{([^}]+)\}', metadata)[1]
assert sum(Decimal(row[2]) for row in items) == Decimal(total) == Decimal('4.50')
rendered_amounts = re.findall(r'\d+\.\d{2}', norm(main[-1].get_text(clip=fitz.Rect(324, 152, 387, 740))))
assert rendered_amounts == [row[2] for row in items] + [total], rendered_amounts
assert total in norm(main[1].get_text())
budget_text = norm(main[-1].get_text())
for _, category, _, note in items:
    assert norm(category) in budget_text
    assert norm(note.replace(r'\newline', '')) in budget_text
assert not re.search(r'\d+\.\d{2}', blank[-1].get_text())
assert json.loads((HERE / 'blank-regression/compare-report.json').read_text())['identical']

regressions = []
for source in json.loads((HERE / 'regression-scope.json').read_text()):
    name = source['project']
    report = HERE / 'compatibility-compare/compare-report.json' if name == P.name else (
        HERE.parent / 'regression' / name / 'compare/compare-report.json')
    result = json.loads(report.read_text())
    assert result['identical']
    regressions.append({'project': name, 'pages': result['project_pages'], 'identical': True})

warnings = lambda p: re.findall(r'Underfull \\hbox \(badness \d+\)', p.read_text())
before_warnings = warnings(HERE / 'before/main.log')
after_warnings = warnings(P / '.latex-cache/main.log')
report = {'main_pages': len(main), 'blank_pages': len(blank),
          'cover_title_font_bp': 15.95, 'cover_title_baselines_bp': baselines,
          'cover_title_separate_underlines': rules,
          'bibliography_justified_nonfinal_lines': len(nonfinal),
          'bibliography_max_ink_right_edge_bp': max(row['right'] for row in nonfinal),
          'bibliography_item_baselines_bp': sorted(set(full['bibliography_between_item_baselines_bp'])),
          'budget_total_wan': total, 'budget_rendered_amounts_wan': rendered_amounts,
          'budget_status': 'proposal; unit prices and categories require applicant review',
          'blank_unchanged': True, 'consumer_regressions': regressions,
          'existing_underfull': before_warnings,
          'new_underfull': list((collections.Counter(after_warnings) - collections.Counter(before_warnings)).elements()),
          'main_pdf_sha256': hashlib.sha256((P / 'main.pdf').read_bytes()).hexdigest(),
          'style_sha256': full['style_sha256']}
(HERE / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
