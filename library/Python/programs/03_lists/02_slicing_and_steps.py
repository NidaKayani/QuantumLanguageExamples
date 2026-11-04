"""Slice lists with steps, negative indices, and slice assignment."""

nums = list(range(10))
print("nums:", nums)
print("nums[2:7]:", nums[2:7])
print("nums[:3]:", nums[:3], "nums[-3:]:", nums[-3:])
print("nums[::2]:", nums[::2], "nums[1::2]:", nums[1::2])
print("nums[::-1]:", nums[::-1])
print("nums[8:2:-2]:", nums[8:2:-2])
print("nums[-1:-4:-1]:", nums[-1:-4:-1])

# slice assignment can grow or shrink a list
work = nums[:]
work[2:5] = ["a", "b"]
print("replace 3 with 2:", work)
work[1:1] = [100, 200, 300]
print("insert via empty slice:", work)
work[-2:] = []
print("delete tail:", work)

# extended slice assignment needs matching length
evens = list(range(10))
evens[::2] = [0] * 5
print("zero even positions:", evens)
try:
    evens[::2] = [1, 2]
except ValueError as e:
    print("ValueError:", e)

# deleting with a stepped slice
seq = list("abcdefghij")
del seq[::3]
print("del every third:", seq)

# chunks and windows via slicing
data = list(range(1, 12))
chunks = [data[i:i + 4] for i in range(0, len(data), 4)]
print("chunks of 4:", chunks)
windows = [data[i:i + 3] for i in range(len(data) - 2)]
print("first 3 windows:", windows[:3], "count:", len(windows))

# slices never raise IndexError
print("beyond end:", nums[50:], nums[-50:2])
