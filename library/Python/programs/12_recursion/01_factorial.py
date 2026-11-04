"""Recursive factorial compared with iterative and library versions."""

import math
from functools import reduce
from operator import mul


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)


def factorial_tail(n: int, acc: int = 1) -> int:
    return acc if n <= 1 else factorial_tail(n - 1, acc * n)


def factorial_reduce(n: int) -> int:
    return reduce(mul, range(2, n + 1), 1)


for n in [0, 1, 5, 10, 15, 20]:
    values = {factorial(n), factorial_tail(n), factorial_reduce(n), math.factorial(n)}
    assert len(values) == 1
    print(f"{n:>2}! = {factorial(n)}")

big = factorial(50)
print("50! has", len(str(big)), "digits; trailing zeros:", len(str(big)) - len(str(big).rstrip("0")))

try:
    factorial(-3)
except ValueError as exc:
    print("error:", exc)


def count_calls(func):
    def wrapper(*args):
        wrapper.calls += 1
        return func(*args)
    wrapper.calls = 0
    return wrapper


factorial = count_calls(factorial)
factorial(12)
print("recursive calls for 12!:", factorial.calls)
