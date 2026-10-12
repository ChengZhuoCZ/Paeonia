#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
trusted=(ROOT/'protocols/01a_trusted_proof_mode.md').read_text(encoding='utf-8')
task=yaml.safe_load((ROOT/'schemas/task_contract.yaml').read_text(encoding='utf-8'))
gate=(ROOT/'templates/proof_core_gate_report.md').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1, 11, 0),
 'trusted_default':'proof_correctness_mode: trusted_source' in skill,
 'task_contract_default':task.get('proof_correctness_mode')=='trusted_source' and task.get('independent_correctness_audit') is False,
 'no_gap_hunt':'re-prove the argument' in trusted and 'independently search for proof gaps' in trusted,
 'explicit_switch':'verify_proof' in trusted and 'only when the user explicitly' in trusted.lower(),
 'source_missing':'SOURCE-MISSING' in trusted,
 'gate_is_fidelity':'fidelity/coverage gate' in skill and 'not an independent proof-validity audit' in skill,
 'state_trusted':'trusted-proof direct-composition' in state and 'do not independently re-prove them' in state,
 'gate_template': 'Independent correctness audit performed' in gate and 'not independent mathematical verification' in gate,
 'referee_opt_in':'Adversarial referee simulation (explicit audit only)' in skill,
}
fail=[k for k,v in checks.items() if not v]
if fail:
    print('V1_11_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_11_CONTRACT_PASS')
print(f'contract_checks={len(checks)}')
