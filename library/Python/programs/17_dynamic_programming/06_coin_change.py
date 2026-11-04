"""Coin change: minimum coins, number of ways, and why greedy can fail."""
from functools import lru_cache


def min_coins(coins, amount):
    best = [0] + [float("inf")] * amount
    last = [0] * (amount + 1)
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1
                last[a] = c
    if best[amount] == float("inf"):
        return None
    used = []
    while amount:
        used.append(last[amount])
        amount -= last[amount]
    return sorted(used, reverse=True)


def count_ways(coins, amount):
    ways = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            ways[a] += ways[a - c]
    return ways[amount]


def count_ways_memo(coins, amount):
    coins = tuple(sorted(coins))

    @lru_cache(maxsize=None)
    def go(i, remaining):
        if remaining == 0:
            return 1
        if i == len(coins) or remaining < 0:
            return 0
        return go(i, remaining - coins[i]) + go(i + 1, remaining)

    return go(0, amount)


def greedy(coins, amount):
    used = []
    for c in sorted(coins, reverse=True):
        k, amount = divmod(amount, c)
        used += [c] * k
    return used if amount == 0 else None


def main():
    euro = [1, 2, 5, 10, 20, 50, 100, 200]
    print("Ways to make 2 euros from cents:", count_ways(euro, 200))
    print("Memoised check:", count_ways_memo(euro, 200))
    weird = [1, 3, 4]
    for amount in (6, 10, 13):
        dp, gr = min_coins(weird, amount), greedy(weird, amount)
        print(f"{amount:2d} with {weird}: DP {dp} ({len(dp)}) vs greedy {gr} ({len(gr)})")
    print("Impossible 7 with [2, 4]:", min_coins([2, 4], 7))
    us = [1, 5, 10, 25]
    table = [(a, len(min_coins(us, a)), count_ways(us, a)) for a in range(0, 101, 20)]
    print("US coins amount/min/ways:")
    for a, m, w in table:
        print(f"  {a:3d} {m:2d} {w:4d}")


if __name__ == "__main__":
    main()
