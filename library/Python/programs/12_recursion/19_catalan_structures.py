"""Catalan structures: balanced parentheses and binary tree shapes."""

from functools import cache
from math import comb


def parens(open_left: int, close_left: int, prefix: str = ""):
    if open_left == 0 and close_left == 0:
        yield prefix
        return
    if open_left:
        yield from parens(open_left - 1, close_left, prefix + "(")
    if close_left > open_left:
        yield from parens(open_left, close_left - 1, prefix + ")")


@cache
def catalan(n: int) -> int:
    if n <= 1:
        return 1
    return sum(catalan(i) * catalan(n - 1 - i) for i in range(n))


def tree_shapes(n: int) -> list[str]:
    if n == 0:
        return ["."]
    shapes = []
    for left_size in range(n):
        for left in tree_shapes(left_size):
            for right in tree_shapes(n - 1 - left_size):
                shapes.append(f"({left} o {right})")
    return shapes


print("balanced strings with 3 pairs:", list(parens(3, 3)))
for n in range(1, 11):
    generated = sum(1 for _ in parens(n, n))
    formula = comb(2 * n, n) // (n + 1)
    print(f"n={n:2d} catalan={catalan(n):6d} generated={generated:6d} formula={formula:6d}")

print("binary tree shapes with 3 nodes:")
for shape in tree_shapes(3):
    print("  ", shape)
