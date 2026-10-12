#!/usr/bin/env python3
"""Structural audit of a claimed theorem-level proof-by-citation replacement.

Does NOT retrieve source PDFs, read theorem statements, or verify implications.
A PASS means declared audit fields are internally present, not mathematically true.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

import yaml

APPLIED = {'APPLIED_DIRECT', 'APPLIED_ADAPTED', 'APPLIED_PARTIAL'}
ALL = APPLIED | {
    'PROPOSED', 'RETAINED_UNVERIFIED', 'RETAINED_INAPPLICABLE', 'RETAINED_ORIGINAL'
}
NUMBERED = {'Theorem', 'Lemma', 'Proposition', 'Corollary'}
UNNUMBERED = {'NamedResult', 'Unnumbered'}


def populated(value):
    return isinstance(value, str) and bool(value.strip()) and value.strip().lower() not in {
        'tbd', 'todo', 'unknown', 'none', 'null', 'to check'
    }


def audit(doc):
    errors, warnings = [], []
    if not isinstance(doc, dict) or doc.get('artifact') != 'ProofCitationReplacementDossier':
        return ['artifact must be ProofCitationReplacementDossier'], warnings, 0
    entries = doc.get('entries', [])
    if not isinstance(entries, list):
        return ['entries must be a list'], warnings, 0
    applied = 0
    seen = set()
    for i, entry in enumerate(entries):
        label = f'entries[{i}]'
        if not isinstance(entry, dict):
            errors.append(f'{label} must be a mapping')
            continue
        ident = entry.get('id')
        if not populated(ident):
            errors.append(f'{label}.id missing')
        elif ident in seen:
            errors.append(f'{label}.id repeated: {ident}')
        else:
            seen.add(ident)
        decision = entry.get('decision') or {}
        if not isinstance(decision, dict):
            errors.append(f'{label}.decision must be a mapping')
            continue
        status = decision.get('status')
        if status not in ALL:
            errors.append(f'{label}.decision.status invalid: {status}')
            continue
        if status not in APPLIED:
            continue
        applied += 1
        if not populated(doc.get('editable_proof_scope')):
            errors.append('editable_proof_scope is required for any applied replacement')
        source = entry.get('source') or {}
        application = entry.get('application') or {}
        manuscript = entry.get('manuscript') or {}
        if not all(isinstance(part, dict) for part in (source, application, manuscript)):
            errors.append(f'{label} malformed source/application/manuscript')
            continue
        for field in ('location', 'full_claim'):
            if not populated(manuscript.get(field)):
                errors.append(f'{label}.manuscript.{field} missing')
        for field in ('bibkey', 'url', 'version'):
            if not populated(source.get(field)):
                errors.append(f'{label}.source.{field} missing')
        if populated(source.get('url')) and not re.match(r'^https?://', source['url']):
            errors.append(f'{label}.source.url must be a stable HTTP(S) source link')
        kind = source.get('result_kind')
        if kind in NUMBERED:
            if not populated(source.get('result_number')):
                errors.append(f'{label}: numbered {kind} requires inspected result_number')
        elif kind in UNNUMBERED:
            locator = source.get('result_locator')
            if not populated(source.get('result_name')):
                errors.append(f'{label}: unnumbered source requires a distinctive result_name')
            if not populated(locator) or not re.search(r'(?i)\b(page|p\.)\s*\d+', locator):
                errors.append(f'{label}: unnumbered source requires named statement and exact page locator')
        else:
            errors.append(f'{label}.source.result_kind missing or invalid')
        for field in ('metadata_checked', 'locator_checked', 'primary_statement_checked'):
            if source.get(field) is not True:
                errors.append(f'{label}.source.{field} must be true before applying')
        hyps = application.get('hypotheses_map')
        if not isinstance(hyps, list):
            errors.append(f'{label}.application.hypotheses_map must be a list')
        elif not hyps and application.get('no_external_hypotheses') is not True:
            errors.append(f'{label}: no hypothesis map or explicit zero-hypothesis check')
        else:
            for j, mapping in enumerate(hyps):
                if not isinstance(mapping, dict) or not all(populated(mapping.get(k)) for k in (
                    'source_hypothesis', 'local_fact', 'local_locator'
                )):
                    errors.append(f'{label}.application.hypotheses_map[{j}] incomplete')
        if not populated(application.get('conclusion_map')):
            errors.append(f'{label}.application.conclusion_map missing')
        for field in ('scope_uniformity_equality_checked', 'independent_dependency_checked'):
            if application.get(field) is not True:
                errors.append(f'{label}.application.{field} must be true before applying')
        if status == 'APPLIED_ADAPTED' and not application.get('adaptations'):
            errors.append(f'{label}: adapted application must record retained adaptation')
        if status == 'APPLIED_PARTIAL' and not application.get('retained_steps'):
            errors.append(f'{label}: partial replacement must retain unmatched steps')
        for field in ('replacement_location',):
            if not populated(decision.get(field)):
                errors.append(f'{label}.decision.{field} missing')
        for field in ('exact_citation_written', 'downstream_checked', 'protected_scope_checked'):
            if decision.get(field) is not True:
                errors.append(f'{label}.decision.{field} must be true before applying')
    if not entries:
        warnings.append('no material candidates recorded; no theorem citation was audited')
    return errors, warnings, applied


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', required=True, type=Path)
    p.add_argument('--strict', action='store_true')
    p.add_argument('--json', action='store_true')
    a = p.parse_args()
    try:
        d = yaml.safe_load(a.input.read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'PROOF_CITATION_DOSSIER_ERROR: {exc}', file=sys.stderr)
        return 2
    errors, warnings, applied = audit(d)
    report = {'status': 'FAIL' if errors else 'PASS', 'applied_entries': applied,
              'candidate_entries': len((d or {}).get('entries', [])),
              'errors': errors, 'warnings': warnings,
              'scope': 'structural-only; source statements and mathematical applicability not independently verified'}
    if a.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print('PROOF_CITATION_DOSSIER_' + report['status'])
        print('applied_entries=' + str(applied))
        for message in errors: print('ERROR ' + message)
        for message in warnings: print('WARN ' + message)
        print('Note: structural checks cannot certify theorem applicability.')
    return 1 if errors and a.strict else 0


if __name__ == '__main__':
    sys.exit(main())
