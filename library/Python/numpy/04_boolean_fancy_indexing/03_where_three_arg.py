"""np.where in its 1-argument and 3-argument forms."""
import numpy as np

balance = np.array([120.0, -35.5, 0.0, 410.25, -5.0, 88.0, -150.0])
print(repr(balance))

# 3-arg form: elementwise choice
status = np.where(balance < 0, -1, np.where(balance > 0, 1, 0))
print("sign via nested where:", status)
print("matches np.sign:", np.array_equal(status, np.sign(balance).astype(np.int64)))

# Replace negatives by zero
floored = np.where(balance < 0, 0.0, balance)
print("floored:", floored)

# Apply a fee only to negative balances
with_fee = np.where(balance < 0, balance - 10.0, balance)
print("with overdraft fee:", with_fee)

# Broadcasting scalars and arrays together
bonus = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
print("bonus where positive:", np.where(balance > 0, balance + bonus, balance))

# 1-arg form returns a tuple of index arrays
neg_idx = np.where(balance < 0)
print("np.where(balance < 0):", neg_idx)
print("negative positions:", neg_idx[0])
print("negative values:", balance[neg_idx])

# 2-D: where gives (rows, cols)
temps = np.array([[18, 22, 31],
                  [27, 15, 33],
                  [29, 30, 12]])
rows, cols = np.where(temps >= 29)
print("hot cells:")
for r, c in zip(rows, cols):
    print(f"  ({r}, {c}) -> {temps[r, c]}")

# 2-D 3-arg with broadcasting a row
thresholds = np.array([20, 25, 30])
labelled = np.where(temps > thresholds, temps, -1)
print("values above per-column threshold:")
print(labelled)

# Safe division using where
num = np.array([4.0, 9.0, 0.0, 6.0])
den = np.array([2.0, 0.0, 0.0, 3.0])
safe_den = np.where(den == 0, 1.0, den)
ratio = np.where(den == 0, np.nan, num / safe_den)
print("ratio with nan for div-by-zero:", ratio)
print(repr(ratio))

# Piecewise function
x = np.linspace(-2.0, 2.0, 9)
y = np.where(x < 0, x ** 2, np.where(x < 1, x, 2.0 - x))
print("x:", x)
print("piecewise y:", y)
