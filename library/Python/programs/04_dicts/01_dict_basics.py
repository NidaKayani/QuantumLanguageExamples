"""Create dictionaries, access, add, update and delete keys."""

person = {"name": "Grace", "born": 1906, "field": "computing"}
print(person)
print("name:", person["name"], "| keys:", len(person))

person["rank"] = "Rear Admiral"
person["born"] = 1906
print("after add:", person)

del person["rank"]
print("after del:", person)

try:
    person["salary"]
except KeyError as e:
    print("KeyError:", e)

print("'field' in person:", "field" in person, "| 'Grace' in person:", "Grace" in person)
print("'Grace' in values:", "Grace" in person.values())

# different ways to build dicts
a = dict(x=1, y=2)
b = dict([("x", 1), ("y", 2)])
c = dict(zip("xy", (1, 2)))
d = {k: v for k, v in [("x", 1), ("y", 2)]}
print("all equal:", a == b == c == d)

fromkeys = dict.fromkeys(["red", "green", "blue"], 0)
print("fromkeys:", fromkeys)

# keys can be any hashable value
grid = {(0, 0): "origin", (1, 2): "point", 3.5: "float key", True: "bool key", None: "none"}
for key, value in grid.items():
    print(f"  {key!r:>8} -> {value}")

try:
    {[1, 2]: "list key"}
except TypeError as e:
    print("TypeError:", e)

print("insertion order kept:", list({"z": 1, "a": 2, "m": 3}))
print("len, bool:", len({}), bool({}), bool({"k": 0}))
