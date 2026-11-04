"""2D lattice random walks with a hand-written LCG, measuring distance and return statistics."""
import math
from collections import Counter


def lcg(seed, a=6364136223846793005, c=1442695040888963407, m=2**64):
    while True:
        seed = (a * seed + c) % m
        yield seed >> 33


STEPS = {0: (1, 0), 1: (-1, 0), 2: (0, 1), 3: (0, -1)}


def walk(rng, n):
    x = y = 0
    visited = {(0, 0)}
    returned = False
    for _ in range(n):
        dx, dy = STEPS[next(rng) % 4]
        x, y = x + dx, y + dy
        visited.add((x, y))
        returned = returned or (x, y) == (0, 0)
    return (x, y), len(visited), returned


rng = lcg(2024)
for n in (10, 100, 400, 1600):
    results = [walk(rng, n) for _ in range(150)]
    rms = math.sqrt(sum(px * px + py * py for (px, py), _, _ in results) / len(results))
    distinct = sum(v for _, v, _ in results) / len(results)
    back = sum(r for _, _, r in results) / len(results)
    print(f"n={n:>5}: RMS distance {rms:7.2f} (sqrt(n)={math.sqrt(n):6.2f}), "
          f"distinct sites {distinct:7.1f}, returned to origin {back:5.1%}")

rng = lcg(99)
quadrants = Counter()
for _ in range(400):
    (x, y), _, _ = walk(rng, 50)
    key = ("E" if x > 0 else "W" if x < 0 else "-") + ("N" if y > 0 else "S" if y < 0 else "-")
    quadrants[key] += 1
print("Endpoint regions after 50 steps:", sorted(quadrants.items()))

path = []
pos = (0, 0)
rng = lcg(5)
for _ in range(12):
    dx, dy = STEPS[next(rng) % 4]
    pos = (pos[0] + dx, pos[1] + dy)
    path.append(pos)
print("Sample path:", " -> ".join(f"({x},{y})" for x, y in path))
