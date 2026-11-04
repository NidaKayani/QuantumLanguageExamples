"""Instances that act like functions via __call__, keeping state between calls."""


class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = coefficients  # highest degree first

    def __call__(self, x):
        result = 0
        for c in self.coefficients:
            result = result * x + c
        return result

    def __repr__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i, c in enumerate(self.coefficients):
            power = degree - i
            if c == 0:
                continue
            if power == 0:
                terms.append(f"{c}")
            elif power == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{power}")
        return " + ".join(terms).replace("+ -", "- ")


class RunningStats:
    def __init__(self):
        self.count = 0
        self.total = 0
        self.maximum = None

    def __call__(self, value):
        self.count += 1
        self.total += value
        self.maximum = value if self.maximum is None else max(self.maximum, value)
        return self.total / self.count


p = Polynomial(2, -3, 0, 5)
print("p(x) =", p)
print("values:", [p(x) for x in range(-2, 4)])
print("callable(p):", callable(p))
print("map with callable object:", list(map(Polynomial(1, 1), [1, 2, 3])))

stats = RunningStats()
for v in [4, 8, 15, 16, 23, 42]:
    print(f"after {v:>2}: mean={stats(v):.3f}")
print(f"count={stats.count} total={stats.total} max={stats.maximum}")
print("sorted by callable key:", sorted([3, -1, 2, -4], key=Polynomial(1, 0, 0)))
