"""EAFP (try first) versus LBYL (check first) styles applied to the same tasks."""
from collections import defaultdict

records = [
    {"name": "Ann", "dept": "eng", "salary": "120000"},
    {"name": "Bob", "dept": "ops"},
    {"name": "Cid", "dept": "eng", "salary": "n/a"},
    {"name": "Dee", "salary": "90000"},
    {"name": "Eve", "dept": "ops", "salary": "85000"},
]


def total_lbyl(rows):
    totals = {}
    for r in rows:
        if "dept" in r and "salary" in r and r["salary"].isdigit():
            totals[r["dept"]] = totals.get(r["dept"], 0) + int(r["salary"])
    return totals


def total_eafp(rows):
    totals = defaultdict(int)
    skipped = []
    for r in rows:
        try:
            totals[r["dept"]] += int(r["salary"])
        except KeyError as exc:
            skipped.append(f"{r['name']} (missing {exc.args[0]})")
        except ValueError:
            skipped.append(f"{r['name']} (bad salary)")
    return dict(totals), skipped


print("LBYL totals:", total_lbyl(records))
totals, skipped = total_eafp(records)
print("EAFP totals:", totals)
print("EAFP skipped:", skipped)


def first_upper(obj):
    try:
        return obj[0].upper()
    except (IndexError, KeyError):
        return "<empty>"
    except (TypeError, AttributeError) as exc:
        return f"<unsupported: {type(exc).__name__}>"


for value in ["hello", "", ["xy", "z"], [], {0: "zero"}, 42, [5]]:
    print(f"first_upper({value!r}) = {first_upper(value)}")
