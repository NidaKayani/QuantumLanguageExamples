"""Infinite lazy streams with generators: primes, Fibonacci, Hamming numbers and stream combinators."""
import heapq
from itertools import count, islice, takewhile


def take(n, stream):
    return list(islice(stream, n))


def naturals(start=1):
    return count(start)


def primes():
    """Incremental sieve of Eratosthenes using a dict of composites."""
    composites = {}
    for n in count(2):
        if n not in composites:
            yield n
            composites[n * n] = [n]
        else:
            for p in composites.pop(n):
                composites.setdefault(n + p, []).append(p)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def hamming():
    """Numbers whose only prime factors are 2, 3 and 5, in order."""
    heap, seen = [1], {1}
    while True:
        n = heapq.heappop(heap)
        yield n
        for f in (2, 3, 5):
            if n * f not in seen:
                seen.add(n * f)
                heapq.heappush(heap, n * f)


def stream_map(f, s):
    for x in s:
        yield f(x)


def stream_zip_with(f, a, b):
    for x, y in zip(a, b):
        yield f(x, y)


def scan(f, s, initial):
    acc = initial
    yield acc
    for x in s:
        acc = f(acc, x)
        yield acc


print("primes:", take(15, primes()))
print("primes below 60:", list(takewhile(lambda p: p < 60, primes())))
print("fibonacci:", take(15, fibonacci()))
print("even fibs:", take(8, (f for f in fibonacci() if f % 2 == 0)))
print("hamming:", take(20, hamming()))
print("squares:", take(10, stream_map(lambda n: n * n, naturals())))
print("prime gaps:", take(12, stream_zip_with(lambda a, b: b - a, primes(), islice(primes(), 1, None))))
print("triangular:", take(10, scan(lambda a, b: a + b, naturals(), 0)))
twin = ((p, q) for p, q in zip(primes(), islice(primes(), 1, None)) if q - p == 2)
print("twin primes:", take(8, twin))
print("1000th prime:", next(islice(primes(), 999, None)))
print("first fib with 20 digits:", next(f for f in fibonacci() if len(str(f)) >= 20))
