"""Dijkstra shortest paths with heapq on a weighted road network."""

import heapq
from collections import defaultdict

ROADS = [
    ("Amber", "Brook", 7), ("Amber", "Cedar", 9), ("Amber", "Fern", 14),
    ("Brook", "Cedar", 10), ("Brook", "Dune", 15), ("Cedar", "Dune", 11),
    ("Cedar", "Fern", 2), ("Dune", "Elm", 6), ("Elm", "Fern", 9), ("Glen", "Hill", 3),
]

graph = defaultdict(list)
for a, b, w in ROADS:
    graph[a].append((b, w))
    graph[b].append((a, w))


def dijkstra(source):
    dist = {source: 0}
    prev = {}
    heap = [(0, source)]
    visited = set()
    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for nxt, w in graph[node]:
            nd = d + w
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                prev[nxt] = node
                heapq.heappush(heap, (nd, nxt))
    return dist, prev


def path_to(prev, target):
    path = [target]
    while path[-1] in prev:
        path.append(prev[path[-1]])
    return path[::-1]


dist, prev = dijkstra("Amber")
for town in sorted(graph):
    if town in dist:
        print(f"Amber -> {town:<6} {dist[town]:>3}  via {' > '.join(path_to(prev, town))}")
    else:
        print(f"Amber -> {town:<6} unreachable")

dist_e, _ = dijkstra("Elm")
center = min((t for t in dist), key=lambda t: (max(dijkstra(t)[0].values()), t))
print("most central town (min eccentricity):", center)
print("Elm distances:", dict(sorted(dist_e.items())))
