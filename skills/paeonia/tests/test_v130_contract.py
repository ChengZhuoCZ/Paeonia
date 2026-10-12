#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
residue=(ROOT/'protocols/05c_generative_residue_diagnosis.md').read_text(encoding='utf-8')
decision=(ROOT/'protocols/05d_authorial_decision_pass.md').read_text(encoding='utf-8')
transitions=(ROOT/'protocols/05e_mathematical_transition_pass.md').read_text(encoding='utf-8')
cold=(ROOT/'protocols/05f_cold_author_compression.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/classical_analysis_proof_prose.md').read_text(encoding='utf-8')
ledger=(ROOT/'schemas/style_ledger.yaml').read_text(encoding='utf-8')
submission=(ROOT/'protocols/11_submission_gate.md').read_text(encoding='utf-8')

fail=[]
def before(text,a,b,label):
    ia,ib=text.find(a),text.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)

before(skill,'### Pass 14 — Generative-residue diagnosis','### Pass 15 — Authorial-decision pass','residue_before_decision')
before(skill,'### Pass 15 — Authorial-decision pass','### Pass 17 — Mathematical-transition pass','decision_before_transition')
before(skill,'### Pass 17 — Mathematical-transition pass','### Pass 18 — Cold-author compression','transition_before_cold')
before(state,'RESIDUE_DIAGNOSIS','AUTHORIAL_DECISION','state_residue_before_decision')
before(state,'AUTHORIAL_DECISION','COLD_AUTHOR','state_decision_before_cold')

checks={
    'constitutional_rule':'Authorial mathematical prose, never cosmetic humanization' in skill,
    'random_synonym_forbidden':'random synonym substitution' in skill.lower(),
    'detector_optimization_forbidden':'ai-detector score' in skill.lower(),
    'residue_classes':'GR-1' in residue and 'GR-8' in residue,
    'no_synonymize_action':'Never use `SYNONYMIZE`' in residue,
    'six_roles':all(x in decision for x in ['ROUTINE','STRUCTURAL','DELICATE','SURPRISING','BRIDGE','CLOSURE']),
    'controlled_implicitness':all(x in decision for x in ['MUST_EXPLICIT','MAY_BE_IMPLICIT','SHOULD_BE_IMPLICIT']),
    'transition_semantics':'MATHEMATICAL-TRANSITIONS' in skill and 'synonym' in transitions.lower(),
    'cold_math_freeze':'MathLedger' in cold and 'read-only' in cold,
    'profile_overlay':'Authorial Mathematical Prose Overlay' in profile,
    'ledger_overlay':'authorial_naturalization:' in ledger,
    'release_gates':all(x in submission for x in ['GENERATIVE-RESIDUE','AUTHORIAL-DECISION','MATHEMATICAL-TRANSITIONS','COLD-AUTHOR']),
    'diagnostic_tools':all((ROOT/'tools'/x).exists() for x in ['phrase_recurrence_audit.py','prose_rhythm_audit.py','equation_prose_redundancy.py','transition_density.py']),
}
for k,v in checks.items():
    if not v: fail.append(k)

names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for i in range(1,19):
    prefix=f'{i:02d}_'
    if not any(n.startswith(prefix) for n in names): fail.append('missing_regression_'+prefix)

if fail:
    print('V130_CONTRACT_FAIL')
    for x in fail: print(x)
    sys.exit(1)
print('V130_CONTRACT_PASS')
