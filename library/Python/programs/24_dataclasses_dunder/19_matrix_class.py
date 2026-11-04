"""A Matrix class with tuple indexing, __matmul__, __pow__, __eq__, __iter__ and determinant."""
from fractions import Fraction


class Matrix:
    def __init__(self, rows):
        self.rows = [list(r) for r in rows]
        self.n, self.m = len(self.rows), len(self.rows[0])

    @classmethod
    def identity(cls, n):
        return cls([[int(i == j) for j in range(n)] for i in range(n)])

    def __getitem__(self, key):
        i, j = key
        return self.rows[i][j]

    def __setitem__(self, key, value):
        i, j = key
        self.rows[i][j] = value

    def __iter__(self):
        return (tuple(r) for r in self.rows)

    def __eq__(self, other):
        return isinstance(other, Matrix) and self.rows == other.rows

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self.rows, other.rows)])

    def __mul__(self, k):
        return Matrix([[k * x for x in r] for r in self.rows])

    __rmul__ = __mul__

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError(f"shape mismatch {self.shape} @ {other.shape}")
        cols = list(zip(*other.rows))
        return Matrix([[sum(a * b for a, b in zip(r, c)) for c in cols] for r in self.rows])

    def __pow__(self, k):
        result, base = Matrix.identity(self.n), self
        while k:
            if k & 1:
                result = result @ base
            base = base @ base
            k >>= 1
        return result

    @property
    def shape(self):
        return (self.n, self.m)

    @property
    def T(self):
        return Matrix(zip(*self.rows))

    def det(self):
        a = [[Fraction(x) for x in r] for r in self.rows]
        d = Fraction(1)
        for c in range(self.n):
            pivot = next((r for r in range(c, self.n) if a[r][c] != 0), None)
            if pivot is None:
                return Fraction(0)
            if pivot != c:
                a[c], a[pivot] = a[pivot], a[c]
                d = -d
            d *= a[c][c]
            for r in range(c + 1, self.n):
                f = a[r][c] / a[c][c]
                a[r] = [x - f * y for x, y in zip(a[r], a[c])]
        return d

    def __repr__(self):
        width = max(len(str(x)) for r in self.rows for x in r)
        return "\n".join("[" + " ".join(str(x).rjust(width) for x in r) + "]" for r in self.rows)


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[0, 1], [1, 0]])
print("A @ B =\n", A @ B, sep="")
print("A + B =\n", A + B, sep="")
print("2 * A =\n", 2 * A, sep="")
print("A[1, 0] =", A[1, 0], "| shape:", A.shape, "| rows:", list(A))
print("fibonacci via power:", (Matrix([[1, 1], [1, 0]]) ** 30)[0, 1])
M = Matrix([[2, -3, 1], [2, 0, -1], [1, 4, 5]])
print("det(M) =", M.det(), "| det(A) =", A.det(), "| det(M^T) == det(M):", M.T.det() == M.det())
print("A @ I == A:", A @ Matrix.identity(2) == A)
R = Matrix([[1, 2, 3]])
print("row @ col =", (R @ R.T)[0, 0])
try:
    R @ R
except ValueError as exc:
    print("ValueError:", exc)
A[0, 0] = 10
print("after setitem:\n", A, sep="")
