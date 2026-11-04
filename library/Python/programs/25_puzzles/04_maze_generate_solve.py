"""Generate a perfect maze with randomized DFS (own LCG) and solve it with breadth-first search."""
from collections import deque


class LCG:
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = (self.state * 1664525 + 1013904223) % 2**32
        return self.state

    def shuffle(self, items):
        for i in range(len(items) - 1, 0, -1):
            j = self.next() % (i + 1)
            items[i], items[j] = items[j], items[i]
        return items


def generate(width, height, rng):
    grid = [["#"] * (2 * width + 1) for _ in range(2 * height + 1)]
    stack = [(0, 0)]
    seen = {(0, 0)}
    grid[1][1] = " "
    while stack:
        x, y = stack[-1]
        options = [(dx, dy) for dx, dy in rng.shuffle([(1, 0), (-1, 0), (0, 1), (0, -1)])
                   if 0 <= x + dx < width and 0 <= y + dy < height and (x + dx, y + dy) not in seen]
        if not options:
            stack.pop()
            continue
        dx, dy = options[0]
        nx, ny = x + dx, y + dy
        grid[2 * y + 1 + dy][2 * x + 1 + dx] = " "
        grid[2 * ny + 1][2 * nx + 1] = " "
        seen.add((nx, ny))
        stack.append((nx, ny))
    return grid


def solve(grid, start, goal):
    prev = {start: None}
    queue = deque([start])
    while queue:
        cell = queue.popleft()
        if cell == goal:
            break
        r, c = cell
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if grid[nr][nc] == " " and (nr, nc) not in prev:
                prev[(nr, nc)] = cell
                queue.append((nr, nc))
    path, cell = [], goal
    while cell:
        path.append(cell)
        cell = prev[cell]
    return path[::-1], len(prev)


rng = LCG(31337)
maze = generate(12, 8, rng)
start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
path, explored = solve(maze, start, goal)
for r, c in path:
    maze[r][c] = "."
maze[start[0]][start[1]], maze[goal[0]][goal[1]] = "S", "G"
print("\n".join("".join(row) for row in maze))
open_cells = sum(row.count(" ") + row.count(".") for row in maze) + 2
print(f"Path length: {len(path)} cells, explored {explored} of {open_cells} open cells")

lengths = []
for seed in range(1, 6):
    m = generate(10, 10, LCG(seed))
    lengths.append(len(solve(m, (1, 1), (19, 19))[0]))
print("Shortest path lengths for seeds 1-5 on 10x10 mazes:", lengths)
