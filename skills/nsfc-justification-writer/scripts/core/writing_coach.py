#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from .ai_integration import AIIntegration
from .config_access import get_bool, get_mapping, get_str
from .diagnostic import run_tier1
from .dimension_coverage import format_dimension_coverage_markdown
from .io_utils import read_text_streaming
from .limits import ai_max_input_chars, writing_coach_preview_chars
from .prompt_templates import get_prompt
from .security import discover_target_relpath, resolve_target_path
from .style import get_style_mode, style_preamble_text
from .term_consistency import CrossChapterValidator, format_term_matrices_markdown
from .word_target import WordTargetSpec, resolve_word_target

WritingStage = Literal["auto", "skeleton", "draft", "revise", "polish", "final"]


@dataclass(frozen=True)
class CoachInput:
    stage: WritingStage
    style_mode: str
    style_preamble: str
    info_form_text: str
    tex_text: str
    tier1: Dict[str, Any]
    term_matrix_md: str
    word_target: WordTargetSpec
    dimension_coverage_md: str


def _infer_stage(
    *,
    tex_text: str,
    tier1: Dict[str, Any],
    word_target: int,
    tol: int,
    fallback_rules: Optional[Dict[str, Any]] = None,
) -> WritingStage:
    rules = fallback_rules or {}
    draft_ratio = float(rules.get("draft_threshold_ratio", 0.4))
    draft_min_chars = int(rules.get("draft_min_chars", 600))
    if not tex_text.strip():
        return "skeleton"
    if not bool(tier1.get("structure_ok")):
        return "skeleton"
    wc = int(tier1.get("word_count", 0))
    if wc < max(int(word_target * draft_ratio), draft_min_chars):
        return "draft"
    if not bool(tier1.get("citation_ok")) or tier1.get("avoid_commands_hits"):
        return "revise"
    if abs(wc - word_target) > tol:
        return "polish"
    return "final"


def _suggest_questions(
    *,
    stage: WritingStage,
    tier1: Dict[str, Any],
    dimension_coverage_md: str,
    style_mode: str,
) -> List[str]:
    base: List[str]
    if style_mode == "engineering":
        base = [
            "你的一句话问题定义是什么（评审听得懂的版本）？",
            "应用场景/对象/边界条件是什么（哪些情况不适用）？",
            "现有方案的 2–4 条关键不足/瓶颈分别是什么（尽量可量化/可验证；并避免“凭空新增约束”）？",
            "这些瓶颈如何对应到你的科学问题约束（建议逐条写“瓶颈→约束”映射，避免逻辑缝隙）？",
            "你的科学问题是否写成“疑问句”（追问认知缺口），并避免“能否构建/开发/实现...”这类研究目标句式？",
            "你的核心科学假设是否是“陈述句”（预测性结果），并避免“在...验证中/通过...验证”这类验证方式表述？",
            "你准备如何验证（对照实验/数据来源/评价指标/统计检验）？",
            "本项目相对现有工作的差异化切口是什么（方法学/系统设计/流程改造中的关键一处）？",
        ]
    else:
        base = [
            "你的一句话问题定义是什么（评审听得懂的版本）？",
            "现有方案在理论层面的 2–4 条关键瓶颈分别是什么（如假设过强/框架不统一/因果缺失/界不紧）？",
            "这些瓶颈如何对应到你的科学问题约束（建议逐条写“瓶颈→约束”映射，避免逻辑缝隙）？",
            "你的关键科学问题是否写成“疑问句”（追问认知缺口），并避免“能否构建/开发/实现...”这类研究目标句式？",
            "你的核心科学假设是否是“陈述句”（预测性结果），并覆盖科学问题中的关键约束（在假设中给出应对策略）？",
            "你准备如何验证（理论证明/定理/数值验证/对照实验）？",
            "本项目相对现有工作的理论差异化切口是什么（如新表征/新方法学/统一框架）？",
        ]
    if "缺失维度" in dimension_coverage_md:
        base.append("哪些维度缺失？请优先补齐“价值/现状/科学问题/切入点”对应段落。")
    if stage in {"skeleton", "draft"}:
        base.append("正文范围和现有结构命令是否已确认？若需要调整标题，请先明确授权范围。")
    if not bool(tier1.get("citation_ok", True)):
        base.append("缺失引用的 bibkey 准备怎么补：提供 DOI/链接（或可核验题录信息）并补齐 references/*.bib？")
    if tier1.get("missing_doi_keys"):
        base.append("已存在的引用 bibkey 是否补齐 DOI 字段（建议补齐以便可核验）？")
    return base[:8]


def _copyable_prompt(*, stage: WritingStage, style_preamble: str) -> str:
    focus = {
        "skeleton": "先确认正文边界并写出论证要点（不写未经核验的引用）。",
        "draft": "只写用户指定正文范围的段落（不新增引用）。",
        "revise": "只重写/压缩用户指定正文范围，修复逻辑跳跃与不可核验表述（不新增引用）。",
        "polish": "先核对论证、事实和引用未改变，再按专业可读性准则润色语言（不新增引用、不删除必要术语或限定）。",
        "final": "按 DoD 做最终自检：结构/字数/引用/术语一致性（不新增引用）。",
        "auto": "按当前阶段输出下一步。",
    }.get(stage, "按当前阶段输出下一步。")

    pre = style_preamble.strip()
    return (
        "请用 nsfc-justification-writer 的写作规范帮我修改立项依据：\n"
        + "约束：\n"
        + "- 不修改任何标题层级（仅改正文段落）\n"
        + '- 不新增引用；如必须引用，请先提示“需用户提供 DOI/链接（或可核验题录信息），并先补齐 references/*.bib”\n'
        + "- 避免不可核验绝对表述（国际领先/国内首次等），改为可验证指标/对照维度\n"
        + "- 科学问题必须是“疑问句”（追问认知缺口），避免写成“能否构建/开发/实现...”的研究目标\n"
        + "- 科学假设必须是“陈述句”（预测性结果），避免写“在...验证中/通过...验证”等验证方式\n"
        + "- polish 阶段先保护事实/论证/引用/术语/限定/LaTeX 结构，再处理长句、指代、缩写界定与段内衔接；不为通俗而删除专业信息\n"
        + ((pre + "\n") if pre else "")
        + f"任务：{focus}\n"
        + "输入：我会提供（1）信息表（2）当前 tex（如有）。\n"
        + "输出：只给出需要替换的正文文本（不要包裹 \\subsubsection）。\n"
    )


def _fallback_markdown(inp: CoachInput, stage: WritingStage) -> str:
    qs = _suggest_questions(
        stage=stage,
        tier1=inp.tier1,
        dimension_coverage_md=inp.dimension_coverage_md,
        style_mode=inp.style_mode,
    )
    tasks = {
        "skeleton": [
            "确认用户指定的正文范围和已有结构命令，不新增标题或环境。",
            "先写领域事实、已有证据和认知缺口的要点句，不堆引用。",
            "明确“科学问题（疑问句）→科学假设（陈述句）”与“瓶颈→约束”映射，再做独立引用/术语检查。",
        ],
        "draft": [
            "选择一个用户确认的正文范围先写成 1–2 段。",
            "在现状/缺口所在位置点明瓶颈，并把瓶颈收束成科学问题约束。",
            "沿现有结构扩写到用户要求的长度，不改变标题或命令。",
        ],
        "revise": [
            "先修复缺失引用 key（或删掉未核验引用）。",
            "把不可核验表述改成“可对照维度 + 指标 + 预期改善幅度/区间”。",
            "检查科学问题是否写成疑问句、假设是否为预测性陈述且不含验证方式；统一术语/缩写口径并与用户指定的相关章节对齐。",
        ],
        "polish": [
            "第一步只核对论证、事实、引用、术语边界和 LaTeX 结构，列出不可改变的科学含义。",
            "第二步定位长句层级、指代/缩写界定、抽象名词关系和段内衔接问题；在不损失必要限定的前提下拆句、补过渡或克制修饰。",
            "确认已清楚的专业表述不被强行通俗化，并增强结尾到用户指定研究内容的自然过渡。",
        ],
        "final": [
            "最后跑一遍 diagnose（必要时开 tier2）并修复剩余问题。",
            "跑 terms 确认跨章节术语一致。",
            "确认输出只改用户授权的正文范围，且没有未经授权的结构/配置命令。",
        ],
    }.get(stage, ["按当前阶段推进。"])

    md = [
        "## 当前阶段判断",
        f"阶段：`{stage}`（可用 `scripts/run.py coach --stage ...` 强制指定）。",
        "",
        "## 本轮只做三件事",
        "1) " + tasks[0],
        "2) " + tasks[1],
        "3) " + tasks[2],
        "",
        "## 需要你补充/确认的问题（不超过 8 个）",
    ] + [f"- {q}" for q in qs] + [
        "",
        "## 下一步可直接复制的写作提示词",
        "```",
        _copyable_prompt(stage=stage, style_preamble=inp.style_preamble).rstrip(),
        "```",
        "",
        f"## 目标字数：{inp.word_target.target}（容差 ±{inp.word_target.tolerance}，来源：{inp.word_target.source}{'；线索：'+inp.word_target.evidence if inp.word_target.evidence else ''}）",
        "",
        "## 内容维度覆盖（价值/现状/科学问题/切入点）",
        inp.dimension_coverage_md.strip(),
    ]
    return "\n".join(md).strip() + "\n"


async def _infer_stage_auto(
    *,
    tex_text: str,
    tier1: Dict[str, Any],
    word_target: WordTargetSpec,
    fallback_rules: Dict[str, Any],
    ai: Optional[AIIntegration],
    cache_dir: Optional[Path],
    config: Dict[str, Any],
) -> WritingStage:
    fallback_stage = _infer_stage(
        tex_text=tex_text,
        tier1=tier1,
        word_target=word_target.target,
        tol=word_target.tolerance,
        fallback_rules=fallback_rules,
    )

    coach_cfg = get_mapping(config, "writing_coach")
    if not get_bool(coach_cfg, "enable_ai_stage_inference", True):
        return fallback_stage
    ai_mode = get_str(coach_cfg, "ai_inference_mode", "auto").strip().lower()
    if ai is None or not ai.is_available():
        if ai_mode == "ai_only":
            return "auto"
        return fallback_stage

    preview_chars = writing_coach_preview_chars(config)
    preview = (tex_text or "")[:preview_chars]
    prompt = f"""
请分析以下立项依据文本，判断当前处于哪个写作阶段。

写作阶段定义：
1) skeleton（骨架）：刚起步，仅有结构框架，内容严重不足
2) draft（草稿）：有基本内容，但逻辑不完整/论证不充分/需要大量补充
3) revise（修订）：内容基本完整，但有问题（引用缺失/不可核验表述/逻辑跳跃）
4) polish（润色）：内容完整且无重大质量问题，但字数不达标需要压缩/扩写
5) final（定稿）：内容完整、质量合格、字数达标，可最终检查

输入信息：
- 当前字数：{tier1.get('word_count', 0)}（目标：{word_target.target}，容差：±{word_target.tolerance}）
- 结构状态：{'✅ 已按配置检查' if tier1.get('structure_check_enabled') and tier1.get('structure_ok') else ('⚠️ 需按配置修复' if tier1.get('structure_check_enabled') else 'ℹ️ 未启用固定结构检查')}（检测到 subsubsection：{tier1.get('subsubsection_count', 0)}）
- 引用状态：{'✅ 正常' if tier1.get('citation_ok') else '❌ 缺失引用'}
- 质量问题：危险命令 {tier1.get('avoid_commands_hits', [])}；措辞风险由宿主 AI 按 references/boastful_expression_guidelines.md 复核

文本内容（去注释后，最多 {preview_chars} 字）：{preview}

返回 JSON：
{{
  "stage": "skeleton|draft|revise|polish|final",
  "confidence": 0.0,
  "reasoning": "判断依据（2-3 句）",
  "next_steps": ["下一步建议1", "下一步建议2", "下一步建议3"],
  "blocked_by": ["引用缺失", "不可核验表述"]
}}
""".strip()

    def _fallback() -> Dict[str, Any]:
        return {"stage": fallback_stage}

    obj = await ai.process_request(
        task="infer_writing_stage",
        prompt=prompt,
        fallback=_fallback,
        output_format="json",
        cache_dir=cache_dir,
    )
    if isinstance(obj, dict):
        stage = str(obj.get("stage") or "").strip()
        if stage in {"skeleton", "draft", "revise", "polish", "final"}:
            return stage  # type: ignore[return-value]
    return fallback_stage


async def coach_markdown(
    *,
    skill_root: Path,
    project_root: Path,
    config: Dict[str, Any],
    stage: WritingStage = "auto",
    info_form_text: str = "",
    ai: Optional[AIIntegration] = None,
) -> str:
    skill_root = Path(skill_root).resolve()
    project_root = Path(project_root).resolve()
    targets = get_mapping(config, "targets")
    rel = get_str(targets, "justification_tex", "").strip()
    if not rel:
        rel = discover_target_relpath(project_root) or ""
    target = resolve_target_path(project_root, rel) if rel else (project_root / ".__no_target__.tex").resolve()
    tex_text = read_text_streaming(target).text if target.exists() else ""
    style_mode = get_style_mode(config)
    style_preamble = style_preamble_text(style_mode).strip()

    tier1_obj = run_tier1(tex_text=tex_text, project_root=project_root, config=config)
    tier1 = {
        "structure_ok": tier1_obj.structure_ok,
        "structure_check_enabled": tier1_obj.structure_check_enabled,
        "subsubsection_count": tier1_obj.subsubsection_count,
        "missing_subsubsections": tier1_obj.missing_subsubsections,
        "citation_ok": tier1_obj.citation_ok,
        "missing_citation_keys": tier1_obj.missing_citation_keys,
        "missing_doi_keys": tier1_obj.missing_doi_keys,
        "word_count": tier1_obj.word_count,
        "avoid_commands_hits": tier1_obj.avoid_commands_hits,
    }

    # 术语矩阵（尽量不失败）
    related = get_mapping(targets, "related_tex")
    files = {"立项依据": target}
    for label, relpath in related.items():
        files[label] = (project_root / str(relpath)).resolve()
    terminology_cfg = get_mapping(config, "terminology")
    term_matrix_md = format_term_matrices_markdown(CrossChapterValidator(files=files, terminology_config=terminology_cfg).build())

    word_spec = resolve_word_target(
        config=config,
        user_intent_text="",
        info_form_text=info_form_text,
    )

    coach_cfg = get_mapping(config, "writing_coach")
    fallback_rules = get_mapping(coach_cfg, "fallback_rules")

    ai_obj = ai
    if ai_obj is None:
        ai_cfg = get_mapping(config, "ai")
        ai_obj = AIIntegration(enable_ai=get_bool(ai_cfg, "enabled", True), config=config)

    ai_cfg = get_mapping(config, "ai")
    cache_dir = (skill_root / get_str(ai_cfg, "cache_dir", "tests/_artifacts/cache/ai")).resolve()

    auto_stage = await _infer_stage_auto(
        tex_text=tex_text,
        tier1=tier1,
        word_target=word_spec,
        fallback_rules=fallback_rules,
        ai=ai_obj,
        cache_dir=cache_dir,
        config=config,
    )
    chosen_stage: WritingStage = auto_stage if stage == "auto" else stage

    # 内容维度覆盖是可选 legacy 辅助；默认不把固定四维度当作验收门槛。
    dimension_md = ""
    structure_cfg = get_mapping(config, "structure")
    if not get_bool(structure_cfg, "enable_dimension_coverage_check", False):
        dimension_md = "（未启用内容维度覆盖检查）"
    else:
        try:
            from .dimension_coverage import DimensionCoverageAI

            dim_obj = await DimensionCoverageAI(ai_obj).check(
                tex_text=tex_text,
                max_chars=ai_max_input_chars(config),
                cache_dir=cache_dir,
            )
            dimension_md = format_dimension_coverage_markdown(dim_obj)
        except (ModuleNotFoundError, ImportError, RuntimeError):
            dimension_md = "（内容维度覆盖检查不可用）"

    inp = CoachInput(
        stage=chosen_stage,
        style_mode=style_mode,
        style_preamble=style_preamble,
        info_form_text=info_form_text,
        tex_text=tex_text,
        tier1=tier1,
        term_matrix_md=term_matrix_md,
        word_target=word_spec,
        dimension_coverage_md=dimension_md,
    )

    prompt = get_prompt(
        name="writing_coach",
        default="",
        skill_root=skill_root,
        config=config,
        variant=get_str(config, "active_preset", "").strip() or None,
    )

    def _fallback() -> str:
        return _fallback_markdown(inp, chosen_stage)

    if not prompt.strip():
        return _fallback()

    payload = {
        "stage": chosen_stage,
        "info_form": (info_form_text or "").strip(),
        "tier1": tier1,
        "term_matrix": (term_matrix_md or "").strip(),
        "word_target": {"target": word_spec.target, "tolerance": word_spec.tolerance, "source": word_spec.source},
        "dimension_coverage": dimension_md,
        "tex": (tex_text or "")[:12000],
    }
    filled = prompt.format(
        stage=chosen_stage,
        style_preamble=style_preamble,
        info_form=payload["info_form"],
        tier1_json=json.dumps(payload["tier1"], ensure_ascii=False, indent=2),
        term_matrix=payload["term_matrix"],
        tex=payload["tex"],
    )

    obj = await ai_obj.process_request(task="writing_coach", prompt=filled, fallback=_fallback, output_format="text")
    return str(obj).strip() + "\n"
