"""Fenwick tree (binary indexed tree) for prefix sums and inversion counting."""


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @classmethod
    def from_list(cls, values):
        fw = cls(len(values))
        for i, v in enumerate(values):
            fw.add(i, v)
        return fw

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix(self, i):
        """Sum of values[0:i]."""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, lo, hi):
        return self.prefix(hi) - self.prefix(lo)

    def lower_bound(self, target):
        """Smallest index i such that prefix(i + 1) >= target (values non-negative)."""
        pos, step = 0, 1 << self.n.bit_length()
        while step:
            if pos + step <= self.n and self.tree[pos + step] < target:
                pos += step
                target -= self.tree[pos]
            step >>= 1
        return pos


values = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
fw = Fenwick.from_list(values)
print("values:", values)
print("prefix sums:", [fw.prefix(i) for i in range(len(values) + 1)])
print("sum[2:6):", fw.range_sum(2, 6), "check:", sum(values[2:6]))
fw.add(3, 10)
values[3] += 10
print("after values[3] += 10, sum[0:5):", fw.range_sum(0, 5), "check:", sum(values[:5]))


def count_inversions(arr):
    ranks = {v: i for i, v in enumerate(sorted(set(arr)))}
    bit = Fenwick(len(ranks))
    inversions = 0
    for seen, x in enumerate(arr):
        inversions += seen - bit.prefix(ranks[x] + 1)
        bit.add(ranks[x], 1)
    return inversions


for arr in ([2, 4, 1, 3, 5], [5, 4, 3, 2, 1], [1, 2, 3], [3, 3, 1]):
    print(f"inversions in {arr}: {count_inversions(arr)}")

counts = Fenwick.from_list([4, 0, 2, 5, 1])
print("item at 1st/5th/7th/12th position lives in bucket:",
      [counts.lower_bound(k) for k in (1, 5, 7, 12)])
