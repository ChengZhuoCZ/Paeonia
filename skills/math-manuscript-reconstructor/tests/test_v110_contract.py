#!/usr/bin/env python3
"""Backward-compatibility checks for the v1.1 proof-first invariants."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/classical_analysis_proof_prose.md').read_text(encoding='utf-8')
ledger=(ROOT/'profiles/classical_analysis_proof_prose.ledger.yaml').read_text(encoding='utf-8')

fail=[]
def before(text,a,b,label):
    ia,ib=text.find(a),text.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)

before(skill,'### Pass 6 — Proof-core drafting','### Pass 7 — ProofCoreGate','proof_before_gate')
before(skill,'### Pass 7 — ProofCoreGate','### Pass 8 — Fresh manuscript architecture','gate_before_architecture')
before(skill,'### Pass 8 — Fresh manuscript architecture','### Pass 11 — Introduction reconstruction','architecture_before_intro')
before(skill,'### Pass 11 — Introduction reconstruction','### Pass 12 — Abstract reconstruction','intro_before_abstract')
before(state,'PROOF_CORE','PROOF_CORE_GATE','state_proof_before_gate')
before(state,'PROOF_CORE_GATE','FRONTMATTER','state_gate_before_frontmatter')

checks={
    'profile_anti_copy':'source-independent style profile' in profile,
    'style_ledger_no_phrase_storage':'source_phrase_storage: forbidden' in ledger,
    'research_projection':'Research-article projection' in profile,
    'purpose_formula_consequence':'mathematical purpose → displayed relation → mathematical consequence' in profile,
}
for k,v in checks.items():
    if not v: fail.append(k)

regress=[f'{i:02d}_' for i in range(1,11)]
names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for prefix in regress:
    if not any(n.startswith(prefix) for n in names): fail.append('missing_regression_'+prefix)

if fail:
    print('V110_COMPAT_FAIL')
    for x in fail: print(x)
    sys.exit(1)
print('V110_COMPAT_PASS')
