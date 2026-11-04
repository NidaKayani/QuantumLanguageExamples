"""Longest increasing subsequence: O(n^2) DP and O(n log n) patience sorting with bisect."""
from bisect import bisect_left


def lis_quadratic(seq):
    n = len(seq)
    length = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                prev[i] = j
    end = max(range(n), key=length.__getitem__)
    out = []
    while end != -1:
        out.append(seq[end])
        end = prev[end]
    return out[::-1]


def lis_fast(seq):
    tails, tail_idx = [], []
    parent = [-1] * len(seq)
    for i, x in enumerate(seq):
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            tail_idx.append(i)
        else:
            tails[pos] = x
            tail_idx[pos] = i
        parent[i] = tail_idx[pos - 1] if pos else -1
    out, k = [], tail_idx[-1] if tail_idx else -1
    while k != -1:
        out.append(seq[k])
        k = parent[k]
    return out[::-1]


def lcg(seed, n, mod=100):
    for _ in range(n):
        seed = (seed * 1103515245 + 12345) % 2**31
        yield seed % mod


def main():
    samples = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
        [5, 4, 3, 2, 1],
        list(lcg(42, 30)),
    ]
    for seq in samples:
        slow, fast = lis_quadratic(seq), lis_fast(seq)
        print(f"seq={seq}")
        print(f"  O(n^2):     len {len(slow)} {slow}")
        print(f"  O(n log n): len {len(fast)} {fast}")
        assert len(slow) == len(fast)
    envelopes = sorted([(5, 4), (6, 4), (6, 7), (2, 3), (8, 9), (7, 8)],
                       key=lambda e: (e[0], -e[1]))
    nested = lis_fast([h for _, h in envelopes])
    print("Russian-doll envelopes nest depth:", len(nested))


if __name__ == "__main__":
    main()
