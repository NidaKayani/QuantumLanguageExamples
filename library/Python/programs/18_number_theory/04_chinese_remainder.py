"""Chinese Remainder Theorem for coprime and non-coprime moduli."""
from functools import reduce
from math import gcd, prod


def crt_coprime(residues, moduli):
    total = prod(moduli)
    x = 0
    for r, m in zip(residues, moduli):
        partial = total // m
        x += r * partial * pow(partial, -1, m)
    return x % total, total


def crt_pair(a, b):
    (r1, m1), (r2, m2) = a, b
    g = gcd(m1, m2)
    if (r2 - r1) % g:
        return None
    lcm = m1 // g * m2
    k = ((r2 - r1) // g * pow(m1 // g, -1, m2 // g)) % (m2 // g)
    return (r1 + m1 * k) % lcm, lcm


def crt_general(congruences):
    def step(acc, item):
        return None if acc is None else crt_pair(acc, item)
    return reduce(step, congruences[1:], congruences[0])


def main():
    x, m = crt_coprime([2, 3, 2], [3, 5, 7])
    print(f"Sunzi's problem: x = {x} (mod {m})")
    print("  check:", [x % k for k in (3, 5, 7)])
    rems, mods = [1, 2, 3, 4, 5], [2, 3, 5, 7, 11]
    x, m = crt_coprime(rems, mods)
    print(f"x = {rems} mod {mods} -> {x} (mod {m})")
    print("General solver agrees:", crt_general(list(zip(rems, mods))) == (x, m))
    eggs = crt_general([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 7)])
    print("Eggs puzzle (1 left over for 2..6, none for 7):", eggs)
    print("Non-coprime consistent:", crt_general([(2, 6), (8, 10)]))
    print("Non-coprime inconsistent:", crt_general([(1, 6), (2, 4)]))
    big_mods = [1_000_003, 999_983, 1_000_033]
    secret = 123_456_789_012_345
    shares = [secret % q for q in big_mods]
    recovered, _ = crt_coprime(shares, big_mods)
    print(f"Secret {secret} from shares {shares} -> {recovered}")


if __name__ == "__main__":
    main()
