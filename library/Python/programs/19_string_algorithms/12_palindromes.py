"""Palindrome utilities: sentence checks, palindromic permutations, pairs, and next palindrome."""
import re
from collections import Counter
from itertools import permutations


def is_palindrome(text):
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def two_pointer(text):
    i, j = 0, len(text) - 1
    while i < j:
        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        elif text[i].lower() != text[j].lower():
            return False
        else:
            i, j = i + 1, j - 1
    return True


def can_permute_to_palindrome(word):
    return sum(c % 2 for c in Counter(word).values()) <= 1


def palindromic_permutations(word):
    return sorted({"".join(p) for p in permutations(word) if "".join(p) == "".join(p)[::-1]})


def palindrome_pairs(words):
    return [(a, b) for a in words for b in words if a != b and (a + b) == (a + b)[::-1]]


def next_palindrome(n):
    n += 1
    while str(n) != str(n)[::-1]:
        n += 1
    return n


def main():
    sentences = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "Hello, world",
        "Madam, in Eden, I'm Adam.",
    ]
    for s in sentences:
        assert is_palindrome(s) == two_pointer(s)
        print(f"{s!r:<36} palindrome={is_palindrome(s)}")
    for w in ("aabb", "carerac", "code", "aabbc"):
        options = palindromic_permutations(w) if can_permute_to_palindrome(w) else []
        print(f"{w}: can permute={can_permute_to_palindrome(w)} -> {options}")
    print("Palindrome pairs:", palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll", "bat", "tab"]))
    print("Next palindromes:", {n: next_palindrome(n) for n in (9, 123, 808, 1991, 99999)})
    words = "level noon civic radar python refer stats code rotor".split()
    print("Palindromic words:", sorted(filter(is_palindrome, words), key=len))


if __name__ == "__main__":
    main()
