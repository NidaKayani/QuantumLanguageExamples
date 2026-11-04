"""String recursion: palindromes, reversal, edit distance and partitions."""

from functools import lru_cache


def is_palindrome(s: str) -> bool:
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


def clean(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalnum())


def reverse(s: str) -> str:
    return s if len(s) <= 1 else reverse(s[1:]) + s[0]


def edit_distance(a: str, b: str) -> int:
    @lru_cache(maxsize=None)
    def go(i: int, j: int) -> int:
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i
        if a[i] == b[j]:
            return go(i + 1, j + 1)
        return 1 + min(go(i + 1, j), go(i, j + 1), go(i + 1, j + 1))
    return go(0, 0)


def palindrome_partitions(s: str) -> list[list[str]]:
    if not s:
        return [[]]
    result = []
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if is_palindrome(prefix):
            for rest in palindrome_partitions(s[i:]):
                result.append([prefix] + rest)
    return result


for phrase in ["racecar", "A man, a plan, a canal: Panama", "recursion", "Was it a cat I saw?"]:
    print(f"{phrase!r:35} palindrome={is_palindrome(clean(phrase))}")

print("reverse('stressed') =", reverse("stressed"))
for a, b in [("kitten", "sitting"), ("flaw", "lawn"), ("python", "pythons"), ("", "abc")]:
    print(f"edit_distance({a!r}, {b!r}) = {edit_distance(a, b)}")

parts = palindrome_partitions("aabbc")
print(f"palindrome partitions of 'aabbc' ({len(parts)}):")
for p in parts:
    print("  ", " | ".join(p))
