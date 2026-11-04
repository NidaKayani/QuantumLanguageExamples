"""Elementary cellular automaton Rule 30 and its use as a bit generator."""


def make_rule(number):
    return {tuple(int(b) for b in f"{i:03b}"): (number >> i) & 1 for i in range(8)}


def evolve(cells, rule):
    n = len(cells)
    return [rule[(cells[(i - 1) % n], cells[i], cells[(i + 1) % n])] for i in range(n)]


def run(number, width=31, steps=16):
    rule = make_rule(number)
    cells = [0] * width
    cells[width // 2] = 1
    rows = [cells]
    for _ in range(steps - 1):
        cells = evolve(cells, rule)
        rows.append(cells)
    return rows


rows = run(30)
for row in rows:
    print("".join("#" if c else "." for c in row))

center_bits = [row[len(row) // 2] for row in run(30, width=101, steps=48)]
bits = "".join(map(str, center_bits))
print("Center column bits:", bits)
value = int(bits[:32], 2)
print("First 32 bits as integer:", value, hex(value))
print("Ones ratio: %.3f" % (bits.count("1") / len(bits)))
print("Rule table:", {"".join(map(str, k)): v for k, v in sorted(make_rule(30).items(), reverse=True)})
