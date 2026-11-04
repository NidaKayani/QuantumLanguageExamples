"""Exponential search and jump search, including search over an unbounded function."""

import math
from bisect import bisect_left


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n)) or 1
    prev = 0
    while prev < n and arr[min(prev + step, n) - 1] < target:
        prev += step
    for i in range(prev, min(prev + step, n)):
        if arr[i] == target:
            return i
    return -1


def exponential_search(arr, target):
    if not arr:
        return -1
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    lo, hi = bound // 2, min(bound, len(arr) - 1)
    i = bisect_left(arr, target, lo, hi + 1)
    return i if i < len(arr) and arr[i] == target else -1


def first_true(pred):
    """Smallest n >= 0 with pred(n) True, for a monotone predicate."""
    hi = 1
    while not pred(hi):
        hi *= 2
    lo = hi // 2
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


squares = [i * i for i in range(200)]
for t in [0, 144, 1521, 39601, 50]:
    print(f"find {t:>5}: jump={jump_search(squares, t):>4} exponential={exponential_search(squares, t):>4}")

n = first_true(lambda k: k * k * k > 10 ** 12)
print("smallest k with k^3 > 10^12:", n)
n = first_true(lambda k: math.factorial(k) > 10 ** 50)
print("smallest k with k! > 10^50:", n)
n = first_true(lambda k: sum(1 / i for i in range(1, k + 1)) > 7)
print("harmonic series exceeds 7 after", n, "terms")
print("integer sqrt via search:", first_true(lambda k: k * k > 10 ** 10) - 1, "check:", math.isqrt(10 ** 10))
