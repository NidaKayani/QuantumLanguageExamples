"""Breadth-first search on a grid maze with path reconstruction."""

from collections import deque

MAZE = [
    "S.#.......",
    ".##.####..",
    "....#..#.#",
    "##.##.##..",
    "...#...#.#",
    ".#...#...E",
]


def find(ch):
    for r, row in enumerate(MAZE):
        if ch in row:
            return r, row.index(ch)
    raise ValueError(ch)


def neighbours(r, c):
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(MAZE) and 0 <= nc < len(MAZE[0]) and MAZE[nr][nc] != "#":
            yield nr, nc


def bfs(start, goal):
    parent = {start: None}
    queue = deque([start])
    while queue:
        cell = queue.popleft()
        if cell == goal:
            break
        for nxt in neighbours(*cell):
            if nxt not in parent:
                parent[nxt] = cell
                queue.append(nxt)
    if goal not in parent:
        return None, len(parent)
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1], len(parent)


start, goal = find("S"), find("E")
path, explored = bfs(start, goal)
print(f"start {start} goal {goal}")
print(f"shortest path: {len(path) - 1} steps, explored {explored} cells")
on_path = set(path)
for r, row in enumerate(MAZE):
    print("  " + "".join("*" if (r, c) in on_path and ch == "." else ch for c, ch in enumerate(row)))

dist = {start: 0}
q = deque([start])
while q:
    cell = q.popleft()
    for n in neighbours(*cell):
        if n not in dist:
            dist[n] = dist[cell] + 1
            q.append(n)
farthest = max(dist, key=lambda k: (dist[k], k))
print("farthest reachable cell:", farthest, "at distance", dist[farthest])
print("unreachable open cells:", sum(row.count(".") for row in MAZE) + 2 - len(dist))
