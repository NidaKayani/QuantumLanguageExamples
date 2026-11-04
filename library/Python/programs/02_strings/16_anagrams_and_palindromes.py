"""Group anagrams and detect palindromes with sorting and normalization."""

from collections import defaultdict

words = ["listen", "silent", "enlist", "google", "gooegl", "cat", "act", "tac",
         "dog", "god", "evil", "vile", "live", "veil", "python"]

groups = defaultdict(list)
for w in words:
    groups["".join(sorted(w))].append(w)

for key in sorted(groups):
    members = groups[key]
    if len(members) > 1:
        print(f"{key}: {', '.join(sorted(members))}")
print("words without anagrams:", [g[0] for g in groups.values() if len(g) == 1])


def is_palindrome(text):
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]


def longest_palindrome(s):
    best = ""
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > len(best):
                best = s[lo + 1:hi]
    return best


phrases = ["Was it a car or a cat I saw?", "No lemon, no melon", "Hello", "Step on no pets"]
for p in phrases:
    print(f"{p!r:34} palindrome: {is_palindrome(p)}")

for s in ("babad", "forgeeksskeegfor", "abacdfgdcaba", "x"):
    print(f"longest palindrome in {s!r}: {longest_palindrome(s)!r}")
