"""Prim's minimum spanning tree with a lazy heap and a dense-matrix O(V^2) variant."""
import heapq

POINTS = {"P0": (0, 0), "P1": (2, 1), "P2": (5, 0), "P3": (1, 4),
          "P4": (4, 4), "P5": (6, 3), "P6": (3, 7)}


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def prim_heap(points, start):
    visited = {start}
    heap = [(manhattan(points[start], p), start, name)
            for name, p in points.items() if name != start]
    heapq.heapify(heap)
    tree = []
    while heap and len(visited) < len(points):
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        tree.append((u, v, w))
        for name, p in points.items():
            if name not in visited:
                heapq.heappush(heap, (manhattan(points[v], p), v, name))
    return tree


def prim_dense(matrix):
    n = len(matrix)
    in_tree = [False] * n
    best = [float("inf")] * n
    parent = [-1] * n
    best[0] = 0
    for _ in range(n):
        u = min((i for i in range(n) if not in_tree[i]), key=lambda i: best[i])
        in_tree[u] = True
        for v in range(n):
            if not in_tree[v] and matrix[u][v] < best[v]:
                best[v], parent[v] = matrix[u][v], u
    return [(parent[v], v, matrix[parent[v]][v]) for v in range(1, n)]


def main():
    tree = prim_heap(POINTS, "P0")
    print("Heap-based Prim (Manhattan metric):")
    for u, v, w in tree:
        print(f"  {u} -- {v}  cost {w}")
    print("  total:", sum(w for _, _, w in tree))

    names = list(POINTS)
    matrix = [[manhattan(POINTS[a], POINTS[b]) for b in names] for a in names]
    dense = prim_dense(matrix)
    print("Dense Prim total:", sum(w for _, _, w in dense))
    edges = sorted(f"{names[u]}-{names[v]}" for u, v, _ in dense)
    print("Dense edges:", edges)
    degree = {n: 0 for n in names}
    for u, v, _ in tree:
        degree[u] += 1
        degree[v] += 1
    leaves = [n for n, d in degree.items() if d == 1]
    print("Leaves of the tree:", leaves)


if __name__ == "__main__":
    main()
