"""Travelling salesman with Held-Karp bitmask DP, checked against brute force."""
from itertools import permutations
from math import dist, inf

CITIES = {
    "Depot": (0, 0), "Alpha": (2, 6), "Bravo": (5, 2), "Charlie": (8, 7),
    "Delta": (6, 9), "Echo": (1, 3), "Foxtrot": (9, 1), "Golf": (4, 5),
}


def held_karp(d):
    n = len(d)
    full = 1 << n
    cost = [[inf] * n for _ in range(full)]
    parent = [[-1] * n for _ in range(full)]
    cost[1][0] = 0
    for mask in range(1, full, 2):
        for last in range(n):
            if not mask & (1 << last) or cost[mask][last] == inf:
                continue
            for nxt in range(1, n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                cand = cost[mask][last] + d[last][nxt]
                if cand < cost[new_mask][nxt]:
                    cost[new_mask][nxt] = cand
                    parent[new_mask][nxt] = last
    final = full - 1
    best_last = min(range(1, n), key=lambda k: cost[final][k] + d[k][0])
    best = cost[final][best_last] + d[best_last][0]
    tour, mask, cur = [], final, best_last
    while cur != -1:
        tour.append(cur)
        mask, cur = mask ^ (1 << cur), parent[mask][cur]
    return best, tour[::-1] + [0]


def brute_force(d):
    n = len(d)
    best = inf
    for perm in permutations(range(1, n)):
        route = (0, *perm, 0)
        best = min(best, sum(d[a][b] for a, b in zip(route, route[1:])))
    return best


def main():
    names = list(CITIES)
    d = [[dist(CITIES[a], CITIES[b]) for b in names] for a in names]
    best, tour = held_karp(d)
    print("Optimal tour:")
    print("  " + " -> ".join(names[i] for i in tour))
    print(f"  length {best:.4f}")
    legs = [(names[a], names[b], d[a][b]) for a, b in zip(tour, tour[1:])]
    for a, b, w in legs:
        print(f"    {a:>8} -> {b:<8} {w:6.3f}")
    small = [row[:6] for row in d[:6]]
    hk, _ = held_karp(small)
    bf = brute_force(small)
    print(f"First 6 cities: Held-Karp {hk:.4f}, brute force {bf:.4f}, equal={abs(hk - bf) < 1e-9}")


if __name__ == "__main__":
    main()
