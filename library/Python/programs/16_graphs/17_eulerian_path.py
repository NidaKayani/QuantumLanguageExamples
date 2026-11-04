"""Hierholzer's algorithm for Eulerian paths, applied to reconstructing an itinerary."""
from collections import Counter, defaultdict


def eulerian_path(edges):
    graph = defaultdict(list)
    out_deg, in_deg = Counter(), Counter()
    for u, v in edges:
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1
    for node in graph:
        graph[node].sort(reverse=True)  # pop() yields lexicographically smallest
    nodes = set(out_deg) | set(in_deg)
    starts = [n for n in nodes if out_deg[n] - in_deg[n] == 1]
    ends = [n for n in nodes if in_deg[n] - out_deg[n] == 1]
    balanced = all(abs(out_deg[n] - in_deg[n]) <= 1 for n in nodes)
    if not balanced or len(starts) > 1 or len(ends) > 1:
        return None
    start = starts[0] if starts else min(nodes)
    stack, route = [start], []
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        route.append(stack.pop())
    route.reverse()
    return route if len(route) == len(edges) + 1 else None


def main():
    tickets = [("JFK", "SFO"), ("JFK", "ATL"), ("SFO", "ATL"),
               ("ATL", "JFK"), ("ATL", "SFO")]
    print("Itinerary:", " -> ".join(eulerian_path(tickets)))

    tickets2 = [("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    print("Itinerary 2:", " -> ".join(eulerian_path(tickets2)))

    domino = [(1, 2), (2, 3), (3, 1), (1, 4), (4, 5), (5, 1)]
    circuit = eulerian_path(domino)
    print("Domino circuit:", circuit, "closed:", circuit[0] == circuit[-1])

    bad = [("a", "b"), ("a", "c"), ("a", "d")]
    print("Impossible case:", eulerian_path(bad))

    words = ["apple", "egg", "giraffe", "elephant", "tiger", "rabbit"]
    letter_edges = [(w[0], w[-1]) for w in words]
    chain = eulerian_path(letter_edges)
    print("Word chain letters:", "".join(chain) if chain else "none")


if __name__ == "__main__":
    main()
