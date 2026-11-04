"""Comprehensions with filters, conditional expressions, multiple conditions and the walrus operator."""

readings = [21.5, None, 22.1, -999, 23.8, 24.0, None, 19.2, 35.7, 22.9]

valid = [r for r in readings if r is not None and -50 < r < 60]
print("valid readings:", valid)

flags = ["missing" if r is None else "error" if r == -999 else "hot" if r > 30 else "ok"
         for r in readings]
print("flags:", flags)

filled = [r if r is not None and r != -999 else round(sum(valid) / len(valid), 2) for r in readings]
print("filled:", filled)

fizzbuzz = ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n)
            for n in range(1, 21)]
print("fizzbuzz:", " ".join(fizzbuzz))

nums = range(1, 40)
print("divisible by 2 and 3, not 4:", [n for n in nums if n % 2 == 0 if n % 3 == 0 if n % 4])


def expensive(n):
    return (n * 37 + 11) % 23


scores = [(n, s) for n in range(15) if (s := expensive(n)) > 15]
print("walrus avoids recomputing:", scores)

users = [
    {"name": "ann", "age": 31, "email": "ann@x.io", "active": True},
    {"name": "bob", "age": 17, "email": None, "active": True},
    {"name": "cat", "age": 45, "email": "cat@y.io", "active": False},
    {"name": "dan", "age": 22, "email": "dan@x.io", "active": True},
]
mailing = [u["email"] for u in users if u["active"] and u["email"] and u["age"] >= 18]
print("mailing list:", mailing)
status = {u["name"]: ("adult" if u["age"] >= 18 else "minor") + ("" if u["active"] else " (inactive)")
          for u in users}
print("status:", status)

words = ["level", "python", "radar", "noon", "data", "civic", "a"]
print("palindromes > 1 char:", [w for w in words if len(w) > 1 and w == w[::-1]])
print("vowel-masked:", ["".join("*" if c in "aeiou" else c for c in w) for w in words[:4]])

grid = [[3, -1, 4], [-1, 5, -9], [2, -6, 5]]
print("negatives zeroed:", [[x if x > 0 else 0 for x in row] for row in grid])
print("rows with positive sum:", [row for row in grid if sum(row) > 0])
