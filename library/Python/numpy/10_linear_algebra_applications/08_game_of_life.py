"""Conway's Game of Life on a torus, counting neighbours with np.roll."""
import numpy as np


def step(board):
    neighbours = sum(
        np.roll(np.roll(board, dy, axis=0), dx, axis=1)
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if (dy, dx) != (0, 0)
    )
    born = (board == 0) & (neighbours == 3)
    survive = (board == 1) & ((neighbours == 2) | (neighbours == 3))
    return (born | survive).astype(int)


def show(board):
    for row in board:
        print("".join("#" if c else "." for c in row))


# Glider on an 8x8 torus
board = np.zeros((8, 8), dtype=int)
board[1, 2] = 1
board[2, 3] = 1
board[3, 1:4] = 1
print("initial board:")
print(board)
print(repr(board[1:4, 1:4]))

for gen in range(1, 5):
    board = step(board)
    print(f"generation {gen}: population {board.sum()}")
    show(board)

# After 4 generations the glider moved one cell down and right
start = np.zeros((8, 8), dtype=int)
start[1, 2] = 1
start[2, 3] = 1
start[3, 1:4] = 1
print("glider translated by (1, 1):", bool(np.array_equal(board, np.roll(start, (1, 1), axis=(0, 1)))))

# Blinker oscillator has period 2
blinker = np.zeros((5, 5), dtype=int)
blinker[2, 1:4] = 1
b1 = step(blinker)
b2 = step(b1)
print("blinker phase 1:")
print(b1)
print("period 2:", bool(np.array_equal(b2, blinker)))

# Block still life
block = np.zeros((4, 4), dtype=int)
block[1:3, 1:3] = 1
print("block is stable:", bool(np.array_equal(step(block), block)))

# Neighbour count map for the initial glider
nb = sum(np.roll(start, (dy, dx), axis=(0, 1))
         for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0))
print("neighbour counts:")
print(nb[:5, :5])
print("as bool mask of live cells:")
print(start[:5, :5].astype(bool))
