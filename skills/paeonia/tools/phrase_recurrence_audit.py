#!/usr/bin/env python3
import argparse, json, re
from collections import Counter
from pathlib import Path

MATH_BLOCKS = re.compile(r"\\\[(?:.|\n)*?\\\]|\\\((?:.|\n)*?\\\)|\$\$(?:.|\n)*?\$\$|\$(?:\\.|[^$])*?\$", re.S)
COMMAND = re.compile(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

EXCLUDE = {
    ('of','the','proof'), ('in','the','proof'), ('for','all','sufficiently'),
    ('by','the','triangle'), ('by','the','cauchy'), ('with','respect','to'),
}

def prose(text: str) -> str:
    text = MATH_BLOCKS.sub(' ', text)
    text = COMMAND.sub(' ', text)
    text = re.sub(r"%.*", " ", text)
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--ngram', type=int, default=4)
    ap.add_argument('--threshold', type=int, default=5)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--fail-on-review', action='store_true')
    args = ap.parse_args()

    text = prose(Path(args.file).read_text(encoding='utf-8', errors='ignore'))
    words = [w.lower() for w in WORD.findall(text)]
    n = max(2, args.ngram)
    grams = Counter(tuple(words[i:i+n]) for i in range(max(0, len(words)-n+1)))
    repeated = []
    for g,c in grams.most_common():
        if c < args.threshold:
            break
        if n == 3 and g in EXCLUDE:
            continue
        repeated.append({'phrase':' '.join(g), 'count':c})
        if len(repeated) >= args.top:
            break

    starters = Counter()
    for s in re.split(r'(?<=[.!?])\s+', text):
        toks = [w.lower() for w in WORD.findall(s)]
        if len(toks) >= 3:
            starters[' '.join(toks[:3])] += 1
    repeated_starters = [
        {'starter':k,'count':v} for k,v in starters.most_common(args.top)
        if v >= args.threshold
    ]

    out = {
        'tool':'phrase_recurrence_audit',
        'ngram':n,
        'threshold':args.threshold,
        'word_count':len(words),
        'repeated_ngrams':repeated,
        'repeated_sentence_starters':repeated_starters,
        'status':'REVIEW' if repeated or repeated_starters else 'PASS',
        'automatic_rewrite':False,
        'synonym_substitution':False,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    if args.fail_on_review and out['status'] == 'REVIEW':
        raise SystemExit(2)

if __name__ == '__main__':
    main()
