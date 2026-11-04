"""Common folding patterns expressed with functools.reduce."""
from functools import reduce
from operator import add, mul, or_, and_
from math import gcd

numbers = [12, 18, 24, 36, 60]

print("sum:", reduce(add, numbers))
print("product:", reduce(mul, numbers))
print("gcd:", reduce(gcd, numbers))
print("lcm:", reduce(lambda a, b: a * b // gcd(a, b), numbers))
print("max:", reduce(lambda a, b: a if a > b else b, numbers))

digits = [4, 0, 9, 6]
print("digits to int:", reduce(lambda acc, d: acc * 10 + d, digits, 0))

sets = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 6}]
print("union:", sorted(reduce(or_, sets)))
print("intersection:", sorted(reduce(and_, sets)))

nested = {"a": {"b": {"c": {"d": 42}}}}
print("deep get:", reduce(lambda d, k: d[k], ["a", "b", "c", "d"], nested))


def compose(*fns):
    return reduce(lambda f, g: lambda x: g(f(x)), fns, lambda x: x)


pipeline = compose(str.strip, str.lower, lambda s: s.replace(" ", "-"))
print("slug:", pipeline("  Hello Functional World  "))

text = "mississippi"
freq = reduce(lambda acc, ch: {**acc, ch: acc.get(ch, 0) + 1}, text, {})
print("frequencies:", dict(sorted(freq.items())))

running = reduce(lambda acc, x: acc + [acc[-1] + x], [3, 1, 4, 1, 5, 9], [0])[1:]
print("running totals:", running)

pairs = [("x", 1), ("y", 2), ("x", 3), ("z", 4), ("y", 5)]
grouped = reduce(lambda acc, kv: {**acc, kv[0]: acc.get(kv[0], []) + [kv[1]]}, pairs, {})
print("grouped:", grouped)

matrices = [[[1, 1], [1, 0]]] * 10


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


print("fib via matrix power:", reduce(matmul, matrices)[0][1])
print("reversed via reduce:", reduce(lambda acc, x: [x] + acc, range(6), []))
