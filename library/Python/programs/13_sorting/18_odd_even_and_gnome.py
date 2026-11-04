"""Less common comparison sorts: gnome, odd-even transposition and comb sort."""


def gnome_sort(a):
    a = list(a)
    i, steps = 0, 0
    while i < len(a):
        steps += 1
        if i == 0 or a[i - 1] <= a[i]:
            i += 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i -= 1
    return a, steps


def odd_even_sort(a):
    a = list(a)
    rounds = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        rounds += 1
        for start in (1, 0):
            for i in range(start, len(a) - 1, 2):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    is_sorted = False
    return a, rounds


def comb_sort(a, shrink=1.3):
    a = list(a)
    gap, done, gaps = len(a), False, []
    while not done:
        gap = max(1, int(gap / shrink))
        gaps.append(gap)
        done = gap == 1
        for i in range(len(a) - gap):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
                done = False
    return a, gaps


data = [34, 2, 10, -9, 7, 21, 0, 15, 3, 3]
g, steps = gnome_sort(data)
print(f"gnome:    {g} ({steps} steps)")
o, rounds = odd_even_sort(data)
print(f"odd-even: {o} ({rounds} rounds)")
c, gaps = comb_sort(data)
print(f"comb:     {c} gaps={gaps}")
assert g == o == c == sorted(data)

for name, fn in [("gnome", gnome_sort), ("odd-even", odd_even_sort), ("comb", comb_sort)]:
    result, _ = fn("algorithm")
    print(f"{name:<9} on 'algorithm': {''.join(result)}")
