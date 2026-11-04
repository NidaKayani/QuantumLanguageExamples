"""A small Matrix class with indexing, matrix multiplication (@), transpose, and equality."""


class Matrix:
    def __init__(self, rows):
        self.rows = [list(r) for r in rows]
        self.shape = (len(self.rows), len(self.rows[0]) if self.rows else 0)

    @classmethod
    def identity(cls, n):
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def __getitem__(self, pos):
        i, j = pos
        return self.rows[i][j]

    def __setitem__(self, pos, value):
        i, j = pos
        self.rows[i][j] = value

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError(f"shape mismatch {self.shape} @ {other.shape}")
        cols = list(zip(*other.rows))
        return Matrix([[sum(a * b for a, b in zip(row, col)) for col in cols]
                       for row in self.rows])

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(r1, r2)]
                       for r1, r2 in zip(self.rows, other.rows)])

    def __pow__(self, n):
        result = Matrix.identity(self.shape[0])
        for _ in range(n):
            result = result @ self
        return result

    @property
    def T(self):
        return Matrix(zip(*self.rows))

    def __eq__(self, other):
        return isinstance(other, Matrix) and self.rows == other.rows

    def __str__(self):
        width = max(len(str(v)) for row in self.rows for v in row)
        return "\n".join("[" + " ".join(f"{v:>{width}}" for v in row) + "]"
                         for row in self.rows)


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[0, 1], [1, 0]])
print("A =\n" + str(A))
print("A @ B =\n" + str(A @ B))
print("A + B =\n" + str(A + B))
print("A.T =\n" + str(A.T))
print("A @ I == A:", A @ Matrix.identity(2) == A)
fib = Matrix([[1, 1], [1, 0]]) ** 10
print("fib matrix ^10 =\n" + str(fib))
C = Matrix([[1, 2, 3]])
print("C shape:", C.shape, "| C.T shape:", C.T.shape)
print("C @ C.T =", (C @ C.T)[0, 0])
try:
    C @ C
except ValueError as exc:
    print("error:", exc)
A[0, 0] = 100
print("after A[0,0]=100:", A.rows)
