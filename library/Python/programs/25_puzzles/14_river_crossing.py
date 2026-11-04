"""River crossing puzzles (wolf-goat-cabbage, missionaries and cannibals) as BFS over frozenset states."""
from collections import deque
from itertools import combinations


def bfs(start, goal, successors):
    prev = {start: None}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = prev[state]
            return path[::-1]
        for nxt in successors(state):
            if nxt not in prev:
                prev[nxt] = state
                queue.append(nxt)
    return None


ITEMS = frozenset({"farmer", "wolf", "goat", "cabbage"})


def safe(bank):
    if "farmer" in bank:
        return True
    return not ({"wolf", "goat"} <= bank or {"goat", "cabbage"} <= bank)


def wgc_successors(left):
    farmer_left = "farmer" in left
    here = left if farmer_left else ITEMS - left
    for cargo in [None] + sorted(here - {"farmer"}):
        moving = {"farmer"} | ({cargo} if cargo else set())
        new_left = left - moving if farmer_left else left | moving
        if safe(new_left) and safe(ITEMS - new_left):
            yield frozenset(new_left)


path = bfs(ITEMS, frozenset(), wgc_successors)
print(f"Wolf, goat, cabbage: {len(path) - 1} crossings")
for a, b in zip(path, path[1:]):
    moved = sorted(((a - b) | (b - a)) - {"farmer"})
    direction = "->" if "farmer" in a else "<-"
    print(f"  farmer {direction} with {', '.join(moved) or 'nothing':<8}   left bank: {sorted(b) or ['(empty)']}")


def mc_successors(state, total=3, boat=2):
    m, c, boat_left = state
    sign = -1 if boat_left else 1
    for dm in range(boat + 1):
        for dc in range(boat + 1 - dm):
            if dm + dc == 0:
                continue
            nm, nc = m + sign * dm, c + sign * dc
            if not (0 <= nm <= total and 0 <= nc <= total):
                continue
            if (nm and nc > nm) or (total - nm and total - nc > total - nm):
                continue
            yield (nm, nc, not boat_left)


path = bfs((3, 3, True), (0, 0, False), mc_successors)
print(f"\nMissionaries and cannibals: {len(path) - 1} crossings")
for m, c, boat_left in path:
    left = "M" * m + "C" * c
    right = "M" * (3 - m) + "C" * (3 - c)
    print(f"  {left:>6} {'[B]~~~~   ' if boat_left else '   ~~~~[B]'} {right}")

for total in (4, 5):
    result = bfs((total, total, True), (0, 0, False), lambda s, t=total: mc_successors(s, t, 3))
    print(f"{total} pairs with a 3-seat boat: {len(result) - 1 if result else 'impossible'} crossings")
