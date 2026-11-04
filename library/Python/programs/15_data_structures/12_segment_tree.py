"""Iterative segment tree supporting range queries with any associative operation."""

import operator
from math import gcd


class SegmentTree:
    def __init__(self, data, op=operator.add, identity=0):
        self.n = len(data)
        self.op = op
        self.identity = identity
        self.tree = [identity] * (2 * self.n)
        self.tree[self.n:] = data
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        i = index + self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        """Aggregate over the half-open range [left, right)."""
        res_left = res_right = self.identity
        lo, hi = left + self.n, right + self.n
        while lo < hi:
            if lo & 1:
                res_left = self.op(res_left, self.tree[lo])
                lo += 1
            if hi & 1:
                hi -= 1
                res_right = self.op(self.tree[hi], res_right)
            lo //= 2
            hi //= 2
        return self.op(res_left, res_right)


data = [5, 3, 8, 6, 1, 4, 7, 2]
sums = SegmentTree(data)
mins = SegmentTree(data, min, float("inf"))
maxs = SegmentTree(data, max, float("-inf"))

print("data:", data)
for lo, hi in [(0, 8), (2, 5), (3, 4), (1, 7)]:
    print(f"[{lo},{hi}): sum={sums.query(lo, hi):>2} min={mins.query(lo, hi)} max={maxs.query(lo, hi)}"
          f"  check={sum(data[lo:hi])}")

for idx, val in [(4, 10), (0, 0)]:
    data[idx] = val
    sums.update(idx, val)
    mins.update(idx, val)
    maxs.update(idx, val)
    print(f"set data[{idx}]={val}: total={sums.query(0, 8)} min={mins.query(0, 8)} max={maxs.query(0, 8)}")

g = SegmentTree([12, 18, 24, 36, 9, 27], gcd, 0)
print("gcd of [0,4):", g.query(0, 4), "gcd of [3,6):", g.query(3, 6))
