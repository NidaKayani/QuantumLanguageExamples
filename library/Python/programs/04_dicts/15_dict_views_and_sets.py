"""Use dictionary views for set algebra and comparing configurations."""

old = {"host": "a.example", "port": 80, "debug": True, "workers": 4}
new = {"host": "b.example", "port": 80, "workers": 8, "timeout": 30}

added = new.keys() - old.keys()
removed = old.keys() - new.keys()
common = old.keys() & new.keys()
changed = {k for k in common if old[k] != new[k]}

print("added:", sorted(added))
print("removed:", sorted(removed))
print("changed:", sorted(changed))
print("unchanged:", sorted(common - changed))

for key in sorted(added | removed | changed):
    before = old.get(key, "-")
    after = new.get(key, "-")
    print(f"  {key:<8} {before!s:>10} -> {after!s:<10}")

print("identical items:", sorted(old.items() & new.items()))
print("keys disjoint from {'x'}:", old.keys().isdisjoint({"x"}))

view = old.values()
print("values view:", list(view), "| sum of ints:", sum(v for v in view if type(v) is int))
old["workers"] = 16
print("view updated:", list(view))

print("keys view is set-like:", type(old.keys() | set()).__name__)
print("reversed keys:", list(reversed(new.keys())))
print("mapping proxy-like length:", len(new.items()))

required = {"host", "port", "timeout"}
for name, cfg in (("old", old), ("new", new)):
    missing = required - cfg.keys()
    print(f"{name} config missing: {sorted(missing) or 'nothing'}")
