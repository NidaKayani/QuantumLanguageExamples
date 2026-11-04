"""3-D indexing with ellipsis, np.newaxis and None for adding axes."""
import numpy as np

# A small "video": 3 frames of 4x5 pixels
video = np.arange(60).reshape(3, 4, 5)
print("video shape:", video.shape)
print(video)

print("frame 1:")
print(video[1])
print("pixel (2, 3) across all frames:", video[:, 2, 3])
print("row 0 of every frame:")
print(video[:, 0, :])

# Ellipsis stands for "as many : as needed"
print("last column of every row in every frame:")
print(video[..., -1])
print("same as video[:, :, -1]:", np.array_equal(video[..., -1], video[:, :, -1]))
print("frame 2, ellipsis, col 0:", video[2, ..., 0])
print("video[...] is full view shape:", video[...].shape)

# np.newaxis / None insert length-1 axes
v = np.array([1.0, 2.0, 3.0])
print("v:", v, v.shape)
col = v[:, np.newaxis]
row = v[np.newaxis, :]
print("column vector shape:", col.shape)
print(col)
print("row vector shape:", row.shape)
print(repr(row))
print("outer product via broadcasting:")
print(col * row)

# None is an alias for np.newaxis
print("np.newaxis is None:", np.newaxis is None)
print("v[None, :, None].shape:", v[None, :, None].shape)

# Combine ellipsis and newaxis
x = np.arange(24).reshape(2, 3, 4)
y = x[..., None]
print("x[..., None].shape:", y.shape)
z = x[:, None, ...]
print("x[:, None, ...].shape:", z.shape)

# Pairwise differences of points with newaxis
pts = np.array([[0.0, 0.0], [3.0, 4.0], [6.0, 8.0], [1.0, 1.0]])
diff = pts[:, None, :] - pts[None, :, :]
dist = np.sqrt((diff ** 2).sum(axis=-1))
print("pairwise distances:")
print(dist)
print(repr(dist[0]))

# Per-frame normalisation using keepdims-like indexing
frame_max = video.max(axis=(1, 2))
norm = video / frame_max[:, None, None]
print("frame maxima:", frame_max)
print("normalised frame 0, first row:", norm[0, 0])
