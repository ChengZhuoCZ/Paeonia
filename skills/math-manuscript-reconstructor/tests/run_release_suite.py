#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, json, shlex

ROOT=Path(__file__).resolve().parents[1]
TESTS=[
 'tests/run_tests.py','tests/test_tools.py','tests/test_v110_contract.py','tests/test_v120_contract.py','tests/test_v130_contract.py','tests/test_v140_contract.py','tests/test_v150_contract.py','tests/test_v160_contract.py','tests/test_v170_contract.py','tests/test_v180_contract.py','tests/test_v190_contract.py','tests/test_v1_10_contract.py','tests/test_v1_11_contract.py','tests/test_v1_12_contract.py','tests/test_v1_13_contract.py','tests/test_v1_14_contract.py','tests/test_v1_15_contract.py','tests/test_v1_16_contract.py','tests/test_v1_17_contract.py','tests/test_v1_18_contract.py','tests/test_v1_19_contract.py','tests/test_v1_20_contract.py','tests/test_v1_21_contract.py','tests/test_v1_36_contract.py','tests/test_v1_37_contract.py','tests/test_v1_38_contract.py','tests/test_v1_39_contract.py','tests/test_v1_40_contract.py','tests/test_proof_citation_dossier.py','tests/test_v1_41_contract.py','tests/test_notation_choice_audit.py','tests/test_v1_42_contract.py','tests/test_behavioral_regressions.py','tests/test_execution_planner.py','tests/test_gate_repair_routes.py','tests/test_contract_consistency.py','tests/test_proof_explanation.py','tests/test_writing_modes.py','tests/test_citation_inventory.py'
]

# Run short batches in fresh shells. Some contract tests launch their own child
# audit tools; resetting the parent process between batches avoids inherited
# descriptor/process-state accumulation in constrained CI containers.
BATCH_SIZE=8
results=[]
for start in range(0,len(TESTS),BATCH_SIZE):
    batch=TESTS[start:start+BATCH_SIZE]
    commands=[]
    for rel in batch:
        commands.append(f"echo {shlex.quote('RUN '+rel)}")
        commands.append(f"{shlex.quote(sys.executable)} {shlex.quote(str(ROOT/rel))}")
    script='set -e\n'+'\n'.join(commands)
    try:
        p=subprocess.run(['bash','-lc',script],cwd=ROOT,timeout=180)
    except subprocess.TimeoutExpired:
        results.append({'batch':batch,'returncode':'TIMEOUT'})
        print('RELEASE_SUITE_FAIL')
        print(json.dumps(results,indent=2,ensure_ascii=False))
        sys.exit(1)
    results.append({'batch':batch,'returncode':p.returncode})
    if p.returncode!=0:
        print('RELEASE_SUITE_FAIL')
        print(json.dumps(results,indent=2,ensure_ascii=False))
        sys.exit(1)
print('RELEASE_SUITE_PASS')
for rel in TESTS:
    print(rel+': PASS')
