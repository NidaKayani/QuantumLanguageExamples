"""Covariance and Pearson correlation between a few small measurement series."""
import numpy as np

hours_studied = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
exam_score = np.array([52.0, 58.0, 65.0, 70.0, 79.0, 83.0])
tv_hours = np.array([5.0, 4.5, 4.0, 2.5, 2.0, 1.0])

print("hours:", hours_studied)
print("score:", exam_score)
print("tv:   ", tv_hours)

cov2 = np.cov(hours_studied, exam_score)
print("2x2 covariance (ddof=1 default):")
print(cov2)
print(repr(np.round(cov2, 4)))
print("population covariance (bias=True):")
print(np.cov(hours_studied, exam_score, bias=True))

r = np.corrcoef(hours_studied, exam_score)
print("corrcoef matrix:")
print(np.round(r, 5))
print("r(hours, score) =", round(float(r[0, 1]), 5))

data = np.vstack([hours_studied, exam_score, tv_hours])
print("data shape (variables x observations):", data.shape)
C = np.cov(data)
print("3x3 covariance:")
print(np.round(C, 3))
R = np.corrcoef(data)
print("3x3 correlation:")
print(np.round(R, 4))
print("diagonal of R:", np.diag(R))
print("symmetric:", np.allclose(R, R.T))

# rowvar=False: columns are variables
obs = data.T
print("obs shape:", obs.shape)
print("same with rowvar=False:", np.allclose(np.cov(obs, rowvar=False), C))

# manual Pearson r
x = hours_studied - hours_studied.mean()
y = tv_hours - tv_hours.mean()
manual_r = (x * y).sum() / np.sqrt((x ** 2).sum() * (y ** 2).sum())
print("manual r(hours, tv):", round(float(manual_r), 5))
print("matches np.corrcoef:", np.isclose(manual_r, R[0, 2]))

ints = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])
print("perfectly correlated ints:")
print(np.corrcoef(ints))
