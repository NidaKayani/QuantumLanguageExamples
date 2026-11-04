"""Parse CSV text by hand with a quote-aware state machine, then aggregate the rows."""
from collections import defaultdict
from statistics import mean

DATA = '''id,name,department,salary,notes
1,Alice Johnson,Engineering,98000,"Team lead, backend"
2,Bob Smith,Marketing,67000,
3,"Carol ""CJ"" Diaz",Engineering,105000,"Joined 2019"
4,Dan Wu,Sales,72000,"Top seller, Q3, Q4"
5,Eve Adams,Marketing,71000,"Line one
line two"
6,Frank Ng,Sales,64000,
7,Grace Kim,Engineering,91000,"Remote"
'''


def parse_csv(text, delimiter=","):
    rows, row, field = [], [], []
    in_quotes = False
    i = 0
    while i < len(text):
        ch = text[i]
        if in_quotes:
            if ch == '"' and text[i + 1:i + 2] == '"':
                field.append('"')
                i += 1
            elif ch == '"':
                in_quotes = False
            else:
                field.append(ch)
        elif ch == '"':
            in_quotes = True
        elif ch == delimiter:
            row.append("".join(field))
            field = []
        elif ch == "\n":
            row.append("".join(field))
            rows.append(row)
            row, field = [], []
        else:
            field.append(ch)
        i += 1
    if field or row:
        row.append("".join(field))
        rows.append(row)
    return rows


def to_records(rows):
    header, *body = rows
    return [dict(zip(header, r)) for r in body]


def quote(value):
    value = str(value)
    if any(c in value for c in ',"\n'):
        return '"' + value.replace('"', '""') + '"'
    return value


def main():
    records = to_records(parse_csv(DATA))
    print(f"Parsed {len(records)} records")
    for r in records:
        notes = r["notes"].replace("\n", "\\n")
        print(f"  #{r['id']} {r['name']:<20} {r['department']:<12} {int(r['salary']):>7,}  {notes}")
    by_dept = defaultdict(list)
    for r in records:
        by_dept[r["department"]].append(int(r["salary"]))
    print("Department summary:")
    for dept, salaries in sorted(by_dept.items()):
        print(f"  {dept:<12} n={len(salaries)} avg={mean(salaries):>9,.2f} max={max(salaries):,}")
    out_rows = [["department", "headcount", "payroll"]] + [
        [d, len(s), sum(s)] for d, s in sorted(by_dept.items())]
    csv_text = "\n".join(",".join(quote(v) for v in row) for row in out_rows)
    print("Re-serialised summary CSV:")
    print(csv_text)
    print("Round trip of tricky field:", parse_csv(quote('He said "hi", then left'))[0])


if __name__ == "__main__":
    main()
