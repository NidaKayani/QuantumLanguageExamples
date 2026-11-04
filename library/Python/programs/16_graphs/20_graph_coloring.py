"""Greedy and backtracking graph colouring for an exam-scheduling conflict graph."""
from dataclasses import dataclass, field
from itertools import combinations


@dataclass
class ConflictGraph:
    edges: dict = field(default_factory=dict)

    def add(self, a, b):
        self.edges.setdefault(a, set()).add(b)
        self.edges.setdefault(b, set()).add(a)

    def nodes_by_degree(self):
        return sorted(self.edges, key=lambda n: (-len(self.edges[n]), n))

    def greedy(self):
        colors = {}
        for node in self.nodes_by_degree():
            used = {colors[n] for n in self.edges[node] if n in colors}
            colors[node] = next(c for c in range(len(self.edges)) if c not in used)
        return colors

    def k_colorable(self, k):
        order = self.nodes_by_degree()
        colors = {}

        def place(i):
            if i == len(order):
                return True
            node = order[i]
            for c in range(k):
                if all(colors.get(n) != c for n in self.edges[node]):
                    colors[node] = c
                    if place(i + 1):
                        return True
                    del colors[node]
            return False

        return dict(colors) if place(0) else None


def main():
    enrolments = {
        "ana": ["math", "physics", "art"],
        "ben": ["math", "chem"],
        "cara": ["physics", "chem", "bio"],
        "dev": ["art", "bio", "history"],
        "eli": ["history", "math"],
        "fay": ["chem", "art"],
    }
    graph = ConflictGraph()
    for courses in enrolments.values():
        for a, b in combinations(courses, 2):
            graph.add(a, b)
    print("Conflicts:")
    for course in sorted(graph.edges):
        print(f"  {course:<8} clashes with {', '.join(sorted(graph.edges[course]))}")
    greedy = graph.greedy()
    print("Greedy slots used:", max(greedy.values()) + 1)
    for k in range(1, 5):
        result = graph.k_colorable(k)
        if result:
            print(f"Minimum slots: {k}")
            slots = {}
            for course, slot in result.items():
                slots.setdefault(slot, []).append(course)
            for slot in sorted(slots):
                print(f"  Slot {slot + 1}: {', '.join(sorted(slots[slot]))}")
            break
        print(f"{k} slot(s) impossible")


if __name__ == "__main__":
    main()
