"""Simulate a binary-search number guessing game against fixed secret numbers."""


def play(secret, low=1, high=100):
    guesses = []
    while low <= high:
        guess = (low + high) // 2
        guesses.append(guess)
        if guess == secret:
            return guesses
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1
    raise ValueError(f"secret {secret} out of range")


secrets = [1, 37, 50, 64, 99, 100]
for s in secrets:
    trail = play(s)
    hint = " -> ".join(map(str, trail))
    print(f"secret {s:3d}: found in {len(trail)} guesses ({hint})")

# worst case over the whole range
worst = max(range(1, 101), key=lambda s: len(play(s)))
print(f"hardest secret: {worst} ({len(play(worst))} guesses)")

average = sum(len(play(s)) for s in range(1, 101)) / 100
print(f"average guesses: {average:.2f}")

try:
    play(150)
except ValueError as err:
    print("error:", err)
