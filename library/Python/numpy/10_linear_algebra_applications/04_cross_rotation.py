"""3-D geometry: cross products, triangle normals and rotation matrices."""
import math
import numpy as np

x_axis = np.array([1.0, 0.0, 0.0])
y_axis = np.array([0.0, 1.0, 0.0])
print("x cross y =", np.cross(x_axis, y_axis))
print("y cross x =", np.cross(y_axis, x_axis))

a = np.array([2, 3, 4])
b = np.array([5, 6, 7])
c = np.cross(a, b)
print("a cross b =", c)
print(repr(c))
print("orthogonal to a and b:", np.dot(c, a), np.dot(c, b))

# Triangle area and unit normal
p0 = np.array([0.0, 0.0, 0.0])
p1 = np.array([4.0, 0.0, 0.0])
p2 = np.array([0.0, 3.0, 0.0])
n = np.cross(p1 - p0, p2 - p0)
print("triangle normal:", n, "area:", f"{np.linalg.norm(n) / 2:.6f}")

# Batch of cross products
U = np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0]])
V = np.array([[0, 1, 0], [0, 0, 1], [0, 1, 1]])
print("row-wise cross products:")
print(np.cross(U, V))


def rot_z(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def rot_x(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[1.0, 0.0, 0.0], [0.0, c, -s], [0.0, s, c]])


Rz = rot_z(math.pi / 2)
print("Rz(90deg) =")
print(np.round(Rz, 6) + 0.0)
print("Rz @ x =", np.round(Rz @ x_axis, 6) + 0.0)
print("orthogonal (R.T @ R = I):", bool(np.allclose(Rz.T @ Rz, np.eye(3))))
print("det(Rz) =", f"{np.linalg.det(Rz):.6f}")

# Rotations compose; 4 quarter turns return to identity
four = np.linalg.matrix_power(Rz, 4)
print("Rz^4 ~ I:", bool(np.allclose(four, np.eye(3))))

R = rot_x(math.pi / 6) @ rot_z(math.pi / 3)
square = np.array([[1.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, -1.0, 0.0], [1.0, -1.0, 0.0]])
rotated = square @ R.T
print("rotated square corners:")
print(np.round(rotated, 6))
print("lengths preserved:", bool(np.allclose(np.linalg.norm(rotated, axis=1), np.linalg.norm(square, axis=1))))

# 2-D rotation of a polygon
theta = math.radians(45)
R2 = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
tri = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, 0.0]])
print("2-D rotated triangle:")
print(np.round(tri @ R2.T, 6))
