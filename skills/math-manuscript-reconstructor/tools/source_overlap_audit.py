#!/usr/bin/env python3
"""Heuristic prose-overlap audit for source-independence review.

This tool is deliberately conservative. It strips common LaTeX math regions and
reports shared ordinary-prose n-grams. A hit is a review trigger, not proof of
copying.
"""
import argparse, re
from collections import Counter

MATH_PATTERNS = [
    r"\$\$.*?\$\$", r"\$.*?\$", r"\\\[.*?\\\]", r"\\\(.*?\\\)",
    r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{[^}]+\}",
]

COMMON = {
    "this completes the proof", "without loss of generality",
    "by the triangle inequality", "by holder s inequality",
    "by cauchy schwarz", "the following lemma", "the following theorem",
}

def prose_tokens(text: str):
    for p in MATH_PATTERNS:
        text = re.sub(p, " ", text, flags=re.S)
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    text = re.sub(r"[{}_^&~#]", " ", text)
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())

def ngrams(tokens, n):
    return Counter(tuple(tokens[i:i+n]) for i in range(max(0, len(tokens)-n+1)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("final")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()
    s = open(args.source, encoding="utf-8", errors="ignore").read()
    f = open(args.final, encoding="utf-8", errors="ignore").read()
    a, b = ngrams(prose_tokens(s), args.n), ngrams(prose_tokens(f), args.n)
    shared = []
    for g in (a.keys() & b.keys()):
        phrase = " ".join(g)
        if any(c in phrase for c in COMMON):
            continue
        shared.append((min(a[g], b[g]), phrase))
    shared.sort(reverse=True)
    print(f"shared_{args.n}grams={len(shared)}")
    for count, phrase in shared[:args.limit]:
        print(f"{count}\t{phrase}")

if __name__ == "__main__":
    main()
