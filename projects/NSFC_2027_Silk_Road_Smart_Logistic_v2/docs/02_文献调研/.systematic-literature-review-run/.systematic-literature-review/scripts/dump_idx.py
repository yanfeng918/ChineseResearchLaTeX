import json,sys,re
rows=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8')]
idxs=json.load(open(sys.argv[2]))
a,b=int(sys.argv[3]),int(sys.argv[4])
for i in idxs[a:b]:
    r=rows[i]
    ab=re.sub(r'\s+',' ',(r.get('abstract') or '')).strip()
    ab=(ab[:240]+'…') if len(ab)>240 else (ab or '[无摘要]')
    print(f"[{i}] {r.get('year')}|{(r.get('venue') or '')[:32]}|{(r.get('title') or '')[:130]}|{ab}")
