"""Projectile motion with air drag using Euler and semi-implicit Euler integration."""
import math
from typing import NamedTuple

G = 9.81


class State(NamedTuple):
    x: float
    y: float
    vx: float
    vy: float


def launch(speed, angle_deg):
    a = math.radians(angle_deg)
    return State(0.0, 0.0, speed * math.cos(a), speed * math.sin(a))


def fly(state, drag=0.0, dt=0.001):
    t = 0.0
    peak = 0.0
    while True:
        speed = math.hypot(state.vx, state.vy)
        ax = -drag * speed * state.vx
        ay = -G - drag * speed * state.vy
        vx, vy = state.vx + ax * dt, state.vy + ay * dt
        nxt = State(state.x + vx * dt, state.y + vy * dt, vx, vy)
        t += dt
        peak = max(peak, nxt.y)
        if nxt.y < 0:
            frac = state.y / (state.y - nxt.y)
            return state.x + frac * (nxt.x - state.x), peak, t
        state = nxt


speed = 30.0
print("Analytic range at 45 deg (no drag): %.2f m" % (speed ** 2 / G))
print(f"{'angle':>5} {'range':>8} {'peak':>7} {'time':>6} | {'drag range':>10}")
best = (0.0, 0)
for angle in range(15, 80, 10):
    rng, peak, t = fly(launch(speed, angle))
    drag_rng, _, _ = fly(launch(speed, angle), drag=0.01)
    best = max(best, (drag_rng, angle))
    print(f"{angle:>5} {rng:>8.2f} {peak:>7.2f} {t:>6.2f} | {drag_rng:>10.2f}")
print("Best angle with drag among samples: %d deg (%.2f m)" % (best[1], best[0]))
