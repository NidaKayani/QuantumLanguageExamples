"""Nested comprehensions for matrices: transpose, multiply, identity, rotate and Pascal's triangle."""


def show(name, m):
    print(f"{name}:")
    for row in m:
        print("   " + " ".join(f"{x:4}" for x in row))


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

identity = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
show("identity", identity)

transpose = [[row[i] for row in A] for i in range(len(A[0]))]
show("transpose of A", transpose)

product = [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
show("A x B", product)

table = [[i * j for j in range(1, 7)] for i in range(1, 7)]
show("multiplication table", table)

grid = [[r * 4 + c for c in range(4)] for r in range(4)]
rotated = [[grid[len(grid) - 1 - c][r] for c in range(len(grid))] for r in range(len(grid))]
show("rotated 90 degrees clockwise", rotated)

pascal = [[1]]
for _ in range(7):
    prev = pascal[-1]
    pascal.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
for row in pascal:
    print(" ".join(map(str, row)).center(40))

upper = [[x if j >= i else 0 for j, x in enumerate(row)] for i, row in enumerate(table[:4])]
show("upper triangle of first 4 rows", [r[:4] for r in upper])

neighbors = [[sum(grid[rr][cc] for rr in range(max(r - 1, 0), min(r + 2, 4))
                  for cc in range(max(c - 1, 0), min(c + 2, 4)) if (rr, cc) != (r, c))
              for c in range(4)] for r in range(4)]
show("sum of neighbors", neighbors)

coords = [(r, c) for r in range(3) for c in range(3) if (r + c) % 2 == 0]
print("checkerboard coords:", coords)
