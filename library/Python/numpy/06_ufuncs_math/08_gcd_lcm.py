"""Integer number theory with np.gcd and np.lcm: fractions, schedules and coprimality."""
import numpy as np

a = np.array([12, 18, 35, 100, 17, 0, 48])
b = np.array([8, 27, 14, 75, 5, 9, -36])
print("a:", a)
print("b:", b)
print("gcd:", np.gcd(a, b))
print("lcm:", np.lcm(a, b))
print(repr(np.gcd(a, b)))
print("gcd * lcm == |a*b|:", np.array_equal(np.gcd(a, b) * np.lcm(a, b), np.abs(a * b)))

# reduce fractions num/den to lowest terms
num = np.array([6, 10, 21, 45, 7, 120])
den = np.array([8, 25, 14, 60, 13, 36])
g = np.gcd(num, den)
print("fractions:", [f"{n}/{d}" for n, d in zip(num, den)])
print("reduced:  ", [f"{n}/{d}" for n, d in zip(num // g, den // g)])

# gcd/lcm of a whole array via reduce
nums = np.array([84, 126, 210, 42])
print("gcd of all:", np.gcd.reduce(nums))
print("lcm of 1..10:", np.lcm.reduce(np.arange(1, 11)))
print("running lcm 1..12:", np.lcm.accumulate(np.arange(1, 13)))

# buses leaving every k minutes: when do they all meet again?
intervals = np.array([6, 10, 15])
print("intervals:", intervals, " all depart together every", np.lcm.reduce(intervals), "minutes")

# coprime table via broadcasting
n = np.arange(1, 11)
G = np.gcd(n[:, None], n[None, :])
print("gcd table 1..10:")
print(G)
coprime = G == 1
print("coprime pairs (excluding diagonal):", coprime.sum() - 1)

# Euler's totient phi(k) for k = 1..20
k = np.arange(1, 21)
coprime_k = np.gcd(k[:, None], k[None, :]) == 1
upto_k = k[None, :] <= k[:, None]
phi = (coprime_k & upto_k).sum(axis=1)
print("k:  ", k)
print("phi:", phi)

# common denominator for adding fractions
dens = np.array([4, 6, 9])
nums2 = np.array([1, 5, 2])
L = np.lcm.reduce(dens)
total = (nums2 * (L // dens)).sum()
g2 = np.gcd(total, L)
print("1/4 + 5/6 + 2/9 = %d/%d" % (total // g2, L // g2))
