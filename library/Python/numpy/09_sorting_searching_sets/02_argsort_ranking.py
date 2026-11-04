"""Ranking students with np.argsort, stable sorting for ties and inverse permutations."""
import numpy as np

names = ["Ava", "Ben", "Cara", "Dan", "Eli", "Fay", "Gus", "Hana"]
points = np.array([88, 92, 75, 92, 60, 88, 99, 75])
print("points:", points)

order = np.argsort(points, kind="stable")
print("argsort (stable):", order)
print(repr(order))
print("points in order:", points[order])

# Descending, keeping original order among ties: sort the negated values stably
desc = np.argsort(-points, kind="stable")
print("descending order indices:", desc)
for rank, idx in enumerate(desc, start=1):
    print(f"  {rank}. {names[idx]:<5} {points[idx]}")

# Rank of each element = inverse permutation of argsort
ranks = np.empty_like(order)
ranks[desc] = np.arange(1, points.size + 1)
print("rank per student:", ranks)

# Dense rank via np.unique
uniq, inverse = np.unique(-points, return_inverse=True)
dense = inverse + 1
print("dense rank:", dense)

# argsort of argsort also gives ranks (0-based, ascending)
print("argsort(argsort):", np.argsort(np.argsort(points, kind="stable"), kind="stable"))

# 2-D argsort along rows
matrix = np.array([[3.5, 1.0, 2.25],
                   [0.5, 4.0, 0.75],
                   [2.0, 2.0, 1.0]])
idx = np.argsort(matrix, axis=1, kind="stable")
print("row-wise argsort:")
print(idx)
print("rows sorted via take_along_axis:")
print(np.take_along_axis(matrix, idx, axis=1))

# Column-wise argsort
col_idx = np.argsort(matrix, axis=0, kind="stable")
print("column-wise argsort:")
print(col_idx)

# Reorder a parallel array
ages = np.array([20, 21, 19, 22, 20, 23, 21, 19])
print("ages ordered by points (desc):", ages[desc])
print("best student:", names[int(np.argmax(points))], "worst:", names[int(np.argmin(points))])
