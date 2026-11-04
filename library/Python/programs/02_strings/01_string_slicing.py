"""Slice strings with positive, negative and stepped indices."""

s = "Hello, Python World"

print("full:", s)
print("s[0]:", s[0], "| s[-1]:", s[-1])
print("s[7:13]:", s[7:13])
print("s[:5]:", s[:5])
print("s[7:]:", s[7:])
print("s[-5:]:", s[-5:])
print("s[::2]:", s[::2])
print("s[1::2]:", s[1::2])
print("s[::-1]:", s[::-1])
print("s[-1:-6:-1]:", s[-1:-6:-1])
print("out of range slice:", repr(s[100:200]))

# slice objects can be named and reused
YEAR = slice(0, 4)
MONTH = slice(5, 7)
DAY = slice(8, 10)
for date in ("2024-03-15", "1999-12-31"):
    print(f"{date}: year={date[YEAR]} month={date[MONTH]} day={date[DAY]}")

# rotate a string
word = "rotation"
for k in range(0, 4):
    print(f"rotate {k}: {word[k:] + word[:k]}")

# palindromes via slicing
for candidate in ("racecar", "level", "python", "A man a plan a canal Panama"):
    cleaned = "".join(ch.lower() for ch in candidate if ch.isalnum())
    print(f"{candidate!r} palindrome? {cleaned == cleaned[::-1]}")

print("indices:", slice(1, 20, 3).indices(len(s)))
