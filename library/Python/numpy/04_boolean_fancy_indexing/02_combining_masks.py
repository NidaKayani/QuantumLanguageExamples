"""Combining boolean masks with &, |, ~, ^ and the np.logical_* functions."""
import numpy as np

ages = np.array([23, 35, 47, 19, 62, 31, 55, 28, 41, 70])
incomes = np.array([32.0, 58.5, 74.0, 12.0, 49.0, 66.0, 91.5, 40.0, 52.5, 30.0])
member = np.array([True, False, True, False, True, True, False, True, False, True])

adult_mid = (ages >= 30) & (ages < 60)
print("30 <= age < 60:", adult_mid)
print("ages:", ages[adult_mid])

young_or_old = (ages < 25) | (ages >= 65)
print("young or old ages:", ages[young_or_old])

non_members = ~member
print("non-member incomes:", incomes[non_members])

exclusive = (incomes > 50) ^ member
print("high income XOR member:", exclusive)

# Same with np.logical_* functions
la = np.logical_and(ages > 40, incomes > 50)
lo = np.logical_or(ages < 20, incomes > 90)
ln = np.logical_not(member)
lx = np.logical_xor(ages > 40, member)
print("logical_and:", la)
print("logical_or:", lo)
print("logical_not equals ~:", np.array_equal(ln, ~member))
print("logical_xor:", lx)

# Precedence pitfall: parentheses are required
target = member & (incomes >= 40) & ~(ages > 60)
print("target group ages:", ages[target], "incomes:", incomes[target])

# Reduce a list of masks
conds = [ages > 25, incomes > 35, member]
all_three = np.logical_and.reduce(conds)
any_of = np.logical_or.reduce(conds)
print("all three:", all_three)
print("any of:", any_of)

# 2-D mask combination
m = np.arange(25).reshape(5, 5)
r, c = np.indices(m.shape)
diag_band = np.abs(r - c) <= 1
odd = m % 2 == 1
combo = diag_band & ~odd
print("tri-diagonal band:")
print(diag_band.astype(np.int64))
print("even values in band:", m[combo])
print(repr(combo))

# Count combinations in a small contingency table
table = np.array([[np.sum(member & (incomes > 50)), np.sum(member & (incomes <= 50))],
                  [np.sum(~member & (incomes > 50)), np.sum(~member & (incomes <= 50))]])
print("rows: member/non-member, cols: >50 / <=50")
print(table)
