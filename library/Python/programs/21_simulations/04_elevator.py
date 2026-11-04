"""Single elevator using the SCAN algorithm to serve timed floor requests."""
from collections import deque

requests = deque([(0, 5), (0, 2), (1, 8), (3, 1), (6, 4), (6, 9), (10, 0), (12, 3)])


class Elevator:
    def __init__(self, floors):
        self.floors = floors
        self.floor = 0
        self.direction = 1
        self.pending = set()
        self.log = []
        self.moved = 0

    def call(self, floor):
        if floor != self.floor:
            self.pending.add(floor)

    def tick(self, t):
        if not self.pending:
            return
        ahead = [f for f in self.pending if (f - self.floor) * self.direction > 0]
        if not ahead:
            self.direction = -self.direction
        self.floor += self.direction
        self.moved += 1
        if self.floor in self.pending:
            self.pending.discard(self.floor)
            self.log.append((t, self.floor))
            print(f"t={t:2d} stop at floor {self.floor}  pending={sorted(self.pending)}")


elevator = Elevator(floors=10)
t = 0
while requests or elevator.pending:
    while requests and requests[0][0] <= t:
        _, floor = requests.popleft()
        print(f"t={t:2d} request floor {floor}")
        elevator.call(floor)
    elevator.tick(t)
    t += 1

print("Stops served:", [floor for _, floor in elevator.log])
print("Floors travelled:", elevator.moved)
print("Finished at time", t, "on floor", elevator.floor)
