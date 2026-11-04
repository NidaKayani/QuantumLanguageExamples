"""Use np.linspace for evenly spaced samples, with and without endpoint and retstep."""
import numpy as np

x = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", x)
print(repr(x))

x2 = np.linspace(0, 1, 5, endpoint=False)
print("endpoint=False:", x2)

pts, step = np.linspace(-2, 2, 9, retstep=True)
print("Points:", pts)
print("Step:", step)

pts2, step2 = np.linspace(0, 10, 4, endpoint=False, retstep=True)
print("No endpoint points:", pts2, "step:", step2)

# Sample a function
t = np.linspace(0, np.pi, 7)
s = np.sin(t)
print("t:", t)
print("sin(t):", np.round(s, 4))

# Integer-valued linspace
ints = np.linspace(0, 100, 11)
print("Tens as floats:", ints)
print("Tens as int dtype:", repr(np.linspace(0, 100, 11, dtype=int)))

# Trapezoid area under y = x^2 on [0, 1]
xs = np.linspace(0.0, 1.0, 101)
ys = xs ** 2
dx = xs[1] - xs[0]
area = dx * (ys.sum() - 0.5 * (ys[0] + ys[-1]))
print("Approx integral of x^2:", round(float(area), 6))

single = np.linspace(3, 7, 1)
print("Single sample:", repr(single))

descending = np.linspace(1, 0, 6)
print("Descending:", descending)

# Midpoints between consecutive samples
edges = np.linspace(0, 6, 4)
mids = (edges[:-1] + edges[1:]) / 2
print("Edges:", edges, "Midpoints:", mids)
