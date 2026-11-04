"""Floyd-Warshall all-pairs shortest paths with path reconstruction."""
from itertools import product

INF = float("inf")
NAMES = ["W", "X", "Y", "Z", "Q"]
WEIGHTS = {
    ("W", "X"): 3, ("W", "Z"): 7, ("X", "W"): 8, ("X", "Y"): 2,
    ("Y", "W"): 5, ("Y", "Z"): 1, ("Z", "W"): 2, ("Z", "Q"): 4,
    ("Q", "X"): 6,
}


def floyd_warshall(names, weights):
    n = len(names)
    idx = {name: i for i, name in enumerate(names)}
    dist = [[0 if i == j else INF for j in range(n)] for i in range(n)]
    nxt = [[None] * n for _ in range(n)]
    for (a, b), w in weights.items():
        i, j = idx[a], idx[b]
        dist[i][j] = w
        nxt[i][j] = j
    for i in range(n):
        nxt[i][i] = i
    for k, i, j in product(range(n), repeat=3):
        if dist[i][k] + dist[k][j] < dist[i][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
            nxt[i][j] = nxt[i][k]
    return dist, nxt


def route(nxt, names, i, j):
    if nxt[i][j] is None:
        return []
    path = [i]
    while i != j:
        i = nxt[i][j]
        path.append(i)
    return [names[p] for p in path]


def main():
    dist, nxt = floyd_warshall(NAMES, WEIGHTS)
    print("Distance matrix:")
    print("     " + "".join(f"{n:>5}" for n in NAMES))
    for name, row in zip(NAMES, dist):
        cells = "".join(f"{'inf' if d == INF else d:>5}" for d in row)
        print(f"{name:>5}{cells}")
    print("Selected routes:")
    for a, b in [("W", "Y"), ("Q", "Z"), ("Y", "Q"), ("X", "W")]:
        i, j = NAMES.index(a), NAMES.index(b)
        print(f"  {a}->{b}: {'-'.join(route(nxt, NAMES, i, j))} cost {dist[i][j]}")
    ecc = {NAMES[i]: max(row) for i, row in enumerate(dist)}
    center = min(ecc, key=ecc.get)
    print("Eccentricities:", ecc)
    print("Graph center:", center, "radius", ecc[center], "diameter", max(ecc.values()))


if __name__ == "__main__":
    main()
