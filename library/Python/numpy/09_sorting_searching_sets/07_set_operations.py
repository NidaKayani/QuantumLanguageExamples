"""Set algebra on arrays: intersect1d, union1d, setdiff1d, setxor1d and isin."""
import numpy as np

# Course enrollments by student id
math_ids = np.array([101, 104, 107, 110, 113, 104, 116])
physics_ids = np.array([104, 105, 110, 111, 116, 120])
chem_ids = np.array([101, 105, 110, 116, 125])

print("math:   ", math_ids)
print("physics:", physics_ids)
print("chem:   ", chem_ids)

both = np.intersect1d(math_ids, physics_ids)
print("math & physics:", both)
print(repr(both))

either = np.union1d(math_ids, physics_ids)
print("math | physics:", either)

only_math = np.setdiff1d(math_ids, physics_ids)
print("math - physics:", only_math)

exactly_one = np.setxor1d(math_ids, physics_ids)
print("math ^ physics:", exactly_one)

# Intersection with indices into the (deduplicated) inputs
common, ia, ib = np.intersect1d(math_ids, chem_ids, return_indices=True)
print("math & chem:", common, "indices in math:", ia, "indices in chem:", ib)

# All three courses: chain intersections
all_three = np.intersect1d(np.intersect1d(math_ids, physics_ids), chem_ids)
print("in all three:", all_three)

# Union of many arrays
everyone = np.union1d(np.union1d(math_ids, physics_ids), chem_ids)
print("all students:", everyone, "count:", everyone.size)

# Membership masks with isin
mask = np.isin(math_ids, chem_ids)
print("math students also in chem (mask):", mask)
print("those ids:", math_ids[mask])
print("not in chem:", math_ids[np.isin(math_ids, chem_ids, invert=True)])

# isin with a 2-D array keeps the shape
seating = np.array([[101, 102, 103],
                    [104, 105, 106],
                    [107, 108, 110]])
print("seats occupied by physics students:")
print(np.isin(seating, physics_ids))

# Count how many courses each student takes
counts = (np.isin(everyone, math_ids).astype(int)
          + np.isin(everyone, physics_ids).astype(int)
          + np.isin(everyone, chem_ids).astype(int))
print("courses per student:", counts)
print("students in 2+ courses:", everyone[counts >= 2])

# Float sets
a = np.array([0.5, 1.5, 2.5, 3.5])
b = np.array([1.5, 3.5, 4.5])
print("float intersection:", np.intersect1d(a, b), "union:", np.union1d(a, b))
