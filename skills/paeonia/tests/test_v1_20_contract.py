#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json, subprocess, tempfile
ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
p04a=(ROOT/'protocols/04a_grand_introduction_blueprint.md').read_text(encoding='utf-8')
p04d=(ROOT/'protocols/04d_introduction_paragraph_architecture.md').read_text(encoding='utf-8')
p04k=(ROOT/'protocols/04k_scientific_context_research.md').read_text(encoding='utf-8')
p04l=(ROOT/'protocols/04l_scientific_context_integration.md').read_text(encoding='utf-8')
p04m=(ROOT/'protocols/04m_contextual_grandeur.md').read_text(encoding='utf-8')
schema=yaml.safe_load((ROOT/'schemas/scientific_context_ledger.yaml').read_text(encoding='utf-8'))
art=yaml.safe_load((ROOT/'registry/artifacts.yaml').read_text(encoding='utf-8'))
gates=yaml.safe_load((ROOT/'registry/gates.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
checks={
 'version_floor':version >= (1,20,0),
 'two_axis_skill':'scientific-context depth' in skill.lower() and 'mathematical ambition' in skill.lower(),
 'audience_independent_protocol':'Audience specialization does **not** determine this value' in p04k and schema['trigger'].get('audience_independent') is True,
 'depth_modes':set(schema['trigger']['allowed'])=={'NONE','ORIGIN_BRIEF','SUBSTANTIAL','PHYSICS_LED','INTERDISCIPLINARY_LED'},
 'research_breadth_modes':set(schema['trigger']['research_breadth_allowed'])=={'NONE','COMPACT','TRIANGULATED','DEEP'},
 'dossier_roles':all(x in p04k for x in ['MODEL_ORIGIN','MECHANISM','REGIME_OR_SCALING','MATH_BRIDGE']),
 'model_to_math_required':'Map model language to mathematics' in p04k and 'model_to_math_map' in schema,
 'multi_paragraph_context':'multi-paragraph scientific opening is allowed' in p04l,
 'wallpaper_rejected':'Physics wallpaper test' in p04l,
 'grand_formula_first_rejected':'Formula-first prohibition when context is earned' in p04m,
 'pure_math_no_forced_context':'Do not infer that scientific context is needed merely because a PDE appears' in p04k,
 'old_specialist_suppression_removed':'Do not suppress scientifically operative model background' in p04a and 'Do not equate expert audience with removal of physical/scientific context' in p04d,
 'artifact_registered':'ScientificContextLedger' in art.get('artifacts',{}),
 'editorial_gate_repairs':all(x in gates['release_blockers']['EDITORIAL-IMPACT']['allowed_repairs'] for x in ['research_scientific_context','rebuild_grand_opening','add_model_to_math_bridge']),
 'manifest_engine':manifest.get('scientific_context_engine')=='triggered_evidence_dossier_with_model_to_math_map',
 'cases_109_118':all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(109,119)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_20_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)

# deterministic audit: good substantial ledger must pass; thin context must review
good={
 'trigger':{'detected':True,'context_depth':'SUBSTANTIAL','research_breadth':'TRIANGULATED'},
 'model_to_math_map':[{'scientific_object':'frequency','mathematical_object':'lambda_1','meaning':'spectral observable'}],
 'source_dossier':[{'role':r,'verified':True,'claim_supported':'supported','source_type':('ORIGINAL_OR_CANONICAL_SCIENCE' if i<2 else 'MATHEMATICAL_PHYSICS_BRIDGE')} for i,r in enumerate(['MODEL_ORIGIN','MECHANISM','REGIME_OR_SCALING','MATH_BRIDGE'])],
 'introduction_use':{'return_anchor_to_mathematics':'focal theorem'},
 'theorem_interpretation':{'scientific_interpretation':'calibrated','wording_ceiling':'idealized model only'},
 'integrity':{'context_depth_supported':True,'nontrivial_scientific_claims_verified':True,'model_to_math_bridge_complete':True,'decorative_context_removed':True,'theorem_interpretation_calibrated':True},
}
bad={
 'trigger':{'detected':True,'context_depth':'PHYSICS_LED','research_breadth':'COMPACT'},
 'model_to_math_map':[],
 'source_dossier':[{'role':'MODEL_ORIGIN','verified':False,'claim_supported':'generic physics'}],
 'introduction_use':{'return_anchor_to_mathematics':None},
 'theorem_interpretation':{'scientific_interpretation':'real-world consequence','wording_ceiling':None},
 'integrity':{'context_depth_supported':False,'nontrivial_scientific_claims_verified':False,'model_to_math_bridge_complete':False,'decorative_context_removed':False,'theorem_interpretation_calibrated':False},
}
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 gp=td/'good.yaml'; bp=td/'bad.yaml'
 gp.write_text(yaml.safe_dump(good,sort_keys=False),encoding='utf-8')
 bp.write_text(yaml.safe_dump(bad,sort_keys=False),encoding='utf-8')
 tool=ROOT/'tools/scientific_context_audit.py'
 a=subprocess.run([sys.executable,str(tool),str(gp)],capture_output=True,text=True)
 b=subprocess.run([sys.executable,str(tool),str(bp)],capture_output=True,text=True)
 if a.returncode!=0 or '"status": "PASS"' not in a.stdout:
  print(a.stdout,a.stderr); raise SystemExit('scientific context good audit failed')
 if b.returncode!=0 or '"status": "REVIEW"' not in b.stdout:
  print(b.stdout,b.stderr); raise SystemExit('scientific context bad audit failed')
print('V1_20_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
