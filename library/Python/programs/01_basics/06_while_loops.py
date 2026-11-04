"""Use while loops for iteration with unknown bounds such as Collatz and digit sums."""


def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def digit_sum(n):
    total = 0
    while n:
        n, digit = divmod(n, 10)
        total += digit
    return total


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for n in (1, 6, 7, 27, 97):
    print(f"collatz({n}) takes {collatz_steps(n)} steps")

for n in (0, 9, 1234, 987654321):
    print(f"digit_sum({n}) = {digit_sum(n)}")

print("gcd(1071, 462) =", gcd(1071, 462))

# doubling until exceeding a threshold
value, count = 1, 0
while value <= 1_000_000:
    value *= 2
    count += 1
print(f"2**{count} = {value} is the first power of two above a million")

# while with break and continue
n = 0
odds = []
while True:
    n += 1
    if n % 2 == 0:
        continue
    if n > 15:
        break
    odds.append(n)
print("odd numbers up to 15:", odds)
