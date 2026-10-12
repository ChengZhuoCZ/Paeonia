#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/classical_analysis_proof_prose.md').read_text(encoding='utf-8')
protocol=(ROOT/'protocols/05a_style_distillation.md').read_text(encoding='utf-8')
realize=(ROOT/'protocols/05b_style_realization.md').read_text(encoding='utf-8')
ledger=(ROOT/'profiles/classical_analysis_proof_prose.ledger.yaml').read_text(encoding='utf-8')

fail=[]
def before(text,a,b,label):
    ia,ib=text.find(a),text.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)

before(skill,'### Pass 4 — Style-corpus distillation prepass','### Pass 6 — Proof-core drafting','style_before_proof')
before(skill,'### Pass 6 — Proof-core drafting','### Pass 7 — ProofCoreGate','proof_before_gate')
before(skill,'### Pass 7 — ProofCoreGate','### Pass 11 — Introduction reconstruction','gate_before_intro')
before(state,'STYLE_EXTRACT','PROOF_CORE','state_style_before_proof')
before(state,'PROOF_CORE','FRONTMATTER','state_proof_before_frontmatter')

checks={
    'two_ledgers': 'LanguageStyleLedger' in protocol and 'MathematicalWritingStyleLedger' in protocol,
    'stratified_sampling': 'Stratified sampling' in protocol,
    'evidence_requirement': 'Evidence requirement' in protocol,
    'no_source_sentences': 'must **not** store source sentences' in protocol,
    'obstruction_driven': 'Obstacle-driven exposition' in profile,
    'dependency_lemma': 'Theorem and lemma ecology' in profile,
    'compress_pedagogy_before_logic': 'Compress **pedagogy before logic**' in profile,
    'style_drift': 'GENERIC-PROSE-DRIFT' in realize,
    'ledger_split_serialized': 'language_style:' in ledger and 'mathematical_writing_style:' in ledger,
    'style_fidelity_gate': 'STYLE-LEDGER-FIDELITY' in skill,
}
for k,v in checks.items():
    if not v: fail.append(k)

names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for i in range(1,14):
    prefix=f'{i:02d}_'
    if not any(n.startswith(prefix) for n in names):
        fail.append('missing_regression_'+prefix)

if fail:
    print('V120_CONTRACT_FAIL')
    for x in fail: print(x)
    sys.exit(1)
print('V120_CONTRACT_PASS')
