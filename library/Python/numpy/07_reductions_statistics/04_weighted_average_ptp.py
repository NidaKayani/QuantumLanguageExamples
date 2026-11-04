"""Weighted averages for a grade book plus peak-to-peak ranges."""
import numpy as np

components = ["homework", "quiz", "midterm", "final"]
weights = np.array([0.2, 0.1, 0.3, 0.4])
grades = np.array([
    [92.0, 85.0, 78.0, 88.0],
    [70.0, 95.0, 82.0, 75.0],
    [88.0, 72.0, 91.0, 94.0],
    [60.0, 65.0, 70.0, 68.0],
])
print("weights:", weights)
print(grades)

final = np.average(grades, axis=1, weights=weights)
print("weighted grade per student:", np.round(final, 2))
print("plain mean per student:   ", np.round(grades.mean(axis=1), 2))

avg, wsum = np.average(grades, axis=1, weights=weights, returned=True)
print("returned weight sums:", wsum)
print(repr(np.round(avg, 3)))

manual = (grades * weights).sum(axis=1) / weights.sum()
print("manual matches:", np.allclose(manual, final))

# unnormalised integer weights (credit hours)
gpa_points = np.array([4.0, 3.0, 3.7, 2.3, 4.0])
credits = np.array([3, 4, 3, 2, 1])
print("GPA:", round(float(np.average(gpa_points, weights=credits)), 4))
print("unweighted average:", np.average(gpa_points))

# column-wise average weighted by class size
class_size = np.array([30, 25, 40, 20])
print("component averages:", np.round(np.average(grades, axis=0, weights=class_size), 3))

print("range of each component (ptp):", np.ptp(grades, axis=0))
print("range of each student:", np.ptp(grades, axis=1))
print("overall range:", np.ptp(grades))
for name, spread in zip(components, np.ptp(grades, axis=0)):
    print(f"  {name:>8}: spread {spread:.1f}")

temps = np.array([[-3, 4, 9], [12, 18, 7]])
print(repr(np.ptp(temps, axis=1)))
print(repr(np.ptp(temps, axis=0, keepdims=True)))
