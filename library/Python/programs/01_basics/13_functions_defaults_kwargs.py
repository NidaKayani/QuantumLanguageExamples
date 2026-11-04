"""Define functions with default, keyword-only, *args and **kwargs parameters."""


def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


def total(*numbers, start=0):
    result = start
    for n in numbers:
        result += n
    return result


def build_profile(first, last, /, *, age=None, **extra):
    profile = {"first": first, "last": last}
    if age is not None:
        profile["age"] = age
    profile.update(extra)
    return profile


def append_item(item, bucket=None):
    # avoid the mutable default argument pitfall
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(greet("Ada"))
print(greet("Linus", "Hi"))
print(greet("Grace", punctuation="?"))
print(greet(greeting="Welcome", name="Guido"))

print("total():", total())
print("total(1, 2, 3):", total(1, 2, 3))
print("total(*range(5), start=100):", total(*range(5), start=100))

p = build_profile("Alan", "Turing", age=41, field="computing", country="UK")
for key, value in p.items():
    print(f"  {key}: {value}")

print(append_item(1))
print(append_item(2))
shared = append_item("a")
append_item("b", shared)
print(shared)

options = {"greeting": "Good morning", "punctuation": "."}
print(greet("team", **options))
