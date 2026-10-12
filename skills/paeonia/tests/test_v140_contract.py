#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
distill=(ROOT/'protocols/05g_paragraph_fingerprint_distillation.md').read_text(encoding='utf-8')
realize=(ROOT/'protocols/05h_paragraph_fingerprint_realization.md').read_text(encoding='utf-8')
submission=(ROOT/'protocols/11_submission_gate.md').read_text(encoding='utf-8')
fail=[]
def before(t,a,b,label):
    ia,ib=t.find(a),t.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)
before(skill,'### Pass 15 — Authorial-decision pass','### Pass 16 — Paragraph-fingerprint realization','decision_before_para')
before(skill,'### Pass 16 — Paragraph-fingerprint realization','### Pass 17 — Mathematical-transition pass','para_before_transition')
before(state,'AUTHORIAL_DECISION','PARAGRAPH_RHYTHM','state_decision_before_para')
before(state,'PARAGRAPH_RHYTHM','MATHEMATICAL_TRANSITIONS','state_para_before_transition')
checks={
 'constitutional':'C0.10 — Paragraph boundaries are mathematical decisions' in skill,
 'third_ledger':'ParagraphFingerprintLedger' in skill,
 'boundary_taxonomy':'OBLIGATION_SHIFT' in distill and 'LEGALITY_CHECK' in distill and 'EQUALITY_RIGIDITY' in distill,
 'numeric_non_target':'numerical' in realize.lower() and 'never target source medians' in realize.lower(),
 'role_sensitive':all(x in realize for x in ['ROUTINE','STRUCTURAL','DELICATE','BRIDGE','SURPRISING','CLOSURE']),
 'gate':'PARAGRAPH-FINGERPRINT-FIDELITY' in submission and 'PARAGRAPH-FINGERPRINT-FIDELITY' in skill,
 'schema':(ROOT/'schemas/paragraph_fingerprint.yaml').exists(),
 'profile':(ROOT/'profiles/classical_analysis_paragraph_fingerprint.md').exists(),
 'signature':(ROOT/'profiles/classical_analysis_paragraph_fingerprint.signature.json').exists(),
 'tools':(ROOT/'tools/paragraph_fingerprint.py').exists() and (ROOT/'tools/paragraph_fingerprint_audit.py').exists(),
}
for k,v in checks.items():
    if not v: fail.append(k)
names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for i in range(1,24):
    if not any(n.startswith(f'{i:02d}_') for n in names): fail.append(f'missing_regression_{i:02d}')
if fail:
    print('V140_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V140_CONTRACT_PASS')
