"""Longest common substring and shortest common supersequence of string pairs."""


def longest_common_substring(a, b):
    prev = [0] * (len(b) + 1)
    best_len = best_end = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best_len:
                    best_len, best_end = cur[j], i
        prev = cur
    return a[best_end - best_len:best_end]


def shortest_common_supersequence(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = (dp[i][j] + 1 if a[i] == b[j]
                                else max(dp[i][j + 1], dp[i + 1][j]))
    out = []
    i, j = m, n
    while i and j:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            out.append(a[i - 1])
            i -= 1
        else:
            out.append(b[j - 1])
            j -= 1
    out.extend(reversed(a[:i]))
    out.extend(reversed(b[:j]))
    return "".join(reversed(out))


def is_subsequence(small, big):
    it = iter(big)
    return all(ch in it for ch in small)


def main():
    pairs = [("abcdxyz", "xyzabcd"), ("geeksforgeeks", "geeksquiz"),
             ("AGGTAB", "GXTXAYB"), ("photograph", "tomography"), ("abc", "def")]
    print(f"{'A':<14}{'B':<12}{'substring':<10}{'supersequence'}")
    for a, b in pairs:
        sub = longest_common_substring(a, b)
        sup = shortest_common_supersequence(a, b)
        assert is_subsequence(a, sup) and is_subsequence(b, sup)
        print(f"{a:<14}{b:<12}{sub or '-':<10}{sup} ({len(sup)})")
    words = ["interstellar", "stellarator", "constellation"]
    common = words[0]
    for w in words[1:]:
        common = longest_common_substring(common, w)
    print(f"Common substring of {words}: {common!r}")


if __name__ == "__main__":
    main()
