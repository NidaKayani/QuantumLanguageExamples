"""2-D image filtering (blur, edge detection) implemented with array slicing."""
import numpy as np


def convolve2d(image, kernel):
    kh, kw = kernel.shape
    h, w = image.shape
    out = np.zeros((h - kh + 1, w - kw + 1))
    # Accumulate one shifted slice per kernel tap (valid convolution, kernel flipped)
    flipped = kernel[::-1, ::-1]
    for i in range(kh):
        for j in range(kw):
            out += flipped[i, j] * image[i:i + h - kh + 1, j:j + w - kw + 1]
    return out


# Synthetic 8x8 "image": bright square on a gradient background
img = np.add.outer(np.arange(8), np.arange(8)).astype(float)
img[2:6, 2:6] += 20.0
print("image:")
print(img)

box = np.ones((3, 3)) / 9.0
blurred = convolve2d(img, box)
print("3x3 box blur:")
print(np.round(blurred, 3))

sobel_x = np.array([[-1.0, 0.0, 1.0],
                    [-2.0, 0.0, 2.0],
                    [-1.0, 0.0, 1.0]])
gx = convolve2d(img, sobel_x)
gy = convolve2d(img, sobel_x.T)
print("Sobel x response:")
print(gx)
magnitude = np.sqrt(gx ** 2 + gy ** 2)
print("edge magnitude:")
print(np.round(magnitude, 3))
edges = magnitude > 40
print("strong edges:")
print(edges)

# Padded convolution keeps the original size
padded = np.pad(img, 1, mode="edge")
same = convolve2d(padded, box)
print("same-size blur shape:", same.shape)
print(repr(np.round(same[0], 4)))

# Laplacian sharpening
lap = np.array([[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]])
print("Laplacian response:")
print(convolve2d(img, lap))

# 2x2 max pooling via reshape
pooled = img.reshape(4, 2, 4, 2).max(axis=(1, 3))
print("2x2 max pool:")
print(pooled)

# Verify against an explicit loop for one output pixel
r, c = 2, 3
manual = np.sum(img[r:r + 3, c:c + 3] * sobel_x[::-1, ::-1])
print("pixel check:", manual == gx[r, c])
