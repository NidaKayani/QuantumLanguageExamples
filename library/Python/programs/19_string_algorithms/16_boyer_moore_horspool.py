"""Boyer-Moore-Horspool search with a bad-character shift table, compared with naive search."""


def shift_table(pattern):
    m = len(pattern)
    return {ch: m - 1 - i for i, ch in enumerate(pattern[:-1])}


def horspool(text, pattern):
    m, n = len(pattern), len(text)
    table = shift_table(pattern)
    hits, i, comparisons, alignments = [], 0, 0, 0
    while i <= n - m:
        alignments += 1
        j = m - 1
        while j >= 0:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j -= 1
        if j < 0:
            hits.append(i)
        i += table.get(text[i + m - 1], m)
    return hits, comparisons, alignments


def naive(text, pattern):
    hits, comparisons = [], 0
    for i in range(len(text) - len(pattern) + 1):
        for j, ch in enumerate(pattern):
            comparisons += 1
            if text[i + j] != ch:
                break
        else:
            hits.append(i)
    return hits, comparisons


def main():
    text = ("It was the best of times, it was the worst of times, it was the age of "
            "wisdom, it was the age of foolishness, it was the epoch of belief")
    print("Shift table for 'foolish':", shift_table("foolish"))
    print(f"{'pattern':<14}{'hits':<22}{'naive cmp':>10}{'BMH cmp':>9}{'aligns':>8}")
    for pattern in ("times", "it was the", "foolishness", "belief", "age of", "xyz"):
        hits, cmp_bmh, aligns = horspool(text, pattern)
        nhits, cmp_naive = naive(text, pattern)
        assert hits == nhits
        print(f"{pattern!r:<14}{str(hits):<22}{cmp_naive:>10}{cmp_bmh:>9}{aligns:>8}")
    dna = "ACGT" * 50 + "TTGACCA" + "ACGT" * 50
    hits, cmp_bmh, _ = horspool(dna, "TTGACCA")
    _, cmp_naive = naive(dna, "TTGACCA")
    print(f"DNA search: found at {hits}; comparisons naive={cmp_naive}, horspool={cmp_bmh}")
    print("Speedup factor:", round(cmp_naive / cmp_bmh, 2))


if __name__ == "__main__":
    main()
