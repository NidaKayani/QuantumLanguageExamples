"""Matrix chain multiplication order with optimal parenthesisation."""
from functools import reduce


def matrix_chain(dims):
    n = len(dims) - 1
    cost = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")
            for k in range(i, j):
                c = cost[i][k] + cost[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if c < cost[i][j]:
                    cost[i][j], split[i][j] = c, k
    return cost, split


def parenthesize(split, i, j, names):
    if i == j:
        return names[i]
    k = split[i][j]
    return f"({parenthesize(split, i, k, names)} x {parenthesize(split, k + 1, j, names)})"


def left_to_right_cost(dims):
    total, rows = 0, dims[0]
    for k in range(1, len(dims) - 1):
        total += rows * dims[k] * dims[k + 1]
    return total


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main():
    chains = {
        "textbook": [30, 35, 15, 5, 10, 20, 25],
        "small": [10, 20, 30, 40, 30],
        "skinny": [5, 100, 2, 100, 3],
    }
    for label, dims in chains.items():
        names = [chr(ord("A") + i) for i in range(len(dims) - 1)]
        cost, split = matrix_chain(dims)
        best = cost[0][-1]
        naive = left_to_right_cost(dims)
        print(f"{label}: dims {dims}")
        print(f"  optimal {parenthesize(split, 0, len(names) - 1, names)} = {best:,} mults")
        print(f"  left-to-right = {naive:,} mults ({naive / best:.1f}x worse)")
    mats = [[[1, 2], [3, 4]], [[0, 1], [1, 0]], [[2, 0], [0, 2]]]
    print("Product of three 2x2 matrices:", reduce(matmul, mats))


if __name__ == "__main__":
    main()
