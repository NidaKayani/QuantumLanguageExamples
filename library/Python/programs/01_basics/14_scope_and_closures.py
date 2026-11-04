"""Explore local, global and nonlocal scope plus closures that capture state."""

counter = 0


def increment_global():
    global counter
    counter += 1
    return counter


def make_counter(start=0, step=1):
    count = start

    def tick():
        nonlocal count
        count += step
        return count

    return tick


def make_multipliers():
    # late binding fixed with a default argument
    return [lambda x, k=k: x * k for k in range(1, 5)]


def outer():
    message = "outer"

    def inner():
        message = "inner"
        return message

    inner_result = inner()
    return message, inner_result


for _ in range(3):
    increment_global()
print("global counter:", counter)

by_one = make_counter()
by_ten = make_counter(100, 10)
print([by_one() for _ in range(4)])
print([by_ten() for _ in range(4)])
print("independent state:", by_one(), by_ten())

print([f(3) for f in make_multipliers()])
print(outer())

# inspecting closure cells
print("closure vars:", by_ten.__code__.co_freevars)
print("captured count:", by_ten.__closure__[0].cell_contents)
