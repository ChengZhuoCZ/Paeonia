#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

GRAND_SCALES={'EXPANSIVE','GRAND','GRAND_PLUS'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('ledger',type=Path)
    args=ap.parse_args()
    data=yaml.safe_load(args.ledger.read_text(encoding='utf-8')) or {}
    flags=[]
    trigger=data.get('trigger') or {}
    hierarchy=data.get('hierarchy') or {}
    arch=data.get('story_archetypes') or {}
    integrity=data.get('integrity') or {}
    transitions=data.get('scale_transitions') or []
    tensions=data.get('structural_tensions') or []
    ancestry=data.get('mathematical_ancestry') or []
    graph=data.get('story_graph') or {}
    interp=data.get('program_interpretation') or {}
    compression=data.get('story_compression') or {}

    if trigger.get('required'):
        if not hierarchy.get('parent_program'):
            flags.append('missing_parent_program')
        if not hierarchy.get('canonical_principle') and not hierarchy.get('stop_reason_if_no_higher_level'):
            flags.append('missing_canonical_principle_or_stop_reason')
        if not arch.get('primary'):
            flags.append('missing_primary_story_archetype')
        if not transitions and not tensions:
            flags.append('missing_scale_transition_or_structural_tension')
        if not ancestry:
            flags.append('missing_mathematical_ancestry')
        path=graph.get('critical_story_path') or []
        if len(path) < 2:
            flags.append('missing_nontrivial_critical_story_path')
        if not interp.get('program_level_consequence'):
            flags.append('missing_program_level_theorem_interpretation')
        if not compression.get('diagnostic_sentence'):
            flags.append('missing_story_compression_diagnostic')

    required_integrity=[
        'parent_program_is_mathematically_specific',
        'primary_archetype_supported',
        'scale_transition_or_tension_supported',
        'ancestry_claims_verified',
        'story_graph_has_nontrivial_critical_path',
        'theorem_returns_to_parent_program',
        'no_generic_grandeur',
        'no_story_inflation_beyond_evidence',
    ]
    for key in required_integrity:
        if trigger.get('required') and integrity.get(key) is not True:
            flags.append('integrity_'+key)
    if integrity.get('parallel_problems_are_structurally_relevant') is False:
        flags.append('decorative_parallel_problem')

    status='PASS' if not flags else 'REVIEW'
    out={
        'status':status,
        'required':bool(trigger.get('required')),
        'research_depth':trigger.get('research_depth'),
        'parent_program':hierarchy.get('parent_program'),
        'primary_archetype':arch.get('primary'),
        'scale_transition_count':len(transitions),
        'structural_tension_count':len(tensions),
        'ancestry_count':len(ancestry),
        'critical_story_path_length':len(graph.get('critical_story_path') or []),
        'flags':flags,
        'diagnostic_only':True,
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
