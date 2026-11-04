"""Tarjan's strongly connected components and the condensation DAG."""
from collections import defaultdict


def tarjan(graph):
    index_of, low = {}, {}
    on_stack, stack = set(), []
    sccs = []
    counter = 0

    def strongconnect(v):
        nonlocal counter
        index_of[v] = low[v] = counter
        counter += 1
        stack.append(v)
        on_stack.add(v)
        for w in graph.get(v, ()):
            if w not in index_of:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index_of[w])
        if low[v] == index_of[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.discard(w)
                comp.append(w)
                if w == v:
                    break
            sccs.append(sorted(comp))

    for v in graph:
        if v not in index_of:
            strongconnect(v)
    return sccs


def condensation(graph, sccs):
    comp_of = {v: i for i, comp in enumerate(sccs) for v in comp}
    dag = defaultdict(set)
    for u, targets in graph.items():
        for v in targets:
            if comp_of[u] != comp_of[v]:
                dag[comp_of[u]].add(comp_of[v])
    return comp_of, dag


def main():
    graph = {
        "a": ["b"], "b": ["c", "e", "f"], "c": ["d", "g"], "d": ["c", "h"],
        "e": ["a", "f"], "f": ["g"], "g": ["f"], "h": ["d", "g"],
    }
    sccs = tarjan(graph)
    print(f"{len(sccs)} strongly connected components:")
    for i, comp in enumerate(sccs):
        print(f"  C{i}: {{{', '.join(comp)}}}")
    comp_of, dag = condensation(graph, sccs)
    print("Condensation edges:")
    for src in sorted(dag):
        print(f"  C{src} -> {', '.join(f'C{t}' for t in sorted(dag[src]))}")
    sinks = [i for i in range(len(sccs)) if not dag.get(i)]
    print("Sink components:", [sccs[i] for i in sinks])
    print("a and e strongly connected:", comp_of["a"] == comp_of["e"])
    print("a and g strongly connected:", comp_of["a"] == comp_of["g"])


if __name__ == "__main__":
    main()
