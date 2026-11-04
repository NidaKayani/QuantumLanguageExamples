"""Conway's Game of Life on a set of live cells, showing a glider and a blinker."""
from collections import Counter

NEIGHBORS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def step(live):
    counts = Counter((r + dr, c + dc) for r, c in live for dr, dc in NEIGHBORS)
    return {cell for cell, n in counts.items() if n == 3 or (n == 2 and cell in live)}


def render(live, rows, cols):
    return "\n".join(
        "".join("#" if (r, c) in live else "." for c in range(cols)) for r in range(rows)
    )


def parse(pattern, top=0, left=0):
    return {
        (top + r, left + c)
        for r, line in enumerate(pattern.strip().splitlines())
        for c, ch in enumerate(line)
        if ch == "#"
    }


glider = parse("""
.#.
..#
###
""")
blinker = parse("###", top=1, left=7)
world = glider | blinker

for generation in range(5):
    print(f"Generation {generation}: {len(world)} live cells")
    print(render(world, 6, 10))
    print()
    world = step(world)

# A glider moves one cell diagonally every four generations.
g = glider
for _ in range(4):
    g = step(g)
shift = {(r - 1, c - 1) for r, c in g}
print("Glider translated by (1,1) after 4 steps:", shift == glider)
