"""Count islands, measure their areas and perimeters, and flood-fill a grid map."""
from collections import deque

MAP = [
    "11000011",
    "11000111",
    "00100000",
    "00011100",
    "10010100",
    "10011100",
    "00000001",
]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    found = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            cells, queue = [], deque([(r, c)])
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                cells.append((cr, cc))
                for dr, dc in DIRS:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"
                            and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            found.append(cells)
    return found


def perimeter(cells):
    cell_set = set(cells)
    return sum((r + dr, c + dc) not in cell_set for r, c in cells for dr, dc in DIRS)


def flood_fill(grid, r, c, new):
    board = [list(row) for row in grid]
    old = board[r][c]
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == old:
            board[r][c] = new
            stack.extend((r + dr, c + dc) for dr, dc in DIRS)
    return ["".join(row) for row in board]


def main():
    found = islands(MAP)
    print(f"Islands found: {len(found)}")
    for i, cells in enumerate(found, 1):
        print(f"  island {i}: area={len(cells):2d} perimeter={perimeter(cells):2d} "
              f"top-left={min(cells)}")
    labels = [list(row.replace("1", "#").replace("0", ".")) for row in MAP]
    for i, cells in enumerate(found):
        for r, c in cells:
            labels[r][c] = chr(ord("A") + i)
    print("Labelled map:")
    print("\n".join("  " + "".join(row) for row in labels))
    print("Water flood fill from (2,0):")
    print("\n".join("  " + row for row in flood_fill(MAP, 2, 0, "~")))


if __name__ == "__main__":
    main()
