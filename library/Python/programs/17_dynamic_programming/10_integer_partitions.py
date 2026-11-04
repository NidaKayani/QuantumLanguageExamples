"""Integer partitions: counting tables, distinct/odd parts, and generating them."""


def partition_counts(n):
    p = [1] + [0] * n
    for part in range(1, n + 1):
        for total in range(part, n + 1):
            p[total] += p[total - part]
    return p


def distinct_part_counts(n):
    q = [1] + [0] * n
    for part in range(1, n + 1):
        for total in range(n, part - 1, -1):
            q[total] += q[total - part]
    return q


def odd_part_counts(n):
    o = [1] + [0] * n
    for part in range(1, n + 1, 2):
        for total in range(part, n + 1):
            o[total] += o[total - part]
    return o


def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def pentagonal_count(n):
    p = [1] + [0] * n
    for m in range(1, n + 1):
        k, total = 1, 0
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > m:
                break
            sign = 1 if k % 2 else -1
            total += sign * p[m - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= m:
                total += sign * p[m - g2]
            k += 1
        p[m] = total
    return p


def main():
    N = 30
    p, q, o = partition_counts(N), distinct_part_counts(N), odd_part_counts(N)
    print(f"{'n':>3} {'p(n)':>6} {'distinct':>9} {'odd':>6}")
    for n in range(0, N + 1, 5):
        print(f"{n:>3} {p[n]:>6} {q[n]:>9} {o[n]:>6}")
    print("Euler's theorem distinct == odd holds:", q == o)
    print("Pentagonal recurrence agrees:", pentagonal_count(N) == p)
    print("p(100) =", partition_counts(100)[100])
    print("Partitions of 6:")
    for part in partitions(6):
        print("  " + " + ".join(map(str, part)))


if __name__ == "__main__":
    main()
