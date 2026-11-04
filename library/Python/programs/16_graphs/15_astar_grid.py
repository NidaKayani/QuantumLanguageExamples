"""A* search on a character grid with a Manhattan heuristic and path rendering."""
import heapq
from itertools import count

MAZE = """\
S....#........
.##..#.####...
..#..#....#.#.
..#.......#.#.
..####.####.#.
......#.....#G
.####.#.#####.
......#.......""".splitlines()


def find(grid, ch):
    for r, row in enumerate(grid):
        c = row.find(ch)
        if c != -1:
            return r, c
    raise ValueError(ch)


def neighbors(grid, r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
            yield nr, nc


def astar(grid, start, goal):
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    tie = count()
    open_heap = [(h(start), next(tie), start)]
    g = {start: 0}
    came = {}
    expanded = 0
    while open_heap:
        _, _, cur = heapq.heappop(open_heap)
        expanded += 1
        if cur == goal:
            path = [cur]
            while cur in came:
                cur = came[cur]
                path.append(cur)
            return path[::-1], expanded
        for nxt in neighbors(grid, *cur):
            cand = g[cur] + 1
            if cand < g.get(nxt, float("inf")):
                g[nxt] = cand
                came[nxt] = cur
                heapq.heappush(open_heap, (cand + h(nxt), next(tie), nxt))
    return None, expanded


def main():
    start, goal = find(MAZE, "S"), find(MAZE, "G")
    path, expanded = astar(MAZE, start, goal)
    print(f"Start {start}, goal {goal}")
    print(f"Path length {len(path) - 1}, nodes expanded {expanded}")
    canvas = [list(row) for row in MAZE]
    for r, c in path[1:-1]:
        canvas[r][c] = "*"
    for row in canvas:
        print("  " + "".join(row))
    blocked = [row.replace(".", "#", 1) if i == 5 else row for i, row in enumerate(MAZE)]
    blocked[0] = "S#" + blocked[0][2:]
    blocked[1] = "#" + blocked[1][1:]
    result, exp2 = astar(blocked, start, goal)
    print("Walled-in start reachable:", result is not None, f"(expanded {exp2})")


if __name__ == "__main__":
    main()
