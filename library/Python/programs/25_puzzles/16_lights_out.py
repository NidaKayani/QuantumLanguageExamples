"""Lights Out solved exactly with Gaussian elimination over GF(2), using integers as bit rows."""


def toggle_mask(n, r, c):
    mask = 0
    for dr, dc in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < n and 0 <= cc < n:
            mask |= 1 << (rr * n + cc)
    return mask


def solve(n, lights):
    """Return the set of cells to press so every light ends up off, or None."""
    size = n * n
    # Row i: which presses affect cell i, plus the target bit in position `size`.
    rows = []
    for i in range(size):
        row = 0
        for j in range(size):
            if toggle_mask(n, *divmod(j, n)) >> i & 1:
                row |= 1 << j
        row |= (lights >> i & 1) << size
        rows.append(row)
    pivots = []
    rank = 0
    for col in range(size):
        pivot = next((r for r in range(rank, size) if rows[r] >> col & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(size):
            if r != rank and rows[r] >> col & 1:
                rows[r] ^= rows[rank]
        pivots.append(col)
        rank += 1
    if any(rows[r] >> size & 1 for r in range(rank, size)):
        return None
    presses = 0
    for r, col in enumerate(pivots):
        if rows[r] >> size & 1:
            presses |= 1 << col
    return presses, size - rank


def apply(n, lights, presses):
    for j in range(n * n):
        if presses >> j & 1:
            lights ^= toggle_mask(n, *divmod(j, n))
    return lights


def show(n, bits, on="#", off="."):
    return "\n".join(" ".join(on if bits >> (r * n + c) & 1 else off for c in range(n)) for r in range(n))


def parse(text):
    cells = "".join(text.split())
    return sum(1 << i for i, ch in enumerate(cells) if ch == "#")


puzzles = {3: "#.# .#. #.#", 4: "##.. #..# .##. ...#", 5: "##### ##### ##### ##### #####"}
for n, text in puzzles.items():
    lights = parse(text)
    result = solve(n, lights)
    print(f"{n}x{n} puzzle:")
    print(show(n, lights))
    if result is None:
        print("unsolvable\n")
        continue
    presses, free = result
    print(f"press {bin(presses).count('1')} cells (null-space dimension {free}):")
    print(show(n, presses, on="X"))
    print("all lights off afterwards:", apply(n, lights, presses) == 0, "\n")

print("Board size vs. fraction of starting patterns that are solvable:")
for n in range(2, 8):
    _, free = solve(n, 0)
    print(f"  {n}x{n}: null-space dimension {free}, solvable 1 in {2 ** free} patterns")
