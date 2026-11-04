"""Merge dictionaries with |, |=, update, unpacking and ChainMap."""

from collections import ChainMap

defaults = {"theme": "light", "font": "mono", "size": 12, "autosave": True}
user = {"theme": "dark", "size": 14}
session = {"size": 16}

merged = defaults | user
print("defaults | user:", merged)

print("three-way:", defaults | user | session)
print("unpacking:", {**defaults, **user, "extra": 1})

copy_ = dict(defaults)
copy_ |= user
print("|= in place:", copy_)

copy2 = defaults.copy()
copy2.update(user, autosave=False)
print("update with kwargs:", copy2)

print("defaults unchanged:", defaults)

chain = ChainMap(session, user, defaults)
print("ChainMap lookups:", chain["size"], chain["theme"], chain["font"])
print("ChainMap as dict:", dict(chain))
child = chain.new_child({"theme": "solarized"})
print("child theme:", child["theme"], "| parent theme:", chain["theme"])


def deep_merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


base_cfg = {"db": {"host": "localhost", "port": 5432, "opts": {"ssl": False}}, "debug": False}
prod_cfg = {"db": {"host": "db.prod", "opts": {"ssl": True, "timeout": 30}}}
print("deep merge:", deep_merge(base_cfg, prod_cfg))
print("shallow merge loses keys:", base_cfg | prod_cfg)

# summing values when merging
from collections import Counter
q1 = {"north": 10, "south": 5}
q2 = {"south": 7, "west": 3}
print("summed:", dict(Counter(q1) + Counter(q2)))
