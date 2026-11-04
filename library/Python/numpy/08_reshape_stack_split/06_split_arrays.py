"""Breaking arrays apart with split, array_split, hsplit and vsplit."""
import numpy as np

data = np.arange(12)
print(data)

parts = np.split(data, 3)
print("split into 3 equal parts:")
for p in parts:
    print(" ", p)
print(repr(parts[1]))

pieces = np.split(data, [2, 5, 9])
print("split at indices [2, 5, 9]:")
for p in pieces:
    print(" ", p, "len", len(p))

uneven = np.array_split(data, 5)
print("array_split into 5:", [p.tolist() for p in uneven])
print("sizes:", [p.size for p in uneven])

try:
    np.split(data, 5)
except ValueError as exc:
    print("np.split(data, 5) raised ValueError:", exc)

m = np.arange(24).reshape(4, 6)
print(m)
left, mid, right = np.hsplit(m, 3)
print("hsplit into 3, middle:")
print(mid)
top, bottom = np.vsplit(m, 2)
print("vsplit top:")
print(top)
print("vsplit bottom:")
print(bottom)
print("hsplit at [1, 4] shapes:", [p.shape for p in np.hsplit(m, [1, 4])])
print("split axis=1 equals hsplit:", all(np.array_equal(p, q) for p, q in zip(np.split(m, 3, axis=1), np.hsplit(m, 3))))

# train / validation / test split of a small dataset
X = np.arange(20.0).reshape(10, 2)
train, val, test = np.split(X, [6, 8])
print("train shape:", train.shape, "val shape:", val.shape, "test shape:", test.shape)
print("test rows:")
print(test)

# mini-batches with array_split (last batch smaller)
batches = np.array_split(X, 3)
for i, batch in enumerate(batches):
    print(f"batch {i}: shape {batch.shape}, column sums {batch.sum(axis=0)}")

# split features from labels
table = np.array([[1.0, 2.0, 0.0], [3.0, 4.0, 1.0], [5.0, 6.0, 1.0]])
feats, labels = np.hsplit(table, [2])
print("features:")
print(feats)
print("labels:", labels.ravel())
print("rejoined equals original:", np.array_equal(np.hstack([feats, labels]), table))
