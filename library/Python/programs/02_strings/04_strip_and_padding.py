"""Trim whitespace and pad strings with strip, ljust, rjust, center and zfill."""

raw = "   ***hello***   "
print(repr(raw.strip()))
print(repr(raw.lstrip()))
print(repr(raw.rstrip()))
print(repr(raw.strip().strip("*")))
print(repr("xxyhelloyxx".strip("xy")))

print(repr("prefix_value".removeprefix("prefix_")))
print(repr("report.txt".removesuffix(".txt")))
print(repr("report.txt".removesuffix(".csv")))

items = [("apple", 1.5), ("banana", 0.25), ("cherry", 12.0), ("kiwi", 3.75)]
width = 24
print("+" + "-" * width + "+")
print("|" + "PRICE LIST".center(width) + "|")
print("+" + "-" * width + "+")
for name, price in items:
    left = name.ljust(14, ".")
    right = f"${price:.2f}".rjust(width - 14)
    print("|" + left + right + "|")
print("+" + "-" * width + "+")

for n in (7, 42, 123, -5):
    print(f"{n:>5} -> zfill(5): {str(n).zfill(5)}")

print("centered with fill:", "TITLE".center(21, "="))
print("tabs expanded:", repr("a\tbb\tccc".expandtabs(4)))
