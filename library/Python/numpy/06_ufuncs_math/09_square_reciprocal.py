"""np.square and np.reciprocal on floats: variance, resistances and harmonic means."""
import numpy as np

x = np.array([-3.0, -1.5, 0.5, 2.0, 4.0, 10.0])
print("x:", x)
print("square:", np.square(x))
print("reciprocal:", np.reciprocal(x))
print(repr(np.reciprocal(x)))
print("square == x**2:", np.array_equal(np.square(x), x ** 2))
print("reciprocal * x == 1:", np.allclose(np.reciprocal(x) * x, 1.0))

# variance and standard deviation by hand
samples = np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
dev = samples - samples.mean()
var = np.square(dev).mean()
print("deviations:", dev)
print("variance:", var, " np.var:", np.var(samples))
print("std:", np.sqrt(var))

# root mean square of a signal
sig = np.array([1.0, -2.0, 3.0, -4.0, 5.0])
rms = np.sqrt(np.mean(np.square(sig)))
print("RMS: %.6f" % rms)

# resistors in parallel: 1/R = sum(1/R_i)
resistors = np.array([100.0, 220.0, 470.0, 1000.0])
r_par = np.reciprocal(np.sum(np.reciprocal(resistors)))
print("resistors:", resistors)
print("parallel resistance: %.4f ohm" % r_par)
print("series resistance:", resistors.sum())

# harmonic mean of speeds over equal distances
speeds = np.array([60.0, 40.0, 80.0])
hmean = speeds.size / np.reciprocal(speeds).sum()
print("harmonic mean speed: %.4f" % hmean)

# inverse-square law on a grid of distances
d = np.linspace(1.0, 5.0, 9)
intensity = 100.0 * np.reciprocal(np.square(d))
print("distances:", d)
print("intensity:", np.round(intensity, 3))

# squares on a 2-D grid and sum of squares per row
M = np.arange(1, 13, dtype=np.float64).reshape(3, 4) / 2
print("M:")
print(M)
print("square(M):")
print(np.square(M))
print("row sums of squares:", np.square(M).sum(axis=1))
print("row norms:", np.sqrt(np.square(M).sum(axis=1)))

# reciprocal with out= into a preallocated array
out = np.empty(4)
np.reciprocal(np.array([0.25, 0.5, 2.0, 8.0]), out=out)
print("reciprocals:", out)

# series: sum of 1/k^2 approaches pi^2/6
k = np.arange(1, 1001, dtype=np.float64)
partial = np.reciprocal(np.square(k)).sum()
print("sum 1/k^2 (k<=1000): %.8f   pi^2/6: %.8f" % (partial, np.pi ** 2 / 6))
