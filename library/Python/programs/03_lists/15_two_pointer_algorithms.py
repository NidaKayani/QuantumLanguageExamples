"""Solve classic list problems with the two-pointer technique."""


def two_sum_sorted(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return i, j
        if s < target:
            i += 1
        else:
            j -= 1
    return None


def remove_duplicates_sorted(nums):
    if not nums:
        return []
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return nums[:write]


def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


def max_water(heights):
    i, j, best = 0, len(heights) - 1, 0
    while i < j:
        best = max(best, (j - i) * min(heights[i], heights[j]))
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return best


def reverse_in_place(seq):
    i, j = 0, len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i, j = i + 1, j - 1
    return seq


nums = [1, 3, 4, 6, 8, 11, 15]
for t in (10, 19, 2):
    print(f"two_sum({t}) ->", two_sum_sorted(nums, t))
print("dedupe:", remove_duplicates_sorted([1, 1, 2, 3, 3, 3, 4, 5, 5]))
print("merge:", merge_sorted([1, 4, 9, 12], [2, 3, 10, 20, 25]))
print("max water:", max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("reversed:", reverse_in_place(list("two-pointer")))
