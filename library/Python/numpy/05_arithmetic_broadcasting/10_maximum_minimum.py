"""Elementwise np.maximum/np.minimum for clamping, ReLU and envelope tracking."""
import numpy as np


def lcg(seed, n, mod=1000):
    out = []
    state = seed
    for _ in range(n):
        state = (state * 1103515245 + 12345) % (2 ** 31)
        out.append(state % mod)
    return np.array(out)


signal = (lcg(7, 12) - 500) / 100.0
print("signal:", signal)
print(repr(signal))

relu = np.maximum(signal, 0)
print("ReLU:  ", relu)
leaky = np.maximum(signal, 0.1 * signal)
print("leaky: ", leaky)

# clamping with minimum(maximum(...))
clamped = np.minimum(np.maximum(signal, -2.0), 2.0)
print("clamped to [-2, 2]:", clamped)
print("same as np.clip:", np.array_equal(clamped, np.clip(signal, -2.0, 2.0)))

# elementwise max of two arrays vs reduction max
a = lcg(1, 8, 50)
b = lcg(2, 8, 50)
print("a:", a)
print("b:", b)
print("np.maximum(a, b):", np.maximum(a, b))
print("np.minimum(a, b):", np.minimum(a, b))
print("max(a) =", a.max(), " np.max(b) =", np.max(b))

# running max (envelope) via maximum.accumulate
prices = 100 + np.cumsum(lcg(3, 10, 21) - 10)
peak = np.maximum.accumulate(prices)
drawdown = peak - prices
print("prices:  ", prices)
print("peak:    ", peak)
print("drawdown:", drawdown)
print("max drawdown:", drawdown.max())

# broadcasting: per-column floors and per-row caps
data = lcg(11, 12, 100).reshape(3, 4)
floors = np.array([20, 30, 40, 50])
caps = np.array([[60], [70], [80]])
print("data:")
print(data)
print("bounded:")
print(np.minimum(np.maximum(data, floors), caps))

# np.fmax ignores NaN, np.maximum propagates it
p = np.array([1.0, np.nan, 3.0])
q = np.array([2.0, 2.0, np.nan])
print("np.maximum:", np.maximum(p, q))
print("np.fmax:   ", np.fmax(p, q))
