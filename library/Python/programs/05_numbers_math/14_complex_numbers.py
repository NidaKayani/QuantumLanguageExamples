"""Compute with complex numbers using built-in complex and polar conversions."""

import math

z = 3 + 4j
w = complex(1, -2)
print("z =", z, "| w =", w)
print("real, imag:", z.real, z.imag)
print("abs(z):", abs(z), "| conjugate:", z.conjugate())
print("z + w =", z + w, "| z * w =", z * w, "| z / w =", z / w)
print("z ** 2 =", z ** 2, "| 1j ** 2 =", 1j ** 2)


def polar(c):
    return abs(c), math.atan2(c.imag, c.real)


def rect(r, phi):
    return complex(r * math.cos(phi), r * math.sin(phi))


def cexp(c):
    return math.exp(c.real) * complex(math.cos(c.imag), math.sin(c.imag))


r, phi = polar(z)
print(f"polar: r={r}, phi={phi:.4f} rad ({math.degrees(phi):.2f} deg)")
back = rect(r, phi)
print(f"rect back: ({back.real:.6f}, {back.imag:.6f})")

root = (-4) ** 0.5
print(f"(-4) ** 0.5 = {root.real:.1f}{root.imag:+.1f}j, type {type(root).__name__}")
euler = cexp(1j * math.pi) + 1
print(f"e^(i*pi) + 1 = ({euler.real:.1f}, {abs(euler.imag) < 1e-15})")


def solve_quadratic(a, b, c):
    d = complex(b * b - 4 * a * c) ** 0.5
    return (-b + d) / (2 * a), (-b - d) / (2 * a)


for coeffs in ((1, -3, 2), (1, 2, 5), (1, 0, 1)):
    r1, r2 = solve_quadratic(*coeffs)
    print(f"roots of {coeffs}: {r1:.3f}, {r2:.3f}")

n = 6
roots = [cexp(2j * math.pi * k / n) for k in range(n)]
print("6th roots of unity:", [f"{c.real:+.2f}{c.imag:+.2f}j" for c in roots])
print("sum of roots ~ 0:", abs(sum(roots)) < 1e-12)
print("complex('2-3j'):", complex("2-3j"), "| roots[3] ~ -1:", abs(roots[3] + 1) < 1e-12)
mandel = []
for c in (0, -1, 1j, 1, 0.5 + 0.5j):
    zz, steps = 0, 0
    while abs(zz) <= 2 and steps < 50:
        zz = zz * zz + c
        steps += 1
    mandel.append((c, steps == 50))
print("in Mandelbrot set:", mandel)
