"""固定方案训练与矿区级诊断。最终模型全部保存后才在官方验证集评分。"""
from __future__ import annotations
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import argparse,hashlib,json,time,platform,csv,random
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy import ndimage
import torch
from torch import nn
import torch.nn.functional as F

METRICS=['IoU','F1','precision','recall','FPR','small_recall']
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write_json(path,obj):Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
class Block(nn.Sequential):
    def __init__(self,n,m):
        super().__init__(nn.Conv2d(n,m,3,padding=1,bias=False),nn.GroupNorm(4,m),nn.ReLU(),nn.Conv2d(m,m,3,padding=1,bias=False),nn.GroupNorm(4,m),nn.ReLU())
class SiameseTiny(nn.Module):
    def __init__(self,base=16):
        super().__init__();self.e1=Block(3,base);self.e2=Block(base,2*base);self.e3=Block(2*base,4*base);self.d2=Block(6*base,2*base);self.d1=Block(3*base,base);self.head=nn.Conv2d(base,1,1)
    def encode(self,x):
        f1=self.e1(x);f2=self.e2(F.max_pool2d(f1,2));f3=self.e3(F.max_pool2d(f2,2));return f1,f2,f3
    def forward(self,a,b):
        fa=self.encode(a);fb=self.encode(b);ds=[abs(x-y) for x,y in zip(fa,fb)]
        z=self.d2(torch.cat([F.interpolate(ds[2],size=ds[1].shape[-2:],mode='nearest'),ds[1]],1));z=self.d1(torch.cat([F.interpolate(z,size=ds[0].shape[-2:],mode='nearest'),ds[0]],1));return self.head(z),fa[2],fb[2]
def consistency(fa,fb,y,arm):
    if arm=='none':return (fa.sum()+fb.sum())*0
    dist=(F.normalize(fa,dim=1,eps=1e-6)-F.normalize(fb,dim=1,eps=1e-6)).square().sum(1,keepdim=True)
    if arm=='full':mask=torch.ones_like(dist)
    elif arm=='background':
        bg=(y==0).float();bg=-F.max_pool2d(-F.pad(bg,(1,1,1,1),value=0),3,1);mask=1-F.adaptive_max_pool2d(1-bg,dist.shape[-2:])
    else:raise ValueError(arm)
    numerator=(dist*mask).flatten(1).sum(1);denominator=mask.flatten(1).sum(1);return (numerator/denominator.clamp_min(1)).mean()
def small_mask(y,max_area):
    labels,n=ndimage.label(y,structure=np.ones((3,3),dtype=np.uint8));sizes=np.bincount(labels.ravel());ids=np.flatnonzero((sizes>0)&(sizes<=max_area));ids=ids[ids!=0]
    boundary=np.unique(np.concatenate([labels[0],labels[-1],labels[:,0],labels[:,-1]]));ids=np.setdiff1d(ids,boundary);return np.isin(labels,ids)
def metric_counts(y,pred,sm):
    y=y.astype(bool);pred=pred.astype(bool)
    return dict(TP=int((y&pred).sum()),FP=int((~y&pred).sum()),FN=int((y&~pred).sum()),TN=int((~y&~pred).sum()),small_TP=int((sm&pred).sum()),small_total=int(sm.sum()))
def ratio(a,b):return float(a/b) if b else None
def metrics(c):
    tp,fp,fn,tn=[c[k] for k in ['TP','FP','FN','TN']]
    return {'IoU':ratio(tp,tp+fp+fn) if tp+fn else None,'F1':ratio(2*tp,2*tp+fp+fn) if tp+fn else None,'precision':ratio(tp,tp+fp),'recall':ratio(tp,tp+fn),'FPR':ratio(fp,fp+tn),'small_recall':ratio(c['small_TP'],c['small_total'])}
def load_cache(path):
    with np.load(path) as x:return {k:x[k].copy() for k in x.files}
def seed_all(seed):
    random.seed(seed);np.random.seed(seed);torch.manual_seed(seed);torch.cuda.manual_seed_all(seed);torch.backends.cudnn.benchmark=False;torch.backends.cudnn.deterministic=True;torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False;torch.use_deterministic_algorithms(True)
def train_all(cfg,cache,out,device,protocol_hash):
    data=load_cache(cache/'train.npz');a=torch.from_numpy(data['imageA']).permute(0,3,1,2).contiguous();b=torch.from_numpy(data['imageB']).permute(0,3,1,2).contiguous();y=torch.from_numpy(data['label'])[:,None]
    positives=int(y.sum());pixels=y.numel();assert 0<positives<pixels;weight=float(np.clip((pixels-positives)/positives,1,10));n=len(y)
    for seed in cfg['seeds']:
        for arm in cfg['arms']:
            run=out/f'{arm}_seed{seed}';run.mkdir(exist_ok=True);target=run/'model.pt'
            if target.exists():
                prior=json.loads((run/'training_summary.json').read_text());assert prior['protocol_sha256']==protocol_hash;print('already trained',run.name,flush=True);continue
            seed_all(seed);model=SiameseTiny(cfg['base_channels']).to(device);opt=torch.optim.AdamW(model.parameters(),lr=cfg['learning_rate'],weight_decay=cfg['weight_decay']);pos_weight=torch.tensor(weight,device=device)
            order_rng=torch.Generator().manual_seed(seed+1000);aug_rng=torch.Generator().manual_seed(seed+2000);start=time.monotonic();curve=[];max_mem=0
            initial_hash=hashlib.sha256(b''.join(v.detach().cpu().numpy().tobytes() for v in model.state_dict().values())).hexdigest()
            for epoch in range(cfg['epochs']):
                model.train();order=torch.randperm(n,generator=order_rng);acc=np.zeros(3);seen=0
                for indices in order.split(cfg['batch_size']):
                    xa=a[indices].to(device).float()/255;xb=b[indices].to(device).float()/255;yt=y[indices].to(device).float();flip=torch.rand((len(indices),2),generator=aug_rng)
                    for axis,dim in [(0,2),(1,3)]:
                        selected=flip[:,axis]<0.5
                        xa[selected]=xa[selected].flip(dim);xb[selected]=xb[selected].flip(dim);yt[selected]=yt[selected].flip(dim)
                    opt.zero_grad(set_to_none=True);logit,fa,fb=model(xa,xb);bce=F.binary_cross_entropy_with_logits(logit,yt,pos_weight=pos_weight);prob=logit.sigmoid();dice=1-((2*(prob*yt).flatten(1).sum(1)+1)/(prob.flatten(1).sum(1)+yt.flatten(1).sum(1)+1)).mean();seg=bce+dice;cons=consistency(fa,fb,yt,arm);loss=seg+cfg['consistency_weight']*cons
                    if not torch.isfinite(loss):raise ValueError('nonfinite loss')
                    loss.backward();opt.step();bs=len(indices);acc+=np.array([loss.item(),seg.item(),cons.item()])*bs;seen+=bs
                row={'epoch':epoch+1,'loss':float(acc[0]/seen),'segmentation_loss':float(acc[1]/seen),'consistency_loss':float(acc[2]/seen),'elapsed_seconds':time.monotonic()-start};curve.append(row);print(run.name,json.dumps(row),flush=True)
                write_json(run/'training_curve.json',curve)
            torch.cuda.synchronize();elapsed=time.monotonic()-start
            torch.save({'state_dict':model.cpu().state_dict(),'seed':seed,'arm':arm,'protocol_sha256':protocol_hash},target)
            write_json(run/'training_summary.json',{'seed':seed,'arm':arm,'samples':n,'epochs':cfg['epochs'],'pos_weight':weight,'seconds':elapsed,'initial_state_sha256':initial_hash,'checkpoint_sha256':sha(target),'protocol_sha256':protocol_hash,'parameters':sum(p.numel() for p in model.parameters()),'validation_used_for_selection':False,'final_training_loss':curve[-1]['loss']})
            del model,opt;torch.cuda.empty_cache()
    for seed in cfg['seeds']:
        hs=[json.loads((out/f'{arm}_seed{seed}/training_summary.json').read_text())['initial_state_sha256'] for arm in cfg['arms']];assert len(set(hs))==1

def evaluate_all(cfg,cache,out,device):
    d=load_cache(cache/'val.npz');labels=d['label'].astype(bool);small=np.stack([small_mask(y,cfg['small_component_max_pixels']) for y in labels]);domains=d['domain'];sites=sorted(set(domains.tolist()));all_rows=[];summaries=[]
    for seed in cfg['seeds']:
        for arm in cfg['arms']:
            run=out/f'{arm}_seed{seed}';model=SiameseTiny(cfg['base_channels']).to(device);checkpoint=torch.load(run/'model.pt',map_location='cpu',weights_only=True);model.load_state_dict(checkpoint['state_dict']);model.eval();parts=[]
            with torch.no_grad():
                for start in range(0,len(labels),cfg['batch_size']):
                    a=torch.from_numpy(d['imageA'][start:start+cfg['batch_size']]).permute(0,3,1,2).to(device).float()/255;b=torch.from_numpy(d['imageB'][start:start+cfg['batch_size']]).permute(0,3,1,2).to(device).float()/255;p=model(a,b)[0].sigmoid()[:,0].cpu().numpy();parts.append(p)
            probabilities=np.concatenate(parts);pred=probabilities>=cfg['threshold'];np.savez_compressed(run/'validation_predictions.npz',probability=probabilities,prediction=pred,row_index=d['row_index'],domain=domains)
            per_site=[]
            for site in sites:
                idx=domains==site;c=metric_counts(labels[idx],pred[idx],small[idx]);row={'arm':arm,'seed':seed,'domain':site,'tiles':int(idx.sum()),**c,**metrics(c)};all_rows.append(row);per_site.append(row)
            summary={'arm':arm,'seed':seed}
            for m in METRICS:
                v=[x[m] for x in per_site if x[m] is not None];summary[m]=float(np.mean(v)) if v else None;summary[m+'_valid_sites']=len(v)
            summaries.append(summary);write_json(run/'validation_metrics.json',{'per_site':per_site,'macro':summary});print('VALIDATION',json.dumps(summary),flush=True);del model;torch.cuda.empty_cache()
    write_json(out/'per_site_metrics.json',all_rows);write_json(out/'seed_macro_metrics.json',summaries)
    with (out/'per_site_metrics.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(all_rows[0]));w.writeheader();w.writerows(all_rows)
    contrast=[]
    for control in ['full','none']:
        for metric in METRICS:
            differences=[];valid=[]
            for site in sites:
                values={arm:[x[metric] for x in all_rows if x['domain']==site and x['arm']==arm] for arm in ['background',control]}
                if any(any(v is None for v in vs) for vs in values.values()):continue
                differences.append(float(np.mean(values['background'])-np.mean(values[control])));valid.append(site)
            if differences:
                v=np.array(differences);rng=np.random.default_rng(cfg['bootstrap_seed']);resampled=v[rng.integers(0,len(v),size=(cfg['bootstrap_repeats'],len(v)))].mean(1);low,high=np.quantile(resampled,[.025,.975]);row={'contrast':'background - '+control,'metric':metric,'valid_sites':valid,'n':len(v),'mean_difference':float(v.mean()),'ci_low':float(low),'ci_high':float(high),'site_differences':differences}
            else:row={'contrast':'background - '+control,'metric':metric,'valid_sites':[],'n':0,'mean_difference':None,'ci_low':None,'ci_high':None,'site_differences':[]}
            contrast.append(row)
    write_json(out/'paired_site_contrasts.json',contrast)
    aggregate=[]
    for arm in cfg['arms']:
        row={'arm':arm,'seeds':cfg['seeds']}
        for m in METRICS:
            vals=[x[m] for x in summaries if x['arm']==arm and x[m] is not None];row[m]={'mean':float(np.mean(vals)) if vals else None,'seed_std':float(np.std(vals,ddof=1)) if len(vals)>1 else None}
        aggregate.append(row)
    write_json(out/'aggregate_metrics.json',aggregate)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cache-dir',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--protocol',type=Path,default=Path(__file__).with_name('protocol.json'));ap.add_argument('--device',default='cuda');ap.add_argument('--train-only',action='store_true');ap.add_argument('--evaluate-only',action='store_true');args=ap.parse_args();cfg=json.loads(args.protocol.read_text());out=args.output_dir;out.mkdir(parents=True,exist_ok=True);torch.set_num_threads(4)
    device=torch.device(args.device);assert device.type=='cuda' and torch.cuda.is_available();protocol_hash=sha(args.protocol);selection=json.loads((args.cache_dir/'selection.json').read_text());assert selection['protocol_sha256']==protocol_hash
    freeze={'protocol':cfg,'protocol_sha256':protocol_hash,'code_sha256':sha(__file__),'selection_sha256':sha(args.cache_dir/'selection.json'),'train_cache_sha256':sha(args.cache_dir/'train.npz'),'validation_cache_sha256':sha(args.cache_dir/'val.npz'),'started_at':datetime.now(timezone.utc).isoformat(),'environment':{'python':platform.python_version(),'torch':torch.__version__,'cuda':torch.version.cuda,'GPU':torch.cuda.get_device_name(device),'visible_devices':os.environ.get('CUDA_VISIBLE_DEVICES'),'precision':'float32; TF32 off','deterministic_algorithms':True}}
    f=out/'frozen_protocol.json'
    if f.exists():
        prior=json.loads(f.read_text());assert all(prior[k]==freeze[k] for k in ['protocol_sha256','code_sha256','selection_sha256','train_cache_sha256','validation_cache_sha256'])
    else:write_json(f,freeze)
    if not args.evaluate_only:train_all(cfg,args.cache_dir,out,device,protocol_hash)
    if not args.train_only:evaluate_all(cfg,args.cache_dir,out,device)
    print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
if __name__=='__main__':main()
