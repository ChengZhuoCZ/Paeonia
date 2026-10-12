#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1, 8, 0),
 'direct_default':'C0.13 — Direct composition is the default' in skill,
 'writing_order_pass':'### Pass 0a — Writing-order synthesis' in skill,
 'direct_mode_profile':'execution_mode: direct_composition' in skill,
 'director_off':'research_director: off_unless_explicitly_requested' in skill,
 'state_writing_order':'TASK_CONTRACT → WRITING_ORDER → INGEST' in state,
 'optional_exec_plan':'`EXECUTION_PLAN` is a recognized optional state' in state,
 'readme_arrange_then_write':'Default interaction: arrange, then write' in readme,
 'no_mandatory_planner':'Adaptive execution is mandatory' not in skill,
 'proof_first_preserved':'Proof-body-first composition' in skill,
 'frontmatter_after_proof':'frontmatter_gate: after_proof_core_pass' in skill,
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V180_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V180_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
