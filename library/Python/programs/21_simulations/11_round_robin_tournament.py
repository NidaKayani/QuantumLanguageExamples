"""Round-robin tournament scheduling with deterministic match outcomes and a standings table."""
from collections import defaultdict
from itertools import combinations

teams = ["Lions", "Tigers", "Bears", "Wolves", "Hawks", "Sharks"]
ratings = {"Lions": 82, "Tigers": 78, "Bears": 75, "Wolves": 80, "Hawks": 70, "Sharks": 77}


def schedule(teams):
    """Circle method: fix the first team, rotate the rest."""
    teams = list(teams)
    rounds = []
    for _ in range(len(teams) - 1):
        half = len(teams) // 2
        rounds.append(list(zip(teams[:half], reversed(teams[half:]))))
        teams = [teams[0], teams[-1], *teams[1:-1]]
    return rounds


def play(home, away, round_no):
    swing = (len(home) * 7 + len(away) * 3 + round_no * 11) % 9 - 4
    diff = ratings[home] - ratings[away] + swing + 2
    home_goals = max(0, 1 + diff // 4)
    away_goals = max(0, 1 - diff // 4)
    return home_goals, away_goals


table = defaultdict(lambda: {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "Pts": 0})
for r, matches in enumerate(schedule(teams), 1):
    results = []
    for home, away in matches:
        hg, ag = play(home, away, r)
        results.append(f"{home} {hg}-{ag} {away}")
        for team, gf, ga in ((home, hg, ag), (away, ag, hg)):
            row = table[team]
            row["P"] += 1
            row["GF"] += gf
            row["GA"] += ga
            outcome = "W" if gf > ga else "L" if gf < ga else "D"
            row[outcome] += 1
            row["Pts"] += {"W": 3, "D": 1, "L": 0}[outcome]
    print(f"Round {r}: " + "; ".join(results))

all_pairs = {frozenset(p) for rnd in schedule(teams) for p in rnd}
print("Every pair meets exactly once:", all_pairs == {frozenset(c) for c in combinations(teams, 2)})

standings = sorted(table.items(), key=lambda kv: (-kv[1]["Pts"], -(kv[1]["GF"] - kv[1]["GA"]), kv[0]))
print(f"\n{'#':>2} {'Team':<8} P  W  D  L  GF GA Pts")
for pos, (team, s) in enumerate(standings, 1):
    print(f"{pos:>2} {team:<8} {s['P']}  {s['W']}  {s['D']}  {s['L']}  {s['GF']:>2} {s['GA']:>2} {s['Pts']:>3}")
