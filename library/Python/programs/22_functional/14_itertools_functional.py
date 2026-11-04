"""Functional data processing with itertools: accumulate, groupby, starmap, chain, and friends."""
import operator
from itertools import (accumulate, chain, compress, count, dropwhile, filterfalse, groupby,
                       islice, pairwise, product, starmap, takewhile, tee, zip_longest)

temps = [12, 14, 13, 17, 21, 22, 19, 18, 23, 25, 24]
print("running max:", list(accumulate(temps, max)))
print("running sum:", list(accumulate(temps)))
print("compound growth:", [round(x, 2) for x in accumulate([1.0, 1.05, 1.05, 1.05], operator.mul)])
print("deltas:", [b - a for a, b in pairwise(temps)])

print("takewhile < 20:", list(takewhile(lambda t: t < 20, temps)))
print("dropwhile < 20:", list(dropwhile(lambda t: t < 20, temps)))
print("filterfalse even:", list(filterfalse(lambda t: t % 2 == 0, temps)))
print("compress by mask:", list(compress("ABCDEFG", [1, 0, 1, 0, 0, 1, 1])))

words = sorted(["apple", "avocado", "banana", "blueberry", "cherry", "cranberry", "date"])
for letter, group in groupby(words, key=lambda w: w[0]):
    print(f"  {letter}: {list(group)}")

runs = "aaabccddddde"
print("run-length:", "".join(f"{k}{len(list(g))}" for k, g in groupby(runs)))

print("starmap pow:", list(starmap(pow, [(2, 5), (3, 3), (10, 2)])))
print("chain:", list(chain("ab", [1, 2], range(3))))
print("chain.from_iterable:", list(chain.from_iterable([[1], [2, 3], [], [4]])))
print("zip_longest:", list(zip_longest("abc", [1, 2], fillvalue="-")))
print("islice count by 7:", list(islice(count(7, 7), 6)))
print("dice sums=7:", [p for p in product(range(1, 7), repeat=2) if sum(p) == 7])

a, b = tee(x * x for x in range(6))
print("tee copies:", list(a), sum(b))

batches = iter(range(10))
chunks = list(takewhile(bool, (list(islice(batches, 4)) for _ in count())))
print("chunks of 4:", chunks)
