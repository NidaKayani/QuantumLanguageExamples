"""Navigate, update and summarize nested dictionary structures."""

company = {
    "engineering": {
        "manager": "Ana",
        "teams": {
            "backend": {"members": ["Raj", "Li", "Tom"], "budget": 120_000},
            "frontend": {"members": ["Sue", "Kim"], "budget": 90_000},
        },
    },
    "sales": {
        "manager": "Bo",
        "teams": {"emea": {"members": ["Eve"], "budget": 60_000}},
    },
}

print("backend members:", company["engineering"]["teams"]["backend"]["members"])

for dept, info in company.items():
    teams = info["teams"]
    headcount = sum(len(t["members"]) for t in teams.values())
    budget = sum(t["budget"] for t in teams.values())
    print(f"{dept}: manager={info['manager']} teams={len(teams)} people={headcount} budget={budget:,}")

company["sales"]["teams"]["apac"] = {"members": ["Ken", "Mai"], "budget": 55_000}
company["engineering"]["teams"]["frontend"]["members"].append("Ola")


def get_path(data, path, default=None):
    for key in path.split("."):
        if not isinstance(data, dict) or key not in data:
            return default
        data = data[key]
    return data


print("path lookup:", get_path(company, "sales.teams.apac.budget"))
print("missing path:", get_path(company, "sales.teams.latam.budget", "n/a"))


def walk(data, prefix=""):
    for key, value in data.items():
        full = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            yield from walk(value, full)
        else:
            yield full, value


for path, value in walk(company):
    if path.endswith("budget"):
        print(f"  {path} = {value:,}")

everyone = sorted(m for d in company.values() for t in d["teams"].values() for m in t["members"])
print("all members:", everyone)
