"""Reducing boolean arrays with np.any and np.all, globally and along axes."""
import numpy as np

# Quiz results: rows = students, cols = questions (1 = correct)
answers = np.array([[1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0]], dtype=bool)
print("answers:")
print(answers)
print(repr(answers))

print("any correct at all:", np.any(answers))
print("all correct overall:", np.all(answers))

print("student got everything right:", answers.all(axis=1))
print("student got at least one right:", answers.any(axis=1))
print("question answered by everyone:", answers.all(axis=0))
print("question nobody answered:", ~answers.any(axis=0))

perfect = np.flatnonzero(answers.all(axis=1))
print("perfect students:", perfect)

# keepdims for broadcasting back
row_any = np.any(~answers, axis=1, keepdims=True)
print("row has a miss (keepdims):")
print(row_any)

# Numeric arrays: non-zero is truthy
counts = np.array([[0, 2, 0], [0, 0, 0], [5, 1, 3]])
print("rows with any nonzero:", np.any(counts, axis=1))
print("columns with all nonzero:", np.all(counts, axis=0))

# Validation checks with any/all
x = np.linspace(0.0, 1.0, 11)
print("x:", x)
print("all in [0, 1]:", bool(np.all((x >= 0) & (x <= 1))))
print("sorted:", bool(np.all(x[:-1] <= x[1:])))
print("contains nan:", bool(np.any(np.isnan(x))))

# Multiple axes in 3-D
cube = np.arange(24).reshape(2, 3, 4) % 5 == 0
print("cube mask:")
print(cube)
print("any over axes (1, 2):", np.any(cube, axis=(1, 2)))
print("any over axis 0:")
print(np.any(cube, axis=0))
print("all over axis 2:")
print(np.all(cube, axis=2))

# Empty-array conventions
empty = np.array([], dtype=bool)
print("any(empty):", np.any(empty), " all(empty):", np.all(empty))

# Filter rows that contain no negative values
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, -1.0, 6.0],
                 [7.0, 8.0, 9.0],
                 [-2.0, 0.0, 1.0]])
clean = data[np.all(data >= 0, axis=1)]
print("rows without negatives:")
print(clean)
