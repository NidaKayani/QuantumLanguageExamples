"""Integer floor division, modulo and true division, including negative operands."""
import numpy as np

a = np.array([17, -17, 17, -17, 0, 9])
b = np.array([5, 5, -5, -5, 3, 9])

print("a      =", a)
print("b      =", b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("check (a//b)*b + a%b == a:", np.array_equal((a // b) * b + a % b, a))
print(repr(a / b))
print("true division dtype:", (a / b).dtype, " floor dtype:", (a // b).dtype)

q, r = np.divmod(a, b)
print("divmod quotient:", q)
print("divmod remainder:", r)

# floats with // and %
f = np.array([7.5, -7.5, 10.25, 3.0])
print("f // 2 =", f // 2)
print("f % 2  =", f % 2)
print("np.fmod(f, 2) =", np.fmod(f, 2))
print("np.remainder(f, 2) =", np.remainder(f, 2))

# seconds -> h, m, s
seconds = np.array([59, 61, 3600, 3725, 86399])
hours = seconds // 3600
minutes = seconds % 3600 // 60
secs = seconds % 60
for t, h, m, s in zip(seconds, hours, minutes, secs):
    print("%6d s = %02d:%02d:%02d" % (t, h, m, s))

# digits of a number via repeated // and %
n = np.array([9071, 345, 12])
digits = []
x = n.copy()
for _ in range(4):
    digits.append(x % 10)
    x //= 10
print("digit columns (ones..thousands):")
print(np.array(digits).T)

# averaging ints: true division vs floor division
scores = np.array([88, 91, 79, 95])
print("mean via / :", scores.sum() / scores.size)
print("mean via //:", scores.sum() // scores.size)
print("np.true_divide:", np.true_divide(scores, 4))
print("np.floor_divide:", np.floor_divide(scores, 4))
