"""Aggregate list data with sum, min, max, any, all, sorted and statistics."""

import statistics

temps = [21.5, 19.0, 23.4, 25.1, 18.7, 22.0, 24.3]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(f"total: {sum(temps):.1f}")
print(f"mean: {sum(temps) / len(temps):.2f}  (statistics: {statistics.mean(temps):.2f})")
print(f"median: {statistics.median(temps)}")
print(f"stdev: {statistics.stdev(temps):.3f}")
print(f"min: {min(temps)} on {days[temps.index(min(temps))]}")
print(f"max: {max(temps)} on {days[temps.index(max(temps))]}")
print("range:", round(max(temps) - min(temps), 2))

print("any above 25:", any(t > 25 for t in temps))
print("all above 18:", all(t > 18 for t in temps))
warm = [d for d, t in zip(days, temps) if t >= 22]
print("warm days:", warm)

ranked = sorted(zip(temps, days), reverse=True)
print("top 3:", [f"{d}={t}" for t, d in ranked[:3]])

# running max and moving average
running_max = []
current = float("-inf")
for t in temps:
    current = max(current, t)
    running_max.append(current)
print("running max:", running_max)
window = 3
moving = [round(sum(temps[i:i + window]) / window, 2) for i in range(len(temps) - window + 1)]
print("3-day moving avg:", moving)

print("sum with start:", sum([[1], [2, 3], [4]], []))
print("mode:", statistics.mode([3, 1, 3, 2, 1, 3]))
