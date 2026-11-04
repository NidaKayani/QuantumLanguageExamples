"""Merging sorted logs, finding duplicates and nearest neighbours in sorted arrays."""
import numpy as np

# Two sorted event timestamp streams
log_a = np.array([2, 5, 9, 14, 20, 27, 33])
log_b = np.array([1, 5, 8, 15, 20, 21, 40, 41])
print("log A:", log_a)
print("log B:", log_b)

merged = np.sort(np.concatenate((log_a, log_b)), kind="stable")
print("merged:", merged)
print(repr(merged))

# Which source did each merged item come from? (stable keeps A before B on ties)
source = np.concatenate((np.zeros(log_a.size, dtype=int), np.ones(log_b.size, dtype=int)))
order = np.argsort(np.concatenate((log_a, log_b)), kind="stable")
print("source of merged items:", source[order])

# Duplicated timestamps
dup_mask = np.concatenate(([False], merged[1:] == merged[:-1]))
print("duplicate timestamps:", np.unique(merged[dup_mask]))

# Nearest timestamp in log B for each A entry
pos = np.searchsorted(log_b, log_a)
pos = np.clip(pos, 1, log_b.size - 1)
left = log_b[pos - 1]
right = log_b[pos]
nearest = np.where(np.abs(log_a - left) <= np.abs(right - log_a), left, right)
print("nearest B for each A:", nearest)
print("gap:", np.abs(log_a - nearest))

# Gaps in the merged stream and the largest silence
gaps = np.diff(merged)
print("gaps:", gaps)
widest = int(np.argmax(gaps))
print(f"longest silence: {gaps[widest]} between t={merged[widest]} and t={merged[widest + 1]}")

# Sliding-window counts with searchsorted: events in [t, t+10)
starts = np.arange(0, 45, 10)
counts = np.searchsorted(merged, starts + 10) - np.searchsorted(merged, starts)
print("window starts:", starts)
print("events per window:", counts)

# Sort a 2-D event table by time column and look up a time
events = np.array([[20, 3], [5, 1], [33, 2], [9, 1], [14, 3]])
events = events[np.argsort(events[:, 0], kind="stable")]
print("events sorted by time:")
print(events)
t = 14
i = np.searchsorted(events[:, 0], t)
print(f"event at t={t}: found={bool(i < len(events) and events[i, 0] == t)}, code={events[i, 1]}")

# Values that appear in exactly one log
print("exclusive timestamps:", np.setxor1d(log_a, log_b))
print("is merged sorted:", bool(np.all(np.diff(merged) >= 0)))
