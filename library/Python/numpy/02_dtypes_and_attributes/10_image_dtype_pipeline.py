"""Process a tiny grayscale image through uint8, float32/float64 and bool dtypes."""
import numpy as np

# Build a deterministic 6x6 "image" with a small LCG
state = 12345
vals = []
for _ in range(36):
    state = (1103515245 * state + 12345) % (2 ** 31)
    vals.append(state % 256)
img = np.array(vals, dtype=np.uint8).reshape(6, 6)
print("uint8 image:")
print(img)
print("dtype:", img.dtype, "nbytes:", img.nbytes, "min/max:", img.min(), img.max())

# Normalize to [0, 1] in float32
norm = img.astype(np.float32) / 255
print("float32 normalized (rounded):")
print(np.round(norm, 3))
print("norm dtype:", norm.dtype, "nbytes:", norm.nbytes)

# Gamma correction in float64
gamma = norm.astype(np.float64) ** 0.5
print("Gamma-corrected dtype:", gamma.dtype)

# Back to uint8
out = np.round(gamma * 255).astype(np.uint8)
print("Back to uint8:")
print(out)
print(repr(out[0]))

# Thresholding gives a bool mask
mask = out > 128
print("Mask (bool):")
print(mask)
print("Bright pixels:", np.count_nonzero(mask), "of", mask.size)

# Use mask as int to compute coverage per row
coverage = mask.astype(np.int64).sum(axis=1)
print("Bright count per row:", coverage)

# Invert safely: 255 - img stays in uint8 range
inv = np.uint8(255) - img
print("Inverted first row:", inv[0])

# Histogram into 4 bins using integer division
bins = (img // 64).astype(np.int64)
print("Bin indices:")
print(bins)
print("Histogram:", np.bincount(bins.ravel(), minlength=4))

# Mean brightness differs slightly between dtypes
print("Mean uint8 image:", round(float(img.mean()), 4))
print("Mean of output:", round(float(out.mean()), 4))
print("Attributes:", out.shape, out.ndim, out.size, out.itemsize)
