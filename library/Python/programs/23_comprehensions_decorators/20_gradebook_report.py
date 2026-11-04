"""A gradebook report built almost entirely from comprehensions over nested records."""
import statistics

students = {
    "ana": {"math": [92, 88, 95], "physics": [78, 85], "art": [99]},
    "ben": {"math": [65, 70, 58], "physics": [72, 68], "art": [80, 85]},
    "cleo": {"math": [88, 91], "physics": [94, 97, 90], "art": []},
    "dev": {"math": [55, 62, 49], "physics": [], "art": [70, 75]},
}

averages = {name: {subj: round(statistics.mean(s), 1) for subj, s in subjects.items() if s}
            for name, subjects in students.items()}
for name, avg in averages.items():
    print(f"{name:<5}", ", ".join(f"{k}={v}" for k, v in avg.items()))

subjects = sorted({subj for subjects in students.values() for subj in subjects})
print("subjects:", subjects)

subject_means = {subj: round(statistics.mean(score for s in students.values() for score in s[subj]), 2)
                 for subj in subjects}
print("subject means:", subject_means)

overall = {name: round(statistics.mean(a.values()), 1) for name, a in averages.items()}
ranking = sorted(overall, key=overall.get, reverse=True)
print("ranking:", [(rank, n, overall[n]) for rank, n in enumerate(ranking, 1)])


def letter(score):
    return next(g for cutoff, g in [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")] if score >= cutoff)


letters = {name: letter(score) for name, score in overall.items()}
print("letters:", letters)
by_letter = {g: sorted(n for n, l in letters.items() if l == g) for g in sorted(set(letters.values()))}
print("grouped by letter:", by_letter)

missing = [(name, subj) for name, subjects in students.items() for subj, s in subjects.items() if not s]
print("missing work:", missing)

top_per_subject = {subj: max((a[subj], n) for n, a in averages.items() if subj in a)[1] for subj in subjects}
print("top per subject:", top_per_subject)

all_scores = [score for subjects in students.values() for s in subjects.values() for score in s]
histogram = {f"{lo}-{lo + 9}": sum(lo <= x <= lo + 9 for x in all_scores) for lo in range(40, 100, 10)}
for band, n in histogram.items():
    print(f"  {band:>6} {'#' * n}")
print("failing scores:", sorted(x for x in all_scores if x < 60))
