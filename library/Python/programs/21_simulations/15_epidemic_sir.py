"""SIR epidemic model on a population with and without a mid-outbreak intervention."""
from dataclasses import dataclass


@dataclass
class SIR:
    s: float
    i: float
    r: float

    @property
    def total(self):
        return self.s + self.i + self.r


def run(beta, gamma, days, intervention_day=None, factor=1.0, n=10_000, infected=10):
    pop = SIR(n - infected, infected, 0)
    timeline = [pop]
    for day in range(1, days + 1):
        b = beta * factor if intervention_day is not None and day >= intervention_day else beta
        new_inf = b * pop.s * pop.i / n
        new_rec = gamma * pop.i
        pop = SIR(pop.s - new_inf, pop.i + new_inf - new_rec, pop.r + new_rec)
        timeline.append(pop)
    return timeline


def summarize(label, timeline):
    peak_day, peak = max(enumerate(timeline), key=lambda item: item[1].i)
    final = timeline[-1]
    print(f"{label}: peak {peak.i:,.0f} infected on day {peak_day}; "
          f"total ever infected {final.r + final.i:,.0f} ({(final.r + final.i) / final.total:.1%})")


beta, gamma = 0.30, 0.10
print(f"R0 = {beta / gamma:.1f}")
base = run(beta, gamma, 160)
for day in range(0, 161, 20):
    p = base[day]
    print(f"day {day:>3}: S={p.s:>8.0f} I={p.i:>8.0f} R={p.r:>8.0f}  " + "*" * int(p.i / 200))

summarize("No intervention", base)
summarize("Distancing from day 30 (beta x0.5)", run(beta, gamma, 160, 30, 0.5))
summarize("Distancing from day 50 (beta x0.5)", run(beta, gamma, 160, 50, 0.5))
summarize("Strong lockdown day 30 (beta x0.25)", run(beta, gamma, 160, 30, 0.25))
