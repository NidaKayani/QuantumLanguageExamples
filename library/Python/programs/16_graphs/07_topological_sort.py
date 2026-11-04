"""Topological sort of a build dependency graph with Kahn's algorithm and DFS."""
from collections import deque, defaultdict

DEPENDS_ON = {
    "app": ["ui", "network", "storage"],
    "ui": ["widgets", "theme"],
    "widgets": ["core"],
    "theme": ["core"],
    "network": ["core", "crypto"],
    "storage": ["core"],
    "crypto": ["core"],
    "core": [],
    "tests": ["app"],
}


def kahn(deps):
    indegree = {node: len(reqs) for node, reqs in deps.items()}
    dependents = defaultdict(list)
    for node, reqs in deps.items():
        for r in reqs:
            dependents[r].append(node)
    ready = deque(sorted(n for n, d in indegree.items() if d == 0))
    order = []
    while ready:
        node = ready.popleft()
        order.append(node)
        for nxt in sorted(dependents[node]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
    if len(order) != len(deps):
        raise ValueError("cycle detected")
    return order


def dfs_order(deps):
    state, order = {}, []

    def visit(node):
        if state.get(node) == "done":
            return
        if state.get(node) == "active":
            raise ValueError(f"cycle through {node}")
        state[node] = "active"
        for r in deps[node]:
            visit(r)
        state[node] = "done"
        order.append(node)

    for node in sorted(deps):
        visit(node)
    return order


def build_stages(deps):
    stage = {}
    for node in kahn(deps):
        stage[node] = 1 + max((stage[r] for r in deps[node]), default=0)
    stages = defaultdict(list)
    for node, s in stage.items():
        stages[s].append(node)
    return dict(stages)


def main():
    print("Kahn order:", " -> ".join(kahn(DEPENDS_ON)))
    print("DFS order: ", " -> ".join(dfs_order(DEPENDS_ON)))
    for s, nodes in sorted(build_stages(DEPENDS_ON).items()):
        print(f"Stage {s}: {', '.join(sorted(nodes))}")
    cyclic = dict(DEPENDS_ON, core=["tests"])
    try:
        kahn(cyclic)
    except ValueError as exc:
        print("Kahn on cyclic graph:", exc)
    try:
        dfs_order(cyclic)
    except ValueError as exc:
        print("DFS on cyclic graph:", exc)


if __name__ == "__main__":
    main()
