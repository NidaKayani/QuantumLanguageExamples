"""Scoping rules of comprehensions: isolated loop variables, walrus leakage, and class-body gotchas."""

x = "outer"
squares = [x * x for x in range(5)]
print("comprehension result:", squares, "| x is still:", x)

total = 0
running = [total := total + n for n in range(1, 6)]
print("walrus running totals:", running, "| total leaked out:", total)

data = [3, 8, 1, 9, 4]
if any((big := n) > 7 for n in data):
    print("first value > 7 found via walrus:", big)


class Config:
    factor = 10
    values = [1, 2, 3]
    scaled = [v * 2 for v in values]  # 'values' is the iterable: evaluated in class scope
    # [v * factor for v in values] would raise NameError: class scope is skipped inside


print("class comprehension:", Config.scaled)


class Fixed:
    factor = 10
    values = [1, 2, 3]
    scaled = [v * f for v, f in zip(values, [factor] * len(values))]  # outermost iterable sees class scope


print("class-scope workaround:", Fixed.scaled)


def make_tables():
    return {n: [n * i for i in range(1, 4)] for n in range(2, 5)}


print("function-scope nested comprehension:", make_tables())

funcs = [lambda: i for i in range(3)]
print("closures in comprehension share the variable:", [f() for f in funcs])
funcs = [lambda i=i: i for i in range(3)]
print("default-arg capture:", [f() for f in funcs])

matrix = [[(r, c) for c in range(3)] for r in range(2)]
print("inner comprehension sees outer var:", matrix)

first_line = [line for line in ["", "  ", "hello", "world"] if line.strip()][0]
print("first non-blank line:", first_line)
seen = set()
dedup = [w for w in "b a c a b d".split() if not (w in seen or seen.add(w))]
print("order-preserving dedup:", dedup)
