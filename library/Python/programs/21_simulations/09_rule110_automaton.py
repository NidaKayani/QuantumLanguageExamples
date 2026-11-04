"""Rule 110 and other elementary automata compared by density and period detection."""


def step(cells, rule):
    padded = (0,) + cells + (0,)
    return tuple((rule >> (padded[i - 1] << 2 | padded[i] << 1 | padded[i + 1])) & 1
                 for i in range(1, len(padded) - 1))


def show(cells):
    return "".join("#" if c else "." for c in cells)


width = 40
start = tuple(1 if i == width - 1 else 0 for i in range(width))
cells = start
print("Rule 110 from a single right cell:")
for gen in range(20):
    print(f"{gen:2d} {show(cells)}")
    cells = step(cells, 110)


def period_of(rule, width=12):
    cells = tuple(1 if i == width // 2 else 0 for i in range(width))
    seen = {}
    for t in range(500):
        if cells in seen:
            return seen[cells], t - seen[cells]
        seen[cells] = t
        cells = step(cells, rule)
    return None


print()
print(f"{'rule':>5} {'density@30':>11} {'transient,period':>18}")
for rule in (30, 54, 90, 110, 150, 184):
    cells = start
    for _ in range(30):
        cells = step(cells, rule)
    density = sum(cells) / len(cells)
    print(f"{rule:>5} {density:>11.3f} {str(period_of(rule)):>18}")
