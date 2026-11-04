"""Triangular 15-hole peg solitaire (the 'cracker barrel' game) solved with memoized DFS."""
from functools import lru_cache

ROWS = 5
HOLES = [(r, c) for r in range(ROWS) for c in range(r + 1)]
INDEX = {h: i for i, h in enumerate(HOLES)}
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]

JUMPS = []
for (r, c), i in INDEX.items():
    for dr, dc in DIRECTIONS:
        over, land = (r + dr, c + dc), (r + 2 * dr, c + 2 * dc)
        if over in INDEX and land in INDEX:
            JUMPS.append((i, INDEX[over], INDEX[land]))


@lru_cache(maxsize=None)
def best_finish(board):
    """Return (pegs remaining, moves) for the best reachable end state."""
    best = (bin(board).count("1"), ())
    for src, over, dst in JUMPS:
        if board >> src & 1 and board >> over & 1 and not board >> dst & 1:
            nxt = board & ~(1 << src) & ~(1 << over) | (1 << dst)
            pegs, moves = best_finish(nxt)
            if pegs < best[0]:
                best = (pegs, ((src, dst),) + moves)
                if pegs == 1:
                    break
    return best


def show(board):
    lines = []
    for r in range(ROWS):
        cells = ["o" if board >> INDEX[(r, c)] & 1 else "." for c in range(r + 1)]
        lines.append(" " * (ROWS - r - 1) + " ".join(cells))
    return "\n".join(lines)


full = (1 << len(HOLES)) - 1
print(f"{len(JUMPS)} possible jumps on a {len(HOLES)}-hole board")
print("Best result by starting empty hole:")
for hole in range(len(HOLES)):
    pegs, _ = best_finish(full & ~(1 << hole))
    print(f"  empty hole {hole:>2} {HOLES[hole]}: {pegs} peg(s) left")

start = full & ~1
pegs, moves = best_finish(start)
print(f"\nSolution from top hole empty ({len(moves)} jumps):")
board = start
print(show(board))
for src, dst in moves[:3]:
    over = next(o for s, o, d in JUMPS if s == src and d == dst)
    board = board & ~(1 << src) & ~(1 << over) | (1 << dst)
    print(f"jump {src}->{dst}")
    print(show(board))
print("... final moves:", ", ".join(f"{s}->{d}" for s, d in moves[3:]))
print("States explored:", best_finish.cache_info().currsize)
