"""Digit problems: digit sums, digital roots, Armstrong, happy, Kaprekar and Harshad numbers."""


def digits(n, base=10):
    out = []
    while n:
        n, d = divmod(n, base)
        out.append(d)
    return out[::-1] or [0]


def digital_root(n):
    return 0 if n == 0 else 1 + (n - 1) % 9


def is_armstrong(n):
    ds = digits(n)
    return n == sum(d ** len(ds) for d in ds)


def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(d * d for d in digits(n))
    return n == 1


def kaprekar_routine(n):
    steps = [n]
    while n != 6174:
        s = f"{n:04d}"
        big, small = int("".join(sorted(s, reverse=True))), int("".join(sorted(s)))
        n = big - small
        steps.append(n)
        if n == 0:
            break
    return steps


def main():
    n = 9_875_321
    print(f"digits({n}) = {digits(n)}, sum {sum(digits(n))}, root {digital_root(n)}")
    print("Binary digits of 2024:", "".join(map(str, digits(2024, 2))))
    print("Armstrong numbers < 100000:", [k for k in range(1, 100_000) if is_armstrong(k)])
    print("Happy numbers <= 50:", [k for k in range(1, 51) if is_happy(k)])
    for start in (3524, 1112, 8820):
        print(f"Kaprekar from {start}: {' -> '.join(map(str, kaprekar_routine(start)))}")
    harshad = [k for k in range(1, 60) if k % sum(digits(k)) == 0]
    print("Harshad numbers < 60:", harshad)
    rev = lambda k: int(str(k)[::-1])
    lychrel_steps = {}
    for start in (89, 196, 10911):
        k, steps = start, 0
        while steps < 60:
            k += rev(k)
            steps += 1
            if str(k) == str(k)[::-1]:
                break
        lychrel_steps[start] = steps if str(k) == str(k)[::-1] else None
    print("Reverse-and-add palindrome steps:", lychrel_steps)
    print("Digit sum of 2**1000:", sum(map(int, str(2**1000))))


if __name__ == "__main__":
    main()
