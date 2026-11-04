"""Generator-based coroutines that receive values with send() and keep running state."""


def running_stats():
    count, total, low, high = 0, 0.0, None, None
    summary = None
    while True:
        value = yield summary
        count += 1
        total += value
        low = value if low is None else min(low, value)
        high = value if high is None else max(high, value)
        summary = {"n": count, "mean": round(total / count, 2), "min": low, "max": high}


def grep(pattern):
    matches = []
    try:
        while True:
            line = yield
            if pattern in line:
                matches.append(line)
    except GeneratorExit:
        print(f"  grep({pattern!r}) closing with {len(matches)} matches")
        print("  matches:", matches)


def accumulate_until(threshold):
    total = 0
    while total < threshold:
        total += yield total
    return total


stats = running_stats()
next(stats)  # prime the coroutine
for reading in [12.5, 7.0, 21.25, 3.5]:
    print("after", reading, "->", stats.send(reading))

g = grep("error")
next(g)
for line in ["ok: started", "error: disk", "warning: cpu", "error: net"]:
    g.send(line)
g.close()

acc = accumulate_until(10)
next(acc)
try:
    for v in [3, 4, 5, 6]:
        print("running total:", acc.send(v))
except StopIteration as stop:
    print("threshold reached, final total:", stop.value)
