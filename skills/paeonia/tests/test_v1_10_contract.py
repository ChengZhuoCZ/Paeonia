#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
theorem=(ROOT/'protocols/02c_theorem_statement_architecture.md').read_text(encoding='utf-8')
notation=(ROOT/'protocols/02d_notation_architecture.md').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1, 10, 0),
 'direct_default':'Direct composition is the default' in skill,
 'proof_first':'Proof-body-first composition' in skill,
 'notation_before_proof':'NOTATION_ARCHITECTURE' in state and state.index('NOTATION_ARCHITECTURE') < state.index('PROOF_CORE'),
 'theorem_after_gate':state.index('PROOF_CORE_GATE') < state.index('THEOREM_FRAME'),
 'notation_ledger':'NotationLedger' in skill,
 'theorem_ledger':'TheoremStatementLedger' in skill,
 'theorem_protocol':'Reader order' in theorem and 'Assumption discipline' in theorem,
 'notation_protocol':'Canonical-object rule' in notation and 'Constant architecture' in notation,
 'theorem_gate':'THEOREM-STATEMENT-INTEGRITY' in skill,
 'notation_gate':'NOTATION-CONSISTENCY' in skill,
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V1_10_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_10_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
