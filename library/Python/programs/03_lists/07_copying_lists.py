"""Compare assignment, shallow copies and deep copies of lists."""

import copy

original = [1, 2, [3, 4]]
alias = original
shallow1 = original[:]
shallow2 = list(original)
shallow3 = original.copy()
deep = copy.deepcopy(original)

original.append(5)
original[2].append("x")

print("original:", original)
print("alias:   ", alias, "| same object:", alias is original)
print("slice:   ", shallow1)
print("list():  ", shallow2)
print(".copy(): ", shallow3)
print("deepcopy:", deep)
print("inner shared by shallow copy:", shallow1[2] is original[2])
print("inner shared by deep copy:", deep[2] is original[2])

# copying a grid
grid = [[0, 0], [0, 0]]
row_copy = [row[:] for row in grid]
row_copy[0][0] = 9
print("grid untouched:", grid, "copy:", row_copy)

# deepcopy handles self-references
loop = [1, 2]
loop.append(loop)
cloned = copy.deepcopy(loop)
print("cloned refers to itself:", cloned[2] is cloned, "and not original:", cloned[2] is not loop)

# equality vs identity
a = [1, [2, 3]]
b = copy.deepcopy(a)
print("a == b:", a == b, "| a is b:", a is b)


def append_safely(items, value):
    result = items.copy()
    result.append(value)
    return result


base = [10, 20]
extended = append_safely(base, 30)
print("base:", base, "extended:", extended)
