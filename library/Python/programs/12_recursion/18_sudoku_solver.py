"""Recursive backtracking Sudoku solver."""

import math

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
    return [[0 if ch == "." else int(ch) for ch in line] for line in text.split()]


def candidates(board, r, c):
    n = len(board)
    box = math.isqrt(n)
    used = set(board[r]) | {board[i][c] for i in range(n)}
    br, bc = box * (r // box), box * (c // box)
    used |= {board[i][j] for i in range(br, br + box) for j in range(bc, bc + box)}
    return [d for d in range(1, n + 1) if d not in used]


def solve(board, stats):
    empties = [(r, c) for r, row in enumerate(board) for c, v in enumerate(row) if v == 0]
    if not empties:
        return True
    r, c = min(empties, key=lambda rc: len(candidates(board, *rc)))
    for digit in candidates(board, r, c):
        stats["guesses"] += 1
        board[r][c] = digit
        if solve(board, stats):
            return True
        board[r][c] = 0
    return False


def show(board):
    n = len(board)
    box = math.isqrt(n)
    for r, row in enumerate(board):
        if r and r % box == 0:
            print("-" * (2 * n + 2 * (box - 1) - 1))
        chunks = [" ".join(map(str, row[i:i + box])) for i in range(0, n, box)]
        print(" | ".join(chunks))


small = [[1, 0, 0, 0], [0, 0, 3, 0], [0, 4, 0, 0], [0, 0, 0, 2]]
stats = {"guesses": 0}
solve(small, stats)
show(small)
print("4x4 guesses:", stats["guesses"])
print()
board = parse(PUZZLE)
stats = {"guesses": 0}
print("solved:", solve(board, stats))
show(board)
print("9x9 guesses:", stats["guesses"])
