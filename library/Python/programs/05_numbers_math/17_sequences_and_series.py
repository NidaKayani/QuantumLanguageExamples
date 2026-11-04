"""Generate number sequences with generators and compute series sums."""

from itertools import islice, count, takewhile
import math


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def triangular():
    for n in count(1):
        yield n * (n + 1) // 2


def collatz(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def look_and_say(seed="1"):
    while True:
        yield seed
        out, i = [], 0
        while i < len(seed):
            j = i
            while j < len(seed) and seed[j] == seed[i]:
                j += 1
            out.append(f"{j - i}{seed[i]}")
            i = j
        seed = "".join(out)


print("fibonacci:", list(islice(fibonacci(), 15)))
print("triangular:", list(islice(triangular(), 10)))
print("squares < 200:", list(takewhile(lambda x: x < 200, (n * n for n in count(1)))))
print("collatz(27) length:", sum(1 for _ in collatz(27)), "max:", max(collatz(27)))
print("look and say:", list(islice(look_and_say(), 7)))

fibs = list(islice(fibonacci(), 40))
ratios = [fibs[i + 1] / fibs[i] for i in range(30, 35)]
print("fib ratios -> phi:", [round(r, 10) for r in ratios], "phi =", round((1 + math.sqrt(5)) / 2, 10))

print("arithmetic sum 1..100:", sum(range(1, 101)), "| formula:", 100 * 101 // 2)
geom = sum(0.5 ** k for k in range(50))
print("geometric 1 + 1/2 + 1/4 + ...:", geom)
basel = sum(1 / k ** 2 for k in range(1, 100001))
print(f"basel sum: {basel:.6f} vs pi^2/6 = {math.pi ** 2 / 6:.6f}")
even_fib_sum = sum(f for f in takewhile(lambda f: f < 4_000_000, fibonacci()) if f % 2 == 0)
print("sum of even fibs under 4M:", even_fib_sum)
