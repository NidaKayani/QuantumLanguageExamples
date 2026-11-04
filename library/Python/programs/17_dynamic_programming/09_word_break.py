"""Word break: feasibility table, counting segmentations, and listing them all."""
from functools import lru_cache

DICTIONARY = {"apple", "pen", "applepen", "pine", "pineapple", "cats", "dog",
              "cat", "sand", "and", "a", "an", "ant", "pin", "ea", "pp", "le"}


def can_break(text, words):
    longest = max(map(len, words))
    ok = [True] + [False] * len(text)
    for end in range(1, len(text) + 1):
        ok[end] = any(ok[start] and text[start:end] in words
                      for start in range(max(0, end - longest), end))
    return ok[-1]


def count_breaks(text, words):
    ways = [1] + [0] * len(text)
    for end in range(1, len(text) + 1):
        ways[end] = sum(ways[s] for s in range(end) if text[s:end] in words)
    return ways[-1]


def all_breaks(text, words):
    @lru_cache(maxsize=None)
    def go(start):
        if start == len(text):
            return [[]]
        results = []
        for end in range(start + 1, len(text) + 1):
            piece = text[start:end]
            if piece in words:
                results.extend([piece] + rest for rest in go(end))
        return results

    return [" ".join(parts) for parts in go(0)]


def main():
    for text in ["pineapplepenapple", "catsanddog", "catsandog", "applepen", "anant"]:
        feasible = can_break(text, DICTIONARY)
        n = count_breaks(text, DICTIONARY)
        print(f"{text!r}: breakable={feasible}, segmentations={n}")
        for sentence in sorted(all_breaks(text, DICTIONARY))[:6]:
            print(f"    {sentence}")
    hard = "a" * 30 + "b"
    print("Pathological input breakable:", can_break(hard, {"a", "aa", "aaa"}))
    print("Ways for 'a'*30:", count_breaks("a" * 30, {"a", "aa", "aaa"}))


if __name__ == "__main__":
    main()
