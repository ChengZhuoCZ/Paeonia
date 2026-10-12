#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
distill=(ROOT/'protocols/05k_whole_paper_narrative_fingerprint_distillation.md').read_text(encoding='utf-8')
realize=(ROOT/'protocols/05l_whole_paper_narrative_fingerprint_realization.md').read_text(encoding='utf-8')
submission=(ROOT/'protocols/11_submission_gate.md').read_text(encoding='utf-8')
fail=[]
def before(t,a,b,label):
    ia,ib=t.find(a),t.find(b)
    if ia<0 or ib<0 or ia>=ib: fail.append(label)
before(state,'SECTION_FINGERPRINT_LOCK','WHOLE_PAPER_FINGERPRINT_LOCK','section_before_whole_fingerprint')
before(state,'WHOLE_PAPER_FINGERPRINT_LOCK','STYLE_QUARANTINE','whole_before_style_quarantine')
before(state,'MANUSCRIPT_ARCHITECTURE','WHOLE_PAPER_NARRATIVE','architecture_before_whole_realization')
before(state,'WHOLE_PAPER_NARRATIVE','SECTION_NARRATIVE','whole_before_section_realization')
checks={
 'constitutional':'C0.12 — Whole-paper mass follows the proof spine' in skill,
 'whole_ledger':'WholePaperNarrativeFingerprintLedger' in skill,
 'statement_activation_split':'Separate statement exposure from proof activation' in distill,
 'spine_types':'ENGINE_THEN_ASSEMBLY' in distill and 'REGIME_SPLIT_REJOIN' in distill and 'CLASSIFICATION_FUNNEL' in distill,
 'technical_shapes':'COMPACT_PEAK' in distill and 'TWO_PEAK' in distill and 'REGIME_CLUSTER' in distill,
 'frontmatter_compression':'lossy semantic projection' in distill.lower() and 'Do not tune Introduction length' in skill,
 'appendix_test':'Appendix necessity test' in distill and 'Appendix decision table' in realize,
 'no_proof_debt':'hiding a proof gap' in distill and 'proof-debt storage' in realize,
 'no_mandatory_conclusion':'Conclusion' in distill and 'not mandatory' in distill,
 'numeric_non_target':'numeric_targets_forbidden' in distill and 'source_frontmatter_ratio_reuse: forbidden' in skill,
 'gate':'WHOLE-PAPER-NARRATIVE-FIDELITY' in skill and 'WHOLE-PAPER-NARRATIVE-FIDELITY' in submission,
 'schema':(ROOT/'schemas/whole_paper_narrative_fingerprint.yaml').exists(),
 'profile':(ROOT/'profiles/classical_analysis_whole_paper_fingerprint.md').exists(),
 'signature':(ROOT/'profiles/classical_analysis_whole_paper_fingerprint.signature.json').exists(),
 'tools':(ROOT/'tools/whole_paper_narrative_fingerprint.py').exists() and (ROOT/'tools/whole_paper_narrative_audit.py').exists(),
 'checklist':(ROOT/'checklists/whole_paper_narrative_architecture.md').exists(),
}
for k,v in checks.items():
    if not v: fail.append(k)
names=[p.name for p in (ROOT/'tests/regression_cases').glob('*.md')]
for i in range(1,38):
    if not any(n.startswith(f'{i:02d}_') for n in names): fail.append(f'missing_regression_{i:02d}')
if fail:
    print('V160_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V160_CONTRACT_PASS')
