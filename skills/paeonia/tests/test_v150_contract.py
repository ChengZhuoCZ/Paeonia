#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
distill=(ROOT/'protocols/05i_section_narrative_fingerprint_distillation.md').read_text(encoding='utf-8')
realize=(ROOT/'protocols/05j_section_narrative_fingerprint_realization.md').read_text(encoding='utf-8')
submission=(ROOT/'protocols/11_submission_gate.md').read_text(encoding='utf-8')
fail=[]
def before(t,a,b,label):
    ia,ib=t.find(a),t.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)
before(state,'PARAGRAPH_FINGERPRINT_LOCK','SECTION_FINGERPRINT_LOCK','paragraph_before_section_fingerprint')
before(state,'MANUSCRIPT_ARCHITECTURE','SECTION_NARRATIVE','architecture_before_section_realization')
before(state,'SECTION_NARRATIVE','THEOREM_FRAME','section_before_theorem_frame')
checks={
 'constitutional':'C0.11 — Sections are obligation families, not containers' in skill,
 'section_ledger':'SectionNarrativeFingerprintLedger' in skill,
 'latency_modes':all(x in distill and x in realize for x in ['IMMEDIATE','MOTIVATED','DEVELOPED','DEFERRED']),
 'boundary_reasons':'OBLIGATION_FAMILY' in distill and 'METHOD_FAMILY_SHIFT' in distill and 'SYNTHESIS_OR_RETURN' in distill,
 'no_forced_alternation':'Do **not** enforce alternation' in distill and 'Do not force alternation' in realize,
 'subsection_suppression':'Suppress subsections when' in distill and 'Suppress a subsection when' in realize,
 'numeric_non_target':'numeric_targets_forbidden' in distill and 'Never move a theorem earlier merely to satisfy a style profile' in realize,
 'gate':'SECTION-NARRATIVE-FIDELITY' in skill and 'SECTION-NARRATIVE-FIDELITY' in submission,
 'schema':(ROOT/'schemas/section_narrative_fingerprint.yaml').exists(),
 'profile':(ROOT/'profiles/classical_analysis_section_fingerprint.md').exists(),
 'signature':(ROOT/'profiles/classical_analysis_section_fingerprint.signature.json').exists(),
 'tools':(ROOT/'tools/section_narrative_fingerprint.py').exists() and (ROOT/'tools/section_narrative_audit.py').exists(),
 'checklist':(ROOT/'checklists/section_narrative_architecture.md').exists(),
}
for k,v in checks.items():
    if not v: fail.append(k)
names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for i in range(1,30):
    if not any(n.startswith(f'{i:02d}_') for n in names): fail.append(f'missing_regression_{i:02d}')
if fail:
    print('V150_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V150_CONTRACT_PASS')
