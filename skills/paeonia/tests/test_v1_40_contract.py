#!/usr/bin/env python3
"""Version-floor, stage routing, evidence, scope, and release-coverage contract."""
from pathlib import Path
import json
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
read = lambda p: (ROOT / p).read_text(encoding='utf-8')
skill = read('SKILL.md')
proto = read('protocols/07a_exact_theorem_citation_compression.md')
p07 = read('protocols/07_citation_integrity.md')
state = read('protocols/12_execution_state_machine.md')
submission = read('protocols/11_submission_gate.md')
manifest = json.loads(read('MANIFEST.json'))
artifacts = yaml.safe_load(read('registry/artifacts.yaml'))['artifacts']
schema = yaml.safe_load(read('schemas/proof_citation_replacement_dossier.yaml'))
checks = {
    'version_consistency': tuple(map(int,read('VERSION').strip().split('.'))) >= (1,40,0) and tuple(map(int,manifest['version'].split('.'))) >= (1,40,0) and 'version: 1.' in skill,
    'stage_between_proof_and_gate': skill.index('### Pass 6 —') < skill.index('### Pass 6a —') < skill.index('### Pass 7 —'),
    'active_and_scope': all(x in skill for x in ['Proof-citation compression is now a named stage', 'ProofCitationReplacementDossier', 'LOCAL_POLISH', 'Introduction-only']),
    'no_global_proof_audit': 'trusted_source' in proto and 'new proposed external dependency' in proto,
    'primary_source_and_version': all(x in proto for x in ['full-text primary', 'preprint version', 'actual theorem', 'No inferred theorem number']),
    'exact_result_kinds': all(x in proto for x in ['Theorem 2.4', 'Lemma 5.1', 'Proposition 3.7', 'Corollary 6.2', 'unnumbered']),
    'two_sided_entailment': 'H_here ⇒ H_source' in proto and 'C_source ⇒ C_here' in proto,
    'dimensions': all(x in proto for x in ['boundary', 'regularity', 'uniformity', 'rigidity', 'endpoint', 'strictness', 'normalization', 'quantifiers']),
    'four_decisions_and_unverified': all(x in proto for x in ['APPLIED_DIRECT', 'APPLIED_ADAPTED', 'APPLIED_PARTIAL', 'RETAINED_UNVERIFIED', 'RETAINED_ORIGINAL']),
    'avoid_dependency_cycle': all(x in proto for x in ['independent justification', 'logically independent']),
    'preserve_unmatched': all(x in proto for x in ['retain all unmatched estimates', 'uniformity or genuine innovations', 'proof of the remaining claim']),
    'source_verification_reuse': 'Protocol 07 remains authoritative' in proto and 'Protocol 07a' in p07,
    'register_conditional_dossier': 'ProofCitationReplacementDossier' in artifacts and artifacts['ProofCitationReplacementDossier']['required_for'] == ['material_proof_citation_candidates_in_authorized_editable_scope'],
    'dossier_schema': schema['artifact'] == 'ProofCitationReplacementDossier' and schema['candidate_scan']['status'] == 'NOT_STARTED',
    'structural_checker_does_not_certify_math': 'cannot open source papers' in proto and 'cannot prove that a cited theorem applies' in read('README.md').lower(),
    'state_machine_integrated': 'Pass 6a' in state and 'newly introduced external citation' in state,
    'submission_integrated': 'Protocol 07a' in submission and 'primary-text-verified' in submission,
    'intro_credit': 'Reuse exact-source evidence imported in Pass 6a' in skill,
    'proof_core_gate_updated': 'For passages newly replaced by external results under Pass 6a' in skill,
    'no_journal_deletion_based_on_abstract': 'abstract' in proto and 'whole-paper citation' in skill,
    'tools_registered': 'tools/proof_citation_dossier_audit.py' in manifest['tools'] and 'tests/test_proof_citation_dossier.py' in manifest['tests'],
    'new_regression_cases': all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) and any((ROOT/'tests/regression_cases').glob(f'{i}_*.md')) for i in range(173,187)),
    'old_intro_retained': all(x in skill for x in ['04u_literature_discovery_and_credit.md','04v_evidence_grounded_grand_narrative.md']),
}
errors = [n for n, passed in checks.items() if not passed]
if errors:
    print('V1_40_CONTRACT_FAIL', ', '.join(errors))
    sys.exit(1)
print('V1_40_CONTRACT_PASS')
print('checks=' + str(len(checks)))
