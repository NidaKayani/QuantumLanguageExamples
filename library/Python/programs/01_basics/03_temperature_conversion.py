"""Convert temperatures between scales using functions and a formatted table."""


def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius):
    return celsius + 273.15


def describe(celsius):
    if celsius <= 0:
        return "freezing"
    elif celsius < 15:
        return "cold"
    elif celsius < 25:
        return "mild"
    elif celsius < 35:
        return "warm"
    else:
        return "hot"


print(f"{'C':>6} {'F':>8} {'K':>8}  feel")
print("-" * 32)
for c in range(-10, 46, 8):
    print(f"{c:>6} {c_to_f(c):>8.1f} {c_to_k(c):>8.2f}  {describe(c)}")

print()
for f in (32, 98.6, 212, -40):
    print(f"{f}F is {f_to_c(f):.2f}C")

# the one point where the scales agree
t = -40
assert c_to_f(t) == t
print(f"Celsius and Fahrenheit meet at {t} degrees")
