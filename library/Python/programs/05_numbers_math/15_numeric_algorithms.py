"""Implement classic numeric algorithms: Newton's method, bisection, and integration."""

import math


def newton_sqrt(x, tol=1e-12):
    guess = x / 2 or 1.0
    steps = 0
    while abs(guess * guess - x) > tol * max(1, x):
        guess = (guess + x / guess) / 2
        steps += 1
    return guess, steps


def bisection(f, lo, hi, tol=1e-10):
    if f(lo) * f(hi) > 0:
        raise ValueError("root not bracketed")
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def simpson(f, a, b, n=100):
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += f(a + i * h) * (4 if i % 2 else 2)
    return total * h / 3


def trapezoid(f, a, b, n=100):
    h = (b - a) / n
    return h * (sum(f(a + i * h) for i in range(1, n)) + (f(a) + f(b)) / 2)


for x in (2, 10, 12345):
    root, steps = newton_sqrt(x)
    print(f"sqrt({x}) ~ {root:.10f} in {steps} steps (math: {math.sqrt(x):.10f})")

root = bisection(lambda t: t ** 3 - t - 2, 1, 2)
print(f"root of t^3 - t - 2: {root:.8f}")
print(f"cos(t) = t at {bisection(lambda t: math.cos(t) - t, 0, 1):.8f}")

print(f"integral of sin on [0, pi]: simpson={simpson(math.sin, 0, math.pi):.10f} trap={trapezoid(math.sin, 0, math.pi):.10f}")
print(f"integral of x^2 on [0, 3]: {simpson(lambda x: x * x, 0, 3):.6f}")
print(f"pi via integral of 4/(1+x^2): {simpson(lambda x: 4 / (1 + x * x), 0, 1):.12f}")

e_series = sum(1 / math.factorial(k) for k in range(20))
print(f"e via series: {e_series:.15f} (error {abs(e_series - math.e):.1e})")
leibniz = 4 * sum((-1) ** k / (2 * k + 1) for k in range(10000))
print(f"pi via Leibniz (10000 terms): {leibniz:.8f}")
