"""Group anagrams by sorted key and by letter counts, and find anagram windows in text."""
from collections import Counter, defaultdict

WORDS = ["listen", "silent", "enlist", "google", "gooegl", "inlets", "banana",
         "evil", "vile", "live", "veil", "levi", "stone", "tones", "notes",
         "onset", "seton", "apple", "papel", "angel", "glean", "angle"]


def group_sorted(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return groups


def group_counts(words):
    groups = defaultdict(list)
    for w in words:
        counts = [0] * 26
        for ch in w:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(w)
    return groups


def anagram_windows(text, word):
    need, window = Counter(word), Counter(text[:len(word)])
    hits = [0] if window == need else []
    for i in range(len(word), len(text)):
        window[text[i]] += 1
        left = text[i - len(word)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            hits.append(i - len(word) + 1)
    return hits


def main():
    by_sorted = group_sorted(WORDS)
    by_counts = group_counts(WORDS)
    assert sorted(map(sorted, by_sorted.values())) == sorted(map(sorted, by_counts.values()))
    families = sorted((sorted(g) for g in by_sorted.values()), key=lambda g: (-len(g), g))
    print(f"{len(WORDS)} words form {len(families)} anagram families:")
    for fam in families:
        print(f"  [{len(fam)}] {' '.join(fam)}")
    singles = [f[0] for f in families if len(f) == 1]
    print("Words with no anagram partner:", singles)
    text = "cbaebabacdabcbca"
    print(f"Anagrams of 'abc' in {text!r} start at {anagram_windows(text, 'abc')}")
    print("Is 'Dormitory' an anagram of 'Dirty room'?",
          Counter("Dormitory".lower()) == Counter("Dirty room".lower().replace(" ", "")))


if __name__ == "__main__":
    main()
