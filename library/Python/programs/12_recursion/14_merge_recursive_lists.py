"""Recursive list processing in a functional style."""

from typing import Any


def flatten(xs: list[Any]) -> list[Any]:
    if not xs:
        return []
    head, *tail = xs
    if isinstance(head, list):
        return flatten(head) + flatten(tail)
    return [head] + flatten(tail)


def deep_reverse(xs):
    return [deep_reverse(x) if isinstance(x, list) else x for x in reversed(xs)]


def deep_sum(xs):
    return sum(deep_sum(x) if isinstance(x, list) else x for x in xs)


def merge(a: list[int], b: list[int]) -> list[int]:
    if not a:
        return b
    if not b:
        return a
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])


def max_depth(xs) -> int:
    if not isinstance(xs, list):
        return 0
    return 1 + max((max_depth(x) for x in xs), default=0)


def count_leaves(xs) -> int:
    return sum(count_leaves(x) if isinstance(x, list) else 1 for x in xs)


nested = [1, [2, [3, 4], 5], [[6]], [], 7, [8, [9, [10]]]]
print("nested:      ", nested)
print("flattened:   ", flatten(nested))
print("deep reverse:", deep_reverse(nested))
print("deep sum:    ", deep_sum(nested))
print("max depth:   ", max_depth(nested))
print("leaf count:  ", count_leaves(nested))
print("merge:       ", merge([1, 4, 9, 12], [2, 3, 10, 15, 20]))


def zip_lists(a, b):
    if not a or not b:
        return []
    return [(a[0], b[0])] + zip_lists(a[1:], b[1:])


print("zip_lists:   ", zip_lists("abc", [1, 2, 3, 4]))
