"""图文工作流的路径、LaTeX、指纹与图件结构检查。仅在本技能中使用。"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import posixpath
import re
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parent.parent


def module_from(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# 只复用仓库代码，不运行原版 CLI，也不写其断点。
legacy = module_from(SKILL_ROOT.parent / 'nsfc-full-pipeline/scripts/pipeline_state.py', 'illustrated_legacy')
scanner = module_from(SKILL_ROOT.parent / 'nsfc-full-pipeline/scripts/scan_gaps.py', 'illustrated_scanner')
BLOCK = re.compile(r'^% NSFC-ILLUSTRATED BEGIN (F\d+)\n.*?^% NSFC-ILLUSTRATED END \1\n?', re.M | re.S)
INPUT = re.compile(r'\\(?:input|include)\s*\{([^}]+)\}')
GRAPHICS = re.compile(r'\\includegraphics\*?(?:\s*\[[^\]]*\])?\s*\{([^}]+)\}')
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def local(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'路径越界：{value}')
    return path


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def sha(path):
    if not path.is_file():
        return 'missing'
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(dir=path.parent, prefix='.' + path.name, delete=False)
    temp = Path(handle.name)
    try:
        with handle:
            handle.write(content if isinstance(content, bytes) else content.encode('utf-8'))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def strip_managed(text):
    stripped = BLOCK.sub('', text)
    if '% NSFC-ILLUSTRATED BEGIN' in stripped or '% NSFC-ILLUSTRATED END' in stripped:
        raise ValueError('插图受管标记不成对，需先修复，不能删除正文猜测恢复')
    return '\n'.join(line.rstrip() for line in stripped.splitlines() if line.strip())


def clean(text):
    return '\n'.join(scanner.strip_comments(line) for line in text.splitlines())


def tex_graph(root):
    """递归跟随静态 input/include；编译工作目录始终是项目根。"""
    paths, seen = [], set()
    def visit(path):
        if path in seen:
            return
        seen.add(path)
        if not path.is_file():
            raise ValueError(f'活动 TeX 文件不存在：{path.relative_to(root)}')
        paths.append(path)
        for raw in INPUT.findall(clean(path.read_text(encoding='utf-8'))):
            if '\\' in raw or '#' in raw:
                raise ValueError(f'无法静态解析 TeX 加载路径：{raw}')
            visit(local(root, raw if raw.endswith('.tex') else raw + '.tex'))
    visit(local(root, 'main.tex'))
    return paths


def body_files(root):
    paths = [p for p in tex_graph(root) if p.is_relative_to(root / 'extraTex') and not p.name.startswith('@')]
    if not paths:
        raise ValueError('main.tex 没有可写的活动 extraTex 正文')
    return paths


def scan(root, state):
    # 私有 scanner 实例只替换事实源和递归解析入口；保留原版的 ID/占位判断。
    def facts(_root):
        paths = []
        for key in ('applicant_profile_file', 'project_fact_file'):
            value = state['project'].get(key)
            if value:
                paths.append((root / value).resolve())  # 申请人事实允许在项目外，只读。
        fallback = root / 'docs/00_项目事实库.md'
        if fallback.is_file():
            paths.append(fallback)
        paths = list(dict.fromkeys(paths))
        ids = set()
        for path in paths:
            if path.is_file():
                ids.update(scanner.ID_RE.findall(path.read_text(encoding='utf-8')))
        return ids, [str(p) for p in paths if p.is_file()], [str(p) for p in paths if not p.is_file()]
    def active(_root, _body_dir, include_all=False):
        try:
            return body_files(root), []
        except ValueError as exc:
            return [], [str(exc)]
    scanner.collect_known_ids = facts
    scanner.resolve_active_tex_files = active
    return scanner.scan(root)


def fingerprints(root, paths, text_only=False):
    result = {}
    for path in sorted(set(paths)):
        files = sorted(path.rglob('*')) if path.is_dir() else [path]
        for item in files:
            if item.is_dir():
                continue
            key = str(item.relative_to(root)) if item.is_relative_to(root) else str(item)
            result[key] = (digest(strip_managed(item.read_text(encoding='utf-8')))
                           if text_only and item.suffix == '.tex' and item.is_file() else sha(item))
    return digest(result)


def build_inputs(root):
    paths = tex_graph(root)
    for path in list(paths):
        text = clean(path.read_text(encoding='utf-8'))
        for raw in GRAPHICS.findall(text):
            target = local(root, raw)
            candidates = [target] if target.suffix else [target.with_suffix(s) for s in ('.pdf', '.png', '.jpg', '.jpeg')]
            found = next((p for p in candidates if p.is_file()), None)
            if not found:
                raise ValueError(f'引用图件不存在或路径无法静态解析：{raw}')
            paths.append(found)
        for raw in re.findall(r'\\(?:bibliography|addbibresource)(?:\[[^\]]*\])?\{([^}]+)\}', text):
            for part in raw.split(','):
                paths.append(local(root, part if part.endswith('.bib') else part + '.bib'))
    # 官方渲染器若产生 recorder 文件，一并跟踪实际读入的本地/已安装包资源。
    for fls in (root / '.latex-cache').rglob('*.fls'):
        for line in fls.read_text(errors='replace').splitlines():
            if line.startswith('INPUT '):
                path = (root / line[6:]).resolve()
                if path.suffix.lower() in {'.tex', '.sty', '.cls', '.bst', '.bib', '.otf', '.ttf', '.map', '.cfg', '.def'} and path.is_file():
                    paths.append(path)
    return fingerprints(root, paths)


def load_plan(root):
    data = read_json(local(root, 'docs/figure_manifest.json'))
    if not isinstance(data, dict):
        raise ValueError('配图清单必须是 JSON 对象')
    items = data.get('figures', [])
    if not isinstance(items, list) or not items or not isinstance(data.get('route_ids'), list) or not data['route_ids']:
        raise ValueError('配图清单需要 figures 和真实 route_ids')
    if not all(isinstance(r, str) and r for r in data['route_ids']) or len(set(data['route_ids'])) != len(data['route_ids']):
        raise ValueError('route_ids 必须是互不重复的非空字符串')
    active = {str(p.relative_to(root)) for p in body_files(root)}
    ids, labels, outputs = set(), set(), set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('每条图件记录必须是 JSON 对象')
        fid = item.get('id', '')
        if not re.fullmatch(r'F\d{2,}', fid) or fid in ids:
            raise ValueError(f'非法或重复图 ID：{fid}')
        ids.add(fid)
        if not isinstance(item.get('selected'), bool):
            raise ValueError(f'{fid} 缺少 selected 布尔值')
        if not item['selected']:
            if item.get('required') or not item.get('reason'):
                raise ValueError(f'{fid} 必选图不能取消，可选图未入选必须说明理由')
            continue
        if item.get('source_file') not in active:
            raise ValueError(f'{fid} 落点不是活动正文')
        text = strip_managed(local(root, item['source_file']).read_text(encoding='utf-8'))
        for key in ('anchor', 'source_excerpt'):
            if not item.get(key) or item[key] not in text:
                raise ValueError(f'{fid} 的 {key} 未命中当前正文，需复核配图来源')
        for key, suffix, directory in [('prompt', '.md', 'docs'), ('spec', '.json', 'docs'), ('png', '.png', 'figures'), ('pdf', '.pdf', 'figures')]:
            path = local(root, item.get(key, ''))
            if path.suffix != suffix or not path.is_relative_to(root / directory):
                raise ValueError(f'{fid} 的 {key} 路径非法')
            if str(path) in outputs:
                raise ValueError(f'图件路径重复：{path}')
            outputs.add(str(path))
        label = item.get('label', '')
        if not re.fullmatch(r'fig:[A-Za-z0-9:_-]+', label) or label in labels:
            raise ValueError(f'{fid} 图标签非法或重复')
        labels.add(label)
        if not isinstance(item.get('caption'), str) or not item['caption'] or not 0.2 <= float(item.get('width', 0.9)) <= 1.0:
            raise ValueError(f'{fid} 缺少图题或图宽不合法')
    selected = [i for i in items if i['selected']]
    for kind in ('background', 'framework'):
        if not any(i.get('kind') == kind for i in selected):
            raise ValueError(f'缺少核心图：{kind}')
    routes = [i.get('route_id') for i in selected if i.get('kind') == 'route']
    if not all(isinstance(r, str) for r in routes) or sorted(routes) != sorted(data['route_ids']) or len(set(routes)) != len(routes):
        raise ValueError('每条真实研究路线必须对应一张独立技术路线图')
    return sorted(selected, key=lambda item: int(item['id'][1:]))


def figure_input(root, item):
    return digest({'source_excerpt': item['source_excerpt'], 'kind': item.get('kind'),
                   'route_id': item.get('route_id'), 'gaps': item.get('gap_ids', []),
                   'files': fingerprints(root, [local(root, item['prompt']), local(root, item['spec']),
                                                 local(root, 'docs/Figure_Palette.md')])})


def check_png(path):
    from PIL import Image
    with Image.open(path) as img:
        if img.format != 'PNG' or min(img.size) < 128:
            raise ValueError('图件必须是尺寸有效的 PNG')
        img.verify()


def check_pdf(path, pages=None):
    import fitz
    with fitz.open(path) as doc:
        if not doc.is_pdf or doc.is_encrypted or not doc.page_count or (pages is not None and doc.page_count != pages):
            raise ValueError(f'PDF 不可读或页数不符：{path}')
        for page in doc:
            if page.rect.is_empty:
                raise ValueError('PDF 页面尺寸无效')
        return doc.page_count


def check_deck(path, count):
    """结构门槛不替代 editppt 页级视觉验收。"""
    with zipfile.ZipFile(path) as archive:
        required = {'[Content_Types].xml', '_rels/.rels', 'ppt/presentation.xml', 'ppt/_rels/presentation.xml.rels'}
        if not required.issubset(archive.namelist()) or archive.testzip():
            raise ValueError('PPTX 包结构不完整')
        for name in archive.namelist():
            if not name.endswith('.rels'):
                continue
            base = posixpath.dirname(posixpath.dirname(name))
            for rel in ET.fromstring(archive.read(name)):
                if rel.attrib.get('TargetMode') == 'External':
                    continue
                target = rel.attrib.get('Target', '')
                resolved = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(base, target))
                if resolved not in archive.namelist():
                    raise ValueError(f'PPTX 关系引用缺少资源：{resolved}')
        presentation = ET.fromstring(archive.read('ppt/presentation.xml'))
        slides = presentation.findall('p:sldIdLst/p:sldId', NS)
        if len(slides) != count:
            raise ValueError('PPT 页数必须与入选图件数相同')
        relations = ET.fromstring(archive.read('ppt/_rels/presentation.xml.rels'))
        targets = {rel.attrib['Id']: rel.attrib['Target'] for rel in relations}
        size = presentation.find('p:sldSz', NS)
        canvas_area = int(size.attrib['cx']) * int(size.attrib['cy'])
        for slide in slides:
            target = targets[slide.attrib['{' + NS['r'] + '}id']]
            name = ('ppt/' + target) if not target.startswith('/') else target.lstrip('/')
            xml = ET.fromstring(archive.read(name))
            text = xml.findall('.//a:t', NS)
            shapes = xml.findall('.//p:sp', NS) + xml.findall('.//p:cxnSp', NS)
            if not text or len(shapes) < 2:
                raise ValueError('PPT 缺少可编辑文字或独立结构对象')
            for picture in xml.findall('.//p:pic', NS):
                extent = picture.find('p:spPr/a:xfrm/a:ext', NS)
                if extent is not None and int(extent.attrib['cx']) * int(extent.attrib['cy']) >= canvas_area * 0.85:
                    raise ValueError('PPT 含整页位图，不能视为对象级重建')


def evidence(root, value, checks):
    path = local(root, value)
    report = read_json(path)
    if report.get('passed') is not True or any(report.get('checks', {}).get(c) is not True for c in checks):
        raise ValueError('验收报告缺少通过证据：' + ', '.join(checks))
    return {'path': str(path.relative_to(root)), 'sha256': sha(path)}


def escape_tex(text):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
                    '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(replacements.get(char, char) for char in text)


def figure_block(item):
    if any(char in item['pdf'] for char in '{}%\\\n\r'):
        raise ValueError('图件路径不能包含 TeX 控制字符')
    return (f"% NSFC-ILLUSTRATED BEGIN {item['id']}\n"
            f"如图~\\ref{{{item['label']}}} 所示，{escape_tex(item['caption'])}。\n"
            '\\begin{figure}[htbp]\n\\centering\n'
            f"\\includegraphics[width={float(item.get('width', 0.9)):g}\\linewidth]{{{item['pdf']}}}\n"
            f"\\caption{{{escape_tex(item['caption'])}}}\n\\label{{{item['label']}}}\n"
            f"\\end{{figure}}\n% NSFC-ILLUSTRATED END {item['id']}\n")


def insertion(root, items, apply=False):
    texts = {p: p.read_text(encoding='utf-8') for p in body_files(root)}
    proposed = dict(texts)
    all_ids = [m.group(1) for text in texts.values() for m in BLOCK.finditer(text)]
    if len(all_ids) != len(set(all_ids)) or set(all_ids) - {i['id'] for i in items}:
        raise ValueError('存在重复或已退出清单的受管插图，需明确处理后再插入')
    for item in items:
        check_pdf(local(root, item['pdf']), 1)
        path = local(root, item['source_file'])
        for other, text in proposed.items():
            if item['id'] in [m.group(1) for m in BLOCK.finditer(text)] and other != path:
                raise ValueError('图件落点已变化，需先明确迁移已有插图')
        pattern = re.compile(r'^% NSFC-ILLUSTRATED BEGIN ' + item['id'] + r'\n.*?^% NSFC-ILLUSTRATED END ' + item['id'] + r'\n?', re.M | re.S)
        other_text = '\n'.join(pattern.sub('', text) for text in proposed.values())
        if re.search(r'\\label\s*\{' + re.escape(item['label']) + r'\}', clean(other_text)):
            raise ValueError(f"已有非受管图使用标签 {item['label']}，先人工匹配，不能重复插入")
        block = figure_block(item)
        if pattern.search(proposed[path]):
            proposed[path] = pattern.sub(lambda _: block, proposed[path])
        else:
            anchor = item['anchor']
            if proposed[path].count(anchor) != 1:
                raise ValueError(f"{item['id']} 插入锚点必须唯一")
            proposed[path] = proposed[path].replace(anchor, anchor + '\n' + block, 1)
    changes = [str(p.relative_to(root)) for p in proposed if proposed[p] != texts[p]]
    if apply:
        # 先验证所有目标，再逐文件原子落盘；中断后再次执行是幂等更新。
        for path, value in proposed.items():
            if value != texts[path]:
                backup = local(root, 'docs/figure_source/backups/' + sha(path) + '.tex')
                if not backup.exists():
                    atomic(backup, texts[path])
                atomic(path, value)
    return changes
