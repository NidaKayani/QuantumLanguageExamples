"""Fibonacci with naive recursion versus several memoisation strategies."""

from functools import lru_cache, cache

calls = 0


def fib_naive(n):
    global calls
    calls += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_lru(n):
    return n if n < 2 else fib_lru(n - 1) + fib_lru(n - 2)


@cache
def fib_cache(n):
    return n if n < 2 else fib_cache(n - 1) + fib_cache(n - 2)


def fib_dict(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib_dict(n - 1) + fib_dict(n - 2)
    return memo[n]


print("naive fib(20) =", fib_naive(20), "using", calls, "calls")
print("lru fib(20)   =", fib_lru(20), fib_lru.cache_info())
print("first 15:", [fib_cache(i) for i in range(15)])
print("fib(100) =", fib_lru(100))
print("fib_dict(90) =", fib_dict(90))
assert fib_lru(80) == fib_cache(80) == fib_dict(80)

@lru_cache(maxsize=3)
def slow_square(n):
    return n * n

for x in [1, 2, 3, 1, 4, 1, 2]:
    slow_square(x)
info = slow_square.cache_info()
print(f"bounded cache: hits={info.hits} misses={info.misses} size={info.currsize}")
fib_lru.cache_clear()
print("after clear:", fib_lru.cache_info())
