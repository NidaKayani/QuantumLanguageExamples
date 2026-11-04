"""Rabin-Karp rolling-hash search, multi-pattern search, and duplicate substring detection."""

BASE = 256
MOD = 1_000_000_007


def poly_hash(s):
    h = 0
    for ch in s:
        h = (h * BASE + ord(ch)) % MOD
    return h


def rolling_hashes(text, m):
    if m > len(text):
        return
    high = pow(BASE, m - 1, MOD)
    h = poly_hash(text[:m])
    yield 0, h
    for i in range(1, len(text) - m + 1):
        h = ((h - ord(text[i - 1]) * high) * BASE + ord(text[i + m - 1])) % MOD
        yield i, h


def rabin_karp(text, pattern):
    target = poly_hash(pattern)
    hits, false_alarms = [], 0
    for i, h in rolling_hashes(text, len(pattern)):
        if h == target:
            if text[i:i + len(pattern)] == pattern:
                hits.append(i)
            else:
                false_alarms += 1
    return hits, false_alarms


def multi_search(text, patterns):
    by_len = {}
    for p in patterns:
        by_len.setdefault(len(p), {})[poly_hash(p)] = p
    found = []
    for m, table in by_len.items():
        for i, h in rolling_hashes(text, m):
            p = table.get(h)
            if p is not None and text.startswith(p, i):
                found.append((i, p))
    return sorted(found)


def longest_duplicate(s):
    lo, hi, best = 1, len(s) - 1, ""
    while lo <= hi:
        mid = (lo + hi) // 2
        seen, found = {}, None
        for i, h in rolling_hashes(s, mid):
            if h in seen and s[seen[h]:seen[h] + mid] == s[i:i + mid]:
                found = s[i:i + mid]
                break
            seen.setdefault(h, i)
        if found:
            best, lo = found, mid + 1
        else:
            hi = mid - 1
    return best


def main():
    text = "abracadabra is a magic word; abracadabra!"
    hits, fa = rabin_karp(text, "abra")
    print(f"'abra' found at {hits} with {fa} false alarms")
    print("Multi-pattern:", multi_search(text, ["cad", "magic", "ra", "word"]))
    for s in ("banana", "mississippi", "the quick brown fox jumps over the quick dog"):
        print(f"Longest repeated substring of {s!r}: {longest_duplicate(s)!r}")
    print("Hash of 'hello':", poly_hash("hello"))


if __name__ == "__main__":
    main()
