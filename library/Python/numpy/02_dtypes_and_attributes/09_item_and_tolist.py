"""Extract native Python values from arrays with .item() and .tolist()."""
import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:")
print(m)
print(repr(m))

as_list = m.tolist()
print("tolist:", as_list)
print("type of element:", type(as_list[0][0]).__name__)

print("item(4):", m.item(4), type(m.item(4)).__name__)
print("item(1, 2):", m.item(1, 2))
print("m[1, 2] as array scalar:", repr(m[1, 2]))

f = np.array([0.5, 1.25, 2.0])
fl = f.tolist()
print("float tolist:", fl, type(fl[0]).__name__)

b = np.array([True, False, True])
print("bool tolist:", b.tolist())

single = np.array([42.0])
print("item() from size-1 array:", single.item(), type(single.item()).__name__)

total = m.sum()
print("sum.item():", total.item(), type(total.item()).__name__)

# Converting before building JSON-like structures
report = {
    "rows": m.shape[0],
    "cols": m.shape[1],
    "total": m.sum().item(),
    "row_sums": m.sum(axis=1).tolist(),
    "col_means": m.mean(axis=0).tolist(),
}
print("Report:", report)

# Round trip list -> array -> list
original = [[0, 1], [2, 3], [4, 5]]
arr = np.array(original)
print("Round trip equal:", arr.tolist() == original)

# 0-d tolist returns a plain scalar
print("0-d tolist:", np.array(7).tolist(), type(np.array(7).tolist()).__name__)

# Small int types convert to Python int too
small = np.array([250, 5], dtype=np.uint8)
print("uint8 tolist:", small.tolist(), type(small.tolist()[0]).__name__)

try:
    m.item()
except ValueError as exc:
    print("item() on multi-element array:", exc)

cube = np.arange(8).reshape(2, 2, 2)
print("3-D tolist:", cube.tolist())
