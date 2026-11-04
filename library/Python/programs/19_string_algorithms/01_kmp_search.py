"""Knuth-Morris-Pratt substring search with its failure table and period detection."""


def failure_table(pattern):
    fail = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = fail[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        fail[i] = k
    return fail


def kmp_search(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    fail = failure_table(pattern)
    matches, k, comparisons = [], 0, 0
    for i, ch in enumerate(text):
        while k and ch != pattern[k]:
            comparisons += 1
            k = fail[k - 1]
        comparisons += 1
        if ch == pattern[k]:
            k += 1
            if k == len(pattern):
                matches.append(i - k + 1)
                k = fail[k - 1]
    return matches, comparisons


def smallest_period(s):
    p = len(s) - failure_table(s)[-1]
    return p if len(s) % p == 0 else len(s)


def main():
    for pattern in ("ABABCABAB", "AABAACAABAA", "abcabcabc", "aaaa"):
        print(f"failure({pattern}) = {failure_table(pattern)}")
    text = "ABABDABACDABABCABABABABCABABCABAB"
    pattern = "ABABCABAB"
    matches, comparisons = kmp_search(text, pattern)
    print(f"Searching {pattern!r} in {text!r}")
    print(f"  matches at {matches} using {comparisons} comparisons (text length {len(text)})")
    for m in matches:
        print("  " + text)
        print("  " + " " * m + "^" * len(pattern))
    dna = "GATATATGCATATACTTATAT"
    print("Overlapping 'ATAT' in DNA:", kmp_search(dna, "ATAT")[0])
    builtin = [i for i in range(len(dna)) if dna.startswith("ATAT", i)]
    print("Agrees with str.startswith scan:", builtin == kmp_search(dna, "ATAT")[0])
    for s in ("abababab", "abcabcab", "xyzxyzxyz", "aaaaaa"):
        p = smallest_period(s)
        print(f"Period of {s!r}: {p} -> {s[:p]!r} x {len(s) // p if len(s) % p == 0 else 1}")


if __name__ == "__main__":
    main()
