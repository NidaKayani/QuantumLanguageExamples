"""Discrete-event bank queue simulation with multiple tellers driven by a custom LCG."""
import heapq
import math
import statistics


class LCG:
    def __init__(self, seed):
        self.state = seed

    def random(self):
        self.state = (1103515245 * self.state + 12345) % 2**31
        return self.state / 2**31

    def expovariate(self, rate):
        return -math.log(1.0 - self.random()) / rate


def simulate(tellers, customers=200, arrival_rate=1.0, service_rate=0.4, seed=42):
    rng = LCG(seed)
    free_at = [0.0] * tellers
    heapq.heapify(free_at)
    t = 0.0
    waits = []
    for _ in range(customers):
        t += rng.expovariate(arrival_rate)
        earliest = heapq.heappop(free_at)
        start = max(t, earliest)
        waits.append(start - t)
        heapq.heappush(free_at, start + rng.expovariate(service_rate))
    makespan = max(free_at)
    return waits, makespan


print(f"{'tellers':>7} {'mean wait':>10} {'median':>8} {'max':>8} {'waited%':>8} {'end':>8}")
for tellers in range(2, 6):
    waits, end = simulate(tellers)
    waited = sum(1 for w in waits if w > 1e-9) / len(waits)
    print(
        f"{tellers:>7} {statistics.mean(waits):>10.2f} {statistics.median(waits):>8.2f}"
        f" {max(waits):>8.2f} {waited:>8.1%} {end:>8.1f}"
    )

rng = LCG(7)
sample = [rng.random() for _ in range(1000)]
print("LCG sanity: mean=%.3f min=%.4f max=%.4f" % (statistics.mean(sample), min(sample), max(sample)))
