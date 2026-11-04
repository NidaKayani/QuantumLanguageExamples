"""Combinatoric iterators: product, permutations, combinations, and with replacement."""
from itertools import product, permutations, combinations, combinations_with_replacement
from math import comb, perm

print("product('AB', repeat=2):", ["".join(p) for p in product("AB", repeat=2)])
print("product sizes x colors:", list(product(["S", "M"], ["red", "blue"])))

dice = [a + b for a, b in product(range(1, 7), repeat=2)]
print("ways to roll 7 with two dice:", dice.count(7), "of", len(dice))

print("permutations('abc'):", ["".join(p) for p in permutations("abc")])
print("permutations(range(4), 2) count:", len(list(permutations(range(4), 2))), "=", perm(4, 2))

print("combinations('ABCD', 2):", ["".join(c) for c in combinations("ABCD", 2)])
print("C(10, 3):", len(list(combinations(range(10), 3))), "=", comb(10, 3))

coins = [1, 5, 10, 25]
ways = [c for c in combinations_with_replacement(coins, 3) if sum(c) == 30]
print("3 coins totalling 30:", ways)

items = {"tent": 5, "stove": 3, "lamp": 2, "book": 1}
best = max(
    (combo for r in range(len(items) + 1) for combo in combinations(items, r)
     if sum(items[i] for i in combo) <= 7),
    key=lambda combo: (len(combo), -sum(items[i] for i in combo)),
)
print("most items within weight 7:", best)

target = 24
nums = [3, 8, 1, 4]
hits = {p for p in permutations(nums) if p[0] * p[1] + p[2] * p[3] == target}
print("a*b + c*d == 24:", sorted(hits))
