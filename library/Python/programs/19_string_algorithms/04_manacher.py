"""Manacher's linear-time longest palindromic substring, checked against expand-around-centre."""


def manacher(s):
    t = "^#" + "#".join(s) + "#$"
    radius = [0] * len(t)
    center = right = 0
    for i in range(1, len(t) - 1):
        if i < right:
            radius[i] = min(right - i, radius[2 * center - i])
        while t[i + radius[i] + 1] == t[i - radius[i] - 1]:
            radius[i] += 1
        if i + radius[i] > right:
            center, right = i, i + radius[i]
    length, idx = max((r, i) for i, r in enumerate(radius))
    start = (idx - length) // 2
    return s[start:start + length], radius


def expand_around_center(s):
    best = ""
    for center in range(2 * len(s) - 1):
        lo, hi = center // 2, center // 2 + center % 2
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo - 1, hi + 1
        if hi - lo - 1 > len(best):
            best = s[lo + 1:hi]
    return best


def count_palindromic_substrings(radius):
    return sum((r + 1) // 2 for r in radius[1:-1])


def main():
    samples = ["babad", "cbbd", "forgeeksskeegfor", "abacdfgdcaba",
               "racecar", "a", "noonabbad", "xabcbayyabccbaz"]
    for s in samples:
        best, radius = manacher(s)
        slow = expand_around_center(s)
        assert len(best) == len(slow)
        print(f"{s!r:<22} longest={best!r:<16} len={len(best):2d} "
              f"palindromic substrings={count_palindromic_substrings(radius)}")
    _, radius = manacher("abaaba")
    print("Radius array for 'abaaba':", radius[1:-1])
    lcg, chars = 7, []
    for _ in range(200):
        lcg = (lcg * 48271) % 2147483647
        chars.append("ab"[lcg % 2])
    noisy = "".join(chars)
    best, _ = manacher(noisy)
    print(f"Longest palindrome in pseudo-random 200-char a/b string: length {len(best)}")


if __name__ == "__main__":
    main()
