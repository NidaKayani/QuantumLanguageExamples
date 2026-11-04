"""Recursive flood fill on a character grid to label connected regions."""

import string

MAP = """
..##....##
..##..#...
......#..#
##....###.
#..##.....
...##..##.
""".strip().splitlines()


def flood(grid, r, c, target, label):
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return 0
    if grid[r][c] != target:
        return 0
    grid[r][c] = label
    return 1 + sum(flood(grid, r + dr, c + dc, target, label)
                   for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))


grid = [list(row) for row in MAP]
labels = iter(string.ascii_uppercase)
sizes = {}
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "#":
            label = next(labels)
            sizes[label] = flood(grid, r, c, "#", label)

print("labelled walls:")
for row in grid:
    print("  " + "".join(row))
print("wall regions:", len(sizes))
for label, size in sorted(sizes.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"  region {label}: {size} cells")

paint = [list(row) for row in MAP]
filled = flood(paint, 0, 0, ".", "~")
print(f"\nfloor reachable from top-left: {filled} cells")
for row in paint:
    print("  " + "".join(row))
