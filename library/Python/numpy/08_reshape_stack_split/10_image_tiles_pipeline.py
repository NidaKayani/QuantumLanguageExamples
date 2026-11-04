"""Tiling an image into blocks and reassembling it, combining reshape, stack and split."""
import numpy as np

H, W, T = 6, 8, 2
img = (np.arange(H * W) * 7 % 10).reshape(H, W)
print("image:")
print(img)

# cut into T x T tiles: (H, W) -> (H/T, T, W/T, T) -> (H/T, W/T, T, T)
tiles = img.reshape(H // T, T, W // T, T).swapaxes(1, 2)
print("tiles shape:", tiles.shape)
print("tile (0, 1):")
print(tiles[0, 1])
print(repr(tiles[2, 3]))

# per-tile mean (downsampling / average pooling)
pooled = tiles.mean(axis=(2, 3))
print("average-pooled:")
print(pooled)
print("max-pooled:")
print(tiles.max(axis=(2, 3)))

# flatten tiles into a list of patches
patches = tiles.reshape(-1, T * T)
print("patches shape:", patches.shape)
print(patches[:3])

# reassemble and check
rebuilt = patches.reshape(H // T, W // T, T, T).swapaxes(1, 2).reshape(H, W)
print("rebuilt equals image:", np.array_equal(rebuilt, img))

# same thing with split and block stacking
row_strips = np.vsplit(img, H // T)
grid = [np.hsplit(strip, W // T) for strip in row_strips]
print("tile via split (0, 1) matches:", np.array_equal(grid[0][1], tiles[0, 1]))
reassembled = np.vstack([np.hstack(r) for r in grid])
print("vstack/hstack round trip:", np.array_equal(reassembled, img))
print("np.block round trip:", np.array_equal(np.block(grid), img))

# rotate every tile by transposing its last two axes, then restore layout
flipped = np.moveaxis(tiles, -1, -2)
out = flipped.swapaxes(1, 2).reshape(H, W)
print("tile-transposed image:")
print(out)

# add a channel dimension and stack an RGB-like image
rgb = np.stack([img, img // 2, 9 - img], axis=-1)
print("rgb shape:", rgb.shape)
print("channel-first:", np.moveaxis(rgb, -1, 0).shape)
print("pixel (0, 0):", rgb[0, 0])
border = np.pad(img, 1, mode="edge")
print("edge-padded shape:", border.shape)
print(border[:3])
