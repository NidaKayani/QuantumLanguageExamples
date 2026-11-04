"""Track student grades in nested dicts and compute report statistics."""

from collections import defaultdict
from statistics import mean

raw = [
    ("ana", "math", 92), ("ana", "physics", 85), ("ana", "art", 78),
    ("ben", "math", 67), ("ben", "physics", 74), ("ben", "art", 95),
    ("cleo", "math", 88), ("cleo", "physics", 91), ("cleo", "art", 82),
    ("dev", "math", 55), ("dev", "physics", 61),
]

grades = defaultdict(dict)
for student, subject, score in raw:
    grades[student][subject] = score

subjects = sorted({s for _, s, _ in raw})
print(f"{'student':<8}" + "".join(f"{s:>9}" for s in subjects) + f"{'avg':>8}")
for student, scores in grades.items():
    cells = "".join(f"{scores.get(s, '-'):>9}" for s in subjects)
    print(f"{student:<8}{cells}{mean(scores.values()):>8.1f}")

subject_avgs = {s: mean(g[s] for g in grades.values() if s in g) for s in subjects}
print("subject averages:", {s: round(a, 1) for s, a in subject_avgs.items()})

best_per_subject = {
    s: max((g[s], name) for name, g in grades.items() if s in g)[1] for s in subjects
}
print("best per subject:", best_per_subject)

missing = {name: sorted(set(subjects) - g.keys()) for name, g in grades.items() if set(subjects) - g.keys()}
print("missing work:", missing)


def letter(score):
    return next(l for cutoff, l in ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")) if score >= cutoff)


report = {name: {s: letter(v) for s, v in g.items()} for name, g in grades.items()}
for name, letters in report.items():
    print(f"  {name}: {letters}")

honor_roll = [name for name, g in grades.items() if mean(g.values()) >= 85]
print("honor roll:", honor_roll)
