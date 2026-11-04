"""Array-scalar arithmetic: unit conversions and price adjustments."""
import numpy as np

celsius = np.array([-10.0, 0.0, 12.5, 21.0, 37.0, 100.0])
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print("Celsius:   ", celsius)
print("Fahrenheit:", fahrenheit)
print("Kelvin:    ", kelvin)
print(repr(fahrenheit))

# scalar on the left side
print("100 - celsius:", 100 - celsius)
print("1 / (kelvin):", 1 / kelvin)
print("2 ** arange:", 2 ** np.arange(8))

prices = np.array([19.99, 5.49, 120.0, 0.99, 42.5])
discounted = prices * 0.85
taxed = discounted * 1.07
print("prices:    ", prices)
print("discounted:", discounted)
print("with tax:  ", np.round(taxed, 2))
print("total: %.2f" % taxed.sum())

# integer arrays stay integer with integer scalars
counts = np.array([3, 14, 15, 92, 65])
print("counts * 3 =", counts * 3, counts.dtype)
print("counts + 1.0 =", counts + 1.0, (counts + 1.0).dtype)
print("counts // 10 =", counts // 10)
print("counts % 10 =", counts % 10)
print("counts ** 2 =", counts ** 2)

# Python scalars vs numpy scalars
s = np.float64(2.5)
print("np.float64 scalar * counts:", s * counts)
print(repr(counts * np.int64(-1)))

# a 2-D grid scaled by a scalar
grid = np.arange(12).reshape(3, 4)
print("grid:")
print(grid)
print("grid * 0.5:")
print(grid * 0.5)
print("grid - grid.mean():")
print(grid - grid.mean())
