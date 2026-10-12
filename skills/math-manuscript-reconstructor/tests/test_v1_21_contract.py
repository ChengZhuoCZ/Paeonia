#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json, subprocess, tempfile
ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
p04n=(ROOT/'protocols/04n_mathematical_story_discovery.md').read_text(encoding='utf-8')
p04o=(ROOT/'protocols/04o_mathematical_story_integration.md').read_text(encoding='utf-8')
p04d=(ROOT/'protocols/04d_introduction_paragraph_architecture.md').read_text(encoding='utf-8')
p04j=(ROOT/'protocols/04j_editorial_impact_gate.md').read_text(encoding='utf-8')
schema=yaml.safe_load((ROOT/'schemas/mathematical_story_ledger.yaml').read_text(encoding='utf-8'))
art=yaml.safe_load((ROOT/'registry/artifacts.yaml').read_text(encoding='utf-8'))
gates=yaml.safe_load((ROOT/'registry/gates.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
checks={
 'version_floor':version >= (1,21,0),
 'skill_story_contract':'MathematicalStoryLedger' in skill and 'MATHEMATICAL-STORY-INTEGRITY' in skill,
 'hierarchy_climb':all(x in p04n for x in ['FOCAL_THEOREM','FOCAL_PROBLEM','PARENT_PROGRAM','CANONICAL_PRINCIPLE']),
 'story_archetypes':all(x in p04n for x in ['CONTINUUM_TO_FINITE_COMPLEXITY','LIMIT_TO_EXACT_FINITE','LOCAL_TO_GLOBAL','QUALITATIVE_TO_QUANTITATIVE','SYMMETRY_TO_RIGIDITY']),
 'scale_transition':'why the target side is not a routine corollary' in p04n,
 'ancestry_roles':all(x in p04n for x in ['PROGRAM_ORIGIN','CANONICAL_THEOREM','GLOBAL_FRONTIER','OBSTRUCTION_EVIDENCE']),
 'program_return':'interpret it back at the scale of the story ledger' in p04o.lower(),
 'science_independent':'Scientific context from Protocol 04k is a second axis' in p04o,
 'paragraph_roles':all(x in p04d for x in ['PROGRAM_ORIENTATION','CANONICAL_PRINCIPLE','SCALE_TRANSITION','PROGRAM_RETURN']),
 'editorial_story_gate':'MathematicalStoryLedger' in p04j and 'parent mathematical program' in p04j,
 'schema_depth_modes':set(schema['trigger']['research_depth_allowed'])=={'COMPACT','TRIANGULATED','DEEP'},
 'schema_program_return':schema['integrity'].get('theorem_returns_to_parent_program') is False,
 'artifact_registered':'MathematicalStoryLedger' in art.get('artifacts',{}),
 'gate_registered':'MATHEMATICAL-STORY-INTEGRITY' in gates.get('release_blockers',{}),
 'manifest_engine':manifest.get('mathematical_story_engine')=='parent_program_scale_transition_and_program_return',
 'cases_119_128':all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(119,129)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_21_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)

# deterministic ledger audit: a real parent program + transition passes; local-only grandeur reviews
good={
 'trigger':{'required':True,'research_depth':'TRIANGULATED'},
 'hierarchy':{'focal_theorem':'exact finite rigidity','focal_problem':'polygonal extremum','parent_program':'isoperimetric shape optimization under finite complexity','canonical_principle':'symmetrization selects the continuum optimizer'},
 'story_archetypes':{'primary':'CONTINUUM_TO_FINITE_COMPLEXITY','secondary':['LIMIT_TO_EXACT_FINITE']},
 'scale_transitions':[{'from':'continuum optimizer','to':'exact N-sided optimizer','why_not_routine':'symmetrization leaves the polygonal class','evidence_anchor':'verified literature'}],
 'structural_tensions':[{'tension':'continuum symmetry versus finite-side admissibility','mathematical_objects':['disk','N-gon'],'theorem_level_relevance':'central','proof_obstruction_anchor':'proof graph'}],
 'story_graph':{'nodes':['continuum theorem','polygonal problem','present theorem'],'edges':[{'from':'continuum theorem','to':'polygonal problem','relation':'RESTRICTS_TO'},{'from':'polygonal problem','to':'present theorem','relation':'RIGIDIFIES'}],'critical_story_path':['continuum theorem','polygonal problem','present theorem']},
 'mathematical_ancestry':[{'role':'CANONICAL_THEOREM','work':'benchmark','verified_claim':'disk optimizer','evidence_anchor':'verified','why_story_needs_it':'continuum benchmark'}],
 'parallel_problems':[],
 'program_interpretation':{'theorem_role':'UPGRADES_ASYMPTOTIC_SELECTION_TO_EXACT_RIGIDITY','program_level_consequence':'finite-complexity extremal structure becomes exact in the stated regime','factuality_ceiling':'stated regime only'},
 'opening':{'preferred_entry':'CANONICAL_PRINCIPLE','first_page_goal':'continuum-to-finite transition','theorem_entry_anchor':'exact finite gap'},
 'proof_story':{'transition_to_explain':'limit to exact finite','mechanism_that_crosses_transition':'gap plus rigidity'},
 'scientific_context_relation':{'mode':'MATH_ONLY_MAINLINE'},
 'story_compression':{'diagnostic_sentence':'Within the isoperimetric program, the continuum optimizer predicts the finite candidate but the admissible class destroys symmetrization; the theorem restores exact rigidity through a finite-gap mechanism.','publication_template_forbidden':True},
 'integrity':{'parent_program_is_mathematically_specific':True,'primary_archetype_supported':True,'scale_transition_or_tension_supported':True,'ancestry_claims_verified':True,'story_graph_has_nontrivial_critical_path':True,'parallel_problems_are_structurally_relevant':True,'theorem_returns_to_parent_program':True,'no_generic_grandeur':True,'no_story_inflation_beyond_evidence':True},
}
bad={
 'trigger':{'required':True,'research_depth':'COMPACT'},
 'hierarchy':{'focal_theorem':'technical estimate','focal_problem':'same estimate','parent_program':'important area of mathematics','canonical_principle':None},
 'story_archetypes':{'primary':None,'secondary':[]},
 'scale_transitions':[], 'structural_tensions':[], 'story_graph':{'nodes':[],'edges':[],'critical_story_path':[]}, 'mathematical_ancestry':[], 'parallel_problems':[],
 'program_interpretation':{'theorem_role':None,'program_level_consequence':None,'factuality_ceiling':None},
 'opening':{'preferred_entry':'PARENT_PROGRAM','first_page_goal':'say field is important','theorem_entry_anchor':None},
 'proof_story':{'transition_to_explain':None,'mechanism_that_crosses_transition':None},
 'scientific_context_relation':{'mode':'MATH_ONLY_MAINLINE'},
 'story_compression':{'diagnostic_sentence':None,'publication_template_forbidden':True},
 'integrity':{'parent_program_is_mathematically_specific':False,'primary_archetype_supported':False,'scale_transition_or_tension_supported':False,'ancestry_claims_verified':False,'story_graph_has_nontrivial_critical_path':False,'parallel_problems_are_structurally_relevant':True,'theorem_returns_to_parent_program':False,'no_generic_grandeur':False,'no_story_inflation_beyond_evidence':False},
}
with tempfile.TemporaryDirectory() as td:
 td=Path(td); gp=td/'good.yaml'; bp=td/'bad.yaml'
 gp.write_text(yaml.safe_dump(good,sort_keys=False),encoding='utf-8')
 bp.write_text(yaml.safe_dump(bad,sort_keys=False),encoding='utf-8')
 tool=ROOT/'tools/mathematical_story_audit.py'
 a=subprocess.run([sys.executable,str(tool),str(gp)],capture_output=True,text=True)
 b=subprocess.run([sys.executable,str(tool),str(bp)],capture_output=True,text=True)
 if a.returncode!=0 or '"status": "PASS"' not in a.stdout:
  print(a.stdout,a.stderr); raise SystemExit('mathematical story good audit failed')
 if b.returncode!=0 or '"status": "REVIEW"' not in b.stdout:
  print(b.stdout,b.stderr); raise SystemExit('mathematical story bad audit failed')
print('V1_21_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
