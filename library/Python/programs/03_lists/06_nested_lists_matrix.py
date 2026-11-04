"""Represent matrices as nested lists and implement basic matrix operations."""


def show(name, m):
    print(f"{name}:")
    for row in m:
        print("  " + " ".join(f"{v:4}" for v in row))


def mat_add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_mul(a, b):
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def transpose(m):
    return [list(col) for col in zip(*m)]


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def rotate_clockwise(m):
    return [list(row) for row in zip(*m[::-1])]


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
show("A", A)
show("B", B)
show("A x B", mat_mul(A, B))
show("A^T", transpose(A))
show("A + A", mat_add(A, A))
show("I3", identity(3))
print("A x I == A:", mat_mul(A, identity(3)) == A)

square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
show("rotated", rotate_clockwise(square))
print("diagonal:", [square[i][i] for i in range(3)])
print("anti-diagonal:", [square[i][-1 - i] for i in range(3)])
print("row sums:", [sum(r) for r in square], "col sums:", [sum(c) for c in zip(*square)])

# the aliasing pitfall with [[0]*n]*m
bad = [[0] * 3] * 2
bad[0][0] = 1
good = [[0] * 3 for _ in range(2)]
good[0][0] = 1
print("aliased:", bad, "| independent:", good)
