"""Sorting applied: matrix rows/columns, diagonals and interval merging."""

from collections import defaultdict

matrix = [
    [9, 3, 7, 1],
    [4, 8, 2, 6],
    [5, 0, 11, 10],
]

print("rows sorted:", [sorted(row) for row in matrix])
cols_sorted = [list(col) for col in zip(*(sorted(c) for c in zip(*matrix)))]
print("columns sorted:", cols_sorted)
print("rows by sum:", sorted(matrix, key=sum))
print("rows by max desc:", sorted(matrix, key=max, reverse=True))

diagonals = defaultdict(list)
for r, row in enumerate(matrix):
    for c, v in enumerate(row):
        diagonals[r - c].append(v)
for d in diagonals.values():
    d.sort(reverse=True)  # pop smallest from end
diag_sorted = [[diagonals[r - c].pop() for c in range(len(matrix[0]))] for r in range(len(matrix))]
print("each diagonal sorted:")
for row in diag_sorted:
    print("  ", row)


def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


meetings = [(9, 10), (13, 15), (9, 12), (14, 16), (17, 18), (11, 12)]
print("meetings:", meetings)
print("busy blocks:", merge_intervals(meetings))
print("sorted by end (greedy schedule):", sorted(meetings, key=lambda m: m[1]))
chosen, last_end = [], float("-inf")
for s, e in sorted(meetings, key=lambda m: m[1]):
    if s >= last_end:
        chosen.append((s, e))
        last_end = e
print("max non-overlapping:", chosen)
