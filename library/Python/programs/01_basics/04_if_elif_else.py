"""Classify values with if/elif/else chains and nested conditions."""


def grade(score):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter


def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0


def classify_number(n):
    if n == 0:
        return "zero"
    sign = "positive" if n > 0 else "negative"
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return f"{sign} {parity}"


for s in (95, 83, 71, 64, 12, 100):
    print(f"score {s:3d} -> {grade(s)}")

for y in (1900, 2000, 2023, 2024):
    print(f"{y}: {'leap' if leap_year(y) else 'common'} year")

for n in (0, 7, -4, 12, -9):
    print(f"{n:>3} is {classify_number(n)}")

# truthiness of common values
for value in (0, 1, "", "x", [], [0], None, 0.0):
    if value:
        print(f"{value!r} is truthy")
    else:
        print(f"{value!r} is falsy")
