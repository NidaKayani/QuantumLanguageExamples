"""Introduce variables of several types and print them with f-strings."""

name = "Ada"
age = 36
height_m = 1.68
is_programmer = True
languages = ["Python", "C", "Haskell"]

print("Hello, world!")
print(f"Name: {name}")
print(f"Age: {age} (next year {age + 1})")
print(f"Height: {height_m:.2f} m = {height_m * 100:.0f} cm")
print(f"Programmer? {is_programmer}")
print(f"Knows {len(languages)} languages: {', '.join(languages)}")

# multiple assignment and swapping
x, y = 10, 20
print(f"before swap: x={x}, y={y}")
x, y = y, x
print(f"after swap:  x={x}, y={y}")

# chained assignment
a = b = c = 0
a += 1
b += 2
c += 3
print(f"a={a} b={b} c={c}")

# type inspection
for value in (name, age, height_m, is_programmer, languages, None):
    print(f"{value!r:>28} -> {type(value).__name__}")

# self-documenting f-string expressions
total = age * 12
print(f"{total=}")
print(f"{name.upper()=}")
