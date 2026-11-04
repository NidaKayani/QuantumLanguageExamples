"""Hand-written memoization decorators keyed on arguments, with hit statistics and size limits."""
from collections import OrderedDict
from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            wrapper.hits += 1
        else:
            wrapper.misses += 1
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.hits = wrapper.misses = 0
    wrapper.cache = cache
    return wrapper


def bounded_memoize(maxsize):
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            result = cache[args] = func(*args)
            if len(cache) > maxsize:
                evicted, _ = cache.popitem(last=False)
                wrapper.evictions.append(evicted)
            return result

        wrapper.evictions = []
        wrapper.cache = cache
        return wrapper
    return decorator


@memoize
def grid_paths(rows, cols):
    if rows == 0 or cols == 0:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


@memoize
def coin_ways(amount, coins=(1, 5, 10, 25)):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return coin_ways(amount - coins[0], coins) + coin_ways(amount, coins[1:])


@memoize
def describe(n, *, unit="m"):
    return f"{n}{unit}"


@bounded_memoize(maxsize=3)
def slow_upper(word):
    return word.upper()


print("grid paths 10x10:", grid_paths(10, 10))
print(f"  hits={grid_paths.hits} misses={grid_paths.misses} cached={len(grid_paths.cache)}")
print("ways to make 100 cents:", coin_ways(100))
print(f"  hits={coin_ways.hits} misses={coin_ways.misses}")

describe(5)
describe(5, unit="km")
describe(5)
print("keyword-aware keys:", sorted(map(str, describe.cache.values())), "hits:", describe.hits)

for w in ["a", "b", "c", "a", "d", "e", "a"]:
    slow_upper(w)
print("bounded cache keys:", [k[0] for k in slow_upper.cache])
print("evicted in order:", [k[0] for k in slow_upper.evictions])
