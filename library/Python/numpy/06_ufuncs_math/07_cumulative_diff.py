"""Running totals and differences with np.cumsum, np.cumprod and np.diff."""
import numpy as np

deposits = np.array([100, 50, -30, 200, -120, 75, 0, 40])
balance = np.cumsum(deposits)
print("deposits:", deposits)
print("balance: ", balance)
print(repr(balance))
print("diff recovers deposits:", np.array_equal(np.diff(balance, prepend=0), deposits))

# cumulative product: compounding monthly returns
returns = np.array([0.02, -0.01, 0.03, 0.015, -0.02, 0.01])
growth = np.cumprod(1 + returns)
print("growth factors:", np.round(growth, 5))
print("final value of 1000: %.2f" % (1000 * growth[-1]))

# factorials via cumprod
print("factorials 1..10:", np.cumprod(np.arange(1, 11)))

# first and second differences
x = np.arange(8)
y = x ** 3
print("y = x^3:", y)
print("diff:   ", np.diff(y))
print("diff 2: ", np.diff(y, n=2))
print("diff 3: ", np.diff(y, n=3))

# cumsum and diff along axes of a 2-D table
table = np.array([[3, 1, 4, 1], [5, 9, 2, 6], [5, 3, 5, 8]])
print("table:")
print(table)
print("cumsum axis=0:")
print(np.cumsum(table, axis=0))
print("cumsum axis=1:")
print(np.cumsum(table, axis=1))
print("diff axis=1:")
print(np.diff(table, axis=1))
print("flat cumsum:", np.cumsum(table))

# numeric derivative and integral of a sampled function
t = np.linspace(0, 1, 11)
f = t ** 2
dt = t[1] - t[0]
deriv = np.diff(f) / dt
print("forward-difference derivative:", np.round(deriv, 4))
trap = np.concatenate(([0.0], np.cumsum((f[1:] + f[:-1]) / 2 * dt)))
print("cumulative trapezoid integral:", np.round(trap, 5))
print("exact final:", 1 / 3, " approx:", trap[-1])

# moving average with cumsum
signal = np.array([4.0, 8.0, 6.0, -1.0, -2.0, -3.0, -1.0, 3.0, 4.0, 5.0])
w = 3
cs = np.cumsum(np.insert(signal, 0, 0.0))
moving = (cs[w:] - cs[:-w]) / w
print("moving average (w=3):", moving)

# run lengths with diff on a boolean pattern
flags = np.array([0, 1, 1, 1, 0, 0, 1, 1, 0, 1])
edges = np.diff(np.concatenate(([0], flags, [0])))
starts = np.nonzero(edges == 1)[0]
ends = np.nonzero(edges == -1)[0]
print("runs of 1 start:", starts, " lengths:", ends - starts)
