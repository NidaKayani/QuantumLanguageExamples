"""Build adjacency list, adjacency matrix and edge list views of the same graph."""
from collections import defaultdict

EDGES = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("E", "A")]


def adjacency_list(edges, directed=False):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return {k: sorted(vs) for k, vs in sorted(adj.items())}


def adjacency_matrix(edges, directed=False):
    nodes = sorted({n for e in edges for n in e})
    index = {n: i for i, n in enumerate(nodes)}
    matrix = [[0] * len(nodes) for _ in nodes]
    for u, v in edges:
        matrix[index[u]][index[v]] = 1
        if not directed:
            matrix[index[v]][index[u]] = 1
    return nodes, matrix


def degrees(adj):
    return {node: len(neigh) for node, neigh in adj.items()}


def main():
    undirected = adjacency_list(EDGES)
    print("Undirected adjacency list:")
    for node, neigh in undirected.items():
        print(f"  {node}: {', '.join(neigh)}")

    directed = adjacency_list(EDGES, directed=True)
    print("Directed adjacency list:")
    for node, neigh in directed.items():
        print(f"  {node} -> {neigh}")

    nodes, matrix = adjacency_matrix(EDGES)
    print("Adjacency matrix:")
    print("    " + " ".join(nodes))
    for name, row in zip(nodes, matrix):
        print(f"  {name} " + " ".join(str(x) for x in row))

    symmetric = all(matrix[i][j] == matrix[j][i]
                    for i in range(len(nodes)) for j in range(len(nodes)))
    print("Matrix symmetric:", symmetric)
    deg = degrees(undirected)
    print("Degrees:", deg)
    print("Sum of degrees:", sum(deg.values()), "= 2 * edges:", 2 * len(EDGES))
    max_node = max(deg, key=lambda n: (deg[n], n))
    print("Highest degree node:", max_node)


if __name__ == "__main__":
    main()
