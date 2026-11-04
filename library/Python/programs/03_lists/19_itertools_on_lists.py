"""Combine lists with itertools: accumulate, groupby, permutations, combinations."""

from itertools import accumulate, groupby, permutations, combinations, product, pairwise, compress, takewhile, dropwhile
import operator

sales = [3, 5, 2, 8, 6]
print("running total:", list(accumulate(sales)))
print("running product:", list(accumulate(sales, operator.mul)))
print("running max:", list(accumulate([3, 1, 4, 1, 5, 9, 2], max)))

letters = list("aaabbcaaad")
print("groupby:", [(k, len(list(g))) for k, g in groupby(letters)])

words = sorted(["apple", "avocado", "banana", "blueberry", "cherry"], key=lambda w: w[0])
for initial, group in groupby(words, key=lambda w: w[0]):
    print(f"  {initial}: {list(group)}")

print("permutations of ABC:", ["".join(p) for p in permutations("ABC")])
print("2-combinations:", list(combinations([1, 2, 3, 4], 2)))
print("product:", list(product([0, 1], repeat=3)))
print("pairwise:", list(pairwise([1, 4, 9, 16])))
print("compress:", list(compress("ABCDEF", [1, 0, 1, 0, 1, 1])))
print("takewhile < 5:", list(takewhile(lambda x: x < 5, [1, 3, 6, 2])))
print("dropwhile < 5:", list(dropwhile(lambda x: x < 5, [1, 3, 6, 2])))

coins = [1, 5, 10, 25]
ways = [c for r in range(1, 4) for c in combinations(coins, r) if sum(c) == 30]
print("coin subsets summing to 30:", ways)
