"""Set algebra using both operators and named methods."""

python_devs = {"ana", "ben", "cara", "dev", "eli"}
rust_devs = {"cara", "dev", "fay", "gus"}
go_devs = {"ben", "dev", "gus", "hal"}

def show(label, s):
    print(f"{label:<28} {sorted(s)}")

show("python | rust", python_devs | rust_devs)
show("python & rust", python_devs & rust_devs)
show("python - rust", python_devs - rust_devs)
show("python ^ rust", python_devs ^ rust_devs)

show("union(all three)", python_devs.union(rust_devs, go_devs))
show("intersection(all three)", python_devs.intersection(rust_devs, go_devs))
show("difference(rust, go)", python_devs.difference(rust_devs, go_devs))
show("symmetric_difference(go)", rust_devs.symmetric_difference(go_devs))

# Methods accept any iterable, operators need sets
show("union with list", python_devs.union(["zed", "ana"]))

everyone = python_devs | rust_devs | go_devs
only_one = {p for p in everyone
            if sum(p in team for team in (python_devs, rust_devs, go_devs)) == 1}
show("exactly one language", only_one)

counts = {p: sum(p in t for t in (python_devs, rust_devs, go_devs)) for p in everyone}
for person in sorted(counts, key=lambda p: (-counts[p], p)):
    print(f"  {person}: {counts[person]} language(s)")
