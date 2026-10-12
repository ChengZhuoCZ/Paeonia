#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

EMPTY_PATTERNS={
    'we_now':r'\bwe now\b',
    'we_next':r'\bwe next\b',
    'we_proceed':r'\bwe (?:then )?proceed\b',
    'we_turn':r'\bwe (?:now )?turn\b',
    'it_remains':r'\bit remains to\b',
    'worth_noting':r'\bit is worth (?:noting|observing|mentioning)\b',
    'as_seen':r'\bas we have (?:seen|noted|observed)\b',
    'combining_above':r'\bcombining (?:the|these|all the) above\b',
    'generic_key':r'\b(?:the )?(?:key|crucial|important|fundamental) (?:point|observation|step|estimate|fact)\b',
}
ACTION_WORDS=r'\b(?:choose|define|write|split|apply|differentiate|integrate|estimate|bound|compare|rescale|normalize|truncate|localize|project|factor|absorb|sum|interpolate|iterate|let|pass|deduce|exclude|identify|reduce|extend|approximate)\b'
WORD=re.compile(r"[A-Za-z][A-Za-z'-]*")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--review-rate', type=float, default=8.0, help='empty-signposting occurrences per 1000 words')
    ap.add_argument('--fail-on-review', action='store_true')
    args=ap.parse_args()
    text=Path(args.file).read_text(encoding='utf-8',errors='ignore')
    words=WORD.findall(text); wc=max(1,len(words))
    counts={k:len(re.findall(p,text,re.I)) for k,p in EMPTY_PATTERNS.items()}
    empty=sum(counts.values())
    actions=len(re.findall(ACTION_WORDS,text,re.I))
    rate=1000*empty/wc
    out={
        'tool':'transition_density',
        'word_count':wc,
        'empty_signposting_counts':counts,
        'empty_signposting_per_1000_words':round(rate,3),
        'mathematical_action_verbs_per_1000_words':round(1000*actions/wc,3),
        'status':'REVIEW' if rate>args.review_rate else 'PASS',
        'note':'review relation semantics before deleting; do not replace repeated connectors by random synonyms',
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))
    if args.fail_on_review and out['status']=='REVIEW': raise SystemExit(2)

if __name__=='__main__': main()
