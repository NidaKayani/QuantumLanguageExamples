"""Longest common subsequence table, backtracking, and a line-based diff built on it."""


def lcs_table(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp


def lcs(a, b):
    dp = lcs_table(a, b)
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return out


def diff(old, new):
    dp = lcs_table(old, new)
    i = j = 0
    while i < len(old) or j < len(new):
        if i < len(old) and j < len(new) and old[i] == new[j]:
            yield "  " + old[i]
            i += 1
            j += 1
        elif j < len(new) and (i == len(old) or dp[i][j + 1] >= dp[i + 1][j]):
            yield "+ " + new[j]
            j += 1
        else:
            yield "- " + old[i]
            i += 1


def main():
    pairs = [("ABCBDAB", "BDCABA"), ("AGGTAB", "GXTXAYB"), ("dynamic", "programming")]
    for a, b in pairs:
        common = "".join(lcs(a, b))
        print(f"LCS({a!r}, {b!r}) = {common!r} (length {len(common)})")
    old = """def greet(name):
    print("Hello", name)
    return None
greet("world")""".splitlines()
    new = """def greet(name, punct="!"):
    print("Hello", name)
    print("Bye", name + punct)
greet("world")""".splitlines()
    print("Line diff:")
    for line in diff(old, new):
        print("  " + line)
    similarity = 2 * len(lcs(old, new)) / (len(old) + len(new))
    print(f"Similarity ratio: {similarity:.2f}")


if __name__ == "__main__":
    main()
