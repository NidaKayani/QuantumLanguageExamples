"""A* search on a grid with terrain costs and a Manhattan-distance heuristic."""

import heapq

TERRAIN = [
    "S..~~....",
    ".#.~~.##.",
    ".#...^#..",
    ".####^#.#",
    "...^^^..G",
]
COST = {".": 1, "~": 5, "^": 3, "S": 1, "G": 1}


def locate(ch):
    return next((r, row.index(ch)) for r, row in enumerate(TERRAIN) if ch in row)


def astar(start, goal):
    def h(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    open_heap = [(h(start), 0, start)]
    g = {start: 0}
    came_from = {}
    expanded = 0
    while open_heap:
        f, cost, cell = heapq.heappop(open_heap)
        if cost > g[cell]:
            continue
        expanded += 1
        if cell == goal:
            path = [cell]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            return path[::-1], cost, expanded
        r, c = cell
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(TERRAIN) and 0 <= nc < len(TERRAIN[0]) and TERRAIN[nr][nc] != "#":
                new_cost = cost + COST[TERRAIN[nr][nc]]
                if new_cost < g.get((nr, nc), float("inf")):
                    g[(nr, nc)] = new_cost
                    came_from[(nr, nc)] = cell
                    heapq.heappush(open_heap, (new_cost + h((nr, nc)), new_cost, (nr, nc)))
    return None, float("inf"), expanded


start, goal = locate("S"), locate("G")
path, cost, expanded = astar(start, goal)
print(f"A* from {start} to {goal}: cost {cost}, {len(path) - 1} moves, expanded {expanded} nodes")
cells = set(path)
for r, row in enumerate(TERRAIN):
    print("  " + "".join("o" if (r, c) in cells and ch not in "SG" else ch for c, ch in enumerate(row)))
print("path:", " ".join(f"{r},{c}" for r, c in path))
terrain_used = {}
for r, c in path[1:]:
    terrain_used[TERRAIN[r][c]] = terrain_used.get(TERRAIN[r][c], 0) + 1
print("terrain crossed:", dict(sorted(terrain_used.items())))
