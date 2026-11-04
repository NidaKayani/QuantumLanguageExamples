"""Set comprehensions for deduplication and mathematical sets."""

import math

squares = {n * n for n in range(-5, 6)}
print("squares from -5..5:", sorted(squares))

words = "The quick brown fox jumps over the lazy dog The End".split()
lowered = {w.lower() for w in words}
print("unique lowercase words:", sorted(lowered))

lengths = {len(w) for w in words}
print("word lengths present:", sorted(lengths))

first_letters = {w[0].upper() for w in words if len(w) > 3}
print("initials of long words:", sorted(first_letters))

pythagorean = {
    tuple(sorted((a, b)))
    for a in range(1, 30)
    for b in range(a, 30)
    if math.isqrt(a * a + b * b) ** 2 == a * a + b * b
}
print("pythagorean legs < 30:", sorted(pythagorean))

primes = {n for n in range(2, 60) if all(n % d for d in range(2, math.isqrt(n) + 1))}
odds = {n for n in range(60) if n % 2}
print("primes:", sorted(primes))
print("odd non-primes < 60:", sorted(odds - primes))

sums = {a + b for a in primes for b in primes if a <= b < 20}
evens_covered = {n for n in range(4, 40, 2) if n in sums}
print("even numbers 4..38 written as sum of two primes < 20:", len(evens_covered))
