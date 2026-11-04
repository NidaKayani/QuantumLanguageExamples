"""Argument unpacking with * and ** at call sites, including multiple unpackings."""


def point3d(x, y, z):
    return f"Point(x={x}, y={y}, z={z})"


def volume(length, width, height):
    return length * width * height


coords = [1, 2, 3]
print(point3d(*coords))

named = {"z": 30, "x": 10, "y": 20}
print(point3d(**named))

print(point3d(*[7], **{"y": 8, "z": 9}))
print(point3d(*(1,), *(2,), 3))

dims = [(2, 3, 4), (1, 1, 1), (5, 5, 2)]
for d in dims:
    print(f"volume{d} = {volume(*d)}")

base = {"length": 2}
extra = {"width": 3, "height": 7}
print("merged kwargs volume:", volume(**base, **extra))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print("transposed:", transposed)

first, *middle, last = range(8)
print("first:", first, "middle:", middle, "last:", last)

print(*["a", "b", "c"], sep=" | ")
print(max(*[3, 9, 2], 5))

pairs = [("alpha", 1), ("beta", 2)]
lookup = dict(pairs, gamma=3)
print("dict:", lookup)
