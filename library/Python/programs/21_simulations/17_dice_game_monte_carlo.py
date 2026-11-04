"""Monte Carlo comparison of 'Pig' dice game strategies using a custom LCG."""
from collections import Counter


class Rng:
    def __init__(self, seed):
        self.x = seed & 0xFFFFFFFF

    def die(self):
        # xorshift32 is tiny but far better than a raw LCG for low bits
        x = self.x
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= x >> 17
        x ^= (x << 5) & 0xFFFFFFFF
        self.x = x
        return x % 6 + 1


def hold_at(limit):
    def strategy(turn_total, my_score, other_score):
        return turn_total >= limit or my_score + turn_total >= 100
    strategy.__name__ = f"hold@{limit}"
    return strategy


def play(rng, strategies):
    scores = [0, 0]
    player = 0
    while True:
        turn = 0
        while True:
            roll = rng.die()
            if roll == 1:
                turn = 0
                break
            turn += roll
            if strategies[player](turn, scores[player], scores[1 - player]):
                break
        scores[player] += turn
        if scores[player] >= 100:
            return player
        player = 1 - player


rng = Rng(123456789)
rolls = Counter(rng.die() for _ in range(6000))
print("Die distribution:", dict(sorted(rolls.items())))

limits = [10, 15, 20, 25, 30]
strategies = [hold_at(n) for n in limits]
wins = Counter()
games = 200
for a in strategies:
    for b in strategies:
        if a is b:
            continue
        for g in range(games):
            order = (a, b) if g % 2 == 0 else (b, a)
            wins[order[play(rng, order)].__name__] += 1

total = games * 2 * (len(strategies) - 1)
for name, w in wins.most_common():
    print(f"{name:>8}: {w:4d} wins / {total} ({w / total:.1%})")
