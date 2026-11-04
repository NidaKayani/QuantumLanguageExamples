"""Lotka-Volterra predator-prey model integrated with fourth-order Runge-Kutta."""


def derivatives(state, alpha=1.1, beta=0.4, delta=0.1, gamma=0.4):
    prey, predators = state
    return (alpha * prey - beta * prey * predators,
            delta * prey * predators - gamma * predators)


def rk4(f, state, dt):
    def add(s, k, h):
        return tuple(a + h * b for a, b in zip(s, k))

    k1 = f(state)
    k2 = f(add(state, k1, dt / 2))
    k3 = f(add(state, k2, dt / 2))
    k4 = f(add(state, k3, dt))
    return tuple(s + dt / 6 * (a + 2 * b + 2 * c + d)
                 for s, a, b, c, d in zip(state, k1, k2, k3, k4))


state = (10.0, 5.0)
dt = 0.01
history = [state]
for _ in range(3000):
    state = rk4(derivatives, state, dt)
    history.append(state)

print(f"{'time':>5} {'prey':>8} {'predators':>10}  chart")
for i in range(0, len(history), 200):
    prey, pred = history[i]
    bar = "R" * int(prey) + " " * max(0, 25 - int(prey))
    print(f"{i * dt:>5.1f} {prey:>8.3f} {pred:>10.3f}  {bar}|{'F' * int(pred)}")

prey_series = [p for p, _ in history]
peaks = [round(i * dt, 2) for i in range(1, len(prey_series) - 1)
         if prey_series[i - 1] < prey_series[i] > prey_series[i + 1]]
print("Prey peaks at t =", peaks)
if len(peaks) > 1:
    print("Approximate period: %.2f" % ((peaks[-1] - peaks[0]) / (len(peaks) - 1)))
print("Max prey %.2f, max predators %.2f" % (max(prey_series), max(p for _, p in history)))
