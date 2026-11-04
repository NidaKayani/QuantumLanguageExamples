"""Store a sparse matrix as a dict keyed by (row, col) tuples."""


class Sparse:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.cells = {}

    def __setitem__(self, pos, value):
        if value:
            self.cells[pos] = value
        else:
            self.cells.pop(pos, None)

    def __getitem__(self, pos):
        return self.cells.get(pos, 0)

    def __add__(self, other):
        out = Sparse(self.rows, self.cols)
        for key in self.cells.keys() | other.cells.keys():
            out[key] = self[key] + other[key]
        return out

    def __matmul__(self, other):
        out = Sparse(self.rows, other.cols)
        for (i, k), a in self.cells.items():
            for j in range(other.cols):
                b = other[k, j]
                if b:
                    out[i, j] = out[i, j] + a * b
        return out

    def density(self):
        return len(self.cells) / (self.rows * self.cols)

    def show(self):
        for r in range(self.rows):
            print("  " + " ".join(f"{self[r, c]:3}" for c in range(self.cols)))


m = Sparse(4, 5)
m[0, 0] = 3
m[1, 3] = 7
m[3, 4] = -2
m[2, 2] = 5
print("m:")
m.show()
print(f"stored cells: {len(m.cells)}, density: {m.density():.0%}")

ident = Sparse(5, 5)
for i in range(5):
    ident[i, i] = 1
print("m @ I == m:", (m @ ident).cells == m.cells)

n = Sparse(4, 5)
n[1, 3] = -7
n[0, 1] = 4
total = m + n
print("m + n:")
total.show()
print("cells after cancellation:", sorted(total.cells.items()))
