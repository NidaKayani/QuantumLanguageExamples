"""Find bridges and articulation points of a network using low-link values."""
from collections import defaultdict


class Network:
    def __init__(self, links):
        self.adj = defaultdict(list)
        for a, b in links:
            self.adj[a].append(b)
            self.adj[b].append(a)

    def critical(self):
        disc, low = {}, {}
        bridges, cut_vertices = [], set()
        timer = 0

        def dfs(u, parent):
            nonlocal timer
            disc[u] = low[u] = timer
            timer += 1
            children = 0
            for v in self.adj[u]:
                if v == parent:
                    continue
                if v in disc:
                    low[u] = min(low[u], disc[v])
                    continue
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append(tuple(sorted((u, v))))
                if parent is not None and low[v] >= disc[u]:
                    cut_vertices.add(u)
            if parent is None and children > 1:
                cut_vertices.add(u)

        for node in sorted(self.adj):
            if node not in disc:
                dfs(node, None)
        return sorted(bridges), sorted(cut_vertices)


def main():
    links = [
        ("r1", "r2"), ("r2", "r3"), ("r3", "r1"),
        ("r3", "gw"), ("gw", "s1"), ("s1", "s2"), ("s2", "s3"), ("s3", "s1"),
        ("s3", "edge"), ("edge", "client"),
    ]
    net = Network(links)
    bridges, cuts = net.critical()
    print("Nodes:", sorted(net.adj))
    print("Bridges (single points of link failure):")
    for a, b in bridges:
        print(f"  {a} <-> {b}")
    print("Articulation points:", ", ".join(cuts))
    redundant = Network(links + [("r1", "s2"), ("gw", "client"), ("s1", "edge")])
    b2, c2 = redundant.critical()
    print("After adding redundant links:")
    print("  bridges:", b2 or "none")
    print("  articulation points:", c2 or "none")


if __name__ == "__main__":
    main()
