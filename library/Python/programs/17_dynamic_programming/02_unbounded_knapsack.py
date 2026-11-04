"""Unbounded knapsack: filling a cargo hold with unlimited crate types."""
from collections import Counter

CRATES = {"small": (2, 3), "medium": (3, 5), "large": (7, 12), "odd": (5, 8)}


def unbounded(crates, capacity):
    best = [0] * (capacity + 1)
    pick = [None] * (capacity + 1)
    for cap in range(1, capacity + 1):
        best[cap] = best[cap - 1]
        pick[cap] = None
        for name, (weight, value) in crates.items():
            if weight <= cap and best[cap - weight] + value > best[cap]:
                best[cap] = best[cap - weight] + value
                pick[cap] = name
    return best, pick


def reconstruct(pick, crates, cap):
    used = Counter()
    while cap > 0:
        name = pick[cap]
        if name is None:
            cap -= 1
            continue
        used[name] += 1
        cap -= crates[name][0]
    return used


def main():
    best, pick = unbounded(CRATES, 30)
    print("Crate types (weight, value):")
    for name, (w, v) in CRATES.items():
        print(f"  {name:<7} w={w} v={v} ratio={v / w:.3f}")
    for cap in (6, 11, 17, 23, 30):
        used = reconstruct(pick, CRATES, cap)
        detail = ", ".join(f"{n} x{k}" for n, k in sorted(used.items()))
        weight = sum(CRATES[n][0] * k for n, k in used.items())
        print(f"Capacity {cap:2d}: value {best[cap]:2d} using {weight:2d} -> {detail}")
    gains = [best[c] - best[c - 1] for c in range(1, len(best))]
    print("Marginal gains:", gains)
    print("Capacities with zero gain:", [c for c, g in enumerate(gains, 1) if g == 0])


if __name__ == "__main__":
    main()
