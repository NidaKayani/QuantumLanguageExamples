"""Catalan numbers via DP, and the structures they count: parentheses and binary trees."""
from functools import lru_cache
from math import comb


def catalan_dp(n):
    c = [1] + [0] * n
    for i in range(1, n + 1):
        c[i] = sum(c[j] * c[i - 1 - j] for j in range(i))
    return c


@lru_cache(maxsize=None)
def balanced(n):
    if n == 0:
        return ("",)
    out = []
    for inside in range(n):
        for a in balanced(inside):
            for b in balanced(n - 1 - inside):
                out.append(f"({a}){b}")
    return tuple(out)


@lru_cache(maxsize=None)
def tree_shapes(lo, hi):
    """All BST shapes on keys lo..hi as nested tuples (root, left, right)."""
    if lo > hi:
        return (None,)
    shapes = []
    for root in range(lo, hi + 1):
        for left in tree_shapes(lo, root - 1):
            for right in tree_shapes(root + 1, hi):
                shapes.append((root, left, right))
    return tuple(shapes)


def show(tree):
    if tree is None:
        return "."
    root, left, right = tree
    if left is None and right is None:
        return str(root)
    return f"{root}[{show(left)},{show(right)}]"


def main():
    cat = catalan_dp(15)
    print("Catalan numbers:", cat)
    closed = [comb(2 * n, n) // (n + 1) for n in range(16)]
    print("Closed form matches:", cat == closed)
    print("Balanced strings with 3 pairs:", ", ".join(balanced(3)))
    print("Count for 6 pairs:", len(balanced(6)))
    shapes = tree_shapes(1, 3)
    print(f"{len(shapes)} BSTs on keys 1..3:")
    for s in shapes:
        print("  ", show(s))
    print("BSTs on 1..8:", len(tree_shapes(1, 8)), "expected", cat[8])
    print("Cache stats:", tree_shapes.cache_info().hits, "hits")


if __name__ == "__main__":
    main()
