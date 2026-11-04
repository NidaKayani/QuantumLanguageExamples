"""N-Queens: count all solutions with backtracking on sets and print the first board for 8 queens."""


def solve(n):
    cols, diag1, diag2 = set(), set(), set()
    placement = []

    def place(row):
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


def count_bitmask(n):
    full = (1 << n) - 1

    def go(cols, left, right):
        if cols == full:
            return 1
        total = 0
        free = full & ~(cols | left | right)
        while free:
            bit = free & -free
            free -= bit
            total += go(cols | bit, ((left | bit) << 1) & full, (right | bit) >> 1)
        return total

    return go(0, 0, 0)


def canonical(sol):
    n = len(sol)
    boards = []
    b = sol
    for _ in range(4):
        b = tuple(n - 1 - b.index(r) for r in range(n))  # rotate 90 degrees
        boards += [b, tuple(reversed(b))]
    return min(boards)


for n in range(4, 10):
    sols = list(solve(n))
    unique = {canonical(s) for s in sols}
    print(f"n={n}: {len(sols):>3} solutions ({len(unique)} unique up to symmetry), bitmask count={count_bitmask(n)}")

first = next(solve(8))
print("\nFirst 8-queens solution:", first)
for col in first:
    print(" ".join("Q" if c == col else "." for c in range(8)))
