#!/usr/bin/env python3
"""NSFC 图文流程状态入口；生图由宿主 imagegen 执行，本脚本登记与验收。"""
from __future__ import annotations

import argparse
import copy
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import yaml

import artifacts as a

NAME = 'nsfc-illustrated-pipeline'
CONFIG = yaml.safe_load((a.SKILL_ROOT / 'config.yaml').read_text(encoding='utf-8'))
STATUS = CONFIG['checkpoint']['file']
STAGES = dict(a.legacy.STAGE_NAMES)
STAGES.update({
    '15_figure_plan': '配图规划', '16_figure_prompts': '统一配色与逐图提示词',
    '17_imagegen': '逐个调用 imagegen', '18_editable_ppt': '可编辑 PPT',
    '19_figure_pdf': '逐图 PDF', '20_insert_figures': '插入正文',
    '21_joint_review': '图文联合检查', '22_final_compile': '最终构建验收',
})
TEXT = list(a.legacy.STAGE_NAMES)
DONE = {'completed', 'drafted_with_gaps', 'skipped'}
IMAGE_CHECKS = ['chinese', 'direction', 'hierarchy', 'crop', 'source_consistency']
DECK_CHECKS = ['editable_objects', 'text_fidelity', 'page_mapping', 'editppt_validation']
JOINT_CHECKS = ['page_limit', 'legibility', 'no_crop', 'references', 'source_consistency', 'qc']


def path(root, value):
    return a.local(root, value)


def save(root, state):
    state['run']['next_stage'] = next_stage(state)
    a.atomic(path(root, STATUS), yaml.safe_dump(state, allow_unicode=True, sort_keys=False))


def nonempty(root, paths):
    return all(p.is_file() and p.stat().st_size > 0 for p in paths)


def items(root):
    return a.load_plan(root)


def get_item(root, fid):
    return next(i for i in items(root) if i['id'] == fid)


def stored_evidence_valid(root, receipt):
    evidence = receipt.get('evidence', {})
    return bool(evidence.get('sha256') and a.sha(path(root, evidence['path'])) == evidence['sha256'])


def image_valid(root, state, item):
    receipt = state['figures'].get(item['id'], {}).get('image', {})
    return bool(receipt.get('input') == a.figure_input(root, item)
                and receipt.get('output') == a.sha(path(root, item['png']))
                and stored_evidence_valid(root, receipt))


def deck_valid(root, state):
    receipt = state.get('deck', {})
    selected = items(root)
    current = {i['id']: a.sha(path(root, i['png'])) for i in selected}
    return bool(receipt.get('images') == current
                and receipt.get('output') == a.sha(path(root, CONFIG['figures']['deck']))
                and stored_evidence_valid(root, receipt))


def pdf_valid(root, state, item):
    receipt = state['figures'].get(item['id'], {}).get('pdf', {})
    return bool(receipt.get('deck') == a.sha(path(root, CONFIG['figures']['deck']))
                and receipt.get('output') == a.sha(path(root, item['pdf'])))


def build_valid(root, state, phase):
    receipt = state.get('builds', {}).get(phase, {})
    target = 'docs/figure_source/main.text.pdf' if phase == 'text' else 'main.pdf'
    return bool(receipt.get('output') == a.sha(path(root, target))
                and (phase == 'text' or receipt.get('input') == a.build_inputs(root)))


def stage_inputs(root, state, stage):
    if stage in TEXT:
        return a.fingerprints(root, a.legacy.expand_stage_inputs(root, state, stage), text_only=True)
    selected = items(root) if path(root, CONFIG['figures']['manifest']).exists() else []
    if stage == '15_figure_plan':
        rules = state['run'].get('drawing_rules')
        return a.digest([a.fingerprints(root, a.body_files(root), True),
                         a.sha(path(root, 'docs/figure_source/main.text.pdf')),
                         a.sha(Path(rules)) if rules else None])
    if stage == '16_figure_prompts':
        return a.digest([{k: i.get(k) for k in ('id', 'kind', 'route_id', 'source_excerpt', 'spec', 'prompt', 'gap_ids')} for i in selected])
    if stage == '17_imagegen':
        return a.digest([a.figure_input(root, i) for i in selected])
    if stage == '18_editable_ppt':
        return a.digest({i['id']: a.sha(path(root, i['png'])) for i in selected})
    if stage == '19_figure_pdf':
        return a.digest([a.sha(path(root, CONFIG['figures']['deck'])), [(i['id'], i['pdf']) for i in selected]])
    if stage == '20_insert_figures':
        return a.digest([(a.figure_block(i), i['source_file'], i['anchor'], a.sha(path(root, i['pdf']))) for i in selected])
    return a.build_inputs(root)


def stage_outputs(root, state, stage):
    if stage in TEXT:
        if stage == '14_compile':
            paths = [path(root, 'docs/figure_source/main.text.pdf'), path(root, 'review/编译检查报告.md')]
        else:
            paths = a.legacy.expand_stage_outputs(root, state, stage)
        return a.fingerprints(root, paths, text_only=True)
    selected = items(root)
    paths = {
        '15_figure_plan': ['docs/Figure_Plan.md'],
        '16_figure_prompts': ['docs/Figure_Palette.md'] + [i[k] for i in selected for k in ('spec', 'prompt')],
        '17_imagegen': [i['png'] for i in selected],
        '18_editable_ppt': [CONFIG['figures']['deck']],
        '19_figure_pdf': [i['pdf'] for i in selected],
        '20_insert_figures': [i['source_file'] for i in selected] + ['docs/figure_insertion.md'],
        '21_joint_review': ['review/图文联合检查报告.md', 'review/图文联合检查证据.json'],
        '22_final_compile': ['main.pdf', 'review/最终图文编译检查报告.md'],
    }[stage]
    return a.fingerprints(root, [path(root, p) for p in paths])


def validate_project(root, state):
    project = state['project']
    if not all(project.get(k) for k in ('type', 'grant_type', 'layout', 'length_budget')):
        raise ValueError('先登记项目类型、布局、篇幅规则')
    declared = [p for role in a.legacy.ROLE_STAGE for p in project['body_files'][role]]
    active = {str(p.relative_to(root)) for p in a.body_files(root)}
    if len(declared) != len(set(declared)) or set(declared) != active:
        raise ValueError('正文角色映射必须完整且唯一地覆盖活动正文，不得包含孤儿文件')


def validate_stage(root, state, stage):
    if stage in TEXT:
        if stage == '00_layout_resolution':
            validate_project(root, state)
        elif stage == '14_compile':
            if not build_valid(root, state, 'text') or not path(root, 'review/编译检查报告.md').is_file():
                raise ValueError('文字阶段缺少有效构建、稳定 PDF 或编译报告')
            a.check_pdf(path(root, 'docs/figure_source/main.text.pdf'))
        elif not a.legacy.outputs_ready(root, state, stage):
            raise ValueError('阶段产物缺失、为空或仍是未写作占位')
        return
    selected = items(root)
    if stage == '15_figure_plan':
        if not nonempty(root, [path(root, 'docs/Figure_Plan.md')]):
            raise ValueError('缺少 Figure Plan')
    elif stage == '16_figure_prompts':
        paths = [path(root, i[k]) for i in selected for k in ('spec', 'prompt')]
        if not nonempty(root, paths + [path(root, 'docs/Figure_Palette.md')]):
            raise ValueError('每张入选图都必须有 JSON 规范、独立 prompt 及全篇配色')
        for i in selected:
            if not isinstance(a.read_json(path(root, i['spec'])), dict):
                raise ValueError('图件 JSON 规范必须是对象')
    elif stage == '17_imagegen':
        if state.get('active_image') or not all(image_valid(root, state, i) for i in selected):
            raise ValueError('仍有图件未独立调用 imagegen 并通过检查')
    elif stage == '18_editable_ppt':
        if not deck_valid(root, state):
            raise ValueError('PPT 未登记验收或其内容/源 PNG 已变化')
        a.check_deck(path(root, CONFIG['figures']['deck']), len(selected))
    elif stage == '19_figure_pdf':
        if not all(pdf_valid(root, state, i) for i in selected):
            raise ValueError('逐图 PDF 未从当前 PPT 导出')
        for i in selected:
            a.check_pdf(path(root, i['pdf']), 1)
    elif stage == '20_insert_figures':
        if a.insertion(root, selected) or not path(root, 'docs/figure_insertion.md').is_file():
            raise ValueError('正文插图/图题/引用尚未与配图清单一致')
    elif stage == '21_joint_review':
        report_path = 'review/图文联合检查证据.json'
        a.evidence(root, report_path, JOINT_CHECKS)
        report = a.read_json(path(root, report_path))
        if not build_valid(root, state, 'final') or report.get('pdf_sha256') != a.sha(path(root, 'main.pdf')) or report.get('input_sha256') != a.build_inputs(root):
            raise ValueError('图文检查不对应当前构建，必须查看最新 PDF 后重做检查')
        if set(report.get('figure_pages', {})) != {i['id'] for i in selected}:
            raise ValueError('图文检查必须列出每张入选图在最终 PDF 中的页码')
        page_count = a.check_pdf(path(root, 'main.pdf'))
        for pages in report['figure_pages'].values():
            if not pages or not all(isinstance(p, int) and 1 <= p <= page_count for p in pages):
                raise ValueError('图件验收页码无效')
        if not path(root, 'review/图文联合检查报告.md').is_file():
            raise ValueError('缺少图文联合检查报告')
    elif stage == '22_final_compile':
        if not build_valid(root, state, 'final') or not path(root, 'review/最终图文编译检查报告.md').is_file():
            raise ValueError('最终 PDF 或官方构建证据已过期')


def next_stage(state):
    return next((s for s in STAGES if state['stages'][s]['status'] not in DONE), None)


def initialize(root, apply_import=False):
    target = path(root, STATUS)
    if target.exists():
        state = a.legacy.load_state(target)
        if state.get('skill') != NAME or state.get('schema_version') != 3:
            raise ValueError('未知图文断点格式，拒绝覆盖或降级')
        return state
    old_path = path(root, CONFIG['checkpoint']['import_legacy'])
    original = a.legacy.load_state(old_path)
    state, _ = a.legacy.migrate_state(original)
    state.update(skill=NAME, schema_version=3, figures={}, builds={})
    state['run']['mode'] = 'illustrated'
    stamp = a.legacy.now_iso().replace(':', '').replace('-', '')[:13]
    state['run']['workspace'] = f'.bensz-api/task-{stamp}-illustrated/{NAME}'
    state['imported_from'] = {'path': str(old_path.relative_to(root)), 'sha256': a.sha(old_path)} if original else None
    # 原版记录只读导入：验证它的旧指纹再建立本技能的规范化指纹。
    for stage in TEXT:
        record = state['stages'][stage]
        if record['status'] not in DONE:
            continue
        try:
            if not a.legacy.outputs_ready(root, state, stage):
                raise ValueError('原阶段输出无效')
            before = record.get('input_sha256')
            if not before or before != a.legacy._fingerprint_paths(root, a.legacy.expand_stage_inputs(root, state, stage)):
                raise ValueError('原阶段缺少有效输入指纹，需定点复核')
            if stage == '14_compile':
                a.check_pdf(path(root, 'main.pdf'))
                snapshot = path(root, 'docs/figure_source/main.text.pdf')
                if apply_import:
                    a.atomic(snapshot, path(root, 'main.pdf').read_bytes())
                state['builds']['text'] = {'output': a.sha(path(root, 'main.pdf')), 'imported': True}
            record['input'] = stage_inputs(root, state, stage)
            record['output'] = stage_outputs(root, state, stage)
        except (ValueError, OSError) as exc:
            record.update(status='pending', notes=str(exc))
    for stage in list(STAGES)[15:]:
        state['stages'][stage] = {'name': STAGES[stage], 'status': 'pending'}
    return state


def reconcile(root, state):
    report = a.scan(root, state)
    gaps = a.legacy._gaps_by_role(state, report)
    for role, stage in a.legacy.ROLE_STAGE.items():
        record = state['stages'][stage]
        record['gaps'] = gaps[role]
        if record['status'] in DONE:
            record['status'] = 'drafted_with_gaps' if gaps[role] else 'completed'
    invalidated = []
    for stage in STAGES:
        record = state['stages'][stage]
        if record['status'] not in DONE:
            continue
        try:
            validate_stage(root, state, stage)
            if record.get('input') != stage_inputs(root, state, stage) or record.get('output') != stage_outputs(root, state, stage):
                raise ValueError('输入或产物指纹变化，需定点复核')
        except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
            record.update(status='pending', notes=str(exc))
            invalidated.append(stage)
    state['run']['next_stage'] = next_stage(state)
    return {'invalidated': invalidated, 'scan': report}


def finish(root, state, stage):
    record = state['stages'][stage]
    if record['status'] != 'in_progress':
        raise ValueError('必须先 begin；中断后也要核验再显式 finish')
    validate_stage(root, state, stage)
    report = a.scan(root, state)
    if stage in list(STAGES)[8:] and (report['problems'] or report['unfinished_placeholders']):
        raise ValueError('正文存在非法事实 ID、未写作占位或结构问题')
    if stage in a.legacy.ROLE_STAGE.values():
        role = next(r for r, s in a.legacy.ROLE_STAGE.items() if s == stage)
        files = state['project']['body_files'][role]
        if any(any(f in message for f in files) for message in report['problems'] + report['unfinished_placeholders']):
            raise ValueError('当前章节存在非法事实 ID、整段占位或未写作标记')
        if report['open_hard_gaps'] and not report['fact_files']:
            raise ValueError('缺少可追溯的事实库')
    record['gaps'] = a.legacy._gaps_by_role(state, report).get(next((r for r, s in a.legacy.ROLE_STAGE.items() if s == stage), ''), [])
    record.update(status='drafted_with_gaps' if record['gaps'] else 'completed',
                  input=stage_inputs(root, state, stage), output=stage_outputs(root, state, stage),
                  finished_at=a.legacy.now_iso())


def readiness(root, state):
    report = reconcile(root, state)
    scan = report['scan']
    text_done = all(state['stages'][s]['status'] in DONE for s in TEXT)
    body = text_done and not scan['problems'] and not scan['unfinished_placeholders'] and scan['hard_gaps_clear']
    figures = False
    counts = {'selected': 0, 'generated': 0, 'pdf': 0, 'inserted': 0}
    figure_gaps = []
    try:
        selected = items(root)
        counts = {'selected': len(selected), 'generated': sum(image_valid(root, state, i) for i in selected),
                  'pdf': sum(pdf_valid(root, state, i) for i in selected), 'inserted': 0}
        figure_gaps = sorted({g for i in selected for g in i.get('gap_ids', [])})
        for i in selected:
            counts['inserted'] += a.figure_block(i) in path(root, i['source_file']).read_text(encoding='utf-8')
        figures = all(state['stages'][s]['status'] == 'completed' for s in list(STAGES)[15:21]) and not figure_gaps
    except (OSError, ValueError, KeyError):
        pass
    illustrated = body and figures and all(state['stages'][s]['status'] == 'completed' for s in list(STAGES)[21:])
    pending = [k for k, v in state['submission'].items() if v not in ('completed', 'not_applicable')]
    return {'text_stages_done': text_done, 'body_pipeline_ready': body, 'figures_ready': figures,
            'illustrated_body_ready': illustrated, 'submission_ready': illustrated and not pending,
            'pending_submission_items': pending, 'open_hard_gaps': scan['open_hard_gaps'],
            'figure_gap_ids': figure_gaps, 'tentative_count': scan['tentative_count'],
            'counts': counts, 'next_stage': next_stage(state), 'scan_problems': scan['problems']}


def image_start(root, state, fid, prompt=None):
    if state.get('active_image'):
        raise ValueError('已有生图调用未结束；先记录或明确标记失败，不能并发生图')
    selected = items(root)
    candidate = next((i for i in selected if not image_valid(root, state, i)
                      and sum(t['input'] == a.figure_input(root, i) for t in state['figures'].get(i['id'], {}).get('attempts', [])) < 1 + CONFIG['figures']['max_corrections']), None)
    if not candidate or candidate['id'] != fid:
        raise ValueError('必须按图 ID 顺序处理尚未通过且有重试额度的图')
    item = candidate
    record = state['figures'].setdefault(fid, {})
    attempts = record.setdefault('attempts', [])
    prompt = prompt or item['prompt']
    prompt_path = path(root, prompt)
    if not prompt_path.is_file():
        raise ValueError('缺少本次调用的实际 prompt 文件')
    attempt = {'prompt': prompt, 'prompt_sha256': a.sha(prompt_path), 'input': a.figure_input(root, item),
               'before': a.sha(path(root, item['png'])), 'started_at': a.legacy.now_iso(), 'status': 'in_progress'}
    attempts.append(attempt)
    state['active_image'] = fid
    return {'figure': fid, 'attempt': len(attempts), 'prompt': str(prompt_path),
            'instruction': '现在仅调用一次内置 imagegen，为此 prompt 生成一张图；检查并复制 PNG 后 image-record。'}


def image_record(root, state, fid, call_id, evidence_path):
    if state.get('active_image') != fid:
        raise ValueError('没有对应的串行生图开始记录')
    item = get_item(root, fid)
    record = state['figures'][fid]
    attempt = record['attempts'][-1]
    if attempt['input'] != a.figure_input(root, item) or attempt['prompt_sha256'] != a.sha(path(root, attempt['prompt'])):
        raise ValueError('调用过程中 prompt 或图件来源发生变化')
    if any(t.get('call_id') == call_id for r in state['figures'].values() for t in r.get('attempts', [])):
        raise ValueError('每次独立绘图调用必须有独立 call_id')
    image_path = path(root, item['png'])
    a.check_png(image_path)
    if a.sha(image_path) == attempt['before']:
        raise ValueError('PNG 与调用前相同，不能仅凭旧文件记录新调用完成')
    proof = a.evidence(root, evidence_path, IMAGE_CHECKS)
    attempt.update(status='completed', call_id=call_id, finished_at=a.legacy.now_iso())
    record['image'] = {'input': attempt['input'], 'output': a.sha(image_path), 'evidence': proof, 'call_id': call_id}
    state.pop('active_image', None)


def build(root, state, phase):
    official = a.REPO_ROOT / 'packages/bensz-nsfc/scripts/nsfc_project_tool.py'
    command = [sys.executable, str(official), 'build', '--project-dir', str(root)]
    # 捕获 stdout 到项目缓存，不把构建产物散落到仓库根。
    cache = path(root, '.latex-cache/illustrated-pipeline')
    cache.mkdir(parents=True, exist_ok=True)
    source_before = a.fingerprints(root, a.tex_graph(root))
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    a.atomic(cache / (phase + '-build.log'), result.stdout + '\n' + result.stderr)
    if result.returncode:
        raise ValueError(f'官方构建失败（{result.returncode}），查看 {cache / (phase + "-build.log")}')
    if source_before != a.fingerprints(root, a.tex_graph(root)):
        raise ValueError('构建过程中 TeX 源文件被修改，请重新构建')
    pdf = path(root, 'main.pdf')
    pages = a.check_pdf(pdf)
    if phase == 'text':
        a.atomic(path(root, 'docs/figure_source/main.text.pdf'), pdf.read_bytes())
    receipt = {'command': command, 'exit_code': result.returncode, 'input': a.build_inputs(root),
               'output': a.sha(pdf), 'pages': pages, 'built_at': a.legacy.now_iso()}
    state['builds'][phase] = receipt
    return receipt


def export_pdf(root, state):
    if not deck_valid(root, state):
        raise ValueError('先对当前 PPT 执行 deck-record')
    selected = items(root)
    a.check_deck(path(root, CONFIG['figures']['deck']), len(selected))
    executable = shutil.which('libreoffice') or shutil.which('soffice')
    if not executable:
        raise ValueError('缺少 LibreOffice/soffice，无法导出 PPT')
    import tempfile
    import fitz
    task = path(root, state['run']['workspace'] + '/output/pdf')
    task.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=task) as temp:
        work = Path(temp)
        command = [executable, '-env:UserInstallation=' + (work / 'profile').as_uri(), '--headless',
                   '--convert-to', 'pdf', '--outdir', str(work), str(path(root, CONFIG['figures']['deck']))]
        result = subprocess.run(command, cwd=root, capture_output=True, text=True)
        a.atomic(work / 'export.log', result.stdout + '\n' + result.stderr)
        exported = work / Path(CONFIG['figures']['deck']).with_suffix('.pdf').name
        if result.returncode or not exported.is_file():
            raise ValueError('PPT 导出失败：' + result.stderr[-500:])
        a.check_pdf(exported, len(selected))
        outputs = []
        with fitz.open(exported) as doc:
            for index, item in enumerate(selected):
                target = path(root, item['pdf'])
                old = state['figures'].get(item['id'], {}).get('pdf', {})
                if target.exists() and old.get('output') != a.sha(target):
                    raise ValueError(f'{target.name} 是未登记或被用户修改的 PDF，请在清单中使用新的文件名')
                one = fitz.open()
                one.insert_pdf(doc, from_page=index, to_page=index)
                outputs.append((item, target, one.tobytes()))
                one.close()
        for item, target, content in outputs:
            if target.exists():
                a.atomic(path(root, 'docs/figure_source/backups/' + a.sha(target) + '.pdf'), target.read_bytes())
            a.atomic(target, content)
            state['figures'].setdefault(item['id'], {})['pdf'] = {
                'deck': a.sha(path(root, CONFIG['figures']['deck'])), 'output': a.sha(target),
                'slide': selected.index(item) + 1}
    return {'exported': [i['pdf'] for i in selected]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-dir', required=True)
    subs = parser.add_subparsers(dest='command', required=True)
    for name in ('migrate', 'reconcile'):
        subs.add_parser(name).add_argument('--apply', action='store_true')
    for name in ('next', 'readiness', 'scan', 'export-pdf'):
        subs.add_parser(name)
    subs.add_parser('project').add_argument('--from-json', required=True)
    subs.add_parser('drawing-rules').add_argument('--file', required=True)
    for name in ('begin', 'finish', 'fail'):
        p = subs.add_parser(name)
        p.add_argument('--stage', choices=list(STAGES), required=True)
        if name == 'fail':
            p.add_argument('--reason', required=True)
    p = subs.add_parser('image-start')
    p.add_argument('--figure', required=True)
    p.add_argument('--prompt')
    p = subs.add_parser('image-record')
    p.add_argument('--figure', required=True)
    p.add_argument('--call-id', required=True)
    p.add_argument('--evidence', required=True)
    subs.add_parser('image-fail').add_argument('--reason', required=True)
    p = subs.add_parser('image-reset')
    p.add_argument('--figure', required=True)
    p.add_argument('--reason', required=True)
    subs.add_parser('deck-record').add_argument('--evidence', required=True)
    subs.add_parser('insert').add_argument('--apply', action='store_true')
    subs.add_parser('build').add_argument('--phase', choices=['text', 'final'], required=True)
    p = subs.add_parser('submission')
    p.add_argument('--item', choices=a.legacy.SUBMISSION_ITEMS, required=True)
    p.add_argument('--status', choices=['pending', 'completed', 'not_applicable'], required=True)
    p.add_argument('--reason', required=True)
    args = parser.parse_args(argv)
    root = Path(args.project_dir).expanduser().resolve()
    try:
        if not root.is_dir():
            raise ValueError('项目目录不存在')
        state = initialize(root, apply_import=args.command == 'migrate' and args.apply)
        result = {}
        write = args.command not in ('next', 'readiness', 'scan') and getattr(args, 'apply', True)
        if args.command == 'migrate':
            result = {'state_file': str(path(root, STATUS)), 'imported_from': state['imported_from']}
        elif args.command == 'reconcile':
            result = reconcile(root, state)
        elif args.command == 'next':
            reconcile(root, state)
            result = {'next_stage': next_stage(state), 'active_image': state.get('active_image')}
        elif args.command == 'readiness':
            result = readiness(root, state)
        elif args.command == 'scan':
            result = a.scan(root, state)
        elif args.command == 'project':
            state['project'].update(a.read_json(Path(args.from_json).resolve()))
            validate_project(root, state)
            state['stages']['00_layout_resolution']['status'] = 'pending'
        elif args.command == 'drawing-rules':
            source = Path(args.file).expanduser().resolve()
            if not source.is_file():
                raise ValueError('绘图规则文件不存在')
            state['run']['drawing_rules'] = str(source)
        elif args.command == 'begin':
            reconcile(root, state)
            # 允许回调文字检查；新增图件阶段必须按流程顺序执行。
            if args.stage not in TEXT and next_stage(state) != args.stage:
                raise ValueError('前置阶段尚未完成：' + str(next_stage(state)))
            state['stages'][args.stage].update(status='in_progress', started_at=a.legacy.now_iso())
        elif args.command == 'finish':
            finish(root, state, args.stage)
        elif args.command == 'fail':
            state['stages'][args.stage].update(status='failed', notes=args.reason)
        elif args.command == 'image-start':
            validate_stage(root, state, '16_figure_prompts')
            if state['stages']['17_imagegen']['status'] != 'in_progress':
                raise ValueError('先 begin --stage 17_imagegen')
            result = image_start(root, state, args.figure, args.prompt)
        elif args.command == 'image-record':
            image_record(root, state, args.figure, args.call_id, args.evidence)
        elif args.command == 'image-fail':
            fid = state.get('active_image')
            if not fid:
                raise ValueError('没有进行中的图件')
            state['figures'][fid]['attempts'][-1].update(status='failed', reason=args.reason)
            state.pop('active_image')
        elif args.command == 'image-reset':
            if state.get('active_image'):
                raise ValueError('进行中的图件不能重置；先核实调用状态并记录结果')
            get_item(root, args.figure)
            record = state['figures'].setdefault(args.figure, {})
            record.setdefault('history', []).append({'reason': args.reason, 'attempts': record.get('attempts', []), 'image': record.get('image')})
            record['attempts'] = []
            record.pop('image', None)
            state['stages']['17_imagegen']['status'] = 'pending'
        elif args.command == 'deck-record':
            if not all(image_valid(root, state, i) for i in items(root)):
                raise ValueError('先完成每张 PNG 的独立调用验收')
            a.check_deck(path(root, CONFIG['figures']['deck']), len(items(root)))
            proof = a.evidence(root, args.evidence, DECK_CHECKS)
            state['deck'] = {'output': a.sha(path(root, CONFIG['figures']['deck'])), 'evidence': proof,
                             'images': {i['id']: a.sha(path(root, i['png'])) for i in items(root)}}
        elif args.command == 'export-pdf':
            result = export_pdf(root, state)
        elif args.command == 'insert':
            validate_stage(root, state, '19_figure_pdf')
            result = {'changed_files': a.insertion(root, items(root), args.apply)}
        elif args.command == 'build':
            result = build(root, state, args.phase)
        elif args.command == 'submission':
            state['submission'][args.item] = args.status
            state.setdefault('submission_reasons', {})[args.item] = args.reason
        if write:
            save(root, state)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, StopIteration, ImportError, RuntimeError,
            zipfile.BadZipFile, ET.ParseError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
