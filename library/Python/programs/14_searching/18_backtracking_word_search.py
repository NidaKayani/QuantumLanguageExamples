"""Word search in a letter grid using DFS backtracking with prefix pruning."""

BOARD = [
    "OATHS",
    "ETAEN",
    "IHKRS",
    "IFLVE",
]
DICTIONARY = ["oath", "pea", "eat", "rain", "hike", "tea", "teak", "heat", "than", "fake", "seen", "nerve", "kit"]

ROWS, COLS = len(BOARD), len(BOARD[0])
PREFIXES = {w[:i].upper() for w in DICTIONARY for i in range(1, len(w) + 1)}
WORDS = {w.upper() for w in DICTIONARY}


def dfs(r, c, prefix, visited, path, found):
    prefix += BOARD[r][c]
    if prefix not in PREFIXES:
        return
    visited.add((r, c))
    path.append((r, c))
    if prefix in WORDS and prefix not in found:
        found[prefix] = list(path)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            nr, nc = r + dr, c + dc
            if (dr or dc) and 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                dfs(nr, nc, prefix, visited, path, found)
    visited.discard((r, c))
    path.pop()


found = {}
for r in range(ROWS):
    for c in range(COLS):
        dfs(r, c, "", set(), [], found)

print("board:")
for row in BOARD:
    print("  " + " ".join(row))
print(f"found {len(found)} of {len(WORDS)} words:")
for word in sorted(found):
    print(f"  {word:<6} path={found[word]}")
print("not found:", sorted(WORDS - found.keys()))
