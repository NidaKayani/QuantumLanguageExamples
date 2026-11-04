"""Examine floating-point representation, rounding errors and safe comparisons."""

import math

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("isclose:", math.isclose(0.1 + 0.2, 0.3))
print("repr(0.1):", repr(0.1), "| 17 digits:", f"{0.1:.17f}")
print("as_integer_ratio(0.1):", (0.1).as_integer_ratio())
print("hex(0.1):", (0.1).hex())

total = sum([0.1] * 10)
print("sum of ten 0.1:", total, "| fsum:", math.fsum([0.1] * 10))

print("float info: max", 1.7976931348623157e308, "| eps", 2.220446049250313e-16)
print("1.0 + eps/2 == 1.0:", 1.0 + 2.220446049250313e-16 / 2 == 1.0)

inf = float("inf")
nan = float("nan")
print("inf:", inf, -inf, "inf > 1e308:", inf > 1e308)
print("inf - inf:", inf - inf, "| nan == nan:", nan == nan, "| isnan:", math.isnan(nan))
print("isinf:", math.isinf(inf), "| isfinite(1e308):", math.isfinite(1e308))

print("1e16 + 1 - 1e16 =", 1e16 + 1 - 1e16)
print("large then small:", (1e20 + 1.0) - 1e20)

print("is_integer:", (3.0).is_integer(), (3.5).is_integer())
print("ulp(1.0):", math.ulp(1.0), "| nextafter:", math.nextafter(1.0, 2.0))

print("int(3.99):", int(3.99), "| int(-3.99):", int(-3.99))
print("trunc/floor/ceil of -2.5:", math.trunc(-2.5), math.floor(-2.5), math.ceil(-2.5))

for tol in (1e-9, 1e-3):
    print(f"isclose(1.0, 1.0001, rel_tol={tol}):", math.isclose(1.0, 1.0001, rel_tol=tol))
print("abs_tol near zero:", math.isclose(1e-12, 0.0), math.isclose(1e-12, 0.0, abs_tol=1e-9))
