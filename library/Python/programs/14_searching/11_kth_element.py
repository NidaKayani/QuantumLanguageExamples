"""k-th order statistics: sort, heapq, quickselect and a running median."""

import heapq


def kth_sorted(nums, k):
    return sorted(nums)[k - 1]


def kth_heap(nums, k):
    return heapq.nsmallest(k, nums)[-1]


def quickselect(nums, k):
    nums = list(nums)
    lo, hi, target = 0, len(nums) - 1, k - 1
    while True:
        pivot = nums[(lo + hi) // 2]
        lt = [x for x in nums[lo:hi + 1] if x < pivot]
        eq = [x for x in nums[lo:hi + 1] if x == pivot]
        gt = [x for x in nums[lo:hi + 1] if x > pivot]
        nums[lo:hi + 1] = lt + eq + gt
        if target < lo + len(lt):
            hi = lo + len(lt) - 1
        elif target < lo + len(lt) + len(eq):
            return pivot
        else:
            lo = lo + len(lt) + len(eq)


def running_median(stream):
    low, high = [], []   # max-heap (negated) and min-heap
    for x in stream:
        heapq.heappush(low, -x)
        heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        yield -low[0] if len(low) > len(high) else (-low[0] + high[0]) / 2


data = [7, 10, 4, 3, 20, 15, 4, 11, 1, 18]
print("data:", data)
for k in (1, 3, 5, len(data)):
    results = {kth_sorted(data, k), kth_heap(data, k), quickselect(data, k)}
    print(f"k={k:>2}: {results.pop()}")

print("3 largest:", heapq.nlargest(3, data))
print("2nd largest via quickselect:", quickselect(data, len(data) - 1))
print("running medians:", list(running_median(data)))

words = ["kiwi", "fig", "banana", "apple", "cherry", "date"]
print("2nd shortest word:", heapq.nsmallest(2, words, key=len)[-1])
