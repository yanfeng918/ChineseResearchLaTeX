"""Freeze illustrative examples before opening any validation predictions."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--cache-dir', type=Path, required=True)
a = p.parse_args()
with np.load(a.cache_dir / 'val.npz') as d:
    rows = []
    for site in sorted(set(d['domain'].tolist()))[:3]:
        candidates = np.flatnonzero((d['domain'] == site) & (d['label'].sum((1, 2)) > 0))
        i = int(candidates[0] if len(candidates) else np.flatnonzero(d['domain'] == site)[0])
        rows.append({'index': i, 'domain': site, 'row_index': int(d['row_index'][i])})
result = {'rule': '验证矿区名称字典序前3个；每矿区取按原始行号排序的第一个有变化标签切片，无变化则取第一个；采用预定首种子17，不按预测效果选案例', 'created_at': datetime.now(timezone.utc).isoformat(), 'cases': rows}
(a.cache_dir / 'qualitative_selection.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
