"""Implement FizzBuzz several different ways and check they agree."""


def fizzbuzz_if(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_concat(n):
    word = ("Fizz" if n % 3 == 0 else "") + ("Buzz" if n % 5 == 0 else "")
    return word or str(n)


def fizzbuzz_table(n, rules=((3, "Fizz"), (5, "Buzz"), (7, "Bazz"))):
    word = "".join(text for d, text in rules if n % d == 0)
    return word or str(n)


def fizzbuzz_match(n):
    match (n % 3, n % 5):
        case (0, 0):
            return "FizzBuzz"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        case _:
            return str(n)


first = [fizzbuzz_if(i) for i in range(1, 31)]
print(", ".join(first))

same = all(
    fizzbuzz_if(i) == fizzbuzz_concat(i) == fizzbuzz_match(i)
    for i in range(1, 1001)
)
print("all three implementations agree:", same)

print("with Bazz rule:")
print(" ".join(fizzbuzz_table(i) for i in range(1, 36)))

counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0, "number": 0}
for i in range(1, 101):
    w = fizzbuzz_if(i)
    counts[w if w in counts else "number"] += 1
print("counts 1..100:", counts)
