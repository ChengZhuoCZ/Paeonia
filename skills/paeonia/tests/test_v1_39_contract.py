#!/usr/bin/env python3
from pathlib import Path
import json,sys,yaml
ROOT=Path(__file__).resolve().parents[1]
read=lambda p:(ROOT/p).read_text(encoding='utf-8')
skill=read('SKILL.md');p04=read('protocols/04_introduction_abstract.md');u=read('protocols/04u_literature_discovery_and_credit.md');v=read('protocols/04v_evidence_grounded_grand_narrative.md');p07=read('protocols/07_citation_integrity.md');doc=read('README.md')
m=json.loads(read('MANIFEST.json'))
a=yaml.safe_load(read('registry/artifacts.yaml'))['artifacts']
d=yaml.safe_load(read('schemas/introduction_literature_dossier.yaml'))
c=yaml.safe_load(read('schemas/introduction_core_brief.yaml'))
checks={
 'version':tuple(map(int,read('VERSION').strip().split('.'))) >= (1,39,0) and tuple(map(int,m['version'].split('.'))) >= (1,39,0) and 'version: 1.' in skill,
 'default_search_before_intro': all(x in p04 for x in ['before building the final brief','Protocol 04u is the default external scholarly research pass','outside search is unavailable']),
 'skill_routing': all(x in skill for x in ['protocols/04u_literature_discovery_and_credit.md','protocols/04v_evidence_grounded_grand_narrative.md','IntroductionLiteratureDossier']),
 'multiple_discovery_routes': all(x in u for x in ['at least two materially independent discovery routes','outside','arXiv','Crossref','MathSciNet']),
 'fair_credit': all(x in u for x in ['positive credit','ORIGIN','DIRECT_PREDECESSOR','METHOD_ANCESTOR','PARALLEL_OR_INDEPENDENT']),
 'primary_source_priority': all(x in u for x in ['primary source','source and claim verification','failed search','cannot prove an absence']),
 'granularity': all(x in u for x in ['different and sometimes incomparable axes','There is no preset cap','frontier comparison']),
 'program_test_not_hype': all(x in v for x in ['Always test','larger mathematical program','DIRECT','PROGRAMMATIC','HISTORICAL_SYNTHESIS','invented']),
 'grand_requires_credit': all(x in v for x in ['credit map','positive credit','primary story','contrast']),
 'offline_and_polish': all(x in u for x in ['OFFLINE_INCOMPLETE','LOCAL_POLISH','protected prose']),
 'citation_distinction': 'Discovery is not verification' in p07 and 'checking every source already in a `.bib`' in p07,
 'dossier': d['artifact']=='IntroductionLiteratureDossier' and 'IntroductionLiteratureDossier' in a,
 'core_compatibility': c['version']==2 and 'literature_research' in c and 'programmatic_story' in c,
 'docs': 'v1.39.0' in doc and 'fair credit' in doc.lower(),
 'behavioral_regressions': all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) and any((ROOT/'tests/regression_cases').glob(f'{i}_*.md')) for i in range(163,173)),
}
bad=[k for k,val in checks.items() if not val]
if bad:
 print('V1_39_CONTRACT_FAIL',','.join(bad));sys.exit(1)
print('V1_39_CONTRACT_PASS')
print('checks='+str(len(checks)))
