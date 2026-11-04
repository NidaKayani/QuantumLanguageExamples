"""Depth-first search on a grid: counting islands, sizes and perimeters."""

GRID = """
11000111
11010001
00011000
00000011
10100011
11100000
""".split()

ROWS, COLS = len(GRID), len(GRID[0])
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs_iterative(start, seen):
    stack, cells = [start], []
    seen.add(start)
    while stack:
        r, c = stack.pop()
        cells.append((r, c))
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and GRID[nr][nc] == "1" and (nr, nc) not in seen:
                seen.add((nr, nc))
                stack.append((nr, nc))
    return cells


def dfs_recursive(r, c, seen):
    if not (0 <= r < ROWS and 0 <= c < COLS) or GRID[r][c] != "1" or (r, c) in seen:
        return 0
    seen.add((r, c))
    return 1 + sum(dfs_recursive(r + dr, c + dc, seen) for dr, dc in DIRS)


def perimeter(cells):
    cellset = set(cells)
    return sum((r + dr, c + dc) not in cellset for r, c in cells for dr, dc in DIRS)


seen = set()
islands = []
for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == "1" and (r, c) not in seen:
            islands.append(dfs_iterative((r, c), seen))

print("island count:", len(islands))
for i, cells in enumerate(islands, 1):
    top_left = min(cells)
    print(f"  island {i}: size={len(cells)} perimeter={perimeter(cells)} top-left={top_left}")

seen2 = set()
sizes = sorted((dfs_recursive(r, c, seen2) for r in range(ROWS) for c in range(COLS)), reverse=True)
print("recursive sizes:", [s for s in sizes if s])
largest = max(islands, key=len)
print("largest island cells:", sorted(largest))
