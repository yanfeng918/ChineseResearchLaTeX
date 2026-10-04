"""Snapshot existing work; discover consumers and the source's active input tree."""
import hashlib
import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'projects/NSFC_2026_CIESM-STSR'
TARGET = ROOT / 'projects/NSFC_2026_CIESM-STSR_final'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)

def walk(path, seen=None):
    seen = set() if seen is None else seen
    if path in seen:
        return []
    seen.add(path)
    text = uncomment(path.read_text())
    rows = [{'path': str(path.relative_to(SOURCE)), 'sha256': sha(path),
             'graphics': re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', text),
             'labels': re.findall(r'\\label\{([^}]+)\}', text),
             'references': re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text),
             'citations': re.findall(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}', text)}]
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
        child = SOURCE / name
        if not child.suffix:
            child = child.with_suffix('.tex')
        if child.exists():
            rows += walk(child, seen)
    return rows

inventory = walk(SOURCE / 'main.tex')
figures = []
for row in inventory:
    for name in row['graphics']:
        figures.append({'path': name, 'source': row['path'], 'sha256': sha(SOURCE / name)})
(HERE / 'resource-inventory-before.json').write_text(json.dumps(
    {'inputs': inventory, 'figures': figures}, ensure_ascii=False, indent=2) + '\n')

consumers = []
for project in sorted((ROOT / 'projects').iterdir()):
    if not project.is_dir():
        continue
    refs = []
    for path in project.rglob('*.tex'):
        if any(x.startswith('.') for x in path.relative_to(project).parts):
            continue
        if re.search(r'\\(?:usepackage|RequirePackage)(?:\[[^]]*\])?\{[^}]*bensz-thesis[^}]*\}', uncomment(path.read_text(errors='replace'))):
            refs.append(str(path.relative_to(ROOT)))
    if refs:
        dest = HERE / 'fixtures' / project.name
        shutil.copytree(project, dest, ignore=shutil.ignore_patterns('.latex-cache', '.git'), dirs_exist_ok=False)
        consumers.append({'project': str(project.relative_to(ROOT)), 'references': refs,
                          'fixture': str(dest.relative_to(HERE))})
(HERE / 'regression-scope.json').write_text(json.dumps(consumers, ensure_ascii=False, indent=2) + '\n')
shutil.copytree(ROOT / 'packages/bensz-thesis', HERE / 'package-before')
print(f'Snapshotted {len(consumers)} actual consumers; {len(figures)} active figures.')
