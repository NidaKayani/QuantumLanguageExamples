"""Kadane's maximum subarray in 1-D, circular arrays, and the maximum-sum rectangle in 2-D."""
from itertools import accumulate


def kadane(values):
    best = cur = values[0]
    start = best_start = best_end = 0
    for i in range(1, len(values)):
        if cur < 0:
            cur, start = values[i], i
        else:
            cur += values[i]
        if cur > best:
            best, best_start, best_end = cur, start, i
    return best, best_start, best_end


def circular_max(values):
    straight = kadane(values)[0]
    if straight < 0:
        return straight
    inverted = kadane([-v for v in values])[0]
    return max(straight, sum(values) + inverted)


def max_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    best = (matrix[0][0], 0, 0, 0, 0)
    for top in range(rows):
        col_sums = [0] * cols
        for bottom in range(top, rows):
            col_sums = [s + v for s, v in zip(col_sums, matrix[bottom])]
            value, left, right = kadane(col_sums)
            if value > best[0]:
                best = (value, top, bottom, left, right)
    return best


def main():
    series = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    value, lo, hi = kadane(series)
    print(f"Max subarray of {series}: {value} = {series[lo:hi + 1]}")
    prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    changes = [b - a for a, b in zip(prices, prices[1:])]
    gain, buy, sell = kadane(changes)
    print(f"Best trade: buy day {buy} at {prices[buy]}, sell day {sell + 1} at "
          f"{prices[sell + 1]}, profit {gain}")
    print("Running max price:", list(accumulate(prices, max)))
    for arr in ([5, -3, 5], [-3, -2, -3], [8, -1, -3, 8, -6, -9, 2, 4]):
        print(f"Circular max of {arr}: {circular_max(arr)}")
    matrix = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]
    total, top, bottom, left, right = max_rectangle(matrix)
    print(f"Max rectangle sum {total}: rows {top}-{bottom}, cols {left}-{right}")
    for row in matrix[top:bottom + 1]:
        print("  ", row[left:right + 1])


if __name__ == "__main__":
    main()
