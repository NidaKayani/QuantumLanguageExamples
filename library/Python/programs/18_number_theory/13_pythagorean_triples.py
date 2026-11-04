"""Pythagorean triples via Euclid's formula and the Berggren ternary tree."""
from collections import Counter, deque
from math import gcd, isqrt
from typing import NamedTuple


class Triple(NamedTuple):
    a: int
    b: int
    c: int

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def normalized(self):
        return Triple(*sorted(self))


def euclid_primitives(limit_c):
    out = []
    for m in range(2, isqrt(limit_c) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                c = m * m + n * n
                if c <= limit_c:
                    out.append(Triple(m * m - n * n, 2 * m * n, c).normalized())
    return sorted(out, key=lambda t: (t.c, t.a))


BERGGREN = (
    ((1, -2, 2), (2, -1, 2), (2, -2, 3)),
    ((1, 2, 2), (2, 1, 2), (2, 2, 3)),
    ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3)),
)


def berggren(limit_c):
    found, queue = [], deque([Triple(3, 4, 5)])
    while queue:
        t = queue.popleft()
        if t.c > limit_c:
            continue
        found.append(t.normalized())
        for matrix in BERGGREN:
            queue.append(Triple(*(sum(r * v for r, v in zip(row, t)) for row in matrix)))
    return sorted(found, key=lambda t: (t.c, t.a))


def main():
    prims = euclid_primitives(100)
    print(f"{len(prims)} primitive triples with c <= 100:")
    for t in prims:
        print(f"  {t.a:>3}^2 + {t.b:>3}^2 = {t.c:>3}^2")
    print("Berggren tree gives the same set:", berggren(100) == prims)
    perims = Counter()
    for t in euclid_primitives(1000):
        for k in range(1, 1000 // t.perimeter + 1):
            perims[k * t.perimeter] += 1
    best, ways = max(perims.items(), key=lambda kv: (kv[1], -kv[0]))
    print(f"Perimeter <= 1000 with most right triangles: {best} ({ways} ways)")
    special = next(Triple(k * t.a, k * t.b, k * t.c) for t in euclid_primitives(1000)
                   for k in range(1, 100) if k * t.perimeter == 1000)
    print("Triple with a+b+c = 1000:", special, "product", special.a * special.b * special.c)


if __name__ == "__main__":
    main()
