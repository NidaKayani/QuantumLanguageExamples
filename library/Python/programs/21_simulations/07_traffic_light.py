"""Two-way intersection traffic light controller with queued cars on each road."""
from itertools import cycle
from enum import Enum


class Light(Enum):
    GREEN = "G"
    YELLOW = "Y"
    RED = "R"


PHASES = [
    ({"NS": Light.GREEN, "EW": Light.RED}, 4),
    ({"NS": Light.YELLOW, "EW": Light.RED}, 1),
    ({"NS": Light.RED, "EW": Light.GREEN}, 3),
    ({"NS": Light.RED, "EW": Light.YELLOW}, 1),
]

ARRIVALS = {"NS": [1, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1, 0, 1, 0, 0, 1, 0, 0],
            "EW": [0, 2, 1, 0, 1, 1, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0]}


def run(ticks):
    queues = {"NS": 0, "EW": 0}
    passed = {"NS": 0, "EW": 0}
    phase_iter = cycle(PHASES)
    lights, remaining = next(phase_iter)
    timeline = []
    for t in range(ticks):
        for road in queues:
            queues[road] += ARRIVALS[road][t] if t < len(ARRIVALS[road]) else 0
            if lights[road] is Light.GREEN and queues[road]:
                queues[road] -= 1
                passed[road] += 1
        timeline.append(f"{lights['NS'].value}{lights['EW'].value}")
        print(f"t={t:2d} NS={lights['NS'].name:<6} EW={lights['EW'].name:<6} "
              f"queue NS={queues['NS']} EW={queues['EW']}")
        remaining -= 1
        if remaining == 0:
            lights, remaining = next(phase_iter)
    return passed, queues, timeline


passed, left, timeline = run(22)
print("Light timeline:", " ".join(timeline))
print("Cars passed:", passed, "still waiting:", left)
