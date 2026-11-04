"""Objects made callable with __call__: polynomials, accumulators and configurable validators."""
from functools import reduce


class Polynomial:
    def __init__(self, *coeffs):
        """Coefficients from highest degree to constant term."""
        self.coeffs = list(coeffs)

    def __call__(self, x):
        return reduce(lambda acc, c: acc * x + c, self.coeffs, 0)

    def derivative(self):
        n = len(self.coeffs) - 1
        return Polynomial(*[c * (n - i) for i, c in enumerate(self.coeffs[:-1])])

    def __repr__(self):
        n = len(self.coeffs) - 1
        terms = []
        for i, c in enumerate(self.coeffs):
            power = n - i
            if c == 0:
                continue
            var = "" if power == 0 else "x" if power == 1 else f"x^{power}"
            terms.append(f"{c}{var}")
        return " + ".join(terms).replace("+ -", "- ") or "0"


class RunningStats:
    def __init__(self):
        self.n = 0
        self.total = 0.0
        self.low = float("inf")
        self.high = float("-inf")

    def __call__(self, value):
        self.n += 1
        self.total += value
        self.low = min(self.low, value)
        self.high = max(self.high, value)
        return self.total / self.n


class Range:
    def __init__(self, low, high):
        self.low, self.high = low, high

    def __call__(self, value):
        return self.low <= value <= self.high


p = Polynomial(2, -3, 0, 5)
print("p(x) =", p)
print("values:", [p(x) for x in range(-2, 3)])
dp = p.derivative()
print("p'(x) =", dp, "| p'(2) =", dp(2), "| p''(x) =", dp.derivative())

x = 2.0
for _ in range(6):
    x -= p(x) / dp(x)
print(f"Newton root of p: {x:.6f} (p(x)={p(x):.2e})")

stats = RunningStats()
means = [round(stats(v), 2) for v in [4, 8, 15, 16, 23, 42]]
print("running means:", means, "| low/high:", stats.low, stats.high)

teen = Range(13, 19)
print("callable?", callable(teen), callable(p), callable("text"))
print("teens:", list(filter(teen, [9, 13, 16, 19, 20, 25])))
validators = {"age": Range(0, 130), "score": Range(0, 100)}
record = {"age": 42, "score": 104}
print("validation:", {k: validators[k](v) for k, v in record.items()})
print("map callable object:", list(map(Polynomial(1, 0, 0), range(6))))
