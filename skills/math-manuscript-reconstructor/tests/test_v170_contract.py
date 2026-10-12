#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
fail=[]
checks={
 'advanced_director_retained':(ROOT/'protocols/15_adaptive_research_director.md').exists(),
 'repair_protocol':(ROOT/'protocols/16_gate_repair_routing.md').exists(),
 'behavior_protocol':(ROOT/'protocols/17_behavioral_validation.md').exists(),
 'consistency_protocol':(ROOT/'protocols/18_contract_consistency.md').exists(),
 'execution_plan_schema':(ROOT/'schemas/execution_plan.yaml').exists(),
 'artifact_registry':(ROOT/'registry/artifacts.yaml').exists(),
 'gate_registry':(ROOT/'registry/gates.yaml').exists(),
 'planner_tool':(ROOT/'tools/execution_planner.py').exists(),
 'repair_tool':(ROOT/'tools/gate_repair_router.py').exists(),
 'behavior_tool':(ROOT/'tools/behavioral_case_runner.py').exists(),
 'consistency_tool':(ROOT/'tools/contract_consistency.py').exists(),
 'execution_plan_optional':'`EXECUTION_PLAN` is a recognized optional state' in state,
 'planner_not_default':'Adaptive execution is mandatory' not in skill,
 'style_optional_universal_arch':'universal mathematics-driven architecture rules remain active' in state,
}
for k,v in checks.items():
    if not v: fail.append(k)
for i in range(1,38):
    if not any(p.name.startswith(f'{i:02d}_') for p in (ROOT/'tests/behavioral_cases').glob('*.yaml')): fail.append(f'missing_behavioral_{i:02d}')
if fail:
    print('V170_ADVANCED_TOOLING_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V170_ADVANCED_TOOLING_RETAINED')
print(f'contract_checks={len(checks)}')
