"""Langton's ant and a multi-color turmite on an unbounded grid stored in a dict."""
from collections import defaultdict

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left


def run(rule, steps):
    grid = defaultdict(int)
    x = y = 0
    heading = 0
    for _ in range(steps):
        color = grid[(x, y)]
        heading = (heading + (1 if rule[color] == "R" else -1)) % 4
        grid[(x, y)] = (color + 1) % len(rule)
        dx, dy = DIRS[heading]
        x, y = x + dx, y + dy
    return {cell: c for cell, c in grid.items() if c}, (x, y)


def render(cells, symbols=".#ox"):
    xs = [x for x, _ in cells]
    ys = [y for _, y in cells]
    return "\n".join(
        "".join(symbols[cells.get((x, y), 0)] for x in range(min(xs), max(xs) + 1))
        for y in range(min(ys), max(ys) + 1)
    )


cells, pos = run("RL", 500)
print(f"Langton's ant (RL) after 500 steps: {len(cells)} black cells, ant at {pos}")
print(render(cells))

for steps in (1000, 5000, 11000):
    cells, pos = run("RL", steps)
    print(f"steps={steps:>5}: black={len(cells):>4} ant={pos}")

cells, pos = run("RLR", 300)
print(f"\nTurmite RLR after 300 steps: {len(cells)} colored cells")
print(render(cells))
