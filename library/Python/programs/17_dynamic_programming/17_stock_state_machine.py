"""State-machine DP: house robber variants and stock trading with cooldown, fees and k transactions."""
from math import inf


def rob_line(values):
    take = skip = 0
    for v in values:
        take, skip = skip + v, max(take, skip)
    return max(take, skip)


def rob_circle(values):
    if len(values) == 1:
        return values[0]
    return max(rob_line(values[1:]), rob_line(values[:-1]))


def stock_cooldown(prices):
    hold, sold, rest = -inf, 0, 0
    for p in prices:
        hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
    return max(sold, rest)


def stock_fee(prices, fee):
    cash, hold = 0, -prices[0]
    for p in prices[1:]:
        cash, hold = max(cash, hold + p - fee), max(hold, cash - p)
    return cash


def stock_k(prices, k):
    buy = [-inf] * (k + 1)
    sell = [0] * (k + 1)
    for p in prices:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - p)
            sell[t] = max(sell[t], buy[t] + p)
    return sell[k]


def main():
    houses = [2, 7, 9, 3, 1, 5, 8, 4]
    print(f"Houses {houses}")
    print(f"  in a line:   {rob_line(houses)}")
    print(f"  in a circle: {rob_circle(houses)}")
    prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 7, 1, 6]
    print(f"Prices {prices}")
    print(f"  unlimited trades:   {sum(max(0, b - a) for a, b in zip(prices, prices[1:]))}")
    print(f"  with cooldown:      {stock_cooldown(prices)}")
    for fee in (0, 1, 2, 3):
        print(f"  with fee {fee}:         {stock_fee(prices, fee)}")
    for k in range(0, 5):
        print(f"  at most {k} trades:   {stock_k(prices, k)}")


if __name__ == "__main__":
    main()
