"""Word frequency analysis with Counter, stop-word filtering, and frequency bands."""
import re
from collections import Counter

TEXT = """
It was the best of times, it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief, it was the epoch of
incredulity, it was the season of Light, it was the season of Darkness, it was
the spring of hope, it was the winter of despair, we had everything before us,
we had nothing before us, we were all going direct to Heaven, we were all going
direct the other way - in short, the period was so far like the present period,
that some of its noisiest authorities insisted on its being received, for good
or for evil, in the superlative degree of comparison only.
"""

STOP_WORDS = frozenset("""a an and the of to in it was we were is on for or that its so
all had us like some only being""".split())


def tokenize(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())


def main():
    words = tokenize(TEXT)
    counts = Counter(words)
    print(f"Total words: {len(words)}, distinct: {len(counts)}")
    print("Top 8 overall:")
    for word, n in counts.most_common(8):
        print(f"  {word:<8} {n:>3} {'*' * n}")
    content = Counter(w for w in words if w not in STOP_WORDS)
    print("Top 8 content words:")
    for word, n in sorted(content.items(), key=lambda kv: (-kv[1], kv[0]))[:8]:
        print(f"  {word:<12} {n}")
    hapax = sorted(w for w, n in counts.items() if n == 1)
    print(f"Hapax legomena ({len(hapax)}): {', '.join(hapax[:12])}, ...")
    by_length = Counter(len(w) for w in words)
    print("Word length distribution:", dict(sorted(by_length.items())))
    longest = max(counts, key=lambda w: (len(w), w))
    print("Longest word:", longest)
    print(f"Lexical diversity: {len(counts) / len(words):.3f}")
    pairs = Counter(zip(words, words[1:]))
    print("Most common bigrams:", [" ".join(p) for p, _ in pairs.most_common(3)])


if __name__ == "__main__":
    main()
