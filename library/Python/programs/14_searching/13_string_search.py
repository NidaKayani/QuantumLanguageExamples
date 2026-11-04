"""Substring search: naive, Knuth-Morris-Pratt and Horspool, checked against str.find."""

import re


def naive(text, pat):
    return [i for i in range(len(text) - len(pat) + 1) if text[i:i + len(pat)] == pat]


def prefix_table(pat):
    table = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k and pat[i] != pat[k]:
            k = table[k - 1]
        if pat[i] == pat[k]:
            k += 1
        table[i] = k
    return table


def kmp(text, pat):
    table, k, hits = prefix_table(pat), 0, []
    for i, ch in enumerate(text):
        while k and ch != pat[k]:
            k = table[k - 1]
        if ch == pat[k]:
            k += 1
        if k == len(pat):
            hits.append(i - k + 1)
            k = table[k - 1]
    return hits


def horspool(text, pat):
    m = len(pat)
    shift = {ch: m - i - 1 for i, ch in enumerate(pat[:-1])}
    hits, i = [], 0
    while i <= len(text) - m:
        if text[i:i + m] == pat:
            hits.append(i)
        i += shift.get(text[i + m - 1], m)
    return hits


text = "abracadabra abracadabra cadabra"
for pat in ["abra", "cad", "a", "zzz", "abracadabra"]:
    results = naive(text, pat), kmp(text, pat), horspool(text, pat)
    assert results[0] == results[1] == results[2]
    print(f"{pat!r:>14}: {results[0]}")

print("prefix table for 'aabaaab':", prefix_table("aabaaab"))
print("str.find('cad'):", text.find("cad"), "rfind:", text.rfind("cad"), "count:", text.count("abra"))
print("regex overlapping 'aba' in 'abababa':", [m.start() for m in re.finditer(r"(?=aba)", "abababa")])
print("kmp overlapping:", kmp("abababa", "aba"))
