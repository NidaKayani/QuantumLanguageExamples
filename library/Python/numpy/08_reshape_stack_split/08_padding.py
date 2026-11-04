"""Padding arrays with np.pad in constant and edge modes, e.g. for convolutions."""
import numpy as np

signal = np.array([3, 1, 4, 1, 5])
print(signal)

print("pad 2 zeros each side:", np.pad(signal, 2))
print("pad (1, 3) constant 0:", np.pad(signal, (1, 3), mode="constant"))
print("pad with -1:", np.pad(signal, 2, constant_values=-1))
print("different fill per side:", np.pad(signal, (2, 1), constant_values=(7, 9)))
print("edge mode:", np.pad(signal, 2, mode="edge"))
print(repr(np.pad(signal, (0, 3), mode="edge")))

img = np.array([[1, 2, 3], [4, 5, 6]])
print("image:")
print(img)
z = np.pad(img, 1)
print("zero border:")
print(z)
print(repr(z))
print("rows-only padding ((2, 0), (0, 0)):")
print(np.pad(img, ((2, 0), (0, 0))))
print("edge padding (1, 2):")
print(np.pad(img, ((1, 1), (2, 2)), mode="edge"))

# 3-tap moving average that keeps the length by edge-padding
x = np.array([2.0, 4.0, 8.0, 6.0, 10.0, 12.0])
p = np.pad(x, 1, mode="edge")
smooth = (p[:-2] + p[1:-1] + p[2:]) / 3
print("padded:", p)
print("smoothed:", np.round(smooth, 3))
print("length kept:", smooth.shape == x.shape)

# 3x3 box blur on a small image with zero padding
pic = np.array([
    [0, 0, 9, 0],
    [0, 9, 9, 9],
    [0, 0, 9, 0],
    [0, 0, 0, 0],
], dtype=float)
P = np.pad(pic, 1)
out = np.zeros_like(pic)
for di in range(3):
    for dj in range(3):
        out += P[di:di + pic.shape[0], dj:dj + pic.shape[1]]
out /= 9
print("box blur:")
print(np.round(out, 2))

# pad a ragged batch of sequences to equal length
seqs = [np.array([5, 3]), np.array([1, 2, 3, 4]), np.array([9])]
longest = max(s.size for s in seqs)
batch = np.vstack([np.pad(s, (0, longest - s.size)) for s in seqs])
print("padded batch:")
print(batch)
lengths = (batch != 0).sum(axis=1)
print("lengths:", lengths)
