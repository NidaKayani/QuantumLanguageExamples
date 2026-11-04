"""Knight's tour via Warnsdorff's heuristic on several boards, plus exhaustive count on 5x5 from a corner."""

MOVES = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def neighbors(n, r, c, visited):
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
            yield nr, nc


def warnsdorff(n, start=(0, 0)):
    path = [start]
    visited = {start}
    while len(path) < n * n:
        r, c = path[-1]
        options = list(neighbors(n, r, c, visited))
        if not options:
            return None
        nxt = min(options, key=lambda p: (len(list(neighbors(n, *p, visited))), p))
        path.append(nxt)
        visited.add(nxt)
    return path


def count_tours(rows, cols):
    """Exhaustively count open tours on a small rows x cols board from every start square."""
    def go(pos, visited):
        if len(visited) == rows * cols:
            return 1
        total = 0
        for dr, dc in MOVES:
            nxt = (pos[0] + dr, pos[1] + dc)
            if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols and nxt not in visited:
                visited.add(nxt)
                total += go(nxt, visited)
                visited.remove(nxt)
        return total

    return sum(go((r, c), {(r, c)}) for r in range(rows) for c in range(cols))


def board(n, path):
    order = {pos: i + 1 for i, pos in enumerate(path)}
    return "\n".join(" ".join(f"{order[(r, c)]:3d}" for c in range(n)) for r in range(n))


for n in (5, 6, 8):
    tour = warnsdorff(n)
    if tour is None:
        print(f"{n}x{n}: heuristic got stuck")
        continue
    closed = (tour[-1][0] - tour[0][0], tour[-1][1] - tour[0][1]) in MOVES
    print(f"{n}x{n} tour found ({'closed' if closed else 'open'}):")
    print(board(n, tour))
    print()

valid = all(abs(a[0] - b[0]) * abs(a[1] - b[1]) == 2 for a, b in zip(tour, tour[1:]))
print("8x8 tour moves all legal:", valid, "| squares visited:", len(set(tour)))
for rows, cols in [(3, 4), (3, 7), (4, 4)]:
    print(f"Directed open tours on {rows}x{cols}: {count_tours(rows, cols)}")
