"""Dijkstra's single-source shortest paths using heapq on a road network."""
import heapq
from math import inf

ROADS = [
    ("Amsterdam", "Utrecht", 45), ("Amsterdam", "Haarlem", 20),
    ("Haarlem", "Leiden", 30), ("Leiden", "TheHague", 18),
    ("Utrecht", "Rotterdam", 60), ("TheHague", "Rotterdam", 25),
    ("Utrecht", "Arnhem", 65), ("Rotterdam", "Breda", 50),
    ("Arnhem", "Nijmegen", 20), ("Breda", "Eindhoven", 60),
    ("Eindhoven", "Nijmegen", 70), ("Amsterdam", "Leiden", 45),
]


def build_graph(roads):
    graph = {}
    for a, b, w in roads:
        graph.setdefault(a, []).append((b, w))
        graph.setdefault(b, []).append((a, w))
    return graph


def dijkstra(graph, source):
    dist = {node: inf for node in graph}
    prev = {}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, w in graph[node]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                prev[nxt] = node
                heapq.heappush(heap, (nd, nxt))
    return dist, prev


def path_to(prev, target):
    path = [target]
    while path[-1] in prev:
        path.append(prev[path[-1]])
    return list(reversed(path))


def main():
    graph = build_graph(ROADS)
    dist, prev = dijkstra(graph, "Amsterdam")
    print(f"{'City':<12}{'km':>5}  Route")
    for city in sorted(dist, key=lambda c: (dist[c], c)):
        route = " > ".join(path_to(prev, city))
        print(f"{city:<12}{dist[city]:>5}  {route}")
    total = sum(dist.values())
    print(f"Average distance: {total / (len(dist) - 1):.2f} km")


if __name__ == "__main__":
    main()
