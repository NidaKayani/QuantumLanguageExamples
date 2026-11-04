"""Rod cutting with top-down memoisation (functools.cache) and bottom-up tabulation."""
from functools import cache

PRICES = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def top_down(prices, n):
    calls = 0

    @cache
    def best(length):
        nonlocal calls
        calls += 1
        if length == 0:
            return 0
        return max(prices[cut] + best(length - cut)
                   for cut in range(1, min(length, len(prices) - 1) + 1))

    return best(n), calls


def bottom_up(prices, n, cut_cost=0):
    revenue = [0] * (n + 1)
    first_cut = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, min(length, len(prices) - 1) + 1):
            penalty = cut_cost if cut < length else 0
            value = prices[cut] + revenue[length - cut] - penalty
            if value > revenue[length]:
                revenue[length], first_cut[length] = value, cut
    return revenue, first_cut


def pieces(first_cut, n):
    out = []
    while n > 0:
        out.append(first_cut[n])
        n -= first_cut[n]
    return out


def main():
    revenue, first = bottom_up(PRICES, 20)
    print(f"{'len':>3} {'rev':>4}  pieces")
    for n in range(1, 21):
        print(f"{n:>3} {revenue[n]:>4}  {pieces(first, n)}")
    value, calls = top_down(PRICES, 20)
    print(f"Top-down result for 20: {value} with {calls} distinct subproblems")
    rev2, first2 = bottom_up(PRICES, 20, cut_cost=2)
    print(f"With cost 2 per cut, length 20 earns {rev2[20]} using {pieces(first2, 20)}")


if __name__ == "__main__":
    main()
