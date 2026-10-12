#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
protocol=(ROOT/'protocols/05o_author_corpus_supplement.md').read_text(encoding='utf-8')
modes=(ROOT/'protocols/00_writing_modes.md').read_text(encoding='utf-8')
state=(ROOT/'protocols/12_execution_state_machine.md').read_text(encoding='utf-8')
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
dossier=yaml.safe_load((ROOT/'schemas/author_corpus_dossier.yaml').read_text(encoding='utf-8'))
artifacts=yaml.safe_load((ROOT/'registry/artifacts.yaml').read_text(encoding='utf-8'))['artifacts']
checks={
 'version': version >= (1,38,0) and tuple(map(int,manifest.get('version','0.0.0').split('.'))) >= (1,38,0) and 'version: 1.' in skill,
 'author_acquisition_v142_supersession': all(x in protocol for x in ['does **not** ask the user to choose an author', 'user has already supplied', 'Do not ask for an author']) and 'Do not ask for an author/style preference' in state,
 'preserve_old_routes': 'preserves the existing reconstruction and local-polish routes' in protocol and 'does not change the selected writing mode' in modes,
 'identity_before_download': all(x in protocol for x in ['A name is not an identity','do not guess','UNRESOLVED']),
 'open_access': all(x in protocol for x in ['legally accessible','Never circumvent a paywall','prefer the latest author-prepared preprint']),
 'balanced_selection': all(x in protocol for x in ['topic-near','author-central','recent','authorship-control','genre-match']),
 'paper_count': manifest.get('author_corpus_default_papers')==4 and manifest.get('author_corpus_allowed_range')==[3,6],
 'coauthor_caution': all(x in protocol for x in ['A coauthored paper does not reveal who wrote a sentence','author-associated corpus profile','CROSS_COLLABORATION_STABLE']),
 'style_not_literature': 'not automatically evidence' in protocol and 'Protocol 07' in protocol,
 'soft_priority': all(x in protocol for x in ['accepted `LOCAL_POLISH` baseline', 'compatible stable author-corpus traits', 'generic cosmetic preferences', 'Protocol 05p']),
 'dossier': dossier.get('artifact')=='AuthorCorpusDossier' and 'AuthorCorpusDossier' in artifacts,
 'state_integration': 'Protocol 05o runs only' in state and 'AuthorCorpusDossier' in state,
 'no_persona': all(x in protocol for x in ['not to “write like”','phrase bank','persona']),
 'cases_155_162': all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(155,163)),
}
bad=[k for k,v in checks.items() if not v]
if bad:
 print('V1_38_CONTRACT_FAIL')
 for k in bad: print(k)
 sys.exit(1)
print('V1_38_CONTRACT_PASS')
print('checks='+str(len(checks)))
