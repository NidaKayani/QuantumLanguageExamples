"""The 24 game: combine four numbers with + - * / to make 24, using exact Fractions."""
from fractions import Fraction
from itertools import combinations

OPS = [
    ("+", lambda a, b: a + b, True),
    ("-", lambda a, b: a - b, False),
    ("*", lambda a, b: a * b, True),
    ("/", lambda a, b: a / b if b != 0 else None, False),
]


def solutions(numbers, target=24):
    found = set()

    def search(items):
        if len(items) == 1:
            value, expr = items[0]
            if value == target:
                found.add(expr)
            return
        for i, j in combinations(range(len(items)), 2):
            rest = [items[k] for k in range(len(items)) if k not in (i, j)]
            (a, ea), (b, eb) = items[i], items[j]
            for symbol, fn, commutative in OPS:
                pairs = [((a, ea), (b, eb))] if commutative else [((a, ea), (b, eb)), ((b, eb), (a, ea))]
                for (x, ex), (y, ey) in pairs:
                    result = fn(x, y)
                    if result is not None:
                        search(rest + [(result, f"({ex} {symbol} {ey})")])

    search([(Fraction(n), str(n)) for n in numbers])
    return sorted(found, key=lambda e: (len(e), e))


def strip_outer(expr):
    return expr[1:-1] if expr.startswith("(") and expr.endswith(")") else expr


hands = [(4, 7, 8, 8), (1, 5, 5, 5), (3, 3, 8, 8), (1, 1, 1, 1), (6, 6, 6, 6), (2, 3, 4, 5)]
for hand in hands:
    sols = solutions(hand)
    if sols:
        shown = "; ".join(strip_outer(s) for s in sols[:3])
        print(f"{hand}: {len(sols):>3} expressions, e.g. {shown}")
    else:
        print(f"{hand}: impossible")

hands = list(combinations(range(1, 8), 4))
solvable = [h for h in hands if solutions(h)]
print(f"Hands of four distinct digits 1-7 that make 24: {len(solvable)} of {len(hands)}")
print("Unsolvable ones:", [h for h in hands if h not in solvable])
