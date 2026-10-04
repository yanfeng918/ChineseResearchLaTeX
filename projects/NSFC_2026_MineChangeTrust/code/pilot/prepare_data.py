"""从官方Parquet裁切版选定可追溯的矿区子样本；不读取测试影像。"""
from __future__ import annotations
import argparse,hashlib,io,json,csv
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import pyarrow.parquet as pq
from PIL import Image

def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def image_bytes(cell):
    if cell.get('bytes') is None:raise ValueError('Only embedded public image bytes are supported.')
    return cell['bytes']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--protocol',type=Path,default=Path(__file__).with_name('protocol.json'));a=ap.parse_args()
    a.output_dir.mkdir(parents=True,exist_ok=True);cfg=json.loads(a.protocol.read_text());files={s:sorted(a.data_dir.glob(s+'-*.parquet')) for s in ['train','val']};assert len(files['train'])==3 and len(files['val'])==1
    domain_rows={};offsets={};counts={}
    for split,paths in files.items():
        domains=[];off=[]
        for f in paths:
            x=pq.read_table(f,columns=['domain']).column('domain').to_pylist();off.append((f,len(domains),len(x)));domains.extend(x)
        domain_rows[split]={d:np.flatnonzero(np.asarray(domains)==d).tolist() for d in sorted(set(domains))};offsets[split]=off;counts[split]=len(domains)
    train_domains=set(domain_rows['train']);val_domains=set(domain_rows['val']);assert len(train_domains)==60 and len(val_domains)==10 and not train_domains&val_domains
    ranked=sorted(train_domains,key=lambda d:digest('mct-pilot-split-v1|'+d));selected_sites=set(ranked[:50]);heldout=ranked[50:];selections={};manifest=[]
    for split in ['train','val']:
        k=cfg['train_tiles_per_site'] if split=='train' else cfg['validation_tiles_per_site'];eligible=selected_sites if split=='train' else val_domains
        chosen=[]
        for d in sorted(eligible):
            indices=domain_rows[split][d];order=sorted(indices,key=lambda i:digest(cfg['sampling_salt']+'|'+split+'|'+d+'|'+str(i)))
            chosen.extend(order[:k])
        selections[split]=set(chosen)
    # Selection is written before image/label decoding or any model computation.
    selection={'protocol_sha256':hashlib.sha256(a.protocol.read_bytes()).hexdigest(),'selected_train_domains':sorted(selected_sites),'reserved_train_domains':heldout,'validation_domains':sorted(val_domains),'official_counts':counts,'domain_counts':{s:{d:len(v) for d,v in m.items()} for s,m in domain_rows.items()},'selected_indices':{s:sorted(v) for s,v in selections.items()},'created_at':datetime.now(timezone.utc).isoformat()}
    (a.output_dir/'selection.json').write_text(json.dumps(selection,indent=2)+'\n')
    for split in ['train','val']:
        records=[]
        for f,offset,n in offsets[split]:
            wanted=sorted(i-offset for i in selections[split] if offset<=i<offset+n)
            if not wanted:continue
            table=pq.read_table(f).take(wanted)
            for local,row in zip(wanted,table.to_pylist()):
                raw=[image_bytes(row[k]) for k in ['imageA','imageB','label']];ims=[Image.open(io.BytesIO(x)) for x in raw];x1=np.array(ims[0].convert('RGB'));x2=np.array(ims[1].convert('RGB'));label=np.array(ims[2])
                if label.ndim==3:
                    assert np.all(label==label[...,:1]);label=label[...,0]
                assert x1.shape==x2.shape==(256,256,3) and label.shape==(256,256)
                values=set(np.unique(label).tolist());assert values<={0,1,255},values
                y=(label>0).astype(np.uint8);idx=offset+local
                item={'split':split,'domain':row['domain'],'global_row_index':idx,'source_shard':f.name,'row_in_shard':local,'imageA_source_path':row['imageA'].get('path'),'imageB_source_path':row['imageB'].get('path'),'label_source_path':row['label'].get('path'),'imageA_sha256':hashlib.sha256(raw[0]).hexdigest(),'imageB_sha256':hashlib.sha256(raw[1]).hexdigest(),'label_sha256':hashlib.sha256(raw[2]).hexdigest(),'label_values':sorted(values),'positive_pixels':int(y.sum())}
                records.append((idx,x1,x2,y,row['domain'],item))
        records.sort(key=lambda x:x[0]);assert len(records)==len(selections[split])
        np.savez_compressed(a.output_dir/(split+'.npz'),imageA=np.stack([x[1] for x in records]),imageB=np.stack([x[2] for x in records]),label=np.stack([x[3] for x in records]),domain=np.array([x[4] for x in records]),row_index=np.array([x[0] for x in records]))
        manifest.extend(x[5] for x in records);print(split,len(records),'sites',len(set(x[4] for x in records)),flush=True)
    pair_sets={s:{tuple(sorted((x['imageA_sha256'],x['imageB_sha256']))) for x in manifest if x['split']==s} for s in ['train','val']};overlap=pair_sets['train']&pair_sets['val'];assert not overlap,overlap
    with (a.output_dir/'sample_manifest.jsonl').open('w') as out:
        for row in manifest:out.write(json.dumps(row)+'\n')
    audit={'samples':{s:sum(x['split']==s for x in manifest) for s in ['train','val']},'positive_pixels':{s:sum(x['positive_pixels'] for x in manifest if x['split']==s) for s in ['train','val']},'exact_image_pair_overlap_train_val':len(overlap),'duplicate_pairs_within_split':{s:sum(x['split']==s for x in manifest)-len(pair_sets[s]) for s in ['train','val']},'image_shape':[256,256,3],'mask_shape':[256,256],'test_images_read':0,'claims':'矿区ID与字节重复审计不替代地理邻近及配准质量专业核验'}
    (a.output_dir/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print(json.dumps(audit,ensure_ascii=False))
if __name__=='__main__':main()
