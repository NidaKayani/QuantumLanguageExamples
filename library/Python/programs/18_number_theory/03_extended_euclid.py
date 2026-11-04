"""Extended Euclid, modular inverses, and solving linear Diophantine equations."""


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError(f"{a} has no inverse modulo {m}")
    return x % m


def diophantine(a, b, c):
    """Return a particular solution and the step for a*x + b*y = c."""
    g, x, y = extended_gcd(a, b)
    if c % g:
        return None
    k = c // g
    return (x * k, y * k), (b // g, -a // g)


def main():
    for a, b in [(240, 46), (99, 78), (17, 5), (1_000_000_007, 12345)]:
        g, x, y = extended_gcd(a, b)
        print(f"gcd({a}, {b}) = {g} = {a}*({x}) + {b}*({y})")
        assert a * x + b * y == g
    m = 26
    inverses = {a: mod_inverse(a, m) for a in range(1, m) if extended_gcd(a, m)[0] == 1}
    print(f"Inverses mod {m}:", inverses)
    print("Matches pow(a, -1, m):", all(pow(a, -1, m) == inv for a, inv in inverses.items()))
    try:
        mod_inverse(4, 26)
    except ValueError as err:
        print("Error:", err)
    sol = diophantine(15, 21, 39)
    print("15x + 21y = 39 ->", sol)
    (x0, y0), (dx, dy) = diophantine(7, 11, 100)
    nonneg = [(x0 + k * dx, y0 + k * dy) for k in range(-30, 30)
              if x0 + k * dx >= 0 and y0 + k * dy >= 0]
    print("Non-negative solutions of 7x + 11y = 100:", nonneg)
    print("Coin problem 6x + 9y = 20 solvable:", diophantine(6, 9, 20) is not None)


if __name__ == "__main__":
    main()
