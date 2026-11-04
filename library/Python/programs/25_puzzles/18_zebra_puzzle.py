"""The Zebra (Einstein) puzzle solved with permutations and early-pruned generator expressions."""
from itertools import permutations

houses = first, _, middle, _, _ = range(5)
orderings = list(permutations(houses))


def right_of(h1, h2):
    return h1 - h2 == 1


def next_to(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle():
    return next(
        {"color": colors, "nation": nations, "drink": drinks, "smoke": smokes, "pet": pets}
        for colors in orderings
        for (red, green, ivory, yellow, blue) in [colors]
        if right_of(green, ivory)
        for nations in orderings
        for (englishman, spaniard, ukranian, norwegian, japanese) in [nations]
        if englishman == red
        if norwegian == first
        if next_to(norwegian, blue)
        for drinks in orderings
        for (coffee, tea, milk, oj, water) in [drinks]
        if coffee == green
        if ukranian == tea
        if milk == middle
        for smokes in orderings
        for (oldgold, kools, chesterfields, luckystrike, parliaments) in [smokes]
        if kools == yellow
        if luckystrike == oj
        if japanese == parliaments
        for pets in orderings
        for (dog, snails, fox, horse, zebra) in [pets]
        if spaniard == dog
        if oldgold == snails
        if next_to(chesterfields, fox)
        if next_to(kools, horse)
    )


solution = zebra_puzzle()
names = {
    "color": ["red", "green", "ivory", "yellow", "blue"],
    "nation": ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
    "drink": ["coffee", "tea", "milk", "orange juice", "water"],
    "smoke": ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"],
    "pet": ["dog", "snails", "fox", "horse", "zebra"],
}
table = {h: {} for h in houses}
for category, positions in solution.items():
    for name, house in zip(names[category], positions):
        table[house][category] = name

print(f"{'house':<6}" + "".join(f"{c:<14}" for c in names))
for h in houses:
    print(f"{h + 1:<6}" + "".join(f"{table[h][c]:<14}" for c in names))


def who_has(category, item):
    house = solution[category][names[category].index(item)]
    return table[house]["nation"]


print()
print(f"The {who_has('drink', 'water')} drinks water; the {who_has('pet', 'zebra')} owns the zebra.")
