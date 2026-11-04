"""Sliding window patterns: fixed-size sums, longest unique substring, anagram finding."""

from collections import Counter, deque


def max_sum_window(nums, k):
    window = sum(nums[:k])
    best, best_start = window, 0
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        if window > best:
            best, best_start = window, i - k + 1
    return best, nums[best_start:best_start + k]


def longest_unique_substring(s):
    last_seen, start, best = {}, 0, ""
    for i, ch in enumerate(s):
        if last_seen.get(ch, -1) >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        if i - start + 1 > len(best):
            best = s[start:i + 1]
    return best


def shortest_subarray_at_least(nums, target):
    left, total, best = 0, 0, None
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            if best is None or right - left + 1 < len(best):
                best = nums[left:right + 1]
            total -= nums[left]
            left += 1
    return best


def find_anagrams(text, pattern):
    need, have = Counter(pattern), Counter(text[:len(pattern)])
    hits = [0] if have == need else []
    for i in range(len(pattern), len(text)):
        have[text[i]] += 1
        have[text[i - len(pattern)]] -= 1
        if have == need:
            hits.append(i - len(pattern) + 1)
    return hits


def window_maxima(nums, k):
    dq, out = deque(), []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


sales = [2, 1, 5, 1, 3, 2, 9, 4, 1, 7]
print("best 3-day sales:", max_sum_window(sales, 3))
for s in ["abcabcbb", "bbbbb", "pwwkew", "dvdf"]:
    print(f"longest unique in {s!r}: {longest_unique_substring(s)!r}")
print("shortest subarray with sum >= 15:", shortest_subarray_at_least(sales, 15))
print("anagrams of 'abc' in 'cbaebabacd':", find_anagrams("cbaebabacd", "abc"))
print("sliding max (k=3):", window_maxima([1, 3, -1, -3, 5, 3, 6, 7], 3))
