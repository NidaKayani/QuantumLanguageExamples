"""Radix sort: LSD for non-negative integers and strings, with negatives handled."""


def lsd_radix_sort(nums, base=10):
    if not nums:
        return []
    out = list(nums)
    place = 1
    largest = max(out)
    passes = 0
    while largest // place:
        buckets = [[] for _ in range(base)]
        for n in out:
            buckets[(n // place) % base].append(n)
        out = [n for bucket in buckets for n in bucket]
        place *= base
        passes += 1
    return out, passes


def radix_sort_signed(nums):
    neg = [-n for n in nums if n < 0]
    pos = [n for n in nums if n >= 0]
    sorted_neg = lsd_radix_sort(neg)[0] if neg else []
    sorted_pos = lsd_radix_sort(pos)[0] if pos else []
    return [-n for n in reversed(sorted_neg)] + sorted_pos


def string_radix_sort(words, width):
    padded = [w.ljust(width) for w in words]
    for pos in range(width - 1, -1, -1):
        buckets = {}
        for w in padded:
            buckets.setdefault(w[pos], []).append(w)
        padded = [w for ch in sorted(buckets) for w in buckets[ch]]
    return [w.rstrip() for w in padded]


data = [170, 45, 75, 90, 802, 24, 2, 66]
result, passes = lsd_radix_sort(data)
print(f"base 10: {result} in {passes} passes")
result, passes = lsd_radix_sort(data, base=2)
print(f"base 2:  {result} in {passes} passes")
result, passes = lsd_radix_sort(data, base=256)
print(f"base 256: {result} in {passes} passes")

mixed = [-5, 13, -100, 0, 7, -1, 42]
print("signed:", radix_sort_signed(mixed))

codes = ["dab", "cab", "fad", "bad", "dad", "ebb", "ace", "add", "fed", "bed", "fee", "bee"]
print("strings:", string_radix_sort(codes, 3))
print("ragged:", string_radix_sort(["to", "tea", "ted", "ten", "i", "in", "inn"], 3))
