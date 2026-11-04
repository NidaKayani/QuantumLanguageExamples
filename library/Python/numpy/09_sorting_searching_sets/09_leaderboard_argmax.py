"""A tournament leaderboard built with argmax/argmin, where, nonzero and repeated extraction."""
import numpy as np

teams = ["Lions", "Hawks", "Bears", "Otters", "Wolves", "Foxes"]
# rounds x teams score matrix
scores = np.array([[12, 9, 15, 7, 11, 10],
                   [8, 14, 10, 13, 9, 12],
                   [11, 11, 9, 14, 15, 8],
                   [13, 7, 12, 10, 10, 14]])
print("scores per round:")
print(scores)

round_winner = np.argmax(scores, axis=1)
print("winner index per round:", round_winner)
for r, w in enumerate(round_winner):
    print(f"  round {r + 1}: {teams[w]} ({scores[r, w]})")

round_loser = np.argmin(scores, axis=1)
print("loser index per round:", round_loser)

totals = scores.sum(axis=0)
print("totals:", totals)
print(repr(totals))

# Repeated argmax extraction for a full ranking (masking out picked items)
work = totals.astype(float)
ranking = []
for _ in range(len(teams)):
    best = int(np.argmax(work))
    ranking.append(best)
    work[best] = -np.inf
ranking = np.array(ranking)
print("ranking by repeated argmax:", ranking)
for place, t in enumerate(ranking, 1):
    print(f"  {place}. {teams[t]:<7} {totals[t]}")

# Position of the overall max in 2-D via unravel_index
flat = np.argmax(scores)
r, c = np.unravel_index(flat, scores.shape)
print("highest single score:", scores[r, c], "by", teams[c], "in round", r + 1)

# Teams that ever scored >= 14
hi_rows, hi_cols = np.nonzero(scores >= 14)
print("rows/cols with score >= 14:", hi_rows, hi_cols)
print("teams with a 14+:", sorted({teams[c] for c in hi_cols}))

# Wins per team using one-hot comparison
wins = np.bincount(round_winner, minlength=len(teams))
print("round wins:", wins)

# Margin of victory per round: top minus second
top2 = np.sort(scores, axis=1)[:, -2:]
print("margins:", top2[:, 1] - top2[:, 0])

# np.where to label rounds above average
avg = scores.mean(axis=1, keepdims=True)
print("above round average:")
print(np.where(scores > avg, 1, 0))
print("first round each team beat average:", np.argmax(scores > avg, axis=0))
