#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from execution_planner import plan
fail=[]

def before(seq,a,b,label):
    try:
        if seq.index(a)>=seq.index(b): fail.append(label)
    except ValueError: fail.append(label+'_missing')

full=plan({'workflow':'FULL_MANUSCRIPT_RECONSTRUCTION','has_math_sources':True,'has_style_corpus':True,'authorial_naturalization':True,'latex_output':True,'citations_or_external_inputs':True})
before(full['required_states'],'EXECUTION_PLAN','INGEST','plan_before_ingest')
before(full['required_states'],'STYLE_QUARANTINE','PROOF_CORE','style_before_proof')
before(full['required_states'],'PROOF_CORE_GATE','FRONTMATTER','proof_before_frontmatter')
if 'LATEX-INTEGRITY' not in full['applicable_gates']: fail.append('latex_gate_missing')
if 'CITATION-INTEGRITY' not in full['applicable_gates']: fail.append('citation_gate_missing')

nstyle=plan({'workflow':'FULL_MANUSCRIPT_RECONSTRUCTION','has_math_sources':True,'has_style_corpus':False})
if any(s in nstyle['required_states'] for s in ['STYLE_EXTRACT','STYLE_QUARANTINE']): fail.append('style_states_not_skipped')
if 'MANUSCRIPT_ARCHITECTURE' not in nstyle['required_states']: fail.append('universal_architecture_disabled_without_style')

proof=plan({'workflow':'PROOF_BODY_ONLY','has_math_sources':True,'has_style_corpus':False})
if 'FRONTMATTER' in proof['required_states']: fail.append('proof_only_frontmatter')
if 'PROOF_CORE_GATE' not in proof['required_states']: fail.append('proof_only_missing_gate')

front=plan({'workflow':'FRONTMATTER_FROM_VERIFIED_PROOF','has_math_sources':False,'existing_proof_core_gate':'PASS'})
if 'PROOF_CORE' in front['required_states']: fail.append('frontmatter_rebuilt_proof_unnecessarily')
if 'FRONTMATTER' not in front['required_states']: fail.append('frontmatter_missing')

try:
    plan({'workflow':'FRONTMATTER_FROM_VERIFIED_PROOF','existing_proof_core_gate':'NONE'})
    fail.append('unverified_frontmatter_accepted')
except ValueError:
    pass

try:
    plan({'workflow':'AUTHORIAL_NATURALIZATION_ONLY','semantic_checksum_available':False})
    fail.append('naturalization_without_checksum_accepted')
except ValueError:
    pass

advised=plan({'workflow':'FULL_MANUSCRIPT_RECONSTRUCTION','has_math_sources':True,'has_style_corpus':False,'director_advice':{'recommended_skips':['LEDGER_LOCK','PROOF_CORE_GATE'],'recommended_required_states':['STYLE_EXTRACT']}})
if 'LEDGER_LOCK' not in advised['required_states'] or 'PROOF_CORE_GATE' not in advised['required_states']: fail.append('director_advice_bypassed_mandatory_state')
rejected=' '.join(x['recommendation'] for x in advised['director_advice_review']['rejected'])
if 'skip:LEDGER_LOCK' not in rejected or 'skip:PROOF_CORE_GATE' not in rejected or 'require:STYLE_EXTRACT' not in rejected: fail.append('director_advice_filter_not_recording_rejections')

if fail:
    print('EXECUTION_PLANNER_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('EXECUTION_PLANNER_PASS')
