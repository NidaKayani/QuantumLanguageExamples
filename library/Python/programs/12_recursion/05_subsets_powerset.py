"""Power sets, combinations and subset-sum via recursion and backtracking."""


def powerset(items):
    if not items:
        return [[]]
    rest = powerset(items[1:])
    return rest + [[items[0]] + s for s in rest]


def combinations(items, k, start=0, chosen=None):
    chosen = [] if chosen is None else chosen
    if len(chosen) == k:
        yield tuple(chosen)
        return
    for i in range(start, len(items)):
        chosen.append(items[i])
        yield from combinations(items, k, i + 1, chosen)
        chosen.pop()


def subset_sums(nums, target, idx=0, path=()):
    if target == 0:
        yield path
        return
    if idx == len(nums) or target < 0:
        return
    yield from subset_sums(nums, target - nums[idx], idx + 1, path + (nums[idx],))
    yield from subset_sums(nums, target, idx + 1, path)


subsets = powerset(["x", "y", "z"])
print(f"{len(subsets)} subsets:")
for s in sorted(subsets, key=lambda s: (len(s), s)):
    print("  {" + ", ".join(s) + "}")

print("C(5, 3):", list(combinations("abcde", 3)))

coins = [8, 6, 7, 5, 3, 10, 9]
print("subsets of", coins, "summing to 15:")
for combo in subset_sums(coins, 15):
    print("  ", " + ".join(map(str, combo)))

def count_subsets_with_sum(nums, target):
    if target == 0:
        return 1
    if not nums or target < 0:
        return 0
    return count_subsets_with_sum(nums[1:], target - nums[0]) + count_subsets_with_sum(nums[1:], target)

print("count via pure recursion:", count_subsets_with_sum(coins, 15))
