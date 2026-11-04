"""Convert numbers between binary, octal, hexadecimal and arbitrary bases."""

for n in (0, 5, 42, 255, 1000, -19):
    print(f"{n:>5}: bin={bin(n):>12} oct={oct(n):>7} hex={hex(n):>6}")

print("\nparsing with int(x, base):")
for text, base in (("101010", 2), ("777", 8), ("ff", 16), ("0xff", 16), ("0b1101", 0), ("z", 36), ("helloworld", 36)):
    print(f"  int({text!r}, {base}) = {int(text, base)}")

print("literals:", 0b1010, 0o17, 0xFF, 1_000_000)
print("format without prefix:", format(255, "b"), format(255, "o"), format(255, "x"), format(255, "08b"))

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def to_base(n, base):
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(DIGITS[r])
    return sign + "".join(reversed(out))


for base in (2, 3, 7, 16, 36):
    s = to_base(123456789, base)
    print(f"123456789 in base {base:>2}: {s}  (round trip {int(s, base) == 123456789})")

print("-255 base 16:", to_base(-255, 16))
print("bit_count of 255:", (255).bit_count(), "| bit_length of 1000:", (1000).bit_length())

roman_values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def to_roman(n):
    out = ""
    for value, sym in roman_values:
        count, n = divmod(n, value)
        out += sym * count
    return out


print("roman:", {y: to_roman(y) for y in (4, 9, 14, 1994, 2024, 3999)})
try:
    int("12z", 10)
except ValueError as e:
    print("ValueError:", e)
