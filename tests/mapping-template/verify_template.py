"""真实填写、长正文、错误输入与同包项目隔离回归；仅写 tests/mapping-template。"""
from pathlib import Path
import json,re,shutil,subprocess,sys
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
PROJECT=ROOT/'projects/NSFC_2027_Mapping_final'
TOOL=ROOT/'packages/bensz-thesis/scripts/thesis_project_tool.py'

def run(project,name,expect=True):
 r=subprocess.run([sys.executable,str(TOOL),'build','--project-dir',str(project)],capture_output=True,text=True)
 (OUT/f'{name}.log').write_text(r.stdout+r.stderr)
 log=(project/'.latex-cache/main.log').read_text(errors='replace')
 warnings=[l for l in log.splitlines() if any(k in l for k in ('Warning','Overfull','Underfull','Missing character'))]
 result={'success':r.returncode==0,'returncode':r.returncode,'warnings':warnings}
 if expect:
  assert r.returncode==0, name+': '+(r.stdout+r.stderr)[-2000:]
  with fitz.open(project/'main.pdf') as doc: result['pages']=len(doc)
 print(name,result,flush=True)
 return result

def copy(name):
 dest=OUT/'cases'/name
 shutil.copytree(PROJECT,dest,dirs_exist_ok=True,ignore=shutil.ignore_patterns('.latex-cache','*.pdf'))
 return dest

report={'target':run(PROJECT,'target')}
with fitz.open(PROJECT/'main.pdf') as doc:
 assert len(doc)==10
 assert doc[3].rect.width>doc[3].rect.height
 assert all(p.rect.width<p.rect.height for i,p in enumerate(doc) if i!=3)
 assert all(not p.get_images() for p in doc), 'Must render native text and rules'
 assert [doc[i].get_text().splitlines()[-1] for i in range(2,10)]==list(map(str,range(1,9)))
 assert len(doc[5].get_text())>250

p=copy('filled-and-long')
with (p/'extraTex/metadata.tex').open('a') as s:
 s.write(r'''
\CasmSetup{title={多源遥感变化检测与不确定性量化方法研究},title-en={Multi-source change detection and uncertainty quantification},
 applicant={测试甲},organization={测试研究单位},sex={女},birth={1990.01},ethnicity={汉族},degree={博士},
 professional-title={副研究员},work-months={6},phone={010-12345678},email={test@example.org},
 fax={010-12345678},country={中国},address={测试市测试区测试路一号},research-area={遥感测绘},
 direction={全域遥感与智能处理},period={2026 年 11 月 1 日—2027 年 10 月 31 日},category={一般课题},
 funding={5.00 万元},keywords={变化检测；不确定性}}
''')
(p/'extraTex/abstract.tex').write_text('摘要填写测试。'+ '本研究面向遥感测绘，研究变化检测与不确定性表达方法。'*10)
(p/'extraTex/members.tex').write_text('\n'.join(r'\CasmMember{' + str(i) + r'}{member-name={测试乙},member-sex={男},member-degree={博士},member-birth={1991.01},member-age={35},member-title={副研究员},member-unit={测试研究单位},member-task={方法验证}}' for i in (1,10))+r'\CasmMemberTotals{2}{2}{0}{0}{0}{2}{0}')
(p/'extraTex/budget.tex').write_text(r'\CasmBudgetTotals{5.00}{5.00}{5.00}'+'\n'+'\n'.join(fr'\CasmBudgetRow{{{i}}}{{0.00}}' for i in range(1,16)))
(p/'extraTex/budget-basis.tex').write_text('按实际任务测算差旅、材料和劳务支出，金额与明细逐项核对。')
paragraph='这是用于检验模板自动分页的测试正文。研究内容围绕测绘遥感方法、实验设计与验证流程展开，包含普通中文及 English 2026。'
with (p/'extraTex/proposal.tex').open('a') as s:
 for i in range(80): s.write(f'\n\n第{i+1}段。'+paragraph*2+'\n')
 s.write('\n\n正文终点标记。\n')
report['filled_and_long']=run(p,'filled-and-long')
with fitz.open(p/'main.pdf') as doc:
 texts=[x.get_text() for x in doc]; full=''.join(texts)
 for term in ['测试甲','测试乙','test@example.org','正文终点标记','按实际任务测算']: assert term in full,term
 assert len(doc)>10
 body_pages=[page for page in doc if '这是用于检验' in page.get_text()]
 assert len(body_pages)>2
 for page in body_pages:
  assert '四、立项依据与研究内容' in page.get_text()
  assert len(page.get_drawings())>=5
  assert page.rect.width<page.rect.height
 report['filled_and_long']['research_pages']=len(body_pages)
 assert [x.splitlines()[-1] for x in texts[2:]]==list(map(str,range(1,len(doc)-1)))
 assert not report['filled_and_long']['warnings']

p=copy('overflow')
(p/'extraTex/metadata.tex').write_text('\\CasmSetup{title={'+('超长字段'*90)+'}}')
report['overflow']=run(p,'overflow',False)
assert not report['overflow']['success']
assert 'Fixed form cell overflow' in (OUT/'overflow.log').read_text()
p=copy('bad-row'); (p/'extraTex/members.tex').write_text(r'\CasmMember{11}{member-name={测试}}')
report['bad_row']=run(p,'bad-row',False)
assert not report['bad_row']['success']
assert 'Member row must be' in (OUT/'bad-row.log').read_text()

plan=json.loads((OUT/'regression-plan.json').read_text())
# 共享工作区可能同时修改其它 profile。冻结两份包，仅移除控制组的 CASM 新文件，
# 对同份项目源码验证本任务的增量；不将其它任务尚未刷新的磁盘 PDF 当成回归结论。
full_package=OUT/'package-snapshot/bensz-thesis'
control_package=OUT/'package-control/bensz-thesis'
for package in (full_package,control_package):
 shutil.copytree(ROOT/'packages/bensz-thesis',package,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 fonts=package.parent/'bensz-fonts'
 if not fonts.exists(): fonts.symlink_to(ROOT/'packages/bensz-fonts',target_is_directory=True)
for path in list(control_package.glob('profiles/*casm*'))+list(control_package.glob('styles/*casm*')):
 path.unlink()
TOOL=full_package/'scripts/thesis_project_tool.py'
control_tool=control_package/'scripts/thesis_project_tool.py'
report['regressions']={}
for item in plan['actual_projects']:
 name=item['project']; p=OUT/'regression-rerun'/name
 shutil.copytree(ROOT/'projects'/name,p,dirs_exist_ok=True,ignore=shutil.ignore_patterns('.latex-cache','.git','docs','review'))
 if (p/'main.pdf').exists(): shutil.copy2(p/'main.pdf',p/'before.pdf')
 result=run(p,'regression-'+name)
 shutil.copy2(p/'main.pdf',p/'candidate.pdf')
 r=subprocess.run([sys.executable,str(control_tool),'build','--project-dir',str(p)],capture_output=True,text=True)
 (OUT/f'control-{name}.log').write_text(r.stdout+r.stderr); assert r.returncode==0
 control_log=(p/'.latex-cache/main.log').read_text(errors='replace')
 control_warnings=[l for l in control_log.splitlines() if any(k in l for k in ('Warning','Overfull','Underfull','Missing character'))]
 normalize=lambda lines: [re.sub(r'in font.*', 'in font [shared font path]', line) for line in lines]
 assert normalize(control_warnings)==normalize(result['warnings']), name + ': new build warnings'
 result['control_warning_count']=len(control_warnings)
 result['new_warnings']=[]
 r=subprocess.run([sys.executable,str(TOOL),'compare','--project-dir',str(p),'--baseline-pdf',str(p/'candidate.pdf'),'--output-dir',str(OUT/'regression-control-diff'/name)],capture_output=True,text=True)
 comp=json.loads((OUT/'regression-control-diff'/name/'compare-report.json').read_text())
 result['identical']=comp['identical']; result['comparison']='同份项目源码、冻结包副本：加载完整包 vs 移除本任务新增 CASM profile/style/artwork 的控制包'
 assert comp['identical'], name + ': CASM addition changed another profile'
 report['regressions'][name]=result
(OUT/'verification-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Verification complete',flush=True)
