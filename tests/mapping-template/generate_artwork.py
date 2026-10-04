"""一次性提取官方固定标签；生成原生 TeX，不参与项目构建。"""
from pathlib import Path
import pymupdf as fitz
ROOT=Path('../..').resolve()
DOC=fitz.open(ROOT/'projects/NSFC_2027_Mapping_final/测绘科学与工程自然资源部重点实验室.pdf')
NAMES=['Cover','Instructions','Information','Members','Budget','Proposal','Foundation','Commitment','Review','Attachments']
FONTS={'SimSun':r'\CasmSong','SimHei':r'\CasmHei','KaiTi':r'\CasmKai','FangSong':r'\CasmFang','TimesNewRomanPSMT':r'\CasmTimes','TimesNewRomanPS-BoldMT':r'\CasmTimes\bfseries'}
def esc(s):
 return ''.join({'\\':r'\textbackslash{}','%':r'\%','&':r'\&','#':r'\#','_':r'\_','{':r'\{','}':r'\}','$':r'\$','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in s)
output=['% 官方 PDF 固定表头、说明与表格矢量坐标（bp）；无 PDF/图片运行时依赖。']
for i,p in enumerate(DOC):
 output.append(r'\newcommand{\Casm'+NAMES[i]+r'Artwork}{%')
 for d in p.get_drawings():
  if d['rect'].y0<60: continue
  for it in d['items']:
   if it[0]=='l':
    a,b=it[1:3]; output.append(fr'  \CasmLine{{{d["width"]:.2f}}}{{{a.x:.2f}}}{{{a.y:.2f}}}{{{b.x:.2f}}}{{{b.y:.2f}}}%')
   elif it[0]=='re':
    r=it[1]; output.append(fr'  \fill ({r.x0:.2f},{r.y0:.2f}) rectangle ({r.x1:.2f},{r.y1:.2f});')
 bold_points={(round(c[2][0],1),round(c[2][1],1)) for t in p.get_texttrace() if t['type']==1 for c in t['chars']}
 for b in p.get_text('rawdict')['blocks']:
  for l in b.get('lines',[]):
   for s in l['spans']:
    x,y=s['origin']; chars=s['chars']; txt=''.join(c['c'] for c in chars)
    if not txt.strip() or y<60 or y>770 or (i==3 and y>535): continue
    if i in (5,6) and y>100: continue
    if i==7 and (140<y<280 or 489<y<580): continue
    if i==9 and y>100: continue
    if i==2 and y>542: continue
    font=FONTS[s['font']]
    if (round(x,1),round(y,1)) in bold_points and 'bfseries' not in font: font+=r'\bfseries'
    color=fr'\color[HTML]{{{s["color"]:06X}}}' if s['color'] else ''
    # WPS 为均匀分布的字段标签插入额外字距，按连续字串拆开，仍保留可编辑文字。
    groups=[]; start=0
    for j in range(1,len(chars)):
     gap=chars[j]['origin'][0]-chars[j-1]['bbox'][2]
     if gap>1.0:
      groups.append(chars[start:j]); start=j
    groups.append(chars[start:])
    lines=[]
    for group in groups:
     tx=''.join(c['c'] for c in group)
     if not tx.strip(): continue
     gx,gy=group[0]['origin']
     lines.append(fr'  \CasmText{{{gx:.2f}}}{{{gy:.2f}}}{{{s["size"]:.2f}}}{{{font}{color} {esc(tx)}}}%')
    key=None
    if i==2 and x>165:
     if 397<y<420: key='direction'
     elif 435<y<441: key='period'
     elif 461<y<467: key='category'
     elif 487<y<493: key='funding'
    if key: output.append(fr'  \CasmIfEmpty{{{key}}}{{%'); output.extend(lines); output.append('  }{}%')
    else: output.extend(lines)
 output.append('}\n')
(ROOT/'packages/bensz-thesis/styles/bthesis-artwork-casm-open-fund-2026.tex').write_text('\n'.join(output)+'\n')
print('artwork',len(output),'lines')
