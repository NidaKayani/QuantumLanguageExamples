"""Kruskal's minimum spanning tree with a union-find class using path compression."""


class DisjointSet:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = dict.fromkeys(items, 0)
        self.count = len(self.parent)

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True


def kruskal(nodes, edges):
    ds = DisjointSet(nodes)
    tree = []
    for w, u, v in sorted(edges):
        if ds.union(u, v):
            tree.append((u, v, w))
            if len(tree) == len(nodes) - 1:
                break
    return tree, ds.count


def main():
    nodes = list("ABCDEFG")
    edges = [(7, "A", "B"), (5, "A", "D"), (8, "B", "C"), (9, "B", "D"),
             (7, "B", "E"), (5, "C", "E"), (15, "D", "E"), (6, "D", "F"),
             (8, "E", "F"), (9, "E", "G"), (11, "F", "G")]
    tree, comps = kruskal(nodes, edges)
    print("MST edges:")
    for u, v, w in tree:
        print(f"  {u}-{v} ({w})")
    print("Total weight:", sum(w for *_, w in tree))
    print("Components after build:", comps)

    forest_nodes = nodes + ["H", "I"]
    forest_edges = edges + [(2, "H", "I")]
    forest, parts = kruskal(forest_nodes, forest_edges)
    print(f"Spanning forest has {len(forest)} edges and {parts} trees")
    ds = DisjointSet(range(10))
    for a, b in [(0, 1), (2, 3), (1, 3), (5, 6), (7, 8), (8, 9)]:
        ds.union(a, b)
    groups = {}
    for x in range(10):
        groups.setdefault(ds.find(x), []).append(x)
    print("Union-find groups:", sorted(groups.values()))


if __name__ == "__main__":
    main()
