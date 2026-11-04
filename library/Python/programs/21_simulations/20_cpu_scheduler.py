"""CPU scheduling simulation comparing FCFS, SJF and round-robin on the same workload."""
import heapq
from collections import deque, namedtuple

Process = namedtuple("Process", "pid arrival burst")

WORKLOAD = [Process("P1", 0, 8), Process("P2", 1, 4), Process("P3", 2, 9),
            Process("P4", 3, 5), Process("P5", 6, 2), Process("P6", 10, 3)]


def fcfs(procs):
    t, finish = 0, {}
    for p in sorted(procs, key=lambda p: p.arrival):
        t = max(t, p.arrival) + p.burst
        finish[p.pid] = t
    return finish


def sjf(procs):
    pending = sorted(procs, key=lambda p: p.arrival)
    ready, t, finish, i = [], 0, {}, 0
    while i < len(pending) or ready:
        while i < len(pending) and pending[i].arrival <= t:
            heapq.heappush(ready, (pending[i].burst, pending[i].arrival, pending[i].pid))
            i += 1
        if not ready:
            t = pending[i].arrival
            continue
        burst, _, pid = heapq.heappop(ready)
        t += burst
        finish[pid] = t
    return finish


def round_robin(procs, quantum=3):
    pending = deque(sorted(procs, key=lambda p: p.arrival))
    remaining = {p.pid: p.burst for p in procs}
    queue, t, finish, gantt = deque(), 0, {}, []
    while pending or queue:
        while pending and pending[0].arrival <= t:
            queue.append(pending.popleft().pid)
        if not queue:
            t = pending[0].arrival
            continue
        pid = queue.popleft()
        run = min(quantum, remaining[pid])
        gantt.append(f"{pid}[{t}-{t + run}]")
        t += run
        remaining[pid] -= run
        while pending and pending[0].arrival <= t:
            queue.append(pending.popleft().pid)
        if remaining[pid]:
            queue.append(pid)
        else:
            finish[pid] = t
    print("RR Gantt:", " ".join(gantt))
    return finish


for name, scheduler in (("FCFS", fcfs), ("SJF", sjf), ("RR q=3", round_robin)):
    finish = scheduler(WORKLOAD)
    turnaround = {p.pid: finish[p.pid] - p.arrival for p in WORKLOAD}
    waiting = {p.pid: turnaround[p.pid] - p.burst for p in WORKLOAD}
    print(f"{name:<7} finish={finish}")
    print(f"{'':<7} avg turnaround={sum(turnaround.values()) / len(WORKLOAD):.2f} "
          f"avg wait={sum(waiting.values()) / len(WORKLOAD):.2f}")
