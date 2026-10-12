#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
intro=(ROOT/'protocols/04a_grand_introduction_blueprint.md').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1, 9, 0),
 'proof_first_preserved':'Proof-body-first composition' in skill,
 'intro_after_proof':'PROOF_CORE_GATE: PASS' in state and 'INTRODUCTION_NARRATIVE' in state,
 'intro_ledger':'IntroductionNarrativeLedger' in skill,
 'scale_selector':'STANDARD' in intro and 'EXPANSIVE' in intro and 'GRAND' in intro,
 'problem_tension':'ProblemTensionMap' in intro,
 'result_hierarchy':'ResultHierarchy' in intro,
 'literature_roles':'LiteratureLandscape' in intro,
 'adjacent_bridge':'Adjacent-problem bridges' in intro,
 'mechanism_first':'Proof mechanism narrative' in intro,
 'grand_gate':'GRAND-NARRATIVE-INTEGRITY' in skill,
 'anti_hype':'Grand Introduction is mathematics-positioning, not rhetorical inflation' in skill,
 'direct_default_preserved':'Direct composition is the default' in skill,
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V190_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V190_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
