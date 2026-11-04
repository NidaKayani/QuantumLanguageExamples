"""8-puzzle solved with BFS and A* (Manhattan distance), comparing nodes expanded."""
import heapq
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = {"U": -3, "D": 3, "L": -1, "R": 1}


def successors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for name, delta in MOVES.items():
        if (name == "U" and r == 0) or (name == "D" and r == 2) or (name == "L" and c == 0) or (name == "R" and c == 2):
            continue
        s = list(state)
        s[z], s[z + delta] = s[z + delta], s[z]
        yield name, tuple(s)


def solvable(state):
    tiles = [t for t in state if t]
    inversions = sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inversions % 2 == 0


def bfs(start):
    prev = {start: (None, None)}
    queue = deque([start])
    while queue:
        s = queue.popleft()
        if s == GOAL:
            break
        for move, nxt in successors(s):
            if nxt not in prev:
                prev[nxt] = (s, move)
                queue.append(nxt)
    path, s = [], GOAL
    while prev[s][0] is not None:
        s, move = prev[s]
        path.append(move)
    return "".join(reversed(path)), len(prev)


def manhattan(state):
    return sum(abs(i // 3 - (t - 1) // 3) + abs(i % 3 - (t - 1) % 3) for i, t in enumerate(state) if t)


def astar(start):
    frontier = [(manhattan(start), 0, start, "")]
    best = {start: 0}
    expanded = 0
    while frontier:
        f, g, s, path = heapq.heappop(frontier)
        if s == GOAL:
            return path, expanded
        if g > best[s]:
            continue
        expanded += 1
        for move, nxt in successors(s):
            if g + 1 < best.get(nxt, 1 << 30):
                best[nxt] = g + 1
                heapq.heappush(frontier, (g + 1 + manhattan(nxt), g + 1, nxt, path + move))
    return None, expanded


def show(state):
    return "\n".join(" ".join(str(t) if t else "_" for t in state[i:i + 3]) for i in (0, 3, 6))


puzzles = [(1, 2, 3, 4, 5, 6, 0, 7, 8), (4, 1, 3, 7, 2, 6, 0, 5, 8), (8, 6, 7, 2, 5, 4, 3, 0, 1)[::-1],
           (1, 2, 3, 4, 5, 6, 8, 7, 0)]
for p in puzzles:
    print(show(p))
    if not solvable(p):
        print("-> unsolvable (odd inversion count)\n")
        continue
    a_path, a_nodes = astar(p)
    b_path, b_nodes = bfs(p) if len(a_path) <= 14 else ("(skipped)", 0)
    print(f"-> A*: {len(a_path)} moves {a_path} expanded {a_nodes}; BFS: {b_path} visited {b_nodes}\n")
