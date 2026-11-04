"""Parking lot with sized spots, nearest-spot allocation via heaps, and hourly billing."""
import heapq
import math
from enum import IntEnum


class Size(IntEnum):
    MOTO = 1
    CAR = 2
    VAN = 3


RATES = {Size.MOTO: 1.0, Size.CAR: 2.5, Size.VAN: 4.0}


class ParkingLot:
    def __init__(self, layout):
        self.free = {size: [] for size in Size}
        for spot, size in enumerate(layout):
            heapq.heappush(self.free[size], spot)
        self.parked = {}
        self.revenue = 0.0

    def park(self, plate, vehicle, minute):
        for size in Size:
            if size >= vehicle and self.free[size]:
                spot = heapq.heappop(self.free[size])
                self.parked[plate] = (spot, size, vehicle, minute)
                return spot
        return None

    def leave(self, plate, minute):
        spot, size, vehicle, start = self.parked.pop(plate)
        heapq.heappush(self.free[size], spot)
        hours = max(1, math.ceil((minute - start) / 60))
        fee = hours * RATES[vehicle]
        self.revenue += fee
        return spot, fee


lot = ParkingLot([Size.MOTO, Size.CAR, Size.CAR, Size.VAN, Size.CAR, Size.MOTO, Size.VAN])
events = [
    (0, "in", "AB-1", Size.CAR), (5, "in", "MC-7", Size.MOTO), (10, "in", "VN-3", Size.VAN),
    (12, "in", "CR-9", Size.CAR), (15, "in", "CR-4", Size.CAR), (20, "in", "VN-8", Size.VAN),
    (25, "in", "CR-2", Size.CAR), (95, "out", "AB-1", None), (100, "in", "CR-5", Size.CAR),
    (200, "out", "VN-3", None), (210, "in", "MC-1", Size.MOTO), (215, "in", "MC-2", Size.MOTO),
    (240, "out", "MC-7", None), (241, "out", "CR-5", None),
]
for minute, kind, plate, vehicle in events:
    if kind == "in":
        spot = lot.park(plate, vehicle, minute)
        status = f"spot {spot}" if spot is not None else "LOT FULL for this size"
        print(f"{minute:>4}m  {plate} ({vehicle.name}) arrives -> {status}")
    else:
        spot, fee = lot.leave(plate, minute)
        print(f"{minute:>4}m  {plate} leaves spot {spot}, pays ${fee:.2f}")

print("Still parked:", sorted((p, s[0]) for p, s in lot.parked.items()))
print("Free spots:", {size.name: sorted(spots) for size, spots in lot.free.items()})
print(f"Revenue: ${lot.revenue:.2f}")
