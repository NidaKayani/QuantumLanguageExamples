"""Breadth-first search for unweighted shortest paths and distance levels."""
from collections import deque

GRAPH = {
    "home": ["park", "school", "store"],
    "park": ["home", "lake"],
    "school": ["home", "library", "gym"],
    "store": ["home", "mall"],
    "lake": ["park", "forest"],
    "library": ["school", "museum"],
    "gym": ["school"],
    "mall": ["store", "museum"],
    "museum": ["library", "mall"],
    "forest": ["lake"],
}


def bfs_levels(graph, start):
    dist = {start: 0}
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                parent[nxt] = node
                queue.append(nxt)
    return dist, parent


def reconstruct(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]


def main():
    dist, parent = bfs_levels(GRAPH, "home")
    by_level = {}
    for node, d in dist.items():
        by_level.setdefault(d, []).append(node)
    for level in sorted(by_level):
        print(f"Level {level}: {sorted(by_level[level])}")
    for target in ("museum", "forest", "gym"):
        path = reconstruct(parent, target)
        print(f"home -> {target}: {' -> '.join(path)} ({len(path) - 1} hops)")
    farthest = max(dist.items(), key=lambda kv: (kv[1], kv[0]))
    print("Farthest place:", farthest)


if __name__ == "__main__":
    main()
