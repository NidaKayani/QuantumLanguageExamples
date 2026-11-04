"""N-Queens via recursive backtracking with set-based conflict tracking."""


def solve_queens(n: int):
    cols, diag1, diag2 = set(), set(), set()
    placement = []

    def place(row: int):
        if row == n:
            yield tuple(placement)
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            placement.append(col)
            yield from place(row + 1)
            placement.pop()
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    yield from place(0)


def render(solution):
    n = len(solution)
    return "\n".join(" ".join("Q" if c == col else "." for c in range(n)) for col in solution)


for n in range(1, 9):
    solutions = list(solve_queens(n))
    print(f"{n} queens: {len(solutions)} solutions")

first = next(solve_queens(8))
print("\nfirst 8-queens solution:", first)
print(render(first))

symmetric = [s for s in solve_queens(6)]
print("\nall 6-queens solutions:")
for s in symmetric:
    print("  ", s, "mirror:", tuple(reversed(s)))
