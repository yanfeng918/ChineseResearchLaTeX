"""Official builds against fixed consumer sources; before/after pixel comparison."""
import concurrent.futures
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TOOL = ROOT / 'packages/bensz-thesis/scripts/thesis_project_tool.py'
phase = sys.argv[1]
scope = json.loads((HERE / 'regression-scope.json').read_text())

def run(row):
    fixture = HERE / row['fixture']
    out = HERE / 'regression' / fixture.name
    out.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, str(TOOL), 'build', '--project-dir', str(fixture)]
    p = subprocess.run(command, cwd=HERE, capture_output=True, text=True)
    (out / f'{phase}-build.log').write_text(p.stdout + p.stderr)
    result = {'project': row['project'], 'exit': p.returncode}
    if p.returncode == 0:
        shutil.copy2(fixture / 'main.pdf', out / f'{phase}.pdf')
        shutil.copy2(fixture / '.latex-cache/main.log', out / f'{phase}-latex.log')
        if phase == 'after':
            q = subprocess.run([sys.executable, str(TOOL), 'compare', '--project-dir', str(fixture),
                '--baseline-pdf', str(out / 'before.pdf'), '--output-dir', str(out / 'compare')],
                cwd=HERE, capture_output=True, text=True)
            (out / 'compare.log').write_text(q.stdout + q.stderr)
            result['compare_exit'] = q.returncode
    print(result, flush=True)
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(run, scope))
(HERE / f'regression-{phase}.json').write_text(json.dumps(results, indent=2) + '\n')
sys.exit(any(r['exit'] for r in results))
