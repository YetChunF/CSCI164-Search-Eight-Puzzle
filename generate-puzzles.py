from animate import puzzle
import random

NUM_PUZZLES = 4
NUM_SHUFFLES = 100000000
moves = "ULDR"
all_puzzles = []
for _ in range(NUM_PUZZLES):
    state = "012345678"
    for _ in range(NUM_SHUFFLES):
        neighbors = puzzle.get_neighbors(state)
        state, op = neighbors[random.randrange(0, len(neighbors))]
    all_puzzles.append(state)
print(all_puzzles)