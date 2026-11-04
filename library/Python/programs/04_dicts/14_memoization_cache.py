"""Speed up recursive functions with dict-based memoization and functools caches."""

from functools import lru_cache, cache

memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    result = n if n < 2 else fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result


print("fib(80):", fib(80))
print("memo entries:", len(memo))


@lru_cache(maxsize=None)
def grid_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


print("grid paths 10x10:", grid_paths(10, 10))
print("cache info:", grid_paths.cache_info())


@cache
def partitions(n, largest=None):
    if largest is None:
        largest = n
    if n == 0:
        return 1
    return sum(partitions(n - k, k) for k in range(1, min(n, largest) + 1))


print("partitions:", [partitions(n) for n in range(1, 16)])


def edit_distance(a, b):
    table = {}
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                table[i, j] = i + j
            else:
                cost = a[i - 1] != b[j - 1]
                table[i, j] = min(table[i - 1, j] + 1, table[i, j - 1] + 1, table[i - 1, j - 1] + cost)
    return table[len(a), len(b)]


for x, y in (("kitten", "sitting"), ("flaw", "lawn"), ("python", "python")):
    print(f"edit_distance({x!r}, {y!r}) = {edit_distance(x, y)}")

coins = (1, 5, 10, 25)
ways = {0: 1}
for coin in coins:
    for amount in range(coin, 101):
        ways[amount] = ways.get(amount, 0) + ways.get(amount - coin, 0)
print("ways to make 100 cents:", ways[100])
