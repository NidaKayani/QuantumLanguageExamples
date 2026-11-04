"""Sudoku solver using constraint sets and most-constrained-cell backtracking."""

PUZZLE = """
53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
"""


def parse(text):
    rows = [line.strip() for line in text.strip().splitlines()]
    return [[int(ch) if ch.isdigit() else 0 for ch in row] for row in rows]


def candidates(grid, r, c):
    used = set(grid[r]) | {grid[i][c] for i in range(9)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {grid[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    return set(range(1, 10)) - used


stats = {"guesses": 0}


def solve(grid):
    empties = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]
    if not empties:
        return True
    r, c = min(empties, key=lambda rc: len(candidates(grid, *rc)))
    for digit in sorted(candidates(grid, r, c)):
        stats["guesses"] += 1
        grid[r][c] = digit
        if solve(grid):
            return True
    grid[r][c] = 0
    return False


def show(grid):
    lines = []
    for r, row in enumerate(grid):
        if r and r % 3 == 0:
            lines.append("------+-------+------")
        cells = [str(d) if d else "." for d in row]
        lines.append(" | ".join(" ".join(cells[i:i + 3]) for i in (0, 3, 6)))
    return "\n".join(lines)


def is_valid(grid):
    groups = [row for row in grid] + [list(col) for col in zip(*grid)]
    groups += [[grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
               for br in (0, 3, 6) for bc in (0, 3, 6)]
    return all(sorted(g) == list(range(1, 10)) for g in groups)


grid = parse(PUZZLE)
print("Puzzle:")
print(show(grid))
print("Givens:", sum(d != 0 for row in grid for d in row))
solved = solve(grid)
print("\nSolved:" if solved else "\nNo solution")
print(show(grid))
print("Valid:", is_valid(grid), "| guesses made:", stats["guesses"])
