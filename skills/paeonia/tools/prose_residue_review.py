#!/usr/bin/env python3
"""Flag repeated formulaic manuscript prose for contextual editorial review.

No authorship classification and no AI percentage. Findings are not automatic errors.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re

from no_box_audit import clean_tex

# Deliberately short, high-precision review triggers rather than a blacklist of
# common mathematical English. One use of a phrase is not proof of bad prose.
PATTERNS = {
    'EMPTY_SIGNPOST': r'\b(?:we now (?:turn|proceed|move)|we next (?:turn|proceed)|we are now (?:ready|in a position)|it is worth noting that)\b',
    'UNSUPPORTED_GRANDEUR': r'\b(?:a topic of fundamental importance|far-reaching implications|opens up new avenues|a rich and fascinating (?:area|field)|sheds new light on)\b',
    'PROOF_TEMPLATE': r'\b(?:the proof consists of the following (?:steps|parts)|we organize the proof into (?:three|four|five) steps|this completes the proof of the (?:lemma|theorem))\b',
    'META_RECAP': r'\b(?:in summary, we have shown|as we have seen above|to summarize the preceding discussion)\b',
    'CN_ADMINISTRATIVE': r'(?:接下来我们将|值得注意的是|在本节中我们将|不难看出|综上所述)',
}
REVIEW_THRESHOLD={'EMPTY_SIGNPOST':2,'UNSUPPORTED_GRANDEUR':1,'PROOF_TEMPLATE':3,'META_RECAP':2,'CN_ADMINISTRATIVE':3}


def review(path: Path):
    src=path.read_text(encoding='utf-8',errors='replace')
    cleaned=clean_tex(src) if path.suffix.lower()=='.tex' else src
    grouped=defaultdict(list)
    for tag,pat in PATTERNS.items():
        for m in re.finditer(pat,cleaned,flags=re.I):
            # Skip TeX command names and citation/label contexts where feasible.
            prefix=cleaned[max(0,m.start()-12):m.start()]
            if re.search(r'\\(?:cite|label|ref|eqref)\{[^}]*$',prefix): continue
            line=cleaned.count('\n',0,m.start())+1
            grouped[tag].append({'line':line,'phrase':m.group(0)})
    findings=[]
    for tag,items in grouped.items():
        if len(items)>=REVIEW_THRESHOLD[tag]:
            findings.append({'category':tag,'count':len(items),'locations':items,
                             'decision':'REVIEW_IN_MATHEMATICAL_CONTEXT'})
    return {'file':str(path),'diagnosis':'REVIEW' if findings else 'NO_HIGH_CONFIDENCE_RECURRENT_PATTERNS',
            'findings':findings,'authorship_inference':'NOT_SUPPORTED','ai_percentage':'NOT_DEFINED'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('files',nargs='+',type=Path)
    p.add_argument('--json',action='store_true')
    args=p.parse_args()
    results=[review(file) for file in args.files]
    if args.json: print(json.dumps(results,indent=2,ensure_ascii=False))
    else:
        for result in results:
            print(result['file']+': '+result['diagnosis'])
            for f in result['findings']:
                print('  '+f['category']+': '+str(f['count'])+' occurrences at lines '+', '.join(str(x['line']) for x in f['locations']))
        print('Review diagnostics only; no AI authorship score or literary certification.')

if __name__=='__main__':
    main()
