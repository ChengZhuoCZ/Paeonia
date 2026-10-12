#!/usr/bin/env python3
"""Validate an outline record's dependency structure, not its prose or mathematics."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import yaml

BRIDGES = {'exact_identity', 'equivalence', 'one_way_reduction', 'principal_order', 'controlled_comparison'}

def audit(data, tex=None):
    errors = []
    if not isinstance(data, dict):
        return result(['record must be a mapping'])
    record = data.get('proof_explanation', data)
    if not isinstance(record, dict):
        return result(['proof_explanation must be a mapping'])
    if record.get('enabled') is not True:
        return {'status': 'NOT_APPLICABLE', 'errors': [], 'prose_comprehension': 'NOT_ASSESSED'}
    evidence = record.get('evidence', {})
    if not isinstance(evidence, dict):
        errors.append('evidence must be a mapping')
        evidence = {}
    labels = set(re.findall(r'\\label\{([^}]+)\}', tex)) if tex is not None else None
    for key, anchor in evidence.items():
        if not isinstance(anchor, dict) or not anchor.get('locator') or not anchor.get('role'):
            errors.append(f'evidence {key}: locator and explanatory role required')
            continue
        if anchor.get('source') not in ('manuscript', 'literature'):
            errors.append(f'evidence {key}: unsupported source type')
        if labels is not None and anchor.get('source') == 'manuscript' and anchor['locator'] not in labels:
            errors.append(f'evidence {key}: manuscript label not found: {anchor["locator"]}')
    def refs(item, where):
        values = item.get('evidence', [])
        if not isinstance(values, list) or not values:
            errors.append(f'{where}: evidence references required')
            return
        for v in values:
            if not isinstance(v, str) or v not in evidence:
                errors.append(f'{where}: unknown evidence reference {v}')
    def required_text(item, names, where):
        for name in names:
            if not isinstance(item.get(name), str) or not item[name].strip():
                errors.append(f'{where}: {name} explanation required')
    def items(name):
        xs = record.get(name, [])
        if not isinstance(xs, list):
            errors.append(f'{name} must be a list')
            return []
        if any(not isinstance(x, dict) for x in xs):
            errors.append(f'{name} entries must be mappings')
        return [x for x in xs if isinstance(x, dict)]
    available = set()
    for fact in items('initial_facts'):
        required_text(fact, ['id', 'meaning'], 'initial fact')
        fid = fact.get('id')
        if isinstance(fid, str):
            if fid in available:
                errors.append(f'duplicate fact: {fid}')
            available.add(fid)
        refs(fact, f'initial fact {fid}')
    for reformulation in items('reformulations'):
        required_text(reformulation, ['id', 'original_problem', 'obstruction', 'dictionary', 'new_capability', 'remaining_cost'], 'reformulation')
        if reformulation.get('bridge_kind') not in BRIDGES:
            errors.append('reformulation: explicit supported bridge_kind required')
        refs(reformulation, 'reformulation')
    stages = items('stages')
    if not stages:
        errors.append('at least one stage is required for an enabled record')
    stage_ids = set()
    for stage in stages:
        sid = stage.get('id')
        required_text(stage, ['id', 'obstacle', 'action', 'payoff', 'regime'], f'stage {sid}')
        if isinstance(sid, str):
            if sid in stage_ids:
                errors.append(f'duplicate stage: {sid}')
            stage_ids.add(sid)
        needs = stage.get('requires', [])
        if not isinstance(needs, list):
            errors.append(f'stage {sid}: requires must be a list')
            needs = []
        for fid in needs:
            if not isinstance(fid, str) or fid not in available:
                errors.append(f'stage {sid}: unavailable input {fid}; possible circular or missing dependency')
        outputs = stage.get('produces', [])
        if not isinstance(outputs, list) or not outputs:
            errors.append(f'stage {sid}: explicit output facts required')
            outputs = []
        for fact in outputs:
            if not isinstance(fact, dict):
                errors.append(f'stage {sid}: output must be a mapping')
                continue
            required_text(fact, ['id', 'meaning'], f'stage {sid} output')
            fid = fact.get('id')
            if isinstance(fid, str):
                if fid in available:
                    errors.append(f'stage {sid}: duplicate fact {fid}')
                available.add(fid)
        refs(stage, f'stage {sid}')
    assembly = record.get('assembly', {})
    if not isinstance(assembly, dict):
        errors.append('assembly must be a mapping')
        assembly = {}
    required_text(assembly, ['implication', 'scope'], 'assembly')
    needs = assembly.get('requires', [])
    if not isinstance(needs, list) or not needs:
        errors.append('assembly: explicit input facts required')
        needs = []
    for fid in needs:
        if not isinstance(fid, str) or fid not in available:
            errors.append(f'assembly: unavailable input {fid}')
    if assembly.get('claims_equality') is True:
        required_text(assembly, ['equality_recovery'], 'assembly')
    refs(assembly, 'assembly')
    return result(errors)

def result(errors):
    return {'status': 'REVIEW' if errors else 'STRUCTURE_OK', 'errors': errors,
            'prose_comprehension': 'NOT_ASSESSED', 'mathematical_correctness': 'NOT_ASSESSED',
            'next_action': 'Apply Protocol 04q to the actual Introduction and outline.'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('record', type=Path)
    p.add_argument('--tex', type=Path, help='Optional source for checking manuscript label existence only')
    args = p.parse_args()
    try:
        data = yaml.safe_load(args.record.read_text())
        tex = args.tex.read_text() if args.tex else None
        report = audit(data, tex)
    except (OSError, yaml.YAMLError) as error:
        report = result([str(error)])
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(1 if report['status'] == 'REVIEW' else 0)

if __name__ == '__main__':
    main()
