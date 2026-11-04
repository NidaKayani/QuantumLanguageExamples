"""Longest palindromic subsequence, minimum insertions to make a palindrome, and palindromic cuts."""
from functools import lru_cache


def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    left, right = [], []
    i, j = 0, n - 1
    while i <= j:
        if i == j:
            left.append(s[i])
            break
        if s[i] == s[j]:
            left.append(s[i])
            right.append(s[j])
            i, j = i + 1, j - 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    return dp[0][n - 1] if n else 0, "".join(left + right[::-1])


def min_insertions(s):
    @lru_cache(maxsize=None)
    def go(i, j):
        if i >= j:
            return 0
        if s[i] == s[j]:
            return go(i + 1, j - 1)
        return 1 + min(go(i + 1, j), go(i, j - 1))
    return go(0, len(s) - 1)


def min_palindrome_cuts(s):
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    cuts = [0] * n
    for end in range(n):
        best = end
        for start in range(end + 1):
            if s[start] == s[end] and (end - start < 2 or is_pal[start + 1][end - 1]):
                is_pal[start][end] = True
                best = 0 if start == 0 else min(best, cuts[start - 1] + 1)
        cuts[end] = best
    return cuts[-1]


def main():
    words = ["bbbab", "character", "racecar", "agbdba", "programming", "abacdfgdcaba"]
    print(f"{'word':<14}{'LPS':>4}  {'example':<10}{'ins':>4}{'cuts':>5}")
    for w in words:
        length, example = lps(w)
        ins = min_insertions(w)
        assert ins == len(w) - length
        print(f"{w:<14}{length:>4}  {example:<10}{ins:>4}{min_palindrome_cuts(w):>5}")


if __name__ == "__main__":
    main()
