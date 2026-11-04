"""Use conditional expressions for concise value selection."""


def sign(n):
    return "positive" if n > 0 else "negative" if n < 0 else "zero"


def pluralize(count, word):
    return f"{count} {word if count == 1 else word + 's'}"


def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


for n in (-3, 0, 8):
    print(f"{n} is {sign(n)}")

for k in (0, 1, 2, 5):
    print(pluralize(k, "apple"))

print([clamp(x, 0, 10) for x in (-5, 3, 10, 15)])

# ternaries inside comprehensions
nums = range(1, 16)
fizz = ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n) for n in nums]
print(" ".join(fizz))

# ternary vs. or-default
user_name = ""
display = user_name if user_name else "anonymous"
display2 = user_name or "anonymous"
print(display, display2, display == display2)

# selecting functions with a ternary
values = [4, 1, 9, 2]
descending = True
pick = max if descending else min
print("picked:", pick(values))
ordered = sorted(values, reverse=True) if descending else sorted(values)
print("ordered:", ordered)
