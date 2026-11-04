"""The Z-algorithm: Z-arrays, pattern matching, and counting distinct substrings."""


def z_array(s):
    n = len(s)
    z = [0] * n
    if n:
        z[0] = n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def z_search(text, pattern, sep="\x00"):
    combined = pattern + sep + text
    z = z_array(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] >= m]


def distinct_substrings(s):
    count, current = 0, ""
    for ch in s:
        current += ch
        rev = current[::-1]
        z = z_array(rev)
        longest_repeat = max(z[1:], default=0)
        count += len(current) - longest_repeat
    return count


def main():
    s = "aabcaabxaaaz"
    print("String: ", " ".join(s))
    print("Z-array:", " ".join(map(str, z_array(s))))
    text = "the cat sat on the mat with the hat"
    for word in ("the", "at", "dog"):
        print(f"positions of {word!r}: {z_search(text, word)}")
    for word in ("banana", "abab", "aaaa", "abcd"):
        n = distinct_substrings(word)
        brute = len({word[i:j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)})
        print(f"distinct substrings of {word!r}: {n} (brute force {brute})")
    z = z_array("abacabadabacaba")
    border = [i for i in range(1, len(z)) if i + z[i] == len(z)]
    print("Suffixes that are also prefixes start at:", border)


if __name__ == "__main__":
    main()
