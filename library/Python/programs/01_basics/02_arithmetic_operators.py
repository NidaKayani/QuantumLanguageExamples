"""Demonstrate Python's arithmetic and augmented assignment operators."""

a, b = 17, 5

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# negative operands follow floor semantics
print(f"-17 // 5 = {-17 // 5}")
print(f"-17 % 5 = {-17 % 5}")
print(f"17 % -5 = {17 % -5}")

# operator precedence
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("-2 ** 2 =", -2 ** 2)

# augmented assignment
counter = 100
counter += 5
counter -= 3
counter *= 2
counter //= 7
counter **= 2
counter %= 1000
print("counter:", counter)

# mixing int and float
print("int + float:", 3 + 0.5, type(3 + 0.5).__name__)
print("true division always float:", 10 / 2, type(10 / 2).__name__)

# comparisons can be chained
temperature = 22
print("comfortable:", 18 <= temperature < 25)
print("abs(-7) =", abs(-7), "max:", max(3, 9, 4), "min:", min(3, 9, 4))
