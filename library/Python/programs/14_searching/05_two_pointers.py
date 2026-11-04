"""Two-pointer techniques on sorted arrays and strings."""


def pair_with_sum(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return nums[lo], nums[hi]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return None


def three_sum_zero(nums):
    nums = sorted(nums)
    found = []
    for i, a in enumerate(nums[:-2]):
        if i and a == nums[i - 1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = a + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                found.append((a, nums[lo], nums[hi]))
                while lo < hi and nums[lo] == nums[lo + 1]:
                    lo += 1
                lo += 1
                hi -= 1
    return found


def dedupe_sorted(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def max_water(heights):
    lo, hi, best = 0, len(heights) - 1, (0, 0, 0)
    while lo < hi:
        area = min(heights[lo], heights[hi]) * (hi - lo)
        best = max(best, (area, lo, hi))
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return best


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


sorted_nums = [1, 3, 4, 6, 8, 11, 15]
for t in [10, 19, 2]:
    print(f"pair summing to {t}: {pair_with_sum(sorted_nums, t)}")
print("three-sum zero:", three_sum_zero([-1, 0, 1, 2, -1, -4, 2, -2]))
arr = [1, 1, 2, 3, 3, 3, 4, 5, 5]
k = dedupe_sorted(arr)
print("deduped in place:", arr[:k])
area, i, j = max_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(f"max water area {area} between walls {i} and {j}")
print("palindromes:", [is_palindrome(s) for s in ["No 'x' in Nixon", "two pointers", "Step on no pets!"]])
