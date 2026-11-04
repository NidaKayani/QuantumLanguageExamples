"""Bellman-Ford shortest paths with negative edges and negative-cycle detection."""
from typing import NamedTuple


class Edge(NamedTuple):
    src: str
    dst: str
    weight: int


def bellman_ford(nodes, edges, source):
    dist = dict.fromkeys(nodes, float("inf"))
    pred = dict.fromkeys(nodes)
    dist[source] = 0
    for _ in range(len(nodes) - 1):
        changed = False
        for e in edges:
            if dist[e.src] + e.weight < dist[e.dst]:
                dist[e.dst] = dist[e.src] + e.weight
                pred[e.dst] = e.src
                changed = True
        if not changed:
            break
    cycle_edges = [e for e in edges if dist[e.src] + e.weight < dist[e.dst]]
    return dist, pred, cycle_edges


def run(title, nodes, edges, source):
    print(f"== {title} ==")
    dist, pred, bad = bellman_ford(nodes, edges, source)
    if bad:
        print("Negative cycle detected via edges:",
              ", ".join(f"{e.src}->{e.dst}({e.weight})" for e in bad))
        return
    for n in nodes:
        chain, cur = [], n
        while cur is not None:
            chain.append(cur)
            cur = pred[cur]
        d = dist[n]
        shown = "unreachable" if d == float("inf") else str(d)
        print(f"  {n}: {shown:>11}  via {'<-'.join(chain)}")


def main():
    nodes = ["S", "A", "B", "C", "D", "E"]
    edges = [Edge("S", "A", 10), Edge("S", "E", 8), Edge("E", "D", 1),
             Edge("D", "A", -4), Edge("D", "C", -1), Edge("A", "C", 2),
             Edge("C", "B", -2), Edge("B", "A", 1)]
    run("Graph with negative edges", nodes, edges, "S")
    edges_cycle = edges + [Edge("A", "D", 1)]
    run("Graph with a negative cycle", nodes, edges_cycle, "S")
    run("Disconnected node", nodes + ["Z"], edges, "S")
    print("Edge example:", edges[0], "weight field =", edges[0].weight)


if __name__ == "__main__":
    main()
