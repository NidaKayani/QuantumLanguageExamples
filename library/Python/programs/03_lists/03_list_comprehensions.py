"""Build lists with comprehensions, filters, nesting and conditional expressions."""

squares = [n * n for n in range(1, 11)]
print("squares:", squares)

even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
print("even squares:", even_squares)

labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print("labels:", labels)

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print("pairs:", pairs)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [v for row in matrix for v in row]
print("flattened:", flat)
transposed = [[row[i] for row in matrix] for i in range(3)]
print("transposed:", transposed)

words = ["Python", "is", "a", "Great", "language", "Indeed"]
caps = [w for w in words if w[0].isupper()]
lengths = [len(w) for w in words]
print("capitalized:", caps, "lengths:", lengths)

pythagorean = [(a, b, c) for c in range(1, 30) for b in range(1, c) for a in range(1, b)
               if a * a + b * b == c * c]
print("pythagorean triples:", pythagorean)

primes = [n for n in range(2, 60) if all(n % d for d in range(2, int(n ** 0.5) + 1))]
print("primes:", primes)

# comprehension variables don't leak
x = "outer"
_ = [x for x in range(3)]
print("x after comprehension:", x)

grid = [[(r * 3 + c) % 4 for c in range(5)] for r in range(3)]
for row in grid:
    print(" ".join(str(v) for v in row))
