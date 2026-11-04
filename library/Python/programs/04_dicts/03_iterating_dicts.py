"""Iterate over keys, values and items, with sorting and filtering."""

capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia",
            "Kenya": "Nairobi", "Canada": "Ottawa"}

print("keys:", list(capitals))
print("values:", list(capitals.values()))

for country, city in capitals.items():
    print(f"  The capital of {country} is {city}.")

print("sorted by country:")
for country in sorted(capitals):
    print(f"  {country:<7} {capitals[country]}")

print("sorted by city length desc:")
for country, city in sorted(capitals.items(), key=lambda kv: (-len(kv[1]), kv[1])):
    print(f"  {city:<9} ({country})")

long_names = {c: v for c, v in capitals.items() if len(c) > 5}
print("countries with long names:", long_names)

# views are live
keys = capitals.keys()
capitals["Peru"] = "Lima"
print("view sees new key:", "Peru" in keys, len(keys))

# set operations on key views
other = {"Japan": "Tokyo", "Peru": "Lima", "Chile": "Santiago"}
print("common:", sorted(capitals.keys() & other.keys()))
print("only first:", sorted(capitals.keys() - other.keys()))
print("items overlap:", sorted(capitals.items() & other.items()))

# can't change size while iterating; iterate over a copy
for country in list(capitals):
    if country.startswith(("B", "C")):
        del capitals[country]
print("after removal:", capitals)

for i, (k, v) in enumerate(reversed(capitals.items()), 1):
    print(f"  {i}. {k} -> {v}")
