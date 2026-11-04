"""String rotations: rotation tests, Booth's least rotation, Lyndon factorisation, and necklaces."""


def is_rotation(a, b):
    return len(a) == len(b) and b in a + a


def least_rotation(s):
    """Booth's algorithm: index of the lexicographically smallest rotation."""
    doubled = s + s
    fail = [-1] * len(doubled)
    k = 0
    for j in range(1, len(doubled)):
        ch = doubled[j]
        i = fail[j - k - 1]
        while i != -1 and ch != doubled[k + i + 1]:
            if ch < doubled[k + i + 1]:
                k = j - i - 1
            i = fail[i]
        if i == -1 and ch != doubled[k + i + 1]:
            if ch < doubled[k + i + 1]:
                k = j
            fail[j - k] = -1
        else:
            fail[j - k] = i + 1
    return k


def lyndon_factorization(s):
    """Duval's algorithm."""
    factors, i = [], 0
    while i < len(s):
        j, k = i + 1, i
        while j < len(s) and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        while i <= k:
            factors.append(s[i:i + j - k])
            i += j - k
    return factors


def necklaces(n, alphabet="01"):
    seen, result = set(), []
    for value in range(len(alphabet) ** n):
        digits = []
        for _ in range(n):
            value, r = divmod(value, len(alphabet))
            digits.append(alphabet[r])
        word = "".join(reversed(digits))
        canon = min(word[i:] + word[:i] for i in range(n))
        if canon not in seen:
            seen.add(canon)
            result.append(canon)
    return sorted(result)


def main():
    for a, b in [("waterbottle", "erbottlewat"), ("abcd", "acbd"), ("aa", "aa")]:
        print(f"is_rotation({a!r}, {b!r}) = {is_rotation(a, b)}")
    for s in ("bbaaccaadd", "cabbage", "baca", "zyxwv", "abab"):
        k = least_rotation(s)
        rotated = s[k:] + s[:k]
        assert rotated == min(s[i:] + s[:i] for i in range(len(s)))
        print(f"least rotation of {s!r}: start {k} -> {rotated!r}")
    for s in ("banana", "abracadabra", "aabaabaab", "zyx"):
        print(f"Lyndon factors of {s!r}: {lyndon_factorization(s)}")
    for n in (3, 4, 5):
        neck = necklaces(n)
        print(f"Binary necklaces of length {n}: {len(neck)} -> {neck}")


if __name__ == "__main__":
    main()
