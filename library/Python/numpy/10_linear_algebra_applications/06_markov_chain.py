"""Weather Markov chain: state evolution and steady state via np.linalg.matrix_power."""
import numpy as np

states = ["sunny", "cloudy", "rainy"]
# Row-stochastic transition matrix: P[i, j] = Pr(next = j | now = i)
P = np.array([[0.7, 0.2, 0.1],
              [0.3, 0.4, 0.3],
              [0.2, 0.3, 0.5]])
print("transition matrix:")
print(P)
print("rows sum to 1:", bool(np.allclose(P.sum(axis=1), 1.0)))

start = np.array([1.0, 0.0, 0.0])
dist = start.copy()
print("day 0:", dist)
for day in range(1, 6):
    dist = dist @ P
    print(f"day {day}:", np.round(dist, 6))

# Same result in one shot with matrix_power
P5 = np.linalg.matrix_power(P, 5)
print("P^5 =")
print(np.round(P5, 6))
print("start @ P^5 matches loop:", bool(np.allclose(start @ P5, dist)))

# Long-run behaviour: every row of P^n converges to the steady state
P64 = np.linalg.matrix_power(P, 64)
steady = P64[0]
print("P^64 rows:")
print(np.round(P64, 6))
print("steady state:", np.round(steady, 6))
for name, p in zip(states, steady):
    print(f"  {name:<7} {p:.6f}")

# Verify pi = pi P and compare with solving the linear system
print("pi @ P == pi:", bool(np.allclose(steady @ P, steady)))
n = P.shape[0]
A = P.T - np.eye(n)
A[-1, :] = 1.0
rhs = np.zeros(n)
rhs[-1] = 1.0
exact = np.linalg.solve(A, rhs)
print("steady state via solve:", np.round(exact, 6))
print("agree:", bool(np.allclose(exact, steady)))

# Expected number of sunny days in the next 30 starting from rainy
dist = np.array([0.0, 0.0, 1.0])
total = np.zeros(3)
for _ in range(30):
    dist = dist @ P
    total += dist
print("expected days per state over 30 days:", np.round(total, 6))

# Integer matrix powers stay exact: Fibonacci numbers
F = np.array([[1, 1], [1, 0]])
print("Fibonacci matrix ^10:")
print(np.linalg.matrix_power(F, 10))
print(repr(np.linalg.matrix_power(F, 0)))
