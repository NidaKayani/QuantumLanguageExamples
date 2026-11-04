"""Absolute value and sign: deviations, direction changes and copysign."""
import numpy as np

changes = np.array([3, -2, 0, 5, -7, -1, 4, 0, -3])
print("changes:", changes)
print("np.abs:  ", np.abs(changes))
print("np.absolute:", np.absolute(changes))
print("np.sign: ", np.sign(changes))
print(repr(np.sign(changes)))

ups = (np.sign(changes) > 0).sum()
downs = (np.sign(changes) < 0).sum()
print("up moves:", ups, " down moves:", downs)

# mean absolute deviation and max absolute error
obs = np.array([10.2, 9.8, 11.5, 8.9, 10.0, 10.6])
pred = np.array([10.0, 10.0, 11.0, 9.5, 10.0, 10.0])
err = obs - pred
print("errors:", err)
print("abs errors:", np.abs(err))
print("MAE: %.4f" % np.abs(err).mean())
print("max abs error:", np.max(np.abs(err)))
print("mean abs deviation from mean: %.4f" % np.abs(obs - obs.mean()).mean())

# fabs works on floats, sign on floats gives -1., 0., 1.
f = np.array([-3.5, -0.0, 0.0, 2.25])
print("np.fabs:", np.fabs(f))
print("np.sign floats:", np.sign(f))

# copysign transfers the sign
mag = np.array([1.0, 2.0, 3.0, 4.0])
sgn = np.array([-1.0, 1.0, -5.0, 0.5])
print("copysign:", np.copysign(mag, sgn))

# direction changes: sign of consecutive differences
path = np.array([0, 2, 5, 4, 1, 1, 3, 6, 5])
steps = np.sign(np.diff(path))
print("path: ", path)
print("steps:", steps)
turns = np.nonzero(steps[1:] * steps[:-1] < 0)[0] + 1
print("turning points at indices:", turns)

# Manhattan distance matrix with abs and broadcasting
pts = np.array([[0, 0], [2, 3], [-1, 4], [5, -2]])
manhattan = np.abs(pts[:, None, :] - pts[None, :, :]).sum(axis=-1)
print("manhattan distances:")
print(manhattan)

# abs on 2-D and sign-preserving square
m = np.array([[-1.5, 2.0], [0.0, -4.0]])
print("abs(m):")
print(np.abs(m))
print("signed square:")
print(np.sign(m) * m ** 2)
