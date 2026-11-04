"""Check whether graphs are bipartite with BFS two-colouring and report odd cycles."""
from collections import deque


def two_color(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [None] * n
    parent = [None] * n
    for start in range(n):
        if color[start] is not None:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] is None:
                    color[v] = 1 - color[u]
                    parent[v] = u
                    queue.append(v)
                elif color[v] == color[u]:
                    return False, odd_cycle(parent, u, v)
    return True, color


def ancestors(parent, x):
    chain = [x]
    while parent[x] is not None:
        x = parent[x]
        chain.append(x)
    return chain


def odd_cycle(parent, u, v):
    pu, pv = ancestors(parent, u), ancestors(parent, v)
    common = next(x for x in pu if x in set(pv))
    left = pu[:pu.index(common) + 1]
    right = pv[:pv.index(common)]
    return left + right[::-1]


def describe(name, n, edges):
    ok, info = two_color(n, edges)
    if ok:
        side_a = [i for i, c in enumerate(info) if c == 0]
        side_b = [i for i, c in enumerate(info) if c == 1]
        print(f"{name}: bipartite  A={side_a} B={side_b}")
    else:
        print(f"{name}: NOT bipartite, odd cycle {info} (length {len(info)})")


def main():
    describe("Square", 4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    describe("Triangle", 3, [(0, 1), (1, 2), (2, 0)])
    describe("Pentagon", 5, [(i, (i + 1) % 5) for i in range(5)])
    describe("Hexagon", 6, [(i, (i + 1) % 6) for i in range(6)])
    cube = [(a, b) for a in range(8) for b in range(a + 1, 8)
            if bin(a ^ b).count("1") == 1]
    describe("Cube", 8, cube)
    describe("Forest", 7, [(0, 1), (0, 2), (3, 4), (5, 6), (4, 5)])
    describe("Petersen", 10,
             [(i, (i + 1) % 5) for i in range(5)]
             + [(i, i + 5) for i in range(5)]
             + [(5 + i, 5 + (i + 2) % 5) for i in range(5)])


if __name__ == "__main__":
    main()
