"""Polymorphic state machine: traffic-light states as subclasses that return the next state."""


class State:
    duration = 0

    def next(self):
        raise NotImplementedError

    def on_enter(self, log):
        log.append(f"enter {self}")

    def __str__(self):
        return type(self).__name__.upper()


class Red(State):
    duration = 30

    def next(self):
        return Green()


class Green(State):
    duration = 25

    def next(self):
        return Yellow()


class Yellow(State):
    duration = 5

    def next(self):
        return Red()


class FlashingRed(Red):
    duration = 1

    def next(self):
        return self

    def on_enter(self, log):
        super().on_enter(log)
        log.append("  (maintenance mode)")


def simulate(start, steps):
    log, state, elapsed = [], start, 0
    for _ in range(steps):
        state.on_enter(log)
        elapsed += state.duration
        state = state.next()
    return log, elapsed


log, elapsed = simulate(Red(), 7)
print("\n".join(log))
print("elapsed seconds:", elapsed)

log, elapsed = simulate(FlashingRed(), 3)
print("\n".join(log))
print("elapsed seconds:", elapsed)
print("FlashingRed is a Red:", isinstance(FlashingRed(), Red))
