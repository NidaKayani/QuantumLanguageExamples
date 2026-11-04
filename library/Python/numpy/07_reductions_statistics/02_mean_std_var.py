"""Mean, standard deviation and variance with axis, keepdims and ddof."""
import numpy as np

# exam scores: rows = students, columns = exams
scores = np.array([
    [78.0, 85.0, 92.0, 70.0],
    [64.0, 72.0, 58.0, 80.0],
    [90.0, 94.0, 88.0, 97.0],
    [55.0, 61.0, 67.0, 59.0],
    [82.0, 79.0, 85.0, 88.0],
])
print(scores)

print("overall mean:", scores.mean())
print("mean per exam:", scores.mean(axis=0))
print("mean per student:", np.mean(scores, axis=1))

print("population std (ddof=0):", np.std(scores))
print("sample std (ddof=1):", np.std(scores, ddof=1))
print("std per exam ddof=1:", np.round(scores.std(axis=0, ddof=1), 4))
print("var per student:", np.round(scores.var(axis=1), 4))
print("sample var per student:", np.round(np.var(scores, axis=1, ddof=1), 4))

# z-scores per exam using keepdims for broadcasting
mu = scores.mean(axis=0, keepdims=True)
sigma = scores.std(axis=0, keepdims=True)
print("mu shape:", mu.shape, "sigma shape:", sigma.shape)
z = (scores - mu) / sigma
print("z-scores:")
print(np.round(z, 3))
print("z means ~0:", np.allclose(z.mean(axis=0), 0.0))
print("z stds ~1:", np.allclose(z.std(axis=0), 1.0))

# manual check of the variance formula
x = scores[:, 2]
manual = ((x - x.mean()) ** 2).sum() / (x.size - 1)
print("manual sample var of exam 3:", manual)
print("np.var ddof=1 matches:", np.isclose(manual, x.var(ddof=1)))

ints = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print(repr(ints))
print("int mean:", ints.mean(), "int std:", ints.std())
print("mean dtype:", ints.mean().dtype)
print(repr(np.round(scores.mean(axis=1), 2)))
