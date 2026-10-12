#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
para=(ROOT/'protocols/04d_introduction_paragraph_architecture.md').read_text(encoding='utf-8')
prose=(ROOT/'protocols/04e_introduction_prose_realization.md').read_text(encoding='utf-8')
cold=(ROOT/'protocols/04f_introduction_cold_read.md').read_text(encoding='utf-8')
gate=(ROOT/'protocols/04g_introduction_prose_integrity.md').read_text(encoding='utf-8')
plan=yaml.safe_load((ROOT/'schemas/introduction_paragraph_plan.yaml').read_text(encoding='utf-8'))
sys.path.insert(0, str(ROOT/'tools'))
from execution_planner import plan as execution_plan
reconstructed_intro=execution_plan(dict(writing_mode='RECONSTRUCT', editable_scope=['Introduction'], has_math_sources=True))
polished_intro=execution_plan(dict(writing_mode='LOCAL_POLISH', editable_scope=['Introduction'], has_editing_baseline=True))
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,12,0),
 'trusted_proof_preserved':'proof_correctness_mode: trusted_source' in skill,
 'intro_from_scratch_when_reconstructing':'SOURCE-INDEPENDENCE' in reconstructed_intro['applicable_gates'] and 'SOURCE-INDEPENDENCE' not in polished_intro['applicable_gates'],
 'source_intro_not_template':'source Introduction sentences, paragraph order, theorem latency, citation choreography' in skill,
 'paragraph_plan':'IntroductionParagraphPlan' in skill and plan.get('reconstruction_mode')=='from_scratch',
 'paragraph_roles':'one dominant role' in para.lower() and 'entry_anchor' in para and 'exit_anchor' in para,
 'specialist_compression':'research-specialist compression' in prose.lower(),
 'claim_centered_literature':'result-centered' in prose.lower(),
 'continuity_pass':'first and last sentence' in prose.lower(),
 'cold_read':'Paragraph-removal test' in cold,
 'prose_gate':'INTRODUCTION-PROSE-INTEGRITY' in skill and 'From-scratch realization' in gate,
 'state_plan_before_frontmatter':'IntroductionParagraphPlan' in state and state.index('INTRODUCTION_NARRATIVE') < state.index('FRONTMATTER'),
 'new_tool':(ROOT/'tools/introduction_prose_audit.py').exists(),
 'behavioral_cases':all((ROOT/'tests/behavioral_cases'/next(p.name for p in (ROOT/'tests/behavioral_cases').glob(f'{i:02d}_*.yaml'))).exists() for i in range(56,66)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V1_12_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_12_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
