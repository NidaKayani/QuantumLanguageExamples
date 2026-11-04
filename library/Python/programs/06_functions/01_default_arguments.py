"""Default argument values, including the mutable-default pitfall and the None idiom."""


def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


def append_bad(item, bucket=[]):
    bucket.append(item)
    return bucket


def append_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def power(base, exponent=2, modulus=None):
    result = base ** exponent
    return result % modulus if modulus is not None else result


print(greet("Ada"))
print(greet("Grace", "Good morning"))
print(greet("Linus", punctuation="?"))
print(greet(greeting="Hey", name="Guido"))

print("shared default:", append_bad(1), append_bad(2), append_bad(3))
print("fresh default:", append_good(1), append_good(2), append_good(3))
print("defaults tuple:", append_bad.__defaults__)

for args in [(3,), (3, 3), (7, 5, 13)]:
    print(f"power{args} = {power(*args)}")
print("greet defaults:", greet.__defaults__)
