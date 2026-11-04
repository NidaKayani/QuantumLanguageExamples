"""Detect cycles in directed graphs (three-colour DFS) and undirected graphs (union-find)."""
from enum import Enum


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


def directed_cycle(graph):
    color = {n: Color.WHITE for n in graph}
    path = []

    def dfs(u):
        color[u] = Color.GRAY
        path.append(u)
        for v in graph[u]:
            if color[v] is Color.GRAY:
                return path[path.index(v):] + [v]
            if color[v] is Color.WHITE:
                found = dfs(v)
                if found:
                    return found
        color[u] = Color.BLACK
        path.pop()
        return None

    for node in graph:
        if color[node] is Color.WHITE:
            cycle = dfs(node)
            if cycle:
                return cycle
    return None


def undirected_cycle(nodes, edges):
    parent = {n: n for n in nodes}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return (u, v)
        parent[ru] = rv
    return None


def main():
    tasks = {"fetch": ["parse"], "parse": ["validate"], "validate": ["store"],
             "store": [], "log": ["store"]}
    print("Pipeline cycle:", directed_cycle(tasks))
    tasks["store"] = ["fetch"]
    cycle = directed_cycle(tasks)
    print("After adding store->fetch:", " -> ".join(cycle))

    nodes = range(6)
    tree_edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    print("Tree has cycle:", undirected_cycle(nodes, tree_edges))
    closing = undirected_cycle(nodes, tree_edges + [(4, 5)])
    print("Edge that closes a cycle:", closing)

    print("Color states:", [c.name for c in Color])
    self_loop = {"x": ["x"]}
    print("Self loop cycle:", directed_cycle(self_loop))


if __name__ == "__main__":
    main()
