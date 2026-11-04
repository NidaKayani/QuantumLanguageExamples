"""Variadic positional arguments with *args for aggregation helpers."""
import math


def total(*numbers):
    return sum(numbers)


def mean(first, *rest):
    values = (first, *rest)
    return sum(values) / len(values)


def join_words(sep, *words):
    return sep.join(words)


def geometric_mean(*values):
    if not values:
        raise ValueError("need at least one value")
    return math.prod(values) ** (1 / len(values))


def log_call(fmt, *args):
    print("LOG:", fmt.format(*args))


print("total() =", total())
print("total(1, 2, 3) =", total(1, 2, 3))
print("total(*range(10)) =", total(*range(10)))
print("mean(4) =", mean(4))
print("mean(1, 2, 3, 4) =", mean(1, 2, 3, 4))
print(join_words("-", "a", "b", "c"))
print(join_words(" ", *"quantum language".split()))
print(f"geometric_mean(2, 8) = {geometric_mean(2, 8):.4f}")
print(f"geometric_mean(1, 3, 9) = {geometric_mean(1, 3, 9):.4f}")
try:
    geometric_mean()
except ValueError as exc:
    print("error:", exc)
log_call("{} + {} = {}", 2, 3, 5)
log_call("user {0} logged in {1} times", "nida", 7)
