"""Generator functions with yield: lazy sequences and resumable state."""


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def primes():
    found = []
    n = 2
    while True:
        if all(n % p for p in found if p * p <= n):
            found.append(n)
            yield n
        n += 1


def chunked(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def trace():
    print("  generator started")
    yield 1
    print("  resumed after 1")
    yield 2
    print("  resumed after 2, finishing")


print("fibonacci < 100:", list(fibonacci(100)))
gen = primes()
print("first 15 primes:", [next(gen) for _ in range(15)])
print("next prime:", next(gen))
print("chunks:", list(chunked("abcdefghij", 3)))

print("tracing:")
t = trace()
print("created, nothing printed yet")
for value in t:
    print("  consumer got", value)

g = fibonacci(10)
print("type:", type(g).__name__, "| has __next__:", hasattr(g, "__next__"))
print("sum of fibs < 1000:", sum(fibonacci(1000)))
