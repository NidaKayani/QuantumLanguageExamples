"""Searching sorted 2-D matrices: flattened binary search and staircase search."""

from bisect import bisect_left

FULLY_SORTED = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60],
]

ROW_COL_SORTED = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]


def search_flat(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return divmod(mid, cols)
        lo, hi = (mid + 1, hi) if value < target else (lo, mid - 1)
    return None


def staircase(matrix, target):
    r, c, steps = 0, len(matrix[0]) - 1, 0
    while r < len(matrix) and c >= 0:
        steps += 1
        v = matrix[r][c]
        if v == target:
            return (r, c), steps
        if v > target:
            c -= 1
        else:
            r += 1
    return None, steps


def count_less_equal(matrix, x):
    return sum(bisect_left(row, x + 1) for row in matrix)


for t in [16, 1, 60, 13]:
    print(f"fully sorted, find {t}: {search_flat(FULLY_SORTED, t)}")

for t in [5, 20, 30, 18, 0]:
    pos, steps = staircase(ROW_COL_SORTED, t)
    print(f"staircase find {t:>2}: {pos} in {steps} steps")

lo, hi, k = 1, 30, 8
while lo < hi:
    mid = (lo + hi) // 2
    if count_less_equal(ROW_COL_SORTED, mid) < k:
        lo = mid + 1
    else:
        hi = mid
print(f"{k}th smallest in row/col sorted matrix: {lo}")
