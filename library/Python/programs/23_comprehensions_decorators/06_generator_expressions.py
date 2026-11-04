"""Generator expressions: lazy evaluation, short-circuiting with any/all, and memory-friendly sums."""
import math

print("sum of squares 1..1000:", sum(n * n for n in range(1, 1001)))
print("max word length:", max(len(w) for w in "generators are lazy and composable".split()))
print("any negative?", any(x < 0 for x in [3, 1, -4, 1, 5]))
print("all positive?", all(x > 0 for x in [3, 1, 4, 1, 5]))

checked = []


def is_big(n):
    checked.append(n)
    return n > 10


found = any(is_big(n) for n in [1, 5, 12, 3, 50])
print("short-circuit any:", found, "checked only", checked)

gen = (n ** 2 for n in range(5))
print("first next():", next(gen), next(gen))
print("rest:", list(gen))
print("exhausted:", list(gen))

lines = ["# header", "alpha=1", "", "beta = 22", "# note", "gamma=333 "]
pairs = (line.split("=") for line in lines if line and not line.startswith("#"))
config = {k.strip(): int(v) for k, v in pairs}
print("config:", config)

dot = sum(a * b for a, b in zip([1, 2, 3], [4, 5, 6]))
norm = math.sqrt(sum(x * x for x in [3, 4, 12]))
print("dot product:", dot, "| norm:", norm)

first_square_over = next((n for n in range(1, 100) if n * n > 500), None)
print("first n with n^2 > 500:", first_square_over)
print("missing default:", next((n for n in range(10) if n > 100), "none found"))

nested_gen = (x * y for x in range(1, 4) for y in range(1, 4) if x != y)
print("products x!=y:", sorted(nested_gen))

text = "To be or not to be that is the question"
print("joined upper:", "-".join(w.upper() for w in text.split() if len(w) == 2))
print("count of 'be':", sum(1 for w in text.lower().split() if w == "be"))
print("tuple from gen:", tuple(c for c in "hello" if c not in "aeiou"))
print("sorted unique lengths:", sorted(set(len(w) for w in text.split())))
print("min by key:", min((w for w in text.split()), key=len))
