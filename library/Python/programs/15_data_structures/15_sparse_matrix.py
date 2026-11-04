"""A dictionary-of-keys sparse matrix supporting +, * and transpose."""

from fractions import Fraction


class SparseMatrix:
    def __init__(self, rows, cols, entries=None):
        self.rows, self.cols = rows, cols
        self.data = {k: v for k, v in (entries or {}).items() if v}

    @classmethod
    def from_dense(cls, dense):
        return cls(len(dense), len(dense[0]),
                   {(r, c): v for r, row in enumerate(dense) for c, v in enumerate(row)})

    def __getitem__(self, rc):
        return self.data.get(rc, 0)

    def __add__(self, other):
        keys = self.data.keys() | other.data.keys()
        return SparseMatrix(self.rows, self.cols, {k: self[k] + other[k] for k in keys})

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("shape mismatch")
        by_row = {}
        for (r, c), v in other.data.items():
            by_row.setdefault(r, []).append((c, v))
        result = {}
        for (r, k), v in self.data.items():
            for c, w in by_row.get(k, ()):
                result[(r, c)] = result.get((r, c), 0) + v * w
        return SparseMatrix(self.rows, other.cols, result)

    def transpose(self):
        return SparseMatrix(self.cols, self.rows, {(c, r): v for (r, c), v in self.data.items()})

    @property
    def density(self):
        return Fraction(len(self.data), self.rows * self.cols)

    def __str__(self):
        return "\n".join(" ".join(f"{self[r, c]:>4}" for c in range(self.cols)) for r in range(self.rows))


A = SparseMatrix.from_dense([[1, 0, 0, 2], [0, 0, 3, 0], [0, 4, 0, 0]])
B = SparseMatrix.from_dense([[0, 1], [5, 0], [0, 0], [1, 1]])
print("A =\n" + str(A))
print("non-zeros:", sorted(A.data.items()), "density:", A.density)
print("A^T =\n" + str(A.transpose()))
print("A @ B =\n" + str(A @ B))
print("A + A =\n" + str(A + A))
identity = SparseMatrix(4, 4, {(i, i): 1 for i in range(4)})
print("A @ I == A:", (A @ identity).data == A.data)
try:
    A @ A
except ValueError as exc:
    print("A @ A:", exc)
