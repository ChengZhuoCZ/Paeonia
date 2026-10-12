#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

FULL_STATES = [
    'TASK_CONTRACT','EXECUTION_PLAN','INGEST','EXTRACT','LEDGER_LOCK','SOURCE_QUARANTINE',
    'STYLE_EXTRACT','PARAGRAPH_FINGERPRINT_LOCK','SECTION_FINGERPRINT_LOCK','WHOLE_PAPER_FINGERPRINT_LOCK','STYLE_QUARANTINE',
    'PROOF_GRAPH','NOTATION_ARCHITECTURE','PROOF_CORE','PROOF_CORE_GATE','MANUSCRIPT_ARCHITECTURE','WHOLE_PAPER_NARRATIVE','SECTION_NARRATIVE',
    'THEOREM_FRAME','INTRODUCTION_NARRATIVE','FRONTMATTER','EDIT','RESIDUE_DIAGNOSIS','AUTHORIAL_DECISION','PARAGRAPH_RHYTHM',
    'MATHEMATICAL_TRANSITIONS','COLD_AUTHOR','AUDIT','RELEASE'
]
STYLE_STATES = ['STYLE_EXTRACT','PARAGRAPH_FINGERPRINT_LOCK','SECTION_FINGERPRINT_LOCK','WHOLE_PAPER_FINGERPRINT_LOCK','STYLE_QUARANTINE']
NAT_STATES = ['RESIDUE_DIAGNOSIS','AUTHORIAL_DECISION','PARAGRAPH_RHYTHM','MATHEMATICAL_TRANSITIONS','COLD_AUTHOR']
ALL_GATES = [
    'MATH-SEMANTICS','PROOF-CORE-ORDER','SOURCE-INDEPENDENCE','STYLE-SOURCE-INDEPENDENCE','STYLE-LEDGER-FIDELITY',
    'GENERATIVE-RESIDUE','AUTHORIAL-DECISION','PARAGRAPH-FINGERPRINT-FIDELITY','SECTION-NARRATIVE-FIDELITY',
    'WHOLE-PAPER-NARRATIVE-FIDELITY','GRAND-NARRATIVE-INTEGRITY','THEOREM-STATEMENT-INTEGRITY','MATHEMATICAL-TRANSITIONS','COLD-AUTHOR','CITATION-INTEGRITY',
    'NOTATION-CONSISTENCY','PROOF-CLOSURE','LATEX-INTEGRITY'
]

def load_data(path: Path):
    text = path.read_text(encoding='utf-8')
    if path.suffix.lower() == '.json':
        return json.loads(text)
    if yaml is None:
        raise RuntimeError('PyYAML unavailable')
    return yaml.safe_load(text)

def ordered_subset(states):
    seen=set(states)
    return [s for s in FULL_STATES if s in seen]

def skip_records(required, reasons):
    req=set(required)
    out=[]
    for state in FULL_STATES:
        if state in req:
            continue
        out.append({
            'state': state,
            'reason': reasons.get(state, 'not required by requested workflow'),
            'prerequisites_satisfied_elsewhere': [],
            'risk_if_wrong': 'requested deliverable may become unverifiable if this skip assumption is false',
            'artifacts_not_produced': [],
            'gates_that_become_unavailable': [],
        })
    return out

def resolve_writing_mode(task):
    """Resolve explicit metadata, not natural language. Keep legacy calls valid."""
    mode = str(task.get('writing_mode') or '').upper() or None
    if mode not in {None, 'RECONSTRUCT', 'LOCAL_POLISH'}:
        raise ValueError(f'unknown writing_mode: {mode}')
    scopes = {}
    for key in ('editable_scope', 'protected_scope'):
        value = task.get(key) or []
        if isinstance(value, str):
            value = [value]
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            raise ValueError(f'{key} must contain nonempty scope descriptions')
        scopes[key] = [x.strip() for x in value]
    scope = scopes['editable_scope']
    workflow = str(task.get('workflow') or '').upper()
    if not workflow:
        if mode == 'LOCAL_POLISH':
            workflow = 'LOCAL_POLISH'
        elif mode == 'RECONSTRUCT' and scope and scope != ['whole_manuscript']:
            workflow = 'SCOPED_RECONSTRUCTION'
        else:
            workflow = 'FULL_MANUSCRIPT_RECONSTRUCTION'
    implied = {
        'FULL_MANUSCRIPT_RECONSTRUCTION': 'RECONSTRUCT',
        'SCOPED_RECONSTRUCTION': 'RECONSTRUCT',
        'PROOF_BODY_ONLY': 'RECONSTRUCT',
        'FRONTMATTER_FROM_VERIFIED_PROOF': 'RECONSTRUCT',
        'ARCHITECTURE_ONLY': 'RECONSTRUCT',
        'LOCAL_POLISH': 'LOCAL_POLISH',
        'LATEX_NOTATION_ONLY': 'LOCAL_POLISH',
        'AUTHORIAL_NATURALIZATION_ONLY': 'LOCAL_POLISH',
        'STYLE_DISTILLATION_ONLY': None,
        'SUBMISSION_AUDIT_ONLY': None,
    }.get(workflow)
    if mode and mode != implied:
        raise ValueError('writing_mode conflicts with workflow; select the intended route explicitly')
    if workflow in {'LOCAL_POLISH', 'SCOPED_RECONSTRUCTION'} and not scope:
        raise ValueError(f'{workflow} requires editable_scope')
    if set(scope) & set(scopes['protected_scope']):
        raise ValueError('same scope is both editable and protected; describe disjoint regions')
    if workflow == 'SCOPED_RECONSTRUCTION' and 'whole_manuscript' in scope:
        raise ValueError('whole manuscript reconstruction must use the full workflow')
    if workflow == 'FULL_MANUSCRIPT_RECONSTRUCTION' and (scope and scope != ['whole_manuscript'] or scopes['protected_scope']):
        raise ValueError('bounded or protected regions require a scoped workflow')
    return workflow, implied, scopes

def plan(task: dict) -> dict:
    workflow, writing_mode, scopes = resolve_writing_mode(task)
    bounded = workflow in {'LOCAL_POLISH', 'SCOPED_RECONSTRUCTION'}
    has_sources = bool(task.get('has_math_sources', True))
    has_style = bool(task.get('has_style_corpus', False))
    naturalize = bool(task.get('authorial_naturalization', True))
    citations = bool(task.get('citations_or_external_inputs', False))
    latex = bool(task.get('latex_output', False))
    submission = bool(task.get('submission_claim', workflow in {'FULL_MANUSCRIPT_RECONSTRUCTION','SUBMISSION_AUDIT_ONLY'}))
    prior_gate = str(task.get('existing_proof_core_gate','NONE')).upper()
    checksum = bool(task.get('semantic_checksum_available', False))
    reasons={}

    if workflow == 'LOCAL_POLISH':
        if task.get('has_editing_baseline') is not True:
            raise ValueError('LOCAL_POLISH requires has_editing_baseline=true')
        required = ['TASK_CONTRACT','EXECUTION_PLAN','EDIT','AUDIT','RELEASE']
        reasons = {s: 'baseline-preserving local edit; reconstruction states are outside the selected mode' for s in FULL_STATES}
    elif workflow == 'SCOPED_RECONSTRUCTION':
        if task.get('has_math_sources') is not True:
            raise ValueError('SCOPED_RECONSTRUCTION requires has_math_sources=true')
        required = ['TASK_CONTRACT','EXECUTION_PLAN','INGEST','EXTRACT','LEDGER_LOCK','SOURCE_QUARANTINE','EDIT','AUDIT','RELEASE']
        if has_style:
            required += ['STYLE_EXTRACT', 'STYLE_QUARANTINE']
        reasons = {s: 'compose only the selected region from trusted sources; no protected proof-body redraft' for s in FULL_STATES}
    elif workflow == 'FULL_MANUSCRIPT_RECONSTRUCTION':
        if not has_sources:
            raise ValueError('FULL_MANUSCRIPT_RECONSTRUCTION requires mathematical sources')
        required = [s for s in FULL_STATES]
        if not has_style:
            required = [s for s in required if s not in STYLE_STATES]
            for s in STYLE_STATES: reasons[s]='no style corpus supplied; universal mathematics-driven architecture remains active'
        if not naturalize:
            required = [s for s in required if s not in NAT_STATES]
            for s in NAT_STATES: reasons[s]='authorial naturalization not requested'
    elif workflow == 'PROOF_BODY_ONLY':
        if not has_sources:
            raise ValueError('PROOF_BODY_ONLY requires mathematical sources')
        required = ['TASK_CONTRACT','EXECUTION_PLAN','INGEST','EXTRACT','LEDGER_LOCK','SOURCE_QUARANTINE']
        if has_style: required += STYLE_STATES
        required += ['PROOF_GRAPH','NOTATION_ARCHITECTURE','PROOF_CORE','PROOF_CORE_GATE','EDIT']
        if naturalize: required += NAT_STATES
        required += ['AUDIT','RELEASE']
    elif workflow == 'FRONTMATTER_FROM_VERIFIED_PROOF':
        if prior_gate != 'PASS':
            raise ValueError('FRONTMATTER_FROM_VERIFIED_PROOF requires existing_proof_core_gate=PASS')
        required = ['TASK_CONTRACT','EXECUTION_PLAN','THEOREM_FRAME','INTRODUCTION_NARRATIVE','FRONTMATTER','EDIT','AUDIT','RELEASE']
        if has_style:
            required = ['TASK_CONTRACT','EXECUTION_PLAN'] + STYLE_STATES + ['THEOREM_FRAME','INTRODUCTION_NARRATIVE','FRONTMATTER','EDIT','AUDIT','RELEASE']
    elif workflow == 'ARCHITECTURE_ONLY':
        if prior_gate != 'PASS':
            raise ValueError('ARCHITECTURE_ONLY requires a verified closed proof')
        required=['TASK_CONTRACT','EXECUTION_PLAN','MANUSCRIPT_ARCHITECTURE','WHOLE_PAPER_NARRATIVE','SECTION_NARRATIVE','AUDIT','RELEASE']
    elif workflow == 'STYLE_DISTILLATION_ONLY':
        if not has_style:
            raise ValueError('STYLE_DISTILLATION_ONLY requires a style corpus')
        required=['TASK_CONTRACT','EXECUTION_PLAN','INGEST']+STYLE_STATES+['RELEASE']
    elif workflow == 'AUTHORIAL_NATURALIZATION_ONLY':
        if not checksum:
            raise ValueError('AUTHORIAL_NATURALIZATION_ONLY requires semantic_checksum_available=true')
        required=['TASK_CONTRACT','EXECUTION_PLAN','EDIT']+NAT_STATES+['AUDIT','RELEASE']
    elif workflow == 'SUBMISSION_AUDIT_ONLY':
        required=['TASK_CONTRACT','EXECUTION_PLAN','AUDIT','RELEASE']
    elif workflow == 'LATEX_NOTATION_ONLY':
        if not checksum:
            raise ValueError('LATEX_NOTATION_ONLY requires semantic_checksum_available=true')
        required=['TASK_CONTRACT','EXECUTION_PLAN','EDIT','AUDIT','RELEASE']
    else:
        raise ValueError(f'unknown workflow: {workflow}')

    required=ordered_subset(required)
    gates=[]
    if bounded:
        gates += ['MATH-SEMANTICS','NOTATION-CONSISTENCY']
        if workflow == 'SCOPED_RECONSTRUCTION':
            gates += ['SOURCE-INDEPENDENCE']
        if has_style:
            gates += ['STYLE-SOURCE-INDEPENDENCE']
    elif workflow in {'FULL_MANUSCRIPT_RECONSTRUCTION','PROOF_BODY_ONLY'}:
        gates += ['MATH-SEMANTICS','PROOF-CORE-ORDER','SOURCE-INDEPENDENCE','PROOF-CLOSURE','NOTATION-CONSISTENCY']
        if has_style: gates += ['STYLE-SOURCE-INDEPENDENCE','STYLE-LEDGER-FIDELITY']
        if naturalize: gates += ['GENERATIVE-RESIDUE','AUTHORIAL-DECISION','PARAGRAPH-FINGERPRINT-FIDELITY','MATHEMATICAL-TRANSITIONS','COLD-AUTHOR']
        if workflow=='FULL_MANUSCRIPT_RECONSTRUCTION': gates += ['SECTION-NARRATIVE-FIDELITY','WHOLE-PAPER-NARRATIVE-FIDELITY','GRAND-NARRATIVE-INTEGRITY','THEOREM-STATEMENT-INTEGRITY']
    elif workflow == 'FRONTMATTER_FROM_VERIFIED_PROOF':
        gates += ['MATH-SEMANTICS','PROOF-CLOSURE','GRAND-NARRATIVE-INTEGRITY','THEOREM-STATEMENT-INTEGRITY','NOTATION-CONSISTENCY']
        if has_style: gates += ['STYLE-SOURCE-INDEPENDENCE','STYLE-LEDGER-FIDELITY']
    elif workflow == 'ARCHITECTURE_ONLY':
        gates += ['SECTION-NARRATIVE-FIDELITY','WHOLE-PAPER-NARRATIVE-FIDELITY']
    elif workflow == 'AUTHORIAL_NATURALIZATION_ONLY':
        gates += ['MATH-SEMANTICS','GENERATIVE-RESIDUE','AUTHORIAL-DECISION','PARAGRAPH-FINGERPRINT-FIDELITY','MATHEMATICAL-TRANSITIONS','COLD-AUTHOR']
    elif workflow == 'LATEX_NOTATION_ONLY':
        gates += ['MATH-SEMANTICS','NOTATION-CONSISTENCY']
    elif workflow == 'SUBMISSION_AUDIT_ONLY':
        gates += ALL_GATES
    if citations: gates.append('CITATION-INTEGRITY')
    if latex: gates.append('LATEX-INTEGRITY')
    gates=list(dict.fromkeys(gates))

    # Provisional ResearchDirectorAdvice is advisory only. Required states derived
    # from the TaskContract cannot be removed by advice. Unsupported additions
    # are rejected rather than silently changing workflow semantics.
    advice=task.get('director_advice') or {}
    advice_review={'accepted':[],'rejected':[]}
    for st in advice.get('recommended_skips',[]):
        if st in required:
            advice_review['rejected'].append({'recommendation':f'skip:{st}','reason':'state is required by deterministic workflow admissibility'})
        elif st in FULL_STATES:
            advice_review['accepted'].append({'recommendation':f'skip:{st}','reason':'state already non-required under deterministic plan'})
        else:
            advice_review['rejected'].append({'recommendation':f'skip:{st}','reason':'unknown state'})
    for st in advice.get('recommended_required_states',[]):
        if st in required:
            advice_review['accepted'].append({'recommendation':f'require:{st}','reason':'already required'})
        elif st not in FULL_STATES:
            advice_review['rejected'].append({'recommendation':f'require:{st}','reason':'unknown state'})
        elif bounded or writing_mode == 'LOCAL_POLISH':
            advice_review['rejected'].append({'recommendation':f'require:{st}','reason':'addition would expand the selected bounded writing route'})
        elif st in STYLE_STATES and not has_style:
            advice_review['rejected'].append({'recommendation':f'require:{st}','reason':'style-corpus state inadmissible without style corpus'})
        elif st in {'INTRODUCTION_NARRATIVE','FRONTMATTER'} and prior_gate != 'PASS' and 'PROOF_CORE_GATE' not in required:
            advice_review['rejected'].append({'recommendation':f'require:{st}','reason':'front matter lacks verified proof closure'})
        else:
            # Additions are conservative: they may increase work but cannot change canonical order.
            required=ordered_subset(required+[st])
            advice_review['accepted'].append({'recommendation':f'require:{st}','reason':'safe conservative addition'})

    # invariant checks
    pos={s:i for i,s in enumerate(required)}
    if 'FRONTMATTER' in pos and prior_gate != 'PASS':
        if 'PROOF_CORE_GATE' not in pos or pos['PROOF_CORE_GATE'] > pos['FRONTMATTER']:
            raise ValueError('front matter is inadmissible before verified proof closure')
    if 'INTRODUCTION_NARRATIVE' in pos and 'FRONTMATTER' in pos and pos['INTRODUCTION_NARRATIVE'] > pos['FRONTMATTER']:
        raise ValueError('introduction narrative must precede front matter')
    if 'PROOF_CORE' in pos and 'NOTATION_ARCHITECTURE' in pos and pos['NOTATION_ARCHITECTURE'] > pos['PROOF_CORE']:
        raise ValueError('notation architecture must precede proof core')
    if has_sources and workflow in {'FULL_MANUSCRIPT_RECONSTRUCTION','PROOF_BODY_ONLY'}:
        for s in ['INGEST','EXTRACT','LEDGER_LOCK','SOURCE_QUARANTINE']:
            if s not in pos: raise ValueError(f'missing mandatory source state: {s}')
    if has_style and any(s in pos for s in ['PROOF_CORE','FRONTMATTER']):
        if 'STYLE_QUARANTINE' not in pos:
            raise ValueError('style corpus must be distilled and quarantined before manuscript prose')

    return {
        'workflow': workflow,
        'writing_mode': writing_mode,
        **scopes,
        'required_states': required,
        'conditional_states': [] if bounded else (STYLE_STATES if not has_style else []),
        'skipped_states': skip_records(required,reasons),
        'artifact_inputs': task.get('artifact_inputs',[]),
        'artifact_outputs': task.get('requested_outputs',[]),
        'reused_artifacts': task.get('reused_artifacts',[]),
        'applicable_gates': gates,
        'blocker_owners': {},
        'critical_path': required,
        'director_advice_review': advice_review,
        'release_condition': 'accurate_status_only',
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('task', type=Path)
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    try:
        result=plan(load_data(args.task))
    except Exception as e:
        print(f'PLAN_INVALID: {e}', file=sys.stderr)
        sys.exit(2)
    if args.json or yaml is None:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(yaml.safe_dump(result, sort_keys=False, allow_unicode=True))
if __name__=='__main__': main()
