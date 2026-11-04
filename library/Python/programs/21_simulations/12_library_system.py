"""Library lending system with holds, due dates in days and overdue fines."""
from collections import defaultdict, deque


class Library:
    LOAN_DAYS = 14
    FINE_PER_DAY = 0.25

    def __init__(self, catalog):
        self.copies = dict(catalog)
        self.loans = {}
        self.holds = defaultdict(deque)
        self.fines = defaultdict(float)
        self.events = []

    def checkout(self, member, title, day):
        if self.copies.get(title, 0) == 0:
            if member not in self.holds[title]:
                self.holds[title].append(member)
            self.events.append(f"day {day}: {member} placed hold on {title!r}")
            return False
        if self.holds[title] and self.holds[title][0] != member:
            self.events.append(f"day {day}: {title!r} reserved for {self.holds[title][0]}")
            return False
        if self.holds[title]:
            self.holds[title].popleft()
        self.copies[title] -= 1
        self.loans[(member, title)] = day + self.LOAN_DAYS
        self.events.append(f"day {day}: {member} borrowed {title!r}, due day {day + self.LOAN_DAYS}")
        return True

    def checkin(self, member, title, day):
        due = self.loans.pop((member, title))
        late = max(0, day - due)
        if late:
            self.fines[member] += late * self.FINE_PER_DAY
        self.copies[title] += 1
        note = f", {late} days late" if late else ""
        self.events.append(f"day {day}: {member} returned {title!r}{note}")
        if self.holds[title]:
            self.checkout(self.holds[title][0], title, day)


lib = Library({"Dune": 1, "Emma": 2, "Ulysses": 1})
lib.checkout("ann", "Dune", 1)
lib.checkout("ben", "Dune", 2)
lib.checkout("cat", "Dune", 3)
lib.checkout("ben", "Emma", 3)
lib.checkout("ann", "Ulysses", 4)
lib.checkin("ben", "Emma", 10)
lib.checkin("ann", "Dune", 20)
lib.checkin("ann", "Ulysses", 25)
lib.checkin("ben", "Dune", 30)

print("\n".join(lib.events))
print("Outstanding loans:", sorted(lib.loans.items()))
print("Fines:", {m: f"${f:.2f}" for m, f in sorted(lib.fines.items())})
print("Copies on shelf:", lib.copies)
