"""Five ways to compute Fibonacci numbers: naive, dict memo, lru_cache, tabulation, generator."""
from functools import lru_cache, wraps
from itertools import islice


def counted(fn):
    @wraps(fn)
    def wrapper(*args):
        wrapper.calls += 1
        return fn(*args)
    wrapper.calls = 0
    return wrapper


@counted
def fib_naive(n):
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib_cached(n):
    return n if n < 2 else fib_cached(n - 1) + fib_cached(n - 2)


def fib_table(n):
    table = [0, 1] + [0] * max(0, n - 1)
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_stream():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_doubling(n):
    if n == 0:
        return 0, 1
    a, b = fib_doubling(n >> 1)
    c = a * (2 * b - a)
    d = a * a + b * b
    return (d, c + d) if n & 1 else (c, d)


def main():
    print("First 15 from generator:", list(islice(fib_stream(), 15)))
    value = fib_naive(22)
    print(f"Naive fib(22) = {value} using {fib_naive.calls} calls")
    print("Dict memo fib(90) =", fib_memo(90))
    print("lru_cache fib(90) =", fib_cached(90), fib_cached.cache_info())
    print("Tabulated fib(90) =", fib_table(90))
    print("Doubling fib(300) =", fib_doubling(300)[0])
    agree = all(fib_memo(n) == fib_cached(n) == fib_table(n) == fib_doubling(n)[0]
                for n in range(100))
    print("All methods agree for n < 100:", agree)
    evens = [f for f in islice(fib_stream(), 40) if f % 2 == 0 and f < 4_000_000]
    print("Sum of even Fibonacci numbers below four million:", sum(evens))
    print("Function name preserved by wraps:", fib_naive.__name__)


if __name__ == "__main__":
    main()
