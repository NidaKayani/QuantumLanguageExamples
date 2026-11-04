"""Adjacency sets for a social graph: mutual friends and connected components."""

from collections import defaultdict

friendships = [
    ("ann", "bob"), ("bob", "cat"), ("cat", "ann"), ("cat", "dan"),
    ("eve", "fay"), ("fay", "gus"), ("hal", "hal"),
]

graph: defaultdict[str, set[str]] = defaultdict(set)
for a, b in friendships:
    if a == b:
        graph[a]  # ensure isolated node exists
        continue
    graph[a].add(b)
    graph[b].add(a)

for person in sorted(graph):
    print(f"{person}: {sorted(graph[person])}")

def mutual(a, b):
    return graph[a] & graph[b]

print("\nmutual(ann, dan):", sorted(mutual("ann", "dan")))
print("mutual(bob, cat):", sorted(mutual("bob", "cat")))

def suggestions(person):
    friends_of_friends = set().union(*(graph[f] for f in graph[person])) if graph[person] else set()
    return friends_of_friends - graph[person] - {person}

for person in ["ann", "dan", "eve"]:
    print(f"suggest for {person}: {sorted(suggestions(person))}")

def components():
    unvisited = set(graph)
    result = []
    while unvisited:
        start = min(unvisited)
        frontier, comp = {start}, set()
        while frontier:
            comp |= frontier
            frontier = set().union(*(graph[n] for n in frontier)) - comp
        unvisited -= comp
        result.append(sorted(comp))
    return result

print("\ncomponents:", components())
triangles = {frozenset((a, b, c)) for a in graph for b in graph[a] for c in graph[b] if a in graph[c]}
print("triangles:", sorted(sorted(t) for t in triangles))
