"""Show how for/else and while/else run only when the loop wasn't broken."""


def find_first_negative(values):
    for index, v in enumerate(values):
        if v < 0:
            print(f"  found negative {v} at index {index}")
            break
    else:
        print("  no negative values")


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            break
        d += 1
    else:
        return True
    return False


print("search [3, 5, -2, 8]:")
find_first_negative([3, 5, -2, 8])
print("search [1, 2, 3]:")
find_first_negative([1, 2, 3])

primes = [n for n in range(50) if is_prime(n)]
print("primes below 50:", primes)

# nested loop search with for/else
matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
target = 6
for r, row in enumerate(matrix):
    for c, cell in enumerate(row):
        if cell == target:
            print(f"{target} found at row {r}, col {c}")
            break
    else:
        continue
    break
else:
    print(f"{target} not in matrix")

# while/else with a countdown
countdown = 3
while countdown > 0:
    print("tick", countdown)
    countdown -= 1
else:
    print("liftoff!")
