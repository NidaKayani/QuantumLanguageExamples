"""Longest common prefix of many strings: horizontal, vertical, divide-and-conquer, and min/max tricks."""
from functools import reduce
from itertools import takewhile


def lcp_pair(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return a[:i]


def lcp_horizontal(words):
    return reduce(lcp_pair, words) if words else ""


def lcp_vertical(words):
    if not words:
        return ""
    for i, ch in enumerate(words[0]):
        if any(i >= len(w) or w[i] != ch for w in words[1:]):
            return words[0][:i]
    return words[0]


def lcp_divide(words, lo=0, hi=None):
    hi = len(words) - 1 if hi is None else hi
    if lo == hi:
        return words[lo]
    mid = (lo + hi) // 2
    return lcp_pair(lcp_divide(words, lo, mid), lcp_divide(words, mid + 1, hi))


def lcp_zip(words):
    return "".join(chars[0] for chars in takewhile(lambda cs: len(set(cs)) == 1, zip(*words)))


def lcp_minmax(words):
    return lcp_pair(min(words), max(words)) if words else ""


def group_by_prefix(paths):
    groups = {}
    for p in paths:
        groups.setdefault(p.split("/")[1], []).append(p)
    return {k: lcp_vertical(v) for k, v in sorted(groups.items())}


def main():
    cases = [
        ["flower", "flow", "flight"],
        ["interspecies", "interstellar", "interstate"],
        ["dog", "racecar", "car"],
        ["throne", "throne"],
        ["prefix"],
        ["", "abc"],
    ]
    methods = [lcp_horizontal, lcp_vertical, lcp_divide, lcp_zip, lcp_minmax]
    for words in cases:
        results = {m.__name__: m(words) for m in methods}
        assert len(set(results.values())) == 1, results
        print(f"{words} -> {results['lcp_vertical']!r}")
    paths = ["/usr/local/bin/python", "/usr/local/lib/python3", "/usr/local/share/man",
             "/home/ann/docs/a.txt", "/home/ann/docs/b.txt", "/home/bob/music"]
    print("Common prefix of all paths:", repr(lcp_vertical(paths)))
    for top, prefix in group_by_prefix(paths).items():
        print(f"  /{top}: {prefix!r}")
    versions = ["v2.13.4-rc1", "v2.13.4-rc2", "v2.13.40"]
    print("Version prefix:", lcp_minmax(versions))


if __name__ == "__main__":
    main()
