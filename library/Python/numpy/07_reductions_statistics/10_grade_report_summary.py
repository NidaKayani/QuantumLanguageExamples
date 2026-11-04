"""A descriptive-statistics summary report combining many reductions over class data."""
import numpy as np


def make_scores(n_students, n_tests, seed=42):
    state = seed
    vals = []
    for _ in range(n_students * n_tests):
        state = (state * 69069 + 1) % (2 ** 32)
        vals.append(50 + (state >> 8) % 51)
    return np.array(vals).reshape(n_students, n_tests)


scores = make_scores(12, 5)
print("score table:")
print(scores)
print("dtype:", scores.dtype, "shape:", scores.shape)


def describe(x):
    x = np.asarray(x, dtype=float)
    q1, med, q3 = np.percentile(x, [25, 50, 75])
    return {
        "count": x.size,
        "mean": round(float(x.mean()), 3),
        "std": round(float(x.std(ddof=1)), 3),
        "min": float(x.min()),
        "25%": float(q1),
        "50%": float(med),
        "75%": float(q3),
        "max": float(x.max()),
    }


for t in range(scores.shape[1]):
    print(f"test {t + 1}:", describe(scores[:, t]))

totals = scores.sum(axis=1)
print("totals:", totals)
ranking = np.argsort(-totals)
print("ranking (student index):", ranking)
print("top student:", ranking[0], "with", totals[ranking[0]])

letter_edges = np.array([0, 60, 70, 80, 90, 101])
avg = scores.mean(axis=1)
hist, _ = np.histogram(avg, bins=letter_edges)
for letter, n in zip("FDCBA", hist):
    print(f"  {letter}: {n}")

passed = scores >= 65
print("pass rate per test:", np.round(passed.mean(axis=0), 3))
print("students passing all:", np.flatnonzero(passed.all(axis=1)))

print("test means:", repr(np.round(scores.mean(axis=0), 2)))
print("hardest test:", int(np.argmin(scores.mean(axis=0))) + 1)
print("correlation test1 vs test2:", round(float(np.corrcoef(scores[:, 0], scores[:, 1])[0, 1]), 4))
vals, counts = np.unique(scores // 10 * 10, return_counts=True)
print("decade buckets:", dict(zip(vals.tolist(), counts.tolist())))
