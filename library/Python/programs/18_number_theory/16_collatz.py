"""Collatz sequences: cached chain lengths, record holders, and peak values."""
from functools import lru_cache


@lru_cache(maxsize=None)
def chain_length(n):
    if n == 1:
        return 1
    return 1 + chain_length(n // 2 if n % 2 == 0 else 3 * n + 1)


def sequence(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def main():
    print("Sequence from 27 (first 20):", list(sequence(27))[:20], "...")
    print("Length from 27:", chain_length(27), "peak:", max(sequence(27)))
    limit = 50_000
    records, best = [], 0
    for n in range(1, limit):
        length = chain_length(n)
        if length > best:
            best = length
            records.append((n, length))
    print(f"Record setters below {limit}:")
    for n, length in records[-8:]:
        print(f"  {n:>6} -> {length} steps")
    peaks = sorted(((max(sequence(n)), n) for n in range(1, 5_000)), reverse=True)[:5]
    print("Highest peaks for n < 5000:", [(n, p) for p, n in peaks])
    histogram = {}
    for n in range(1, 1001):
        bucket = chain_length(n) // 25 * 25
        histogram[bucket] = histogram.get(bucket, 0) + 1
    print("Length histogram for n <= 1000:")
    for bucket in sorted(histogram):
        print(f"  {bucket:>3}-{bucket + 24:<3} {'#' * (histogram[bucket] // 10)} {histogram[bucket]}")


if __name__ == "__main__":
    main()
