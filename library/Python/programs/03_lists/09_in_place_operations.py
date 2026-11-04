"""Modify lists in place with +=, *=, reverse, sort and slice deletion."""

nums = [4, 1, 3]
ref = nums

nums += [9, 2]
print("after += :", nums, "| same object:", ref is nums)

nums = nums + [0]
print("after + :", nums, "| same object:", ref is nums)
print("ref still:", ref)

items = ["x", "y"]
items *= 3
print("after *= 3:", items)

data = [5, 3, 8, 1, 9, 2]
data.reverse()
print("reversed in place:", data)
data.sort()
print("sorted in place:", data)
data.sort(key=lambda v: v % 3)
print("sorted by v % 3:", data)

# remove all occurrences in place
values = [1, 2, 3, 2, 4, 2, 5]
values[:] = [v for v in values if v != 2]
print("removed 2s:", values)

# in-place transform keeps references valid
scores = [55, 72, 90]
view = scores
for i, s in enumerate(scores):
    scores[i] = min(100, s + 10)
print("curved:", view)

# removing while iterating backwards is safe
nums2 = list(range(10))
for i in range(len(nums2) - 1, -1, -1):
    if nums2[i] % 3 == 0:
        del nums2[i]
print("no multiples of 3:", nums2)

# extend vs append
a = [1, 2]
a.append([3, 4])
b = [1, 2]
b.extend([3, 4])
print("append:", a, "| extend:", b)
b.extend(range(5, 8))
b.extend("hi")
print("extend with iterables:", b)
