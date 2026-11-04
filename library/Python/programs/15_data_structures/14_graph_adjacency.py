"""A directed graph class with topological sorting and cycle detection."""

from collections import defaultdict, deque


class Digraph:
    def __init__(self, edges=()):
        self.adj = defaultdict(list)
        self.nodes = set()
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.nodes |= {u, v}

    def indegrees(self):
        deg = {n: 0 for n in self.nodes}
        for u in list(self.adj):
            for v in self.adj[u]:
                deg[v] += 1
        return deg

    def topo_sort(self):
        deg = self.indegrees()
        ready = deque(sorted(n for n, d in deg.items() if d == 0))
        order = []
        while ready:
            n = ready.popleft()
            order.append(n)
            for m in sorted(self.adj[n]):
                deg[m] -= 1
                if deg[m] == 0:
                    ready.append(m)
        if len(order) != len(self.nodes):
            raise ValueError("graph has a cycle")
        return order

    def find_cycle(self):
        WHITE, GREY, BLACK = 0, 1, 2
        color = dict.fromkeys(self.nodes, WHITE)
        stack = []

        def visit(n):
            color[n] = GREY
            stack.append(n)
            for m in self.adj[n]:
                if color[m] == GREY:
                    return stack[stack.index(m):] + [m]
                if color[m] == WHITE and (cyc := visit(m)):
                    return cyc
            color[n] = BLACK
            stack.pop()
            return None

        for n in sorted(self.nodes):
            if color[n] == WHITE and (cyc := visit(n)):
                return cyc
        return None


build = Digraph([("fetch", "compile"), ("configure", "compile"), ("compile", "link"),
                 ("link", "package"), ("test", "package"), ("compile", "test"), ("docs", "package")])
print("nodes:", sorted(build.nodes))
print("indegrees:", dict(sorted(build.indegrees().items())))
print("build order:", " -> ".join(build.topo_sort()))
print("cycle:", build.find_cycle())

build.add_edge("package", "configure")
print("after adding package->configure cycle:", build.find_cycle())
try:
    build.topo_sort()
except ValueError as exc:
    print("topo sort failed:", exc)
