"""Cumulative sums, products, running max/min and moving averages for a balance sheet."""
import numpy as np

deposits = np.array([100, -20, 35, -50, 80, -10, 25, -60, 40, 15])
print("transactions:", deposits)

balance = np.cumsum(deposits)
print("running balance:", balance)
print(repr(balance))
print("lowest balance:", balance.min(), "at step", balance.argmin())

peak = np.maximum.accumulate(balance)
drawdown = peak - balance
print("running peak:", peak)
print("drawdown:", drawdown)
print("max drawdown:", drawdown.max())
print("running min:", np.minimum.accumulate(balance))

growth = np.array([1.02, 0.98, 1.05, 1.01, 0.97])
print("compound growth factors:", np.round(np.cumprod(growth), 5))
print("factorials:", np.cumprod(np.arange(1, 9)))

# 3-point moving average via cumsum trick
prices = np.array([10.0, 11.0, 12.5, 12.0, 13.5, 14.0, 13.0, 15.5])
c = np.cumsum(np.insert(prices, 0, 0.0))
window = 3
ma = (c[window:] - c[:-window]) / window
print("prices:", prices)
print("3-pt moving average:", np.round(ma, 3))

# running mean
running_mean = np.cumsum(prices) / np.arange(1, prices.size + 1)
print("running mean:", np.round(running_mean, 3))

# cumulative along axes of a 2-D table
table = np.arange(1, 13).reshape(3, 4)
print(table)
print("cumsum axis=0:")
print(np.cumsum(table, axis=0))
print("cumsum axis=1:")
print(table.cumsum(axis=1))
print("cumprod axis=1:")
print(np.cumprod(table, axis=1))
print("flattened cumsum:", table.cumsum())

print("np.diff recovers deposits:", np.array_equal(np.diff(balance, prepend=0), deposits))
print("cumulative count of positives:", np.cumsum(deposits > 0))
