"""Classic recursive functions: factorial, gcd, power, palindromes, and binary search."""


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    return half * half * (base if exp % 2 else 1)


def is_palindrome(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


def binary_search(items, target, lo=0, hi=None):
    if hi is None:
        hi = len(items) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return binary_search(items, target, mid + 1, hi)
    return binary_search(items, target, lo, mid - 1)


for n in (0, 5, 10, 20):
    print(f"{n}! = {factorial(n)}")
print("gcd(1071, 462) =", gcd(1071, 462))
print("2^61 =", fast_power(2, 61))
for phrase in ["Racecar", "A man, a plan, a canal: Panama", "Quantum"]:
    print(f"{phrase!r} palindrome? {is_palindrome(phrase)}")
data = list(range(0, 100, 7))
for t in (0, 49, 98, 50):
    print(f"index of {t}: {binary_search(data, t)}")
