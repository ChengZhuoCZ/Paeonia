#!/usr/bin/env python3
"""v1.43 release behavior: authorial prose, hard no-box, and honest diagnostics."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import yaml

R=Path(__file__).resolve().parents[1]
read=lambda r:(R/r).read_text(encoding='utf8')
manifest=json.loads(read('MANIFEST.json'))
registry=yaml.safe_load(read('registry/gates.yaml'))['release_blockers']
checks={
 'version':read('VERSION').strip()=='1.43.0' and manifest['version']=='1.43.0' and 'version: 1.43.0' in read('SKILL.md'),
 'authorial_protocol': all(x in read('protocols/05q_authorial_prose_integrity.md') for x in ['A1.','A10.','substitution test','cross-section','No ratio','LOCAL_POLISH']),
 'authorial_entry': all(x in read('SKILL.md') for x in ['05q_authorial_prose_integrity.md','authorial_prose_integrity.md','AI rate','Pass 13','Pass 14']),
 'single_voice_retained':'05p_unified_manuscript_voice.md' in read('SKILL.md'),
 'no_box_rule':all(x in read('protocols/09a_no_box_typesetting.md') for x in ['NO BOXES IN THE ARTICLE','\\boxed','\\fbox','tcolorbox','mdframed','framed','empheq','protected','PDF']),
 'no_box_entry':all(x in read('SKILL.md') for x in ['NO-BOX-TYPESETTING','tools/no_box_audit.py','09a_no_box_typesetting.md']),
 'no_box_registered':'NO-BOX-TYPESETTING' in registry and registry['NO-BOX-TYPESETTING']['audit_key']=='no_box_typesetting',
 'no_box_template':'NO-BOX-TYPESETTING: PENDING' in read('templates/submission_gate_report.md'),
 'no_box_schema':'no_box_typesetting' in yaml.safe_load(read('schemas/audit_report.yaml')),
 'no_box_scope':'even when compilation was not requested' in read('protocols/11_submission_gate.md'),
 'submissions':'`NO-BOX-TYPESETTING`' in read('protocols/11_submission_gate.md') and 'Protocol 05q' in read('protocols/11_submission_gate.md'),
 'checklists':all((R/x).is_file() for x in ['checklists/authorial_prose_integrity.md','checklists/no_box_typesetting.md']),
 'manifest_hard_rule':'no_visual_boxes_in_any_delivered_manuscript' in manifest['hard_invariants'],
 'test_declared':'tests/test_v1_43_contract.py' in manifest['tests'],
 'diagnostic_scope':'not an AI classifier' in read('protocols/05q_authorial_prose_integrity.md'),
}

sys.path.insert(0,str(R/'tools'))
from no_box_audit import audit
from prose_residue_review import review
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp)
 p=root/'main.tex'; child=root/'part.tex'
 p.write_text(r'''\documentclass{article}
% \boxed{COMMENT}
\begin{document}
\verb|\boxed{VERBATIM}|
\begin{verbatim}
\boxed{LITERAL}
\end{verbatim}
\input{part}
\begin{equation} a=b\end{equation}
\mbox{invisible alignment text}
\end{document}
''',encoding='utf8')
 child.write_text('Here is a proof without a box.\n',encoding='utf8')
 checks['no_box_clean_inputs']=audit([p])['status']=='STATIC_PASS' and len(audit([p])['files_inspected'])==2
 child.write_text(r'\boxed{a=b}',encoding='utf8')
 checks['no_box_nested_blocked']=audit([p])['status']=='FAIL' and any(i['code']=='BOX_MACRO' for i in audit([p])['violations'])
 child.write_text(r'\begin{tcolorbox} X \end{tcolorbox}',encoding='utf8')
 checks['no_box_env_blocked']=audit([p])['status']=='FAIL' and any(i['code']=='BOX_ENV' for i in audit([p])['violations'])
 child.write_text(r'\usepackage[most]{tcolorbox,hyperref}',encoding='utf8')
 checks['no_box_package_blocked']=audit([p])['status']=='FAIL' and any(i['code']=='BOX_PACKAGE' for i in audit([p])['violations'])
 child.write_text(r'\begin{empheq}[box=\fbox]{align} x=y\end{empheq}',encoding='utf8')
 checks['no_box_empheq_blocked']=audit([p])['status']=='FAIL' and any(i['code']=='BOX_EQUATION_OPTION' for i in audit([p])['violations'])
 child.write_text(r'\newtcolorbox{mydefinition}{}',encoding='utf8')
 checks['no_box_constructor_blocked']=audit([p])['status']=='FAIL'
 child.unlink()
 checks['no_box_missing_local_input']=audit([p])['status']=='FAIL' and len(audit([p])['missing_local_inputs'])==1
 # The English recurrence diagnostic produces locations, not a percentage.
 t=root/'prose.txt';t.write_text(('We now turn to the next result.\n'*3+'The hypothesis forces uniform boundedness.\n'),encoding='utf8')
 r=review(t)
 checks['advisory_only']=r['diagnosis']=='REVIEW' and r['ai_percentage']=='NOT_DEFINED' and r['authorship_inference']=='NOT_SUPPORTED' and bool(r['findings'])

# The pre-existing static manuscript gate must also enforce no-box.
with tempfile.TemporaryDirectory() as tmp:
    tex=Path(tmp)/'boxed.tex'
    tex.write_text(r'\boxed{x=y}',encoding='utf8')
    proc=subprocess.run([sys.executable,str(R/'tools/manuscript_static_gate.py'),str(tex)],capture_output=True,text=True)
    checks['static_gate_integrated']=proc.returncode!=0 and 'NO-BOX-TYPESETTING' in proc.stdout

checks['fixtures']=all(any((R/'tests/behavioral_cases').glob(f'{i}_*.yaml')) and any((R/'tests/regression_cases').glob(f'{i}_*.md')) for i in range(215,223))
if any(not x for x in checks.values()):
 print('V1_43_CONTRACT_FAIL', ', '.join(k for k,v in checks.items() if not v)); sys.exit(1)
print('V1_43_CONTRACT_PASS')
print('checks='+str(len(checks)))
