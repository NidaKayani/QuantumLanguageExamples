"""Binning measurements with np.digitize and building histograms from bin indices."""
import numpy as np

# Pseudo-random heights (cm) from a small linear congruential generator
state = 12345
heights = []
for _ in range(40):
    state = (state * 214013 + 2531011) % 4294967296
    heights.append(150 + (state >> 16) % 45)
heights = np.array(heights, dtype=float)
print("heights:")
print(heights)

bins = np.array([155.0, 165.0, 175.0, 185.0])
idx = np.digitize(heights, bins)
print("bin index per height:")
print(idx)
print(repr(idx[:10]))

labels = ["<155", "155-165", "165-175", "175-185", ">=185"]
counts = np.bincount(idx, minlength=len(bins) + 1)
print("counts per bin:", counts)
for lab, c in zip(labels, counts):
    print(f"  {lab:>8}: {'*' * int(c)}")

# right=True changes which side of an edge a boundary value goes
edges = np.array([0, 10, 20, 30])
vals = np.array([0, 5, 10, 15, 20, 30, 35])
print("vals:", vals)
print("digitize right=False:", np.digitize(vals, edges))
print("digitize right=True: ", np.digitize(vals, edges, right=True))

# Decreasing bins are allowed too
dec = np.array([30, 20, 10, 0])
print("decreasing bins:", np.digitize(vals, dec))

# Compare with np.histogram on the same edges
hist, hedges = np.histogram(heights, bins=np.array([150.0, 160.0, 170.0, 180.0, 195.0]))
print("histogram counts:", hist)
print("histogram edges:", hedges)

# Average value per bin
means = np.array([heights[idx == b].mean() if np.any(idx == b) else 0.0
                  for b in range(len(bins) + 1)])
print("mean height per bin:", np.round(means, 2))

# Temperature classification
temps = np.array([-5.0, 0.0, 4.5, 12.0, 18.5, 25.0, 31.0])
zones = np.digitize(temps, [0.0, 10.0, 20.0, 30.0])
names = ["freezing", "cold", "mild", "warm", "hot"]
for t, z in zip(temps, zones):
    print(f"  {t:6.1f} -> {names[z]}")
