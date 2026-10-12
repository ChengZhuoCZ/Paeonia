#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
import yaml

def fail(msgs,msg): msgs.append(msg)

def parse_states(text):
    m=re.search(r'## Canonical full state order\s+\n\s*`([^`]+)`',text,re.S)
    if not m: return []
    return [x.strip() for x in m.group(1).split('→')]

def compile_contract(root: Path):
    errors=[]; warnings=[]
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    skill=(root/'SKILL.md').read_text(encoding='utf-8')
    state_text=(root/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
    manifest=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
    artifacts=yaml.safe_load((root/'registry/artifacts.yaml').read_text(encoding='utf-8'))['artifacts']
    gates=yaml.safe_load((root/'registry/gates.yaml').read_text(encoding='utf-8'))['release_blockers']
    audit=yaml.safe_load((root/'schemas/audit_report.yaml').read_text(encoding='utf-8'))
    submission=(root/'protocols/11_submission_gate.md').read_text(encoding='utf-8')
    submission_tpl=(root/'templates/submission_gate_report.md').read_text(encoding='utf-8')
    states=parse_states(state_text)
    state_set=set(states)
    # Optional governance states are recognized even when they are not on the ordinary direct-composition path.
    if '`EXECUTION_PLAN` is a recognized optional state' in state_text:
        state_set.add('EXECUTION_PLAN')

    frontmatter=yaml.safe_load(skill.split('---',2)[1]) or {}
    skill_version=str(frontmatter.get('metadata',{}).get('version',frontmatter.get('version','')))
    if version!=skill_version: fail(errors,f'version mismatch VERSION={version} SKILL={skill_version}')
    if str(manifest.get('version'))!=version: fail(errors,f"version mismatch MANIFEST={manifest.get('version')} VERSION={version}")
    if not states: fail(errors,'could not parse canonical state order')

    artifact_section = skill.split('## 7. Required research artifacts',1)[1].split('## 8. Handling incomplete or incorrect source proofs',1)[0] if '## 7. Required research artifacts' in skill and '## 8. Handling incomplete or incorrect source proofs' in skill else ''
    for name,a in artifacts.items():
        owner=a.get('owner_state')
        if owner not in state_set: fail(errors,f'artifact {name} owner_state not in state machine: {owner}')
        for key in ('schema','template'):
            rel=a.get(key)
            if rel and not (root/rel).exists(): fail(errors,f'artifact {name} missing {key}: {rel}')
        if name not in artifact_section: fail(errors,f'artifact registry item absent from SKILL artifact summary: {name}')

    for gate,g in gates.items():
        if g.get('owner_state') not in state_set: fail(errors,f'gate {gate} owner_state missing: {g.get("owner_state")}')
        if g.get('rollback_to') not in state_set: fail(errors,f'gate {gate} rollback_to missing: {g.get("rollback_to")}')
        for req in ('audit_key','allowed_repairs','forbidden_repairs','invalidates','re_audit'):
            if req not in g: fail(errors,f'gate {gate} missing field {req}')
        if g.get('audit_key') not in audit: fail(errors,f'gate {gate} audit_key absent from audit schema: {g.get("audit_key")}')
        if f'`{gate}`' not in submission: fail(errors,f'gate {gate} absent from submission protocol')
        if f'`{gate}`' not in skill: fail(errors,f'gate {gate} absent from SKILL release blocker contract')
        if f'{gate}: PENDING' not in submission_tpl: fail(errors,f'gate {gate} absent from submission report template')
        for dep in g.get('re_audit',[]):
            if dep not in gates: fail(errors,f'gate {gate} re_audit references unknown gate {dep}')
        for artifact in g.get('invalidates',[]):
            if artifact not in artifacts: fail(errors,f'gate {gate} invalidates unknown artifact {artifact}')

    # behavioral coverage
    legacy=[]
    for p in sorted((root/'tests/regression_cases').glob('*.md')):
        mm=re.match(r'(\d+)_',p.name)
        if mm: legacy.append(mm.group(1))
    fixture_schema=yaml.safe_load((root/'schemas/behavioral_case.yaml').read_text(encoding='utf-8'))
    supported_ops=set(fixture_schema.get('supported_assertion_ops',[]))
    required_fixture_fields=set(fixture_schema.get('required_fields',[]))
    fixtures=[]
    for p in sorted((root/'tests/behavioral_cases').glob('*.yaml')):
        data=yaml.safe_load(p.read_text(encoding='utf-8'))
        missing=required_fixture_fields-set(data or {})
        if missing: fail(errors,f'behavioral fixture {p.name} missing fields: {sorted(missing)}')
        cid=str(data.get('id','')).zfill(2); fixtures.append(cid)
        gate=data.get('gate')
        if gate not in gates: fail(errors,f'behavioral fixture {p.name} references unknown gate {gate}')
        spec=root/'tests/regression_cases'/str(data.get('legacy_spec',''))
        if not spec.exists(): fail(errors,f'behavioral fixture {p.name} legacy_spec missing: {data.get("legacy_spec")}')
        for a in data.get('assertions',[]):
            if a.get('op') not in supported_ops: fail(errors,f'behavioral fixture {p.name} uses unsupported op {a.get("op")}')
    if len(fixtures)!=len(set(fixtures)): fail(errors,'duplicate behavioral fixture ids')
    uncovered=sorted(set(legacy)-set(fixtures))
    extra=sorted(set(fixtures)-set(legacy))
    if uncovered: fail(errors,'uncovered regression specs: '+','.join(uncovered))
    if extra: fail(errors,'behavioral fixtures without legacy specs: '+','.join(extra))

    # manifest files
    for rel in manifest.get('tests',[]):
        if not (root/rel).exists(): fail(errors,f'manifest test missing: {rel}')
    for rel in manifest.get('tools',[]):
        if not (root/rel).exists(): fail(errors,f'manifest tool missing: {rel}')

    # required v1.8 interaction contract
    for phrase in ['Direct composition is the default','Writing-order synthesis','research_director: off_unless_explicitly_requested']:
        if phrase not in skill: fail(errors,f'SKILL missing v1.8 contract phrase: {phrase}')
    if 'Adaptive execution is mandatory' in skill:
        fail(errors,'legacy mandatory-planner contract survived into v1.8')
    return {'version':version,'states':len(states),'artifacts':len(artifacts),'gates':len(gates),'legacy_regressions':len(legacy),'behavioral_fixtures':len(fixtures),'errors':errors,'warnings':warnings,'status':'PASS' if not errors else 'FAIL'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--json',action='store_true'); args=ap.parse_args()
    report=compile_contract(args.root)
    if args.json: print(json.dumps(report,indent=2,ensure_ascii=False))
    else:
        print('CONTRACT_CONSISTENCY_'+report['status'])
        for k in ['version','states','artifacts','gates','legacy_regressions','behavioral_fixtures']: print(f'{k}={report[k]}')
        for e in report['errors']: print('ERROR '+e)
        for w in report['warnings']: print('WARN '+w)
    if report['status']!='PASS': sys.exit(1)
if __name__=='__main__': main()
