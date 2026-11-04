"""Reordering axes with transpose, .T, swapaxes and moveaxis."""
import numpy as np

m = np.arange(6).reshape(2, 3)
print(m)
print("m.T:")
print(m.T)
print(repr(m.T))
print("np.transpose(m) equal to m.T:", np.array_equal(np.transpose(m), m.T))

v = np.array([1, 2, 3])
print("1-D .T is unchanged:", v.T, v.T.shape)

# a batch of 2 images, 3 rows, 4 columns
batch = np.arange(24).reshape(2, 3, 4)
print("batch shape:", batch.shape)
print(batch)

t = batch.transpose(0, 2, 1)
print("transpose(0, 2, 1) shape:", t.shape)
print(t)
print("full reverse .T shape:", batch.T.shape)
print("np.transpose with axes (2, 0, 1):", np.transpose(batch, (2, 0, 1)).shape)

s = np.swapaxes(batch, 0, 2)
print("swapaxes(0, 2) shape:", s.shape)
print(s[:, :, 0])
print("same as batch.swapaxes(2, 0):", np.array_equal(s, batch.swapaxes(2, 0)))

# channels-last -> channels-first, like image layouts (H, W, C) -> (C, H, W)
hwc = np.arange(2 * 2 * 3).reshape(2, 2, 3)
chw = np.moveaxis(hwc, -1, 0)
print("HWC shape:", hwc.shape, "-> CHW shape:", chw.shape)
print("channel 0:")
print(chw[0])
back = np.moveaxis(chw, 0, -1)
print("round trip equal:", np.array_equal(back, hwc))
print("moveaxis multiple:", np.moveaxis(batch, [0, 1], [-1, -2]).shape)

# transpose is a view
mt = m.T
mt[0, 1] = 99
print("after editing m.T, m =")
print(m)

# matrix identity: (A @ B).T == B.T @ A.T
A = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
B = np.array([[0.5, -1.0, 2.0], [1.5, 0.0, -0.5]])
print("(A@B).T == B.T@A.T:", np.allclose((A @ B).T, B.T @ A.T))
print(repr((A @ B).T))
