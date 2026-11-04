"""Multi-key sorting of tabular data with np.lexsort (last key is primary)."""
import numpy as np

# Employee table: department id, years of service, salary (in thousands)
dept = np.array([2, 1, 3, 1, 2, 3, 1, 2, 3, 1])
years = np.array([5, 3, 8, 3, 1, 8, 10, 5, 2, 7])
salary = np.array([62.5, 48.0, 91.0, 51.5, 40.0, 87.25, 99.0, 64.0, 55.5, 70.0])
emp_id = np.arange(100, 110)

print("dept:  ", dept)
print("years: ", years)
print("salary:", salary)

# Sort by department, then by years (descending), then by salary
order = np.lexsort((salary, -years, dept))
print("lexsort order:", order)
print(repr(order))

table = np.column_stack((emp_id, dept, years, salary))
print("sorted table (id, dept, years, salary):")
print(table[order])

# Two-key sort of points: by x, ties broken by y
xs = np.array([3, 1, 2, 1, 3, 2, 1])
ys = np.array([0, 5, 2, 1, 4, 1, 3])
pts_order = np.lexsort((ys, xs))
points = np.stack((xs, ys), axis=1)
print("points sorted by (x, y):")
print(points[pts_order])

# Sorting rows of a 2-D array lexicographically: keys are columns reversed
rows = np.array([[2, 9, 1],
                 [1, 4, 4],
                 [2, 3, 7],
                 [1, 4, 2],
                 [0, 8, 8]])
row_order = np.lexsort(rows.T[::-1])
print("rows lexicographically sorted:")
print(rows[row_order])

# Top earner per department using the sorted order
by_dept_salary = np.lexsort((-salary, dept))
sorted_dept = dept[by_dept_salary]
first = np.concatenate(([True], sorted_dept[1:] != sorted_dept[:-1]))
leaders = by_dept_salary[first]
for i in leaders:
    print(f"dept {dept[i]}: top earner id {emp_id[i]} with {salary[i]:.2f}k")

# Compare with a stable argsort chain giving the same answer
chain = np.argsort(salary, kind="stable")
chain = chain[np.argsort(-years[chain], kind="stable")]
chain = chain[np.argsort(dept[chain], kind="stable")]
print("stable argsort chain matches lexsort:", bool(np.array_equal(chain, order)))
