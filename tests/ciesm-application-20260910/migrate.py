"""One-time, assertion-guarded migration of the preserved working manuscript."""
import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
S = ROOT / 'projects/NSFC_2026_CIESM-STSR'
P = ROOT / 'projects/NSFC_2026_CIESM-STSR_final'
E = P / 'extraTex'
assert not (P / 'blank.tex').exists(), 'Migration already applied'

config = E / '@config.tex'
config.write_text(config.read_text() + r'''
\ifdefined\CiesmBlankTemplate
  \CiesmBlanktrue
\else
  \CiesmApplicationMode
\fi
''')
main = P / 'main.tex'
main.write_text(main.read_text().replace(r'\input{extraTex/metadata}',
    '\\input{extraTex/metadata}\n\\addbibresource{references/myexample.bib}'))
(P / 'blank.tex').write_text(r'''% !TeX program = xelatex
% 独立空白入口：不读取申请人、摘要或研究正文。
\documentclass[UTF8,fontset=none,zihao=-4]{ctexart}
\def\CiesmBlankTemplate{1}
\input{extraTex/@config}
\CiesmSetup{
  birth-date={\hspace{1em}年\hspace{1em}月\hspace{1em}日},
  start-year={2027},start-month={1},start-day={1},
  end-year={2027},end-month={12},end-day={31},
  issuer={清华大学科研院},issue-date={二〇二六年八月}}
\begin{document}
\CiesmMakeCover
\CiesmMakeInformation
\input{extraTex/report}
\clearpage
\input{extraTex/budget}
\end{document}
''')

(E / 'metadata.tex').write_text(r'''% 本项目字段唯一入口。来自共用申请人资料（2026-09-10）和原项目事实库。
% 公开来源的待终核状态见 ../填写说明.md；不迁入无对应栏目的证件号码。
\CiesmSetup{
  special-name={P02：算法或数据集},
  title={面向新疆复杂地形的CIESM关键气象场多变量时空超分辨率与物理一致性校正研究},
  applicant={颜丰}, institution={新疆大学}, unit-count={}, sex={男},
  birth-date={1990年11月\hspace{.5em}日},
  professional-title={副教授}, degree={博士}, mentor={硕士研究生导师},
  faculty={计算机科学与技术学院（网络空间安全学院）},
  address={新疆乌鲁木齐市水磨沟区华瑞街777号新疆大学计算机科学与技术学院},
  email={yf@xju.edu.cn}, english-name={Feng Yan},
  talent={新疆大学高层次优秀青年 A 类博士引进人才},
  office={计算机学院 B201}, homepage={https://yanfeng918.github.io/},
  education={2019.09—2023.08，新疆大学，计算机科学与技术，博士。\par
    2012.09—2014.06，上海海事大学，计算机技术，硕士。\par
    2008.09—2012.06，海南热带海洋学院，生态学，学士。},
  employment={2023.12—至今，新疆大学，副教授。\par
    2023.10—2023.12，新疆大学，教学与科研工作。\par
    2018.03—2019.08，浙江大学山东工业技术研究院，科研与技术工作。\par
    2016.10—2017.12，上海中科软科技有限公司，软件技术工作。},
  start-year={2027}, start-month={1}, start-day={1},
  end-year={2027}, end-month={12}, end-day={31},
  total-budget={},
  expected-results={算法、可复现流程与区域试验数据产品各1套；\newline
    论文发表或接收不少于1篇，完成CIESM集成与应用验证。},
  keywords={CIESM；时空超分辨率；多变量耦合；物理一致性；复杂地形},
  issuer={清华大学科研院}, issue-date={二〇二六年八月}
}
''')
# Read the authorized contact field without printing it or copying the ID field.
facts = (ROOT / 'docs/applicants/yan-feng.md').read_text()
phone_row = next(line for line in facts.splitlines() if line.startswith('| 私人电话 |'))
phone = phone_row.split('|')[2].strip().strip('`')
with (E / 'metadata.tex').open('a') as f:
    f.write('\\CiesmSetup{phone={' + phone + '}}\n')

abstract = '本课题面向新疆复杂地形下气候模式粗网格与区域气象信息需求之间的尺度差距，研究CIESM近地面气温、风场、短波辐射和降水的多变量时空超分辨率与物理一致性校正。利用公开再分析资料构造粗细尺度配对样本，结合地形条件与多尺度时间表征，比较联合和独立模型；区分校正后大尺度状态的聚合一致性、非负及变量定义条件与经验性地形约束，检验约束对有效细节和极端结构的影响。通过连续年份、地形留出和跨区域验证，评价变量依赖、时间连续性及泛化边界。CIESM自由运行资料采用独立的分布与结构评价，不强行解释为逐日天气真值重建。预期形成可复现的算法、区域试验数据产品和评估流程，开展CIESM接口集成与应用验证，为复杂地形下的气候影响及资源分析提供基础资料。'
assert len(abstract) <= 400
(E / 'abstract.tex').write_text('% 由既有正文整理；包括标点符号不超过400字。\n' + abstract + '\n')

(P / 'figures').mkdir(exist_ok=True)
for source_name, target_name in [('1.1.立项依据.tex', '1.1.立项依据.tex'), ('2.1.研究内容.tex', '1.2.研究内容.tex')]:
    source = (S / 'extraTex' / source_name).read_text()
    target_path = E / target_name
    target = target_path.read_text()
    for number, block in re.findall(r'% NSFC-ILLUSTRATED BEGIN (F\d+)\n(.*?)% NSFC-ILLUSTRATED END F\d+', source, re.S):
        graphic = re.search(r'\\includegraphics\[[^]]+\]\{([^}]+)\}', block)[1]
        caption = re.search(r'\\caption\{([^}]+)\}', block)[1]
        label = re.search(r'\\label\{([^}]+)\}', block)[1]
        text = block.split('\\begin{figure}')[0]
        replacement = text + '\\CiesmFigure{' + graphic + '}{' + caption + '}{' + label + '}\n'
        pattern = r'% 原稿配图 ' + number + r'[^\n]*\n原稿图[^\n]*\n'
        target, count = re.subn(pattern, lambda m: replacement, target)
        assert count == 1, number
        shutil.copy2(S / graphic, P / graphic)
    if source_name.startswith('1.1'):
        target = target[:target.index('% 主要参考文献目录')] + '\\printbibliography[heading=ciesm]\n'
    target_path.write_text(target)

# Keep the bibliography database byte-for-byte; the official builder detects biber
# from the real addbibresource command in main.tex.
shutil.copy2(S / 'references/myexample.bib', P / 'references/myexample.bib')

# Standalone bold paragraph labels are structural headings, not body emphasis.
for path in E.glob('[12].*.tex'):
    if path.name.startswith('2.2.'):
        continue
    text = path.read_text()
    text = text.replace(r'\textbf{正在承担的相关项目。}', r'\subsubsection{相关在研项目}')
    def heading(m):
        title = re.sub(r'^（\d+）', '', m[1]).rstrip('。')
        return '\\paragraph{' + title + '}'
    text = re.sub(r'^\\textbf\{([^{}\n]+)\}\s*$', heading, text, flags=re.M)
    text = text.replace('申请人颜丰为新疆大学副教授、博士、硕士研究生导师',
        r'申请人\CiesmValue{applicant}为\CiesmValue{institution}\CiesmValue{professional-title}、\CiesmValue{degree}、\CiesmValue{mentor}')
    text = text.replace('研究期限为 2027 年 1 月 1 日至 12 月 31 日', r'研究期限为\CiesmDate{start}至\CiesmDate{end}')
    path.write_text(text)

# Retain source-only NSFC declarations for audit, without adding foreign form fields.
archive = P / 'docs/source-only'
archive.mkdir(parents=True, exist_ok=True)
inventory = json.loads((HERE / 'resource-inventory-before.json').read_text())
for row in inventory['inputs']:
    name = Path(row['path']).name
    if name.startswith(('3.4.', '4.')):
        shutil.copy2(S / row['path'], archive / name)
(P / 'docs/resource-manifest.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
print(f'Migrated 7 original PDF figures; abstract {len(abstract)} characters.')
