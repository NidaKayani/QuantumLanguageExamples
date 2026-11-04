"""Reversing arrays with np.flip, np.fliplr, np.flipud and negative-step slices."""
import numpy as np

word_codes = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("original:", word_codes)
print("np.flip:", np.flip(word_codes))
print("slice [::-1]:", word_codes[::-1])
print("same:", np.array_equal(np.flip(word_codes), word_codes[::-1]))

m = np.arange(1, 13).reshape(3, 4)
print("m:")
print(m)
print("fliplr (mirror left-right):")
print(np.fliplr(m))
print("flipud (mirror up-down):")
print(np.flipud(m))
print("flip axis=0 equals flipud:", np.array_equal(np.flip(m, axis=0), np.flipud(m)))
print("flip both axes:")
print(np.flip(m))
print("rot180 via flip equals rot90 twice:", np.array_equal(np.flip(m), np.rot90(m, 2)))

# flip returns a view
f = np.flip(m, axis=1)
print("flip is a view:", np.shares_memory(f, m))

# Palindrome check for integer sequences
def is_palindrome(arr):
    return bool(np.all(arr == arr[::-1]))

for seq in ([1, 2, 3, 2, 1], [1, 2, 2, 1], [1, 2, 3]):
    print(seq, "palindrome?", is_palindrome(np.array(seq)))

# Symmetric image: mirror left half to the right
half = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
sym = np.hstack([half, np.fliplr(half)])
print("mirrored image:")
print(sym)

# 3-D flip along a chosen axis
cube = np.arange(8).reshape(2, 2, 2)
print("cube:")
print(cube)
print("flip axis=2:")
print(np.flip(cube, axis=2))
print("flip axes (0, 1):")
print(repr(np.flip(cube, axis=(0, 1))))

# Reverse cumulative sum (sum from the right)
vals = np.array([0.5, 1.0, 1.5, 2.0])
rev_cumsum = np.flip(np.cumsum(np.flip(vals)))
print("reverse cumsum:", rev_cumsum)
