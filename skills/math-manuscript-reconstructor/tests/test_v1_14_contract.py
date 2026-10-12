#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
proto=(ROOT/'protocols/05m_high_intensity_corpus_distillation.md').read_text(encoding='utf-8')
real=(ROOT/'protocols/05n_conditional_style_realization.md').read_text(encoding='utf-8')
intro=(ROOT/'protocols/04e_introduction_prose_realization.md').read_text(encoding='utf-8')
arts=yaml.safe_load((ROOT/'registry/artifacts.yaml').read_text(encoding='utf-8'))['artifacts']
gates=yaml.safe_load((ROOT/'registry/gates.yaml').read_text(encoding='utf-8'))['release_blockers']
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,14,0),
 'trusted_proof_preserved':'proof_correctness_mode: trusted_source' in skill,
 'direct_composition_preserved':'Direct composition is the default' in skill,
 'high_intensity_protocol': 'High-Intensity Conditional Corpus Distillation' in proto,
 'role_strata': all(x in proto for x in ['PROOF_ROUTINE','PROOF_DELICATE','PROOF_TECHNICAL_ESTIMATE','PROOF_BRIDGE','THEOREM_LEADIN','INTRO_ORIENTATION']),
 'holdout_stability':'Cross-fold stability' in proto,
 'conditional_ledger':'ConditionalStyleLedger' in skill and 'ConditionalStyleLedger' in arts,
 'evidence_report':'HighIntensityStyleEvidenceReport' in skill and 'HighIntensityStyleEvidenceReport' in arts,
 'conditional_realization':'StyleContextCard' in real and 'Context overrides global style' in real,
 'numeric_fit_forbidden':'Match the covariance, not the numbers' in (ROOT/'profiles/classical_analysis_conditional_style_model.md').read_text(encoding='utf-8'),
 'intro_source_role_separation':'Reference-role separation and high-intensity microstyle' in intro,
 'new_gate':'CONDITIONAL-STYLE-FIDELITY' in gates and 'CONDITIONAL-STYLE-FIDELITY' in skill,
 'new_tools':(ROOT/'tools/high_intensity_corpus_distiller.py').exists() and (ROOT/'tools/conditional_style_audit.py').exists(),
 'new_profile':(ROOT/'profiles/classical_analysis_conditional_style_model.md').exists() and (ROOT/'profiles/classical_analysis_high_intensity_distillation_report.md').exists(),
 'behavioral_cases':all(any((ROOT/'tests/behavioral_cases').glob(f'{i:02d}_*.yaml')) for i in range(76,84)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V1_14_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_14_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
