"""Memoizing recursive functions with a hand-written decorator and functools caches."""
from functools import lru_cache, cache, wraps


def memoize(func):
    store = {}

    @wraps(func)
    def wrapper(*args):
        if args not in store:
            store[args] = func(*args)
        return store[args]

    wrapper.store = store
    return wrapper


@memoize
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def grid_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


@cache
def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return 1
    return sum(partitions(n - k, k) for k in range(1, min(n, max_part) + 1))


print("fib(80) =", fib(80))
print("memo entries:", len(fib.store))
print("fib name preserved:", fib.__name__)

print("grid_paths(10, 10) =", grid_paths(10, 10))
info = grid_paths.cache_info()
print(f"cache hits={info.hits} misses={info.misses}")

for n in (5, 10, 30):
    print(f"partitions({n}) = {partitions(n)}")

grid_paths.cache_clear()
print("after clear:", grid_paths.cache_info().currsize)
