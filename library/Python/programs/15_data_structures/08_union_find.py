"""Disjoint-set union with path compression and union by rank; Kruskal's MST."""


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}
        self.size = {x: 1 for x in items}
        self.components = len(self.parent)

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:          # path compression
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def groups(self):
        out = {}
        for x in self.parent:
            out.setdefault(self.find(x), []).append(x)
        return sorted(sorted(g) for g in out.values())


uf = UnionFind("abcdefgh")
for a, b in [("a", "b"), ("c", "d"), ("b", "d"), ("e", "f"), ("g", "g")]:
    print(f"union({a}, {b}) merged={uf.union(a, b)} components={uf.components}")
print("a~c:", uf.connected("a", "c"), "a~e:", uf.connected("a", "e"))
print("groups:", uf.groups())
print("size of a's group:", uf.size[uf.find("a")])

edges = [(7, "A", "B"), (5, "A", "D"), (8, "B", "C"), (9, "B", "D"), (7, "B", "E"),
         (5, "C", "E"), (15, "D", "E"), (6, "D", "F"), (8, "E", "F"), (9, "E", "G"), (11, "F", "G")]
dsu = UnionFind("ABCDEFG")
mst = [(w, u, v) for w, u, v in sorted(edges) if dsu.union(u, v)]
print("Kruskal MST:")
for w, u, v in mst:
    print(f"  {u}-{v} ({w})")
print("total weight:", sum(w for w, _, _ in mst))

cycle_uf = UnionFind(range(4))
for u, v in [(0, 1), (1, 2), (2, 3), (3, 0)]:
    if not cycle_uf.union(u, v):
        print(f"edge {u}-{v} closes a cycle")
