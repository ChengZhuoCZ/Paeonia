#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml

ROOT=Path(__file__).resolve().parents[1]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
protocol=(ROOT/'protocols/04_introduction_abstract.md').read_text(encoding='utf-8')
prose_gate=(ROOT/'protocols/04g_introduction_prose_integrity.md').read_text(encoding='utf-8')
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
core=yaml.safe_load((ROOT/'schemas/introduction_core_brief.yaml').read_text(encoding='utf-8'))
checks={
    'version_floor': tuple(map(int,manifest.get('version','0.0.0').split('.'))) >= (1,36,0),
    'reader_first_engine': 'introduction_engine: reader_first_core_brief' in skill,
    'protocol_authority': 'This protocol is the ordinary entry point for front matter' in protocol,
    'core_brief': core.get('core',{}).get('exact_question') is None and 'IntroductionCoreBrief' in skill,
    'one_arc': 'choose one narrative arc' in protocol.lower(),
    'swap_test': 'swap test' in protocol.lower() and 'survives the swap test' in prose_gate.lower(),
    'reader_contract': all(x in protocol for x in ['What is the exact problem?', 'What precisely was unknown?', 'What exactly is proved here?']),
    'optional_modules': 'do not instantiate every narrative ledger' in protocol.lower() and 'Do not instantiate all optional artifacts' in skill,
    'amplification_conditional': 'not part of the default route' in protocol.lower() and 'off_unless_specific_underpositioning_is_diagnosed' in skill,
    'integrated_paragraphs': 'Several functions may coexist in one paragraph' in protocol,
    'theorem_page_two_allowed': 'page 2 is natural' in protocol,
    'legacy_compatibility': all(x in skill for x in ['IntroductionNarrativeLedger','MathematicalStoryLedger','NarrativeAmbitionLedger','ScientificContextLedger','IntroductionParagraphPlan','GRAND_PLUS']),
}
bad=[k for k,v in checks.items() if not v]
if bad:
    print('V1_36_CONTRACT_FAIL')
    for k in bad: print(k)
    sys.exit(1)
print('V1_36_CONTRACT_PASS')
print('checks='+str(len(checks)))
