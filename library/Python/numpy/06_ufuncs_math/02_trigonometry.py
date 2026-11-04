"""Trigonometric ufuncs on sampled angles: sin, cos, tan and identities."""
import numpy as np

angles_deg = np.array([0, 30, 45, 60, 90, 120, 180, 270, 360])
angles = np.radians(angles_deg)
print("degrees:", angles_deg)
print("radians:", angles)
print(repr(angles))

s = np.sin(angles)
c = np.cos(angles)
print("sin:", np.round(s, 6))
print("cos:", np.round(c, 6))
print("sin^2 + cos^2 == 1:", np.allclose(s ** 2 + c ** 2, 1.0))

# tan away from the poles
safe = np.radians(np.array([-60, -45, 0, 30, 45, 60]))
print("tan:", np.tan(safe))
print("tan == sin/cos:", np.allclose(np.tan(safe), np.sin(safe) / np.cos(safe)))

# inverse functions
vals = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
print("arcsin (deg):", np.degrees(np.arcsin(vals)))
print("arccos (deg):", np.degrees(np.arccos(vals)))
print("arctan (deg):", np.degrees(np.arctan(vals)))

# sample a sine wave and find zero crossings
t = np.linspace(0, 2 * np.pi, 17)
wave = 3 * np.sin(2 * t) + 0.5
print("wave:")
print(np.round(wave, 3))
crossings = np.nonzero(np.sign(wave[:-1]) != np.sign(wave[1:]))[0]
print("sign changes between indices:", crossings)

# double-angle identities checked on a grid
th = np.linspace(-np.pi, np.pi, 13)
print("sin(2x) == 2 sin x cos x:", np.allclose(np.sin(2 * th), 2 * np.sin(th) * np.cos(th)))
print("cos(2x) == 1 - 2 sin^2 x:", np.allclose(np.cos(2 * th), 1 - 2 * np.sin(th) ** 2))

# rotation matrix built from cos/sin
theta = np.radians(30.0)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
print("rotation by 30 deg:")
print(R)
square = np.array([[1, 1, -1, -1], [1, -1, -1, 1]], dtype=np.float64)
print("rotated square corners:")
print(np.round(R @ square, 4))

# hyperbolic functions
h = np.array([-1.0, 0.0, 1.0, 2.0])
print("sinh:", np.sinh(h))
print("cosh:", np.cosh(h))
print("tanh:", np.tanh(h))
