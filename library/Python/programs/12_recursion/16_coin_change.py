"""Coin change: counting ways and minimum coins using memoised recursion."""

from functools import lru_cache
import math

COINS = (1, 5, 10, 25, 50)


@lru_cache(maxsize=None)
def ways(amount: int, idx: int = 0) -> int:
    if amount == 0:
        return 1
    if amount < 0 or idx == len(COINS):
        return 0
    return ways(amount - COINS[idx], idx) + ways(amount, idx + 1)


def min_coins(coins: tuple[int, ...], amount: int) -> tuple[int, list[int]] | None:
    @lru_cache(maxsize=None)
    def best(rem: int) -> float:
        if rem == 0:
            return 0
        options = [best(rem - c) + 1 for c in coins if c <= rem]
        return min(options, default=math.inf)

    if best(amount) == math.inf:
        return None
    picks, rem = [], amount
    while rem:
        coin = min((c for c in coins if c <= rem and best(rem - c) == best(rem) - 1))
        picks.append(coin)
        rem -= coin
    return int(best(amount)), sorted(picks, reverse=True)


for amount in [0, 5, 11, 26, 100]:
    print(f"ways to make {amount:3d} cents: {ways(amount)}")

for coins, amount in [((1, 3, 4), 6), ((1, 5, 10, 25), 63), ((2, 5), 3), ((7, 3), 20)]:
    result = min_coins(coins, amount)
    if result is None:
        print(f"{amount} with {coins}: impossible")
    else:
        count, picks = result
        print(f"{amount} with {coins}: {count} coins -> {picks}")
print(ways.cache_info())
