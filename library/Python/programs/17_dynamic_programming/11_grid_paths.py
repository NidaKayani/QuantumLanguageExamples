"""Grid path DP: counting lattice paths with obstacles and minimum-cost routes."""
from math import comb

COSTS = [
    [1, 3, 1, 2, 8],
    [1, 5, 1, 9, 1],
    [4, 2, 1, 3, 1],
    [7, 1, 8, 1, 2],
    [2, 6, 1, 1, 1],
]

BLOCKED = {(1, 1), (2, 3), (3, 0), (0, 4)}


def count_paths(rows, cols, blocked=frozenset()):
    ways = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if (r, c) in blocked:
                continue
            if r == c == 0:
                ways[r][c] = 1
                continue
            up = ways[r - 1][c] if r else 0
            left = ways[r][c - 1] if c else 0
            ways[r][c] = up + left
    return ways


def min_path(grid):
    rows, cols = len(grid), len(grid[0])
    best = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            options = []
            if r:
                options.append(best[r - 1][c])
            if c:
                options.append(best[r][c - 1])
            best[r][c] = grid[r][c] + (min(options) if options else 0)
    path, r, c = [(rows - 1, cols - 1)], rows - 1, cols - 1
    while (r, c) != (0, 0):
        if c == 0 or (r and best[r - 1][c] <= best[r][c - 1]):
            r -= 1
        else:
            c -= 1
        path.append((r, c))
    return best[-1][-1], path[::-1]


def main():
    for n in range(2, 8):
        table = count_paths(n, n)
        assert table[-1][-1] == comb(2 * n - 2, n - 1)
        print(f"{n}x{n} open grid: {table[-1][-1]} paths")
    ways = count_paths(5, 5, BLOCKED)
    print("Paths with obstacles:")
    for r, row in enumerate(ways):
        print("  " + " ".join(" X" if (r, c) in BLOCKED else f"{v:2d}"
                              for c, v in enumerate(row)))
    total, path = min_path(COSTS)
    print("Minimum path sum:", total)
    on_path = set(path)
    for r, row in enumerate(COSTS):
        print("  " + " ".join(f"[{v}]" if (r, c) in on_path else f" {v} "
                              for c, v in enumerate(row)))
    print("Steps:", "".join("D" if b[0] > a[0] else "R" for a, b in zip(path, path[1:])))


if __name__ == "__main__":
    main()
