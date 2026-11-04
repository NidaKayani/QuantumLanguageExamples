"""Suffix arrays by sorting and by prefix doubling, the Kasai LCP array, and substring queries."""
from bisect import bisect_left, bisect_right


def suffix_array_naive(s):
    return sorted(range(len(s)), key=lambda i: s[i:])


def suffix_array_doubling(s):
    n = len(s)
    rank = [ord(c) for c in s]
    sa = list(range(n))
    k = 1
    while True:
        key = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=key)
        new_rank = [0] * n
        for a, b in zip(sa, sa[1:]):
            new_rank[b] = new_rank[a] + (key(a) != key(b))
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            return sa
        k *= 2


def kasai_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i, suffix in enumerate(sa):
        rank[suffix] = i
    lcp, h = [0] * n, 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            h = max(h - 1, 0)
        else:
            h = 0
    return lcp


def occurrences(s, sa, pattern):
    suffixes = [s[i:i + len(pattern)] for i in sa]
    lo, hi = bisect_left(suffixes, pattern), bisect_right(suffixes, pattern)
    return sorted(sa[lo:hi])


def main():
    s = "banana"
    sa = suffix_array_doubling(s)
    assert sa == suffix_array_naive(s)
    lcp = kasai_lcp(s, sa)
    print(f"Suffix array of {s!r}:")
    for idx, (start, common) in enumerate(zip(sa, lcp)):
        print(f"  {idx}: {start} lcp={common} {s[start:]}")
    text = "mississippi"
    sa = suffix_array_doubling(text)
    lcp = kasai_lcp(text, sa)
    print(f"SA({text}) = {sa}")
    print(f"LCP        = {lcp}")
    best = max(range(len(lcp)), key=lcp.__getitem__)
    print("Longest repeated substring:", repr(text[sa[best]:sa[best] + lcp[best]]))
    n = len(text)
    print("Distinct substrings:", n * (n + 1) // 2 - sum(lcp))
    for p in ("ssi", "i", "pp", "x"):
        print(f"  occurrences of {p!r}: {occurrences(text, sa, p)}")


if __name__ == "__main__":
    main()
