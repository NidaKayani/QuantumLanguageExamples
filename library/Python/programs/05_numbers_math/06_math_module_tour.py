"""Tour the math module: constants, roots, logs, trig and combinatorics."""

import math

print(f"pi={math.pi:.10f} e={math.e:.10f} tau={math.tau:.6f}")
print("sqrt(2):", math.sqrt(2), "| isqrt(99):", math.isqrt(99), "| cbrt(27):", math.cbrt(27))
print("hypot(3, 4):", math.hypot(3, 4), "| dist:", math.dist((1, 1), (4, 5)))
print("exp(1):", math.exp(1), "| log(e):", math.log(math.e))
print("log10(1000):", math.log10(1000), "| log2(1024):", math.log2(1024), "| log(8, 2):", math.log(8, 2))
print("factorial(10):", math.factorial(10), "| comb(10, 3):", math.comb(10, 3), "| perm(5, 2):", math.perm(5, 2))
print("gcd(84, 36, 120):", math.gcd(84, 36, 120), "| lcm(4, 6, 10):", math.lcm(4, 6, 10))
print("prod([1..6]):", math.prod(range(1, 7)), "| fsum:", math.fsum([0.1] * 3))
print("copysign(3, -0.0):", math.copysign(3, -0.0), "| fabs(-4):", math.fabs(-4))
print("fmod(-7, 3):", math.fmod(-7, 3), "vs -7 % 3:", -7 % 3)
print("modf(3.75):", math.modf(3.75), "| frexp(8.0):", math.frexp(8.0), "| ldexp(0.5, 4):", math.ldexp(0.5, 4))

print("\nangle  sin      cos      tan")
for deg in (0, 30, 45, 60, 90):
    rad = math.radians(deg)
    tan = "inf" if deg == 90 else f"{math.tan(rad):.4f}"
    print(f"{deg:>5}  {math.sin(rad):.4f}   {math.cos(rad):.4f}   {tan}")

print("\natan2(1, -1) in degrees:", math.degrees(math.atan2(1, -1)))
print("asin(1) == pi/2:", math.isclose(math.asin(1), math.pi / 2))
print("sinh/cosh identity:", math.isclose(math.cosh(2) ** 2 - math.sinh(2) ** 2, 1.0))
print("gamma(5):", math.gamma(5), "| lgamma(10):", round(math.lgamma(10), 6))
print("erf(1):", round(math.erf(1), 6))
