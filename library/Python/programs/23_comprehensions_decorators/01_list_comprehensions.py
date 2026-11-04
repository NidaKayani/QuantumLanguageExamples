"""List comprehensions for transforming, filtering and generating sequences."""
import math

numbers = list(range(1, 21))
squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers[:6]]
print("squares:", squares)
print("evens:", evens)
print("labels:", labels)

words = ["Python", "list", "comprehension", "is", "Concise", "and", "readable"]
print("lengths:", [len(w) for w in words])
print("capitalized long words:", [w.capitalize() for w in words if len(w) > 3])
print("initials:", "".join([w[0].upper() for w in words]))

pythagorean = [(a, b, c) for c in range(1, 30) for b in range(1, c) for a in range(1, b)
               if a * a + b * b == c * c]
print("pythagorean triples:", pythagorean)

primes = [n for n in range(2, 60) if all(n % d for d in range(2, math.isqrt(n) + 1))]
print("primes:", primes)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("flatten:", [x for row in matrix for x in row])
print("diagonal:", [matrix[i][i] for i in range(len(matrix))])
print("column sums:", [sum(row[j] for row in matrix) for j in range(3)])

csv_line = " 12, 7 ,abc, 42,, -3 "
parsed = [int(tok) for tok in (t.strip() for t in csv_line.split(",")) if tok.lstrip("-").isdigit()]
print("parsed ints:", parsed)

pairs = [(x, y) for x in "ab" for y in range(3)]
print("cartesian:", pairs)
print("enumerate:", [f"{i}:{w}" for i, w in enumerate(words[:4], start=1)])
print("zip sums:", [a + b for a, b in zip(squares, evens)])
print("walrus filter:", [y for x in numbers if (y := x * x % 7) > 3])
print("divisors of 36:", [d for d in range(1, 37) if 36 % d == 0])
