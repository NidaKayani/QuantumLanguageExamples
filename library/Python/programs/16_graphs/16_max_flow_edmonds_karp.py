"""Edmonds-Karp maximum flow with min-cut extraction on a pipeline network."""
from collections import defaultdict, deque


class FlowNetwork:
    def __init__(self):
        self.cap = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, capacity):
        self.cap[u][v] += capacity
        self.cap[v][u] += 0

    def _augmenting_path(self, source, sink):
        parent = {source: None}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, c in self.cap[u].items():
                if c > 0 and v not in parent:
                    parent[v] = u
                    if v == sink:
                        return parent
                    queue.append(v)
        return None

    def max_flow(self, source, sink):
        total = 0
        paths = []
        while (parent := self._augmenting_path(source, sink)) is not None:
            path, v = [sink], sink
            while parent[v] is not None:
                v = parent[v]
                path.append(v)
            path.reverse()
            bottleneck = min(self.cap[a][b] for a, b in zip(path, path[1:]))
            for a, b in zip(path, path[1:]):
                self.cap[a][b] -= bottleneck
                self.cap[b][a] += bottleneck
            total += bottleneck
            paths.append((path, bottleneck))
        return total, paths

    def min_cut_side(self, source):
        seen, stack = {source}, [source]
        while stack:
            u = stack.pop()
            for v, c in self.cap[u].items():
                if c > 0 and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen


def main():
    pipes = [("src", "a", 16), ("src", "c", 13), ("a", "b", 12), ("c", "a", 4),
             ("b", "c", 9), ("c", "d", 14), ("d", "b", 7), ("b", "sink", 20),
             ("d", "sink", 4)]
    net = FlowNetwork()
    for u, v, c in pipes:
        net.add_edge(u, v, c)
    flow, paths = net.max_flow("src", "sink")
    for i, (path, amount) in enumerate(paths, 1):
        print(f"Augment {i}: {' -> '.join(path)} (+{amount})")
    print("Maximum flow:", flow)
    side = net.min_cut_side("src")
    cut = [(u, v, c) for u, v, c in pipes if u in side and v not in side]
    print("Source side of min cut:", sorted(side))
    print("Cut edges:", cut, "capacity", sum(c for *_, c in cut))


if __name__ == "__main__":
    main()
