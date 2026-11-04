"""Demonstrate wrap-around overflow in small integer types such as int8 and uint8."""
import numpy as np

pixels = np.array([200, 250, 10, 0], dtype=np.uint8)
print("Pixels:", pixels)
print(repr(pixels))

brighter = pixels + np.uint8(60)
print("Add 60 (wraps modulo 256):", brighter)

darker = pixels - np.uint8(20)
print("Subtract 20 (wraps below 0):", darker)

# Safe version: widen first, clip, then narrow
safe = np.clip(pixels.astype(np.int64) + 60, 0, 255).astype(np.uint8)
print("Saturating add:", repr(safe))

small = np.array([120, 127, -128, -100], dtype=np.int8)
print("int8 values:", repr(small))
print("+10:", small + np.int8(10))
print("negate:", -small)
print("*2:", small * np.int8(2))

counter = np.zeros(1, dtype=np.int8)
for _ in range(130):
    counter += 1
print("int8 counter after 130 increments:", counter)

# astype from int64 to narrow types wraps as well
wide = np.array([255, 256, 257, 300, -1])
print("int64 -> uint8:", repr(wide.astype(np.uint8)))
print("int64 -> int8:", repr(wide.astype(np.int8)))

# int16 has much more headroom
s16 = np.array([30000, -30000], dtype=np.int16)
print("int16:", s16, "+ 5000 ->", s16 + np.int16(5000))

# Byte checksum computed with uint8 wrap-around
data = np.array([17, 200, 99, 240, 5, 128], dtype=np.uint8)
running = np.cumsum(data, dtype=np.uint8)
print("uint8 running checksum:", running)
checksum = running[-1]
print("Same as sum mod 256:", int(data.astype(np.int64).sum()) % 256)
