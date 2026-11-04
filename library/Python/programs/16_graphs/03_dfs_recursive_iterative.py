"""Depth-first search, recursively and with an explicit stack, plus connected components."""

GRAPH = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4],
    6: [7],
    7: [6],
    8: [],
}


def dfs_recursive(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for nxt in graph[start]:
        if nxt not in visited:
            dfs_recursive(graph, nxt, visited, order)
    return order


def dfs_iterative(graph, start):
    visited, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph[node]))
    return order


def components(graph):
    seen = set()
    result = []
    for node in graph:
        if node not in seen:
            comp = dfs_iterative(graph, node)
            seen.update(comp)
            result.append(sorted(comp))
    return result


def main():
    print("Recursive DFS from 1:", dfs_recursive(GRAPH, 1))
    print("Iterative DFS from 1:", dfs_iterative(GRAPH, 1))
    comps = components(GRAPH)
    print(f"Found {len(comps)} components:")
    for i, comp in enumerate(comps, start=1):
        kind = "isolated" if len(comp) == 1 else f"{len(comp)} nodes"
        print(f"  #{i}: {comp} ({kind})")
    reachable = {n: len(dfs_iterative(GRAPH, n)) for n in GRAPH}
    print("Reachable count per node:", reachable)


if __name__ == "__main__":
    main()
