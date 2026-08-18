import json,re,sys
src=sys.argv[1]
rows=[json.loads(l) for l in open(src,encoding='utf-8')]
BIO=re.compile(r'extracellular vesicle|exosome|\bRNA\b|drug delivery|nanoparticle|nanocarrier|\bprotein\b|tumou?r|neurodegener|gene therapy|vaccine|\bcancer\b|autophag|lysosom|mitochondri|synap|peptide|antibod|in vivo|mice|clinical trial|patient',re.I)
CRY=re.compile(r'watermark|steganog|image authentication|NoSQL|digital signature.*audio|electronic health record|forensic',re.I)
STD=re.compile(r'^(air cargo equipment|insulated air cargo container|pallet lift truck|fire resistant container|temperature controlled container|tamper evident (composite|plastic|metal) container closure)',re.I)
LOGI=re.compile(r'logistic|freight|supply chain|container|shipping|\bport\b|warehouse|transport|truck|vehicle|cold chain|customs|parcel|package|yard|terminal|cargo',re.I)
TECH=re.compile(r'IoT|internet of things|sensor|wireless|edge comput|LoRa|NB-IoT|LPWAN|delay.tolerant|DTN|digital twin|synchroni|latency|energy|low.power|duty cycl|stream process|out.of.order|watermark.*stream|fusion|anomaly|deep learning|CNN|calibrat|uncertainty|RFID|telematic',re.I)
buckets={'drop':[],'review':[]}
for i,r in enumerate(rows):
    t=(r.get('title') or ''); ab=(r.get('abstract') or ''); blob=t+' '+ab
    drop=None
    if STD.search(t.strip()): drop='航空/包装行业标准条目，非研究文献'
    elif BIO.search(blob) and not LOGI.search(t): drop='生物医学领域歧义召回（cargo=分子货物）'
    elif CRY.search(blob) and not LOGI.search(t): drop='数字水印/取证领域歧义召回（tamper=数据篡改）'
    elif not LOGI.search(blob) and not TECH.search(blob): drop='与主题无技术或应用交集'
    if drop: buckets['drop'].append((i,r,drop))
    else: buckets['review'].append((i,r))
print(f"总计 {len(rows)}  自动低分 {len(buckets['drop'])}  待精读 {len(buckets['review'])}")
json.dump([{'idx':i,'doi':r.get('doi'),'reason':d} for i,r,d in buckets['drop']],open(sys.argv[2],'w'),ensure_ascii=False)
json.dump([i for i,_ in buckets['review']],open(sys.argv[3],'w'))
