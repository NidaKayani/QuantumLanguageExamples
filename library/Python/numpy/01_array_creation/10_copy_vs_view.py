"""Show the difference between views (slices, reshape) and copies (copy, fancy indexing)."""
import numpy as np

a = np.arange(10)
print("Original:", a)

v = a[2:6]
v[0] = 100
print("After editing slice view:", a)
print("view base is a:", v.base is a)
print("shares memory:", np.shares_memory(a, v))

c = a[2:6].copy()
c[0] = -1
print("After editing copy:", a)
print("Copy:", repr(c))
print("copy base:", c.base)

r = a.reshape(2, 5)
r[1, 4] = 999
print("Reshaped view:")
print(r)
print("Original sees change:", a)

f = a[[0, 1, 2]]
f[:] = 0
print("Fancy-index result (copy):", f)
print("Original unchanged:", a)

mask_sel = a[a > 50]
print("Boolean-selected copy:", repr(mask_sel))
print("shares memory with a:", np.shares_memory(a, mask_sel))

m = np.array([[1, 2, 3], [4, 5, 6]])
t = m.T
t[0, 1] = 40
print("Transpose is a view; m now:")
print(m)

ac = np.array(m)
ac[0, 0] = -7
print("np.array copies by default; m[0, 0] =", m[0, 0])
aa = np.asarray(m)
aa[0, 0] = -7
print("np.asarray does not copy; m[0, 0] =", m[0, 0])

step = a[::2]
step *= 2
print("Strided view doubled original evens:", a)
print(repr(a))
