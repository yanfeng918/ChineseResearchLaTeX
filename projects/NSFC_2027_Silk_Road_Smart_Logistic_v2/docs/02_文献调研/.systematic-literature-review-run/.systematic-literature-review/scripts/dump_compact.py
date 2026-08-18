import json,sys,re
p=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
rows=[json.loads(l) for l in open(p,encoding='utf-8')]
for i,r in enumerate(rows):
    if not (a<=i<b): continue
    ab=re.sub(r'\s+',' ',(r.get('abstract') or '')).strip()
    ab=ab[:280]+('…' if len(ab)>280 else '') or '[无摘要]'
    ven=(r.get('venue') or '')[:38]
    print(f"[{i}] {r.get('year')} | {ven}\nT: {(r.get('title') or '')[:150]}\nA: {ab}\nD: {r.get('doi') or 'NO-DOI'}\n")
