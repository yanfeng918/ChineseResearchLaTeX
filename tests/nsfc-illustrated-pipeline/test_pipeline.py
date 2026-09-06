"""隔离的确定性回归；图像/PDF 均为测试夹具，不代表模型生图验收。"""
import copy
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import fitz
from PIL import Image

TEST_ROOT = Path(__file__).resolve().parent
REPO = TEST_ROOT.parents[1]
sys.path.insert(0, str(REPO / 'skills/nsfc-illustrated-pipeline/scripts'))
import pipeline_state as p
import artifacts as a


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=TEST_ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('main.tex', '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n'
                   '\\input{extraTex/body.tex}\n\\input{extraTex/foundation.tex}\n'
                   '\\input{extraTex/statements.tex}\n\\end{document}\n')
        self.write('extraTex/body.tex', 'Research background has an identified scientific knowledge gap.\n\n'
                   'An overall framework connects the research tasks.\n\n'
                   'Route one uses an independent validation method.\n\n'
                   'Route two examines the mechanism in detail.\n\n'
                   'Route three evaluates external generalization.\n')
        self.write('extraTex/foundation.tex', 'Existing evidence supports a feasible research proposal without invented facts.\n')
        self.write('extraTex/statements.tex', 'No other applications have been declared in this synthetic fixture.\n')
        self.write('AGENTS.md', 'NSFC 面上项目，全文不超过30页。')
        self.write('README.md', 'NSFC synthetic fixture')
        self.write('references/myexample.bib', '% no synthetic claims')
        self.write('docs/00_项目事实库.md', 'F-TEST-01 未知的项目批准号')
        self.state = p.initialize(self.root)
        self.state['project'].update(type='NSFC_General', grant_type='面上项目', layout='three-part',
                                    length_budget='30 pages', body_files={
                                        'part_one': ['extraTex/body.tex'],
                                        'foundation': ['extraTex/foundation.tex'],
                                        'statements': ['extraTex/statements.tex']})

    def write(self, rel, value):
        target = self.root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value, encoding='utf-8')
        return target

    def pdf(self, rel, label='Synthetic test fixture'):
        target = self.root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        doc = fitz.open()
        doc.new_page().insert_text((30, 40), label)
        doc.save(target)
        doc.close()

    def plan(self):
        lines = [line for line in (self.root / 'extraTex/body.tex').read_text().splitlines() if line]
        figures = []
        for index, line in enumerate(lines, 1):
            fid = f'F{index:02d}'
            item = {'id': fid, 'kind': 'background' if index == 1 else 'framework' if index == 2 else 'route',
                    'required': True, 'selected': True, 'source_file': 'extraTex/body.tex',
                    'source_excerpt': line, 'anchor': line, 'caption': 'Synthetic figure ' + fid,
                    'label': 'fig:' + fid, 'width': 0.9, 'gap_ids': [],
                    'prompt': f'docs/figure_specs/{fid}.prompt.md', 'spec': f'docs/figure_specs/{fid}.json',
                    'png': f'figures/{fid}.png', 'pdf': f'figures/{fid}.pdf'}
            if index > 2:
                item['route_id'] = f'R{index-2}'
            figures.append(item)
            self.write(item['prompt'], 'Fixture-only prompt ' + fid)
            self.write(item['spec'], json.dumps({'fixture': True, 'label': fid}))
        self.write('docs/figure_manifest.json', json.dumps({'route_ids': ['R1', 'R2', 'R3'], 'figures': figures}))
        self.write('docs/Figure_Plan.md', 'Fixture figure plan')
        self.write('docs/Figure_Palette.md', 'Fixture palette')
        return figures

    def complete_text(self):
        for stage in p.TEXT:
            for output in a.legacy.expand_stage_outputs(self.root, self.state, stage):
                if output.suffix in ('.md', '.bib') and not output.exists():
                    self.write(str(output.relative_to(self.root)), 'Fixture stage output')
                elif not output.suffix:
                    self.write(str(output.relative_to(self.root) / 'README.md'), 'Fixture directory output')
            if stage == '14_compile':
                self.pdf('main.pdf')
                a.atomic(self.root / 'docs/figure_source/main.text.pdf', (self.root / 'main.pdf').read_bytes())
                self.state['builds']['text'] = {'output': a.sha(self.root / 'main.pdf')}
            self.state['stages'][stage]['status'] = 'in_progress'
            p.finish(self.root, self.state, stage)

    def record_image(self, item, call_id=None):
        p.image_start(self.root, self.state, item['id'])
        target = self.root / item['png']
        target.parent.mkdir(parents=True, exist_ok=True)
        Image.new('RGB', (256, 256), (20, int(item['id'][1:]) * 20, 90)).save(target)
        proof = 'review/figures/' + item['id'] + '.json'
        self.write(proof, json.dumps({'passed': True, 'checks': dict.fromkeys(p.IMAGE_CHECKS, True)}))
        p.image_record(self.root, self.state, item['id'], call_id or 'fixture-call-' + item['id'], proof)

    def test_text_completion_transitions_to_plan(self):
        self.complete_text()
        p.reconcile(self.root, self.state)
        self.assertEqual(p.next_stage(self.state), '15_figure_plan')
        self.assertFalse(p.readiness(self.root, self.state)['illustrated_body_ready'])

    def test_layout_can_finish_before_writing(self):
        self.write('extraTex/body.tex', r'\NSFCBlankPara')
        self.state['stages']['00_layout_resolution']['status'] = 'in_progress'
        p.finish(self.root, self.state, '00_layout_resolution')
        self.assertEqual(p.next_stage(self.state), '01_topic_extraction')

    def test_hard_gap_does_not_prevent_drawing(self):
        self.write('extraTex/foundation.tex', 'The documented project was completed during the previous research period, '
                   'and the approval identifier is \\textbf{【待补 F-TEST-01：项目批准号】}.\n')
        self.complete_text()
        result = p.readiness(self.root, self.state)
        self.assertTrue(result['text_stages_done'])
        self.assertFalse(result['body_pipeline_ready'])
        self.assertEqual(result['next_stage'], '15_figure_plan')

    def test_recursive_activity_ignores_orphans_and_comments(self):
        self.write('extraTex/nested.tex', 'Nested active content.')
        with (self.root / 'extraTex/body.tex').open('a') as out:
            out.write('\n\\input{extraTex/nested.tex}\n% \\input{extraTex/orphan.tex}\n')
        self.write('extraTex/orphan.tex', r'\NSFCBlankPara')
        files = {f.name for f in a.body_files(self.root)}
        self.assertIn('nested.tex', files)
        self.assertNotIn('orphan.tex', files)
        self.assertFalse(a.scan(self.root, self.state)['unfinished_placeholders'])

    def test_symlink_and_traversal_refused(self):
        with self.assertRaises(ValueError):
            a.local(self.root, '../escape.tex')
        (self.root / 'figures').symlink_to(TEST_ROOT, target_is_directory=True)
        with self.assertRaises(ValueError):
            a.local(self.root, 'figures/escape.pdf')

    def test_figures_require_five_independent_calls(self):
        selected = self.plan()
        p.image_start(self.root, self.state, 'F01')
        with self.assertRaisesRegex(ValueError, '不能并发'):
            p.image_start(self.root, self.state, 'F02')
        self.state['figures']['F01']['attempts'][-1]['status'] = 'failed'
        self.state.pop('active_image')
        for item in selected:
            self.record_image(item)
        self.assertTrue(all(p.image_valid(self.root, self.state, i) for i in selected))
        self.assertEqual(len({self.state['figures'][i['id']]['image']['call_id'] for i in selected}), 5)

    def test_reuse_one_call_for_distinct_prompts_refused(self):
        selected = self.plan()
        self.record_image(selected[0], 'fixture-same-call')
        with self.assertRaisesRegex(ValueError, '独立 call_id'):
            self.record_image(selected[1], 'fixture-same-call')

    def test_retries_are_bounded_and_other_figures_can_continue(self):
        self.plan()
        for _ in range(3):
            p.image_start(self.root, self.state, 'F01')
            self.state['figures']['F01']['attempts'][-1]['status'] = 'failed'
            self.state.pop('active_image')
        with self.assertRaises(ValueError):
            p.image_start(self.root, self.state, 'F01')
        p.image_start(self.root, self.state, 'F02')
        self.assertEqual(self.state['active_image'], 'F02')

    def test_changed_prompt_invalidates_only_related_image(self):
        selected = self.plan()
        for item in selected:
            self.record_image(item)
        self.write(selected[2]['prompt'], 'A revised fixture prompt')
        self.assertEqual([p.image_valid(self.root, self.state, i) for i in selected], [True, True, False, True, True])

    def test_insert_twice_preserves_text_fingerprint(self):
        self.complete_text()
        selected = self.plan()
        before = p.stage_inputs(self.root, self.state, '08_reference_alignment')
        for item in selected:
            self.pdf(item['pdf'])
        a.insertion(self.root, selected, True)
        first = (self.root / 'extraTex/body.tex').read_bytes()
        self.assertEqual(a.insertion(self.root, selected, True), [])
        self.assertEqual(first, (self.root / 'extraTex/body.tex').read_bytes())
        self.assertEqual(before, p.stage_inputs(self.root, self.state, '08_reference_alignment'))
        p.reconcile(self.root, self.state)
        self.assertEqual(p.next_stage(self.state), '15_figure_plan')

    def test_nonmanaged_label_collision_rejected(self):
        selected = self.plan()
        for item in selected:
            self.pdf(item['pdf'])
        with (self.root / 'extraTex/body.tex').open('a') as out:
            out.write('\n\\label{fig:F01}\n')
        original = (self.root / 'extraTex/body.tex').read_bytes()
        with self.assertRaisesRegex(ValueError, '标签'):
            a.insertion(self.root, selected, True)
        self.assertEqual(original, (self.root / 'extraTex/body.tex').read_bytes())

    def test_image_replacement_invalidates_final_build(self):
        selected = self.plan()
        for item in selected:
            self.pdf(item['pdf'])
        a.insertion(self.root, selected, True)
        self.pdf('main.pdf')
        self.state['builds']['final'] = {'input': a.build_inputs(self.root), 'output': a.sha(self.root / 'main.pdf')}
        self.assertTrue(p.build_valid(self.root, self.state, 'final'))
        (self.root / selected[0]['pdf']).unlink()
        self.pdf(selected[0]['pdf'], 'Revised synthetic fixture')
        self.assertFalse(p.build_valid(self.root, self.state, 'final'))

    def test_import_is_read_only_and_idempotent(self):
        self.complete_text()
        legacy = copy.deepcopy(self.state)
        legacy['schema_version'] = 2
        for stage in p.TEXT:
            legacy['stages'][stage]['input_sha256'] = a.legacy._fingerprint_paths(self.root, a.legacy.expand_stage_inputs(self.root, legacy, stage))
        a.atomic(self.root / 'docs/workflow_status.yaml', yaml_dump(legacy))
        original = (self.root / 'docs/workflow_status.yaml').read_bytes()
        (self.root / 'docs/figure_source/main.text.pdf').unlink()
        p.initialize(self.root)
        self.assertFalse((self.root / 'docs/figure_source/main.text.pdf').exists())
        state = p.initialize(self.root, apply_import=True)
        p.save(self.root, state)
        self.assertEqual(original, (self.root / 'docs/workflow_status.yaml').read_bytes())
        self.assertEqual(state, p.initialize(self.root))
        p.reconcile(self.root, state)
        self.assertEqual(p.next_stage(state), '15_figure_plan')

    def test_fake_pdf_is_rejected(self):
        bad = self.write('figures/bad.pdf', 'not a PDF')
        with self.assertRaises(Exception):
            a.check_pdf(bad)

    def test_single_raster_slide_rejected(self):
        target = self.root / 'raster.pptx'
        with zipfile.ZipFile(target, 'w') as archive:
            archive.writestr('ppt/presentation.xml', f'<p:presentation xmlns:p="{a.NS["p"]}" xmlns:r="{a.NS["r"]}"><p:sldIdLst><p:sldId id="256" r:id="rId1"/></p:sldIdLst><p:sldSz cx="1000" cy="1000"/></p:presentation>')
            archive.writestr('ppt/_rels/presentation.xml.rels', '<Relationships><Relationship Id="rId1" Target="slides/slide1.xml"/></Relationships>')
            archive.writestr('ppt/slides/slide1.xml', f'<p:sld xmlns:p="{a.NS["p"]}" xmlns:a="{a.NS["a"]}"><p:pic/></p:sld>')
        with self.assertRaisesRegex(ValueError, 'PPTX 包结构|可编辑文字'):
            a.check_deck(target, 1)


def yaml_dump(value):
    import yaml
    return yaml.safe_dump(value, allow_unicode=True)


if __name__ == '__main__':
    unittest.main()
