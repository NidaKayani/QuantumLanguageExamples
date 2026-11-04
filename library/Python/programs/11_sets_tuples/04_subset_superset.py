"""Subset, superset and disjoint relationships between sets."""

ROLES = {
    "viewer": {"read"},
    "editor": {"read", "write"},
    "admin": {"read", "write", "delete", "grant"},
    "auditor": {"read", "audit"},
    "guest": set(),
}

def describe(a, b):
    sa, sb = ROLES[a], ROLES[b]
    if sa == sb:
        return "equal"
    if sa < sb:
        return "proper subset"
    if sa > sb:
        return "proper superset"
    if sa.isdisjoint(sb):
        return "disjoint"
    return "overlapping"

names = list(ROLES)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        print(f"{a:>7} vs {b:<7}: {describe(a, b)}")

required = {"read", "write"}
print()
for role, perms in ROLES.items():
    ok = required.issubset(perms)
    print(f"{role:<8} can edit documents: {ok}")

print()
print("admin covers editor:", ROLES["admin"].issuperset(ROLES["editor"]))
print("admin >= admin:", ROLES["admin"] >= ROLES["admin"], "admin > admin:", ROLES["admin"] > ROLES["admin"])
print("empty set is subset of everything:", all(set() <= p for p in ROLES.values()))
