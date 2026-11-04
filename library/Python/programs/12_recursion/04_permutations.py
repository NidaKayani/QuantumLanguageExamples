"""Recursive permutation generation, including unique permutations of multisets."""

from itertools import permutations
from collections import Counter


def perms(items):
    if len(items) <= 1:
        return [list(items)]
    result = []
    for i, head in enumerate(items):
        for tail in perms(items[:i] + items[i + 1:]):
            result.append([head] + tail)
    return result


def unique_perms(counter: Counter, length: int, prefix=()):
    if len(prefix) == length:
        yield "".join(prefix)
        return
    for ch in sorted(counter):
        if counter[ch]:
            counter[ch] -= 1
            yield from unique_perms(counter, length, prefix + (ch,))
            counter[ch] += 1


def swap_perms(arr, k=0):
    if k == len(arr) - 1:
        yield tuple(arr)
    for i in range(k, len(arr)):
        arr[k], arr[i] = arr[i], arr[k]
        yield from swap_perms(arr, k + 1)
        arr[k], arr[i] = arr[i], arr[k]


letters = ["a", "b", "c"]
for p in perms(letters):
    print("".join(p), end=" ")
print()

ours = sorted(tuple(p) for p in perms([1, 2, 3, 4]))
print("matches itertools:", ours == sorted(permutations([1, 2, 3, 4])), "count", len(ours))

word = "banana"
uniq = list(unique_perms(Counter(word), len(word)))
print(f"unique arrangements of {word!r}: {len(uniq)}")
print("first five:", uniq[:5])
print("swap-based for 'xyz':", ["".join(t) for t in swap_perms(list("xyz"))])
