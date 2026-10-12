#!/usr/bin/env python3
"""Static hygiene gate for reconstructed LaTeX manuscripts."""
import argparse, re, sys

FORBIDDEN_INTERNAL = [
    r"\bStage\s+\d", r"\bModule\s+[A-Z0-9]", r"\bFCW\b",
    r"\bproof debt\b", r"\bworkflow\b", r"\bTODO\b", r"\bFIXME\b",
    r"MATHEMATICAL-CHECK", r"CITATION-CHECK", r"FACT-CHECK",
]

FORMULAIC = [
    "we now proceed to", "it is worth noting that",
    "the proof consists of the following steps",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    args = ap.parse_args()
    text = open(args.tex, encoding="utf-8", errors="ignore").read()
    issues = []
    for pat in FORBIDDEN_INTERNAL:
        for m in re.finditer(pat, text, flags=re.I):
            issues.append(("INTERNAL", m.start(), m.group(0)))
    low = text.lower()
    for phrase in FORMULAIC:
        c = low.count(phrase)
        if c >= 2:
            issues.append(("FORMULAIC", c, phrase))
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    for x in set(labels):
        if labels.count(x) > 1:
            issues.append(("DUPLICATE_LABEL", labels.count(x), x))
    if issues:
        for row in issues:
            print("\t".join(map(str, row)))
        sys.exit(1)
    print("STATIC_GATE_PASS")

if __name__ == "__main__":
    main()
