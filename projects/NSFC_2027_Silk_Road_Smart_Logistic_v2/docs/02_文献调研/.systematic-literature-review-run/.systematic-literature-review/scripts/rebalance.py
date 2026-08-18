import json,sys,collections
ART=sys.argv[1]; TARGET=115; FLOOR=8
rows=[json.loads(l) for l in open(f"{ART}/scored_papers_跨境物流弱网感知与数字镜像.jsonl",encoding='utf-8')]
pool=[r for r in rows if r['score']>=5 and r['abstract_ok'] and r.get('subtopic')]
by=collections.defaultdict(list)
for r in pool: by[r['subtopic']].append(r)
for k in by: by[k].sort(key=lambda r:-r['score'])
sel=[]; used=set()
# 1) 每个子主题保底
for k,v in by.items():
    for r in v[:FLOOR]:
        if r['doi'] not in used: sel.append(r); used.add(r['doi'])
# 2) 其余按分数补足
rest=sorted([r for r in pool if r['doi'] not in used], key=lambda r:-r['score'])
for r in rest:
    if len(sel)>=TARGET: break
    sel.append(r); used.add(r['doi'])
sel.sort(key=lambda r:(-r['score'], r.get('year') or 0))
with open(f"{ART}/selected_papers_跨境物流弱网感知与数字镜像.jsonl",'w',encoding='utf-8') as f:
    for r in sel: f.write(json.dumps(r,ensure_ascii=False)+"\n")
c=collections.Counter(r['subtopic'] for r in sel)
print(f"再平衡选中 {len(sel)} 篇（保底 {FLOOR}/子主题）")
for k,v in sorted(c.items(),key=lambda x:-x[1]): print(f"  {k}: {v}")
print("平均分 %.2f"%(sum(r['score'] for r in sel)/len(sel)))
