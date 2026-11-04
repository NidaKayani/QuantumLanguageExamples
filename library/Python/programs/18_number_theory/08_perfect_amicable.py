"""Perfect, abundant, deficient and amicable numbers from a divisor-sum sieve."""
from collections import Counter
from enum import Enum


class Kind(Enum):
    DEFICIENT = "deficient"
    PERFECT = "perfect"
    ABUNDANT = "abundant"


def proper_divisor_sums(limit):
    sums = [0] * (limit + 1)
    for d in range(1, limit // 2 + 1):
        for multiple in range(2 * d, limit + 1, d):
            sums[multiple] += d
    return sums


def classify(n, sums):
    s = sums[n]
    if s < n:
        return Kind.DEFICIENT
    return Kind.PERFECT if s == n else Kind.ABUNDANT


def mersenne_perfects(count):
    found, p = [], 2
    while len(found) < count:
        m = 2**p - 1
        if all(m % k for k in range(2, int(m ** 0.5) + 1)):
            found.append(2 ** (p - 1) * m)
        p += 1
    return found


def main():
    limit = 20_000
    sums = proper_divisor_sums(limit)
    kinds = Counter(classify(n, sums) for n in range(1, limit + 1))
    for kind in Kind:
        print(f"{kind.value:>9}: {kinds[kind]}")
    perfect = [n for n in range(2, limit + 1) if sums[n] == n]
    print("Perfect numbers:", perfect)
    print("From Mersenne primes:", mersenne_perfects(6))
    amicable = [(a, sums[a]) for a in range(2, limit + 1)
                if a < sums[a] <= limit and sums[sums[a]] == a]
    print("Amicable pairs:", amicable)
    odd_abundant = next(n for n in range(1, limit, 2) if sums[n] > n)
    print("Smallest odd abundant number:", odd_abundant, "with sum", sums[odd_abundant])
    abundant = [n for n in range(1, 200) if sums[n] > n]
    print("Abundant numbers below 200:", abundant)


if __name__ == "__main__":
    main()
