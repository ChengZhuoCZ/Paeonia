#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
amb=(ROOT/'protocols/04h_narrative_ambition.md').read_text(encoding='utf-8')
amp=(ROOT/'protocols/04i_narrative_amplification.md').read_text(encoding='utf-8')
gate=(ROOT/'protocols/04j_editorial_impact_gate.md').read_text(encoding='utf-8')
ledger=yaml.safe_load((ROOT/'schemas/narrative_ambition_ledger.yaml').read_text(encoding='utf-8'))
gates=yaml.safe_load((ROOT/'registry/gates.yaml').read_text(encoding='utf-8'))['release_blockers']
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,13,0),
 'trusted_proof_preserved':'proof_correctness_mode: trusted_source' in skill,
 'intro_from_scratch_preserved':'introduction_reconstruction_mode: from_scratch' in skill,
 'narrative_ambition':'NarrativeAmbitionLedger' in skill and 'strongest defensible mathematical position' in amb,
 'grand_plus':'GRAND_PLUS' in skill and 'GRAND_PLUS' in ledger['scale']['allowed'],
 'strong_claim_not_weakened':'do not weaken' in amb.lower() and 'must_surface' in amp,
 'factuality_ceiling':'factuality ceiling' in skill.lower() and 'factuality ceiling' in amp.lower(),
 'licensed_amplification':all(x in amp for x in ['Broaden context','Sharpen contrast','Clarify obstruction','Strengthen consequence','Expose methodological afterlife']),
 'editorial_gate':'EDITORIAL-IMPACT' in skill and 'EDITORIAL-IMPACT' in gates and 'Editorial first-two-pages test' in gate,
 'new_tool':(ROOT/'tools/introduction_editorial_impact.py').exists(),
 'new_profile':(ROOT/'profiles/calibrated_grand_narrative.md').exists(),
 'new_checklist':(ROOT/'checklists/editorial_positioning_introduction.md').exists(),
 'behavioral_cases':all(any((ROOT/'tests/behavioral_cases').glob(f'{i:02d}_*.yaml')) for i in range(66,76)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V1_13_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_13_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
