"""Ternary search for the extremum of unimodal functions."""

import math


def ternary_max_int(f, lo, hi):
    while hi - lo > 2:
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        if f(m1) < f(m2):
            lo = m1 + 1
        else:
            hi = m2 - 1
    return max(range(lo, hi + 1), key=f)


def ternary_min_real(f, lo, hi, eps=1e-9):
    iterations = 0
    while hi - lo > eps:
        iterations += 1
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) > f(m2):
            lo = m1
        else:
            hi = m2
    return (lo + hi) / 2, iterations


def golden_section_min(f, lo, hi, tol=1e-9):
    phi = (math.sqrt(5) - 1) / 2
    c, d = hi - phi * (hi - lo), lo + phi * (hi - lo)
    while abs(hi - lo) > tol:
        if f(c) < f(d):
            hi, d = d, c
            c = hi - phi * (hi - lo)
        else:
            lo, c = c, d
            d = lo + phi * (hi - lo)
    return (lo + hi) / 2


peak = [1, 3, 8, 12, 17, 20, 19, 15, 9, 4, 2]
idx = ternary_max_int(lambda i: peak[i], 0, len(peak) - 1)
print(f"peak of mountain array at index {idx} value {peak[idx]}")

revenue = lambda price: price * (200 - 2 * price)
best_price = ternary_max_int(revenue, 0, 100)
print(f"best integer price {best_price} gives revenue {revenue(best_price)}")

parabola = lambda x: (x - 2.5) ** 2 + 1
x, iters = ternary_min_real(parabola, -10, 10)
print(f"min of (x-2.5)^2+1 at x={x:.6f} after {iters} iterations")

curve = lambda x: x ** 4 - 3 * x ** 3 + 2
x, _ = ternary_min_real(curve, 0, 5)
print(f"min of x^4-3x^3+2 on [0,5]: x={x:.6f}, f={curve(x):.6f} (exact 9/4={9/4})")
print(f"golden section agrees: {golden_section_min(curve, 0, 5):.6f}")

points = [(1, 2), (3, 1), (4, 5), (7, 3)]
dist_sum = lambda x: sum(math.hypot(x - px, py) for px, py in points)
x, _ = ternary_min_real(dist_sum, 0, 10)
print(f"pipeline position on x-axis minimizing total distance: {x:.4f}")
