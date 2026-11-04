"""Memoization with functools.cache and lru_cache, including cache statistics."""
from functools import cache, lru_cache


@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def partitions(n, largest=None):
    """Number of ways to write n as a sum of positive integers <= largest."""
    if largest is None:
        largest = n
    if n == 0:
        return 1
    if n < 0 or largest == 0:
        return 0
    return partitions(n - largest, largest) + partitions(n, largest - 1)


@lru_cache(maxsize=3)
def slow_square(x):
    print(f"    computing {x}^2")
    return x * x


@cache
def edit_distance(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b[0]:
        return edit_distance(a[1:], b[1:])
    return 1 + min(edit_distance(a[1:], b), edit_distance(a, b[1:]), edit_distance(a[1:], b[1:]))


print("fib(90) =", fib(90))
print("fib cache:", fib.cache_info())

print("partitions:", [partitions(n) for n in range(1, 16)])
print("p(60) =", partitions(60))
info = partitions.cache_info()
print(f"partition cache hits={info.hits} misses={info.misses} size={info.currsize}")

print("LRU cache with maxsize=3:")
for x in [1, 2, 3, 1, 4, 2, 1]:
    slow_square(x)
print("  ", slow_square.cache_info())
slow_square.cache_clear()
print("   after clear:", slow_square.cache_info())

for a, b in [("kitten", "sitting"), ("flaw", "lawn"), ("intention", "execution")]:
    print(f"edit_distance({a!r}, {b!r}) = {edit_distance(a, b)}")
print("edit cache entries:", edit_distance.cache_info().currsize)
