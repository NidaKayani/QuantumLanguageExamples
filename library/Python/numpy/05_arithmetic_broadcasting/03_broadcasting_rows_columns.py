"""Broadcasting row and column vectors against a 2-D table."""
import numpy as np

# sales[store, month]
sales = np.array([
    [120, 135, 150, 160],
    [ 80,  95,  90, 110],
    [200, 210, 190, 230],
])
print("sales:")
print(sales)
print("shape:", sales.shape)

# a row vector (shape (4,)) broadcasts across every store
monthly_bonus = np.array([5, 0, 10, 15])
print("sales + monthly_bonus:")
print(sales + monthly_bonus)

# a column vector (shape (3, 1)) broadcasts across every month
store_factor = np.array([[1.0], [1.5], [0.8]])
print("store_factor shape:", store_factor.shape)
print("sales * store_factor:")
print(sales * store_factor)

# center each column (subtract column means)
col_means = sales.mean(axis=0)
print("column means:", col_means)
centered = sales - col_means
print("column-centered:")
print(centered)

# normalize each row to fractions of the row total
row_totals = sales.sum(axis=1, keepdims=True)
print("row totals (keepdims):")
print(row_totals)
shares = sales / row_totals
print("row shares:")
print(np.round(shares, 3))
print("rows sum to 1:", np.round(shares.sum(axis=1), 10))

# the same column vector built with reshape and None
v = np.array([1, 2, 3])
print("v.reshape(-1, 1):")
print(v.reshape(-1, 1))
print("v[:, None] + np.array([10, 20, 30, 40]):")
print(v[:, None] + np.array([10, 20, 30, 40]))

# shapes after broadcasting
for s1, s2 in [((3, 1), (1, 4)), ((5,), (2, 5)), ((2, 1, 3), (4, 1))]:
    res = np.zeros(s1) + np.zeros(s2)
    print(s1, "+", s2, "->", res.shape)

print(repr(np.broadcast_to(np.array([1, 2, 3]), (2, 3))))
