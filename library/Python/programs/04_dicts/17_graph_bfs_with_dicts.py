"""Represent a graph as a dict of lists and run BFS, DFS and shortest paths."""

from collections import deque
import heapq

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}


def bfs(start):
    seen = {start: None}
    order = []
    q = deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph[node]:
            if nxt not in seen:
                seen[nxt] = node
                q.append(nxt)
    return order, seen


def path_to(parents, target):
    path = []
    while target is not None:
        path.append(target)
        target = parents[target]
    return path[::-1]


def dfs(node, visited=None):
    visited = visited if visited is not None else []
    visited.append(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited)
    return visited


order, parents = bfs("A")
print("BFS order:", order)
print("DFS order:", dfs("A"))
print("path A->G:", " -> ".join(path_to(parents, "G")))
print("degrees:", {n: len(nbrs) for n, nbrs in graph.items()})

weighted = {"A": {"B": 4, "C": 1}, "B": {"D": 1}, "C": {"B": 2, "D": 5}, "D": {}}
dist = {"A": 0}
heap = [(0, "A")]
while heap:
    d, node = heapq.heappop(heap)
    if d > dist.get(node, float("inf")):
        continue
    for nxt, w in weighted[node].items():
        if d + w < dist.get(nxt, float("inf")):
            dist[nxt] = d + w
            heapq.heappush(heap, (d + w, nxt))
print("dijkstra distances:", dict(sorted(dist.items())))
