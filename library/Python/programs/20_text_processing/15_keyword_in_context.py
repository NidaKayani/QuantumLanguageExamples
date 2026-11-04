"""Keyword-in-context (KWIC) concordance and collocation counts over a short text."""
import re
from collections import Counter

TEXT = """Time is the most valuable thing a man can spend. Lost time is never found
again. Time flies over us, but leaves its shadow behind. The two most powerful
warriors are patience and time. Time is what we want most, but what we use worst.
Better three hours too soon than a minute too late. They always say time changes
things, but you actually have to change them yourself."""


def tokens_with_spans(text):
    return [(m.group().lower(), m.start(), m.end()) for m in re.finditer(r"[A-Za-z']+", text)]


def kwic(text, keyword, width=28):
    flat = " ".join(text.split())
    rows = []
    for word, start, end in tokens_with_spans(flat):
        if word == keyword:
            left = flat[max(0, start - width):start]
            right = flat[end:end + width]
            rows.append(f"{left:>{width}} [{flat[start:end]}] {right:<{width}}")
    return rows


def collocations(text, keyword, window=2):
    words = [w for w, _, _ in tokens_with_spans(text)]
    near = Counter()
    for i, w in enumerate(words):
        if w == keyword:
            for j in range(max(0, i - window), min(len(words), i + window + 1)):
                if j != i:
                    near[words[j]] += 1
    return near


def main():
    for keyword in ("time", "most"):
        lines = kwic(TEXT, keyword)
        print(f"KWIC for {keyword!r} ({len(lines)} hits):")
        for line in lines:
            print("  " + line)
    near = collocations(TEXT, "time")
    top = sorted(near.items(), key=lambda kv: (-kv[1], kv[0]))[:6]
    print("Words near 'time':", top)
    sentences = re.split(r"(?<=\.)\s+", " ".join(TEXT.split()))
    with_time = [s for s in sentences if re.search(r"\btime\b", s, re.IGNORECASE)]
    print(f"{len(with_time)} of {len(sentences)} sentences mention time")
    first_word = Counter(s.split()[0] for s in sentences)
    print("Sentence openers:", dict(sorted(first_word.items())))


if __name__ == "__main__":
    main()
