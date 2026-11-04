"""Subset sum with bitsets, equal-sum partition, and counting +/- target-sum assignments."""
from collections import Counter


def reachable_sums(nums):
    bits = 1
    for x in nums:
        bits |= bits << x
    return bits


def subset_for(nums, target):
    parent = {0: None}
    for i, x in enumerate(nums):
        for s in list(parent):
            if s + x not in parent:
                parent[s + x] = (s, i)
    if target not in parent:
        return None
    chosen = []
    while parent[target] is not None:
        prev, i = parent[target]
        chosen.append(nums[i])
        target = prev
    return sorted(chosen)


def best_partition(nums):
    total = sum(nums)
    bits = reachable_sums(nums)
    half = max(s for s in range(total // 2 + 1) if bits >> s & 1)
    first = subset_for(nums, half)
    rest = list((Counter(nums) - Counter(first)).elements())
    return first, sorted(rest)


def target_sum_ways(nums, target):
    ways = Counter({0: 1})
    for x in nums:
        nxt = Counter()
        for s, w in ways.items():
            nxt[s + x] += w
            nxt[s - x] += w
        ways = nxt
    return ways[target]


def main():
    nums = [3, 34, 4, 12, 5, 2]
    bits = reachable_sums(nums)
    sums = [s for s in range(sum(nums) + 1) if bits >> s & 1]
    print(f"{len(sums)} reachable sums from {nums}")
    for target in (9, 30, 41, 1):
        print(f"  subset summing to {target}: {subset_for(nums, target)}")
    for weights in ([1, 5, 11, 5], [1, 2, 3, 5], [7, 3, 2, 9, 12, 4, 8], [10, 20, 15, 5, 25]):
        a, b = best_partition(weights)
        print(f"Partition {weights}: {a} | {b} diff {abs(sum(a) - sum(b))}")
    print("Ways to reach 3 with +/- on [1,1,1,1,1]:", target_sum_ways([1] * 5, 3))
    print("Ways to reach 0 with +/- on 1..8:", target_sum_ways(range(1, 9), 0))


if __name__ == "__main__":
    main()
