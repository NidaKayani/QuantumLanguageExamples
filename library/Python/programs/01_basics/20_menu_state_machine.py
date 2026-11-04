"""Drive a vending machine state machine with a scripted sequence of events."""

from enum import Enum, auto


class State(Enum):
    IDLE = auto()
    COLLECTING = auto()
    DISPENSING = auto()


PRICES = {"cola": 125, "chips": 75, "candy": 60}

state = State.IDLE
credit = 0
sales = []

events = [
    ("coin", 25), ("coin", 100), ("select", "cola"),
    ("coin", 50), ("select", "chips"), ("coin", 25), ("select", "chips"),
    ("coin", 100), ("refund", None),
    ("select", "candy"),
]

for kind, value in events:
    match (state, kind):
        case (State.IDLE | State.COLLECTING, "coin"):
            credit += value
            state = State.COLLECTING
            print(f"inserted {value}c, credit {credit}c")
        case (State.COLLECTING, "select"):
            price = PRICES[value]
            if credit >= price:
                state = State.DISPENSING
                change = credit - price
                print(f"dispensing {value}; change {change}c")
                sales.append(value)
                credit = 0
                state = State.IDLE
            else:
                print(f"{value} costs {price}c, need {price - credit}c more")
        case (State.COLLECTING, "refund"):
            print(f"refunding {credit}c")
            credit = 0
            state = State.IDLE
        case (State.IDLE, "select"):
            print(f"insert coins before selecting {value}")
        case _:
            print(f"ignored {kind} in {state.name}")

print("final state:", state.name, "| credit:", credit)
print("sales:", sales, "| revenue:", sum(PRICES[s] for s in sales), "cents")
