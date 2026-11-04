"""Generator expressions versus list comprehensions, and consuming them lazily."""

numbers = range(1, 21)

squares_list = [n * n for n in numbers]
squares_gen = (n * n for n in numbers)
print("list:", squares_list[:5], "...")
print("gen type:", type(squares_gen).__name__)
print("sum of squares:", sum(squares_gen))
print("gen consumed, sum again:", sum(squares_gen))

print("sum of even cubes:", sum(n ** 3 for n in numbers if n % 2 == 0))
print("any > 15:", any(n > 15 for n in numbers), "| all positive:", all(n > 0 for n in numbers))
print("max by last digit:", max((n for n in numbers), key=lambda n: (n % 10, n)))

words = ["generator", "lazy", "expression", "yield", "iterator", "python"]
print("longest word length:", max(len(w) for w in words))
print("joined capitals:", "".join(w[0].upper() for w in words))
print("first word with 'y':", next((w for w in words if "y" in w), None))
print("first word with 'z':", next((w for w in words if "z" in w), "none"))

pairs = ((x, y) for x in range(4) for y in range(x) if (x + y) % 2)
print("odd-sum pairs:", list(pairs))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("trace:", sum(matrix[i][i] for i in range(3)))
print("flattened:", list(x for row in matrix for x in row))
print("dict from gen:", dict((w, len(w)) for w in words[:3]))
print("sorted set from gen:", sorted(set(len(w) for w in words)))
