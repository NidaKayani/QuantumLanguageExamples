"""Explore floor division, modulo and divmod with positive and negative operands."""

pairs = [(17, 5), (-17, 5), (17, -5), (-17, -5), (0, 3), (5, 17)]
print(f"{'a':>4} {'b':>4} {'a//b':>6} {'a%b':>5} {'divmod':>10}  check")
for a, b in pairs:
    q, r = divmod(a, b)
    assert q * b + r == a
    print(f"{a:>4} {b:>4} {a // b:>6} {a % b:>5} {str((q, r)):>10}  {q}*{b}+{r}={a}")

# float floor division and modulo
print("7.5 // 2 =", 7.5 // 2, "| 7.5 % 2 =", 7.5 % 2, "| divmod(-7.5, 2) =", divmod(-7.5, 2))

# truncation toward zero differs from floor
for x in (7, -7):
    print(f"{x}/2: floor={x // 2} trunc={int(x / 2)}")


def to_hms(seconds):
    minutes, s = divmod(seconds, 60)
    hours, m = divmod(minutes, 60)
    days, h = divmod(hours, 24)
    return f"{days}d {h:02d}:{m:02d}:{s:02d}"


for secs in (59, 3600, 86399, 100000, 1234567):
    print(f"{secs:>8} s = {to_hms(secs)}")

# clock arithmetic
hour = 22
for delta in (3, -25, 48):
    print(f"{hour}:00 {delta:+d}h -> {(hour + delta) % 24}:00")

# digits via repeated divmod
n = 9045721
digits = []
while n:
    n, d = divmod(n, 10)
    digits.append(d)
print("digits:", digits[::-1], "sum:", sum(digits))

try:
    1 // 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
