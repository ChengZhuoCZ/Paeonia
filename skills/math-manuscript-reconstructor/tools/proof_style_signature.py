#!/usr/bin/env python3
"""Extract aggregate mathematical-prose metrics without emitting source sentences.

This tool supports style distillation. It is deliberately not an authorship
classifier and never prints source snippets or phrase inventories.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from statistics import mean, median

TRANSITION_PATTERNS = {
    "premise": [r"\bsince\b", r"\bbecause\b"],
    "consequence": [r"\btherefore\b", r"\bthus\b", r"\bhence\b", r"\bconsequently\b", r"\bas a consequence\b"],
    "construction": [r"\bchoose\b", r"\bdefine\b", r"\bset\b", r"\blet\b", r"\bwrite\b"],
    "reduction": [r"\bit suffices\b", r"\bit is enough\b", r"\bwe may assume\b", r"\breduce(?:s|d)? to\b"],
    "contrast": [r"\bhowever\b", r"\binstead\b", r"\bon the other hand\b", r"\bin contrast\b"],
    "recollection": [r"\brecall\b", r"\bnote that\b", r"\bobserve that\b"],
    "closure": [r"\bthis proves\b", r"\bwhich proves\b", r"\bproof is complete\b", r"\bcompletes? the proof\b", r"\bas desired\b"],
}

OPENING_PATTERNS = [
    ("contradiction", [r"^we argue by contradiction", r"^argue by contradiction", r"^suppose.*contradiction"]),
    ("direct_reduction", [r"^it suffices", r"^we may assume", r"^by .* it suffices"]),
    ("direct_construction", [r"^(we )?(choose|define|set|let|write)\b"]),
    ("direct_estimate_or_application", [r"^(by|using|applying|from)\b"]),
    ("strategy_signal", [r"^the idea", r"^the proof .* relies", r"^we first", r"^we begin"]),
]

EVALUATIVE = [r"\bclearly\b", r"\bobviously\b", r"\bimmediate(?:ly)?\b", r"\bstraightforward\b", r"\bsimple\b"]
READER_ADDRESS = [r"\bthe reader\b", r"\bwe leave .* reader\b", r"\byou\b"]
FIRST_PERSON = [r"\bwe\b", r"\bour\b"]


def strip_math_and_markup(s: str) -> str:
    # Remove common TeX math regions but preserve surrounding prose.
    s = re.sub(r"\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[*_#`|]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def words(s: str) -> list[str]:
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s)


def count_patterns(text: str, pats: list[str]) -> int:
    return sum(len(re.findall(p, text, flags=re.I)) for p in pats)


def classify_opening(s: str) -> str:
    x = strip_math_and_markup(s).lower()
    for label, pats in OPENING_PATTERNS:
        if any(re.search(p, x, flags=re.I) for p in pats):
            return label
    return "direct_or_other"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--window-chars", type=int, default=2200)
    args = ap.parse_args()

    text = open(args.source, encoding="utf-8", errors="ignore").read()

    # Handles common OCR/Markdown renderings of Proof and Proof of ...
    proof_re = re.compile(
        r"(?:\*{1,2}\s*Proof(?:\s+of\s+[^*\n.]{0,80})?\s*\*{1,2}\s*[\.:]?|(?<![A-Za-z])Proof(?:\s+of\s+[^\n.]{0,80})?\s*[\.:])",
        flags=re.I,
    )
    starts = list(proof_re.finditer(text))
    windows = [strip_math_and_markup(text[m.end():m.end() + args.window_chars]) for m in starts]
    allp = "\n".join(windows)
    lower = allp.lower()

    sentences = []
    for w in windows:
        for s in re.split(r"(?<=[.!?])\s+", w):
            n = len(words(s))
            if 4 <= n <= 120:
                sentences.append((s, n))
    slens = [n for _, n in sentences]

    paragraphs = []
    for m in starts:
        raw = text[m.end():m.end() + args.window_chars]
        for p in re.split(r"\n\s*\n", raw):
            c = strip_math_and_markup(p)
            n = len(words(c))
            if 12 <= n <= 300:
                paragraphs.append(n)

    transition_counts = {k: count_patterns(lower, v) for k, v in TRANSITION_PATTERNS.items()}
    opening_counts = Counter()
    for m in starts:
        opening_counts[classify_opening(text[m.end():m.end() + 450])] += 1

    total_words = max(1, len(words(allp)))
    numbered_steps = len(re.findall(r"\bstep\s+\d+\b", lower, flags=re.I))
    explicit_closure = transition_counts["closure"]
    evaluative = count_patterns(lower, EVALUATIVE)
    reader_address = count_patterns(lower, READER_ADDRESS)
    first_person = count_patterns(lower, FIRST_PERSON)

    # Sentence-start functional categories; no source starts are emitted.
    sentence_start_counts = Counter()
    for s, _ in sentences:
        x = s.lower().strip()
        if re.match(r"^(since|because)\b", x):
            sentence_start_counts["premise_led"] += 1
        elif re.match(r"^(therefore|thus|hence|consequently)\b", x):
            sentence_start_counts["consequence_led"] += 1
        elif re.match(r"^(we|our)\b", x):
            sentence_start_counts["first_person_led"] += 1
        elif re.match(r"^(choose|define|set|let|write|fix)\b", x):
            sentence_start_counts["direct_action_led"] += 1
        elif re.match(r"^(however|instead|in contrast|on the other hand)\b", x):
            sentence_start_counts["contrast_led"] += 1
        else:
            sentence_start_counts["object_or_other_led"] += 1

    result = {
        "proof_markers": len(starts),
        "sample_window_chars": args.window_chars,
        "sampled_words": total_words,
        "sentence_count_in_windows": len(sentences),
        "sentence_words_mean": round(mean(slens), 2) if slens else 0,
        "sentence_words_median": median(slens) if slens else 0,
        "paragraph_words_mean": round(mean(paragraphs), 2) if paragraphs else 0,
        "paragraph_words_median": median(paragraphs) if paragraphs else 0,
        "proof_opening_class_counts": dict(sorted(opening_counts.items())),
        "sentence_start_class_counts": dict(sorted(sentence_start_counts.items())),
        "transition_class_counts": transition_counts,
        "numbered_step_mentions": numbered_steps,
        "numbered_step_mentions_per_proof": round(numbered_steps / max(1, len(starts)), 3),
        "explicit_closure_markers_per_proof": round(explicit_closure / max(1, len(starts)), 3),
        "first_person_plural_mentions_per_1000_words": round(1000 * first_person / total_words, 2),
        "evaluative_ease_markers_per_1000_words": round(1000 * evaluative / total_words, 2),
        "reader_address_markers_per_1000_words": round(1000 * reader_address / total_words, 2),
        "emits_source_phrases": False,
        "stores_source_sentences": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
