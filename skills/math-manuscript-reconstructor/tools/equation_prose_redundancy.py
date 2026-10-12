#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

DISPLAY = re.compile(r"\\\[(?P<bracket>.*?)\\\]|\$\$(?P<dollar>.*?)\$\$|\\begin\{(?:equation\*?|align\*?|gather\*?)\}(?P<env>.*?)\\end\{(?:equation\*?|align\*?|gather\*?)\}", re.S)
FOLLOW = re.compile(
    r"^\s*(?:This|The)\s+(?:inequality|identity|formula|equation|estimate|relation)\s+"
    r"(?:shows|states|says|means|tells us|expresses)\s+that\b|"
    r"^\s*In\s+other\s+words\b|^\s*Equivalently,?\s+this\s+(?:says|means)\b",
    re.I,
)
ALLOWED = re.compile(r"\b(?:implies|forces|yields|gives|permits|allows|contradicts|converges|vanishes|uniform|equality|rigidity|coerciv|compact|decay|bounded)\b", re.I)

def line_no(text, pos): return text.count('\n',0,pos)+1

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--fail-on-review', action='store_true')
    args=ap.parse_args()
    text=Path(args.file).read_text(encoding='utf-8',errors='ignore')
    flags=[]
    for m in DISPLAY.finditer(text):
        tail=text[m.end():]
        sm=re.search(r"\S(?:.|\n){0,420}?(?:[.!?](?:\s|$)|\n\n)",tail)
        if not sm: continue
        sent=sm.group(0).strip().replace('\n',' ')
        if FOLLOW.search(sent) and not ALLOWED.search(sent):
            flags.append({'line':line_no(text,m.end()),'followup':sent[:220],'reason':'possible_display_restatement'})
    out={
        'tool':'equation_prose_redundancy',
        'flags':flags,
        'status':'REVIEW' if flags else 'PASS',
        'policy':'post-display prose should add consequence, legality, interpretation, parameter dependence, equality, or transition',
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))
    if args.fail_on_review and flags: raise SystemExit(2)

if __name__=='__main__': main()
