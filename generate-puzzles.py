from animate import puzzle
import random

NUM_PUZZLES = 10
NUM_SHUFFLES = 100000
moves = "ULDR"
all_puzzles = []
for _ in range(NUM_PUZZLES):
    state = "865102473"
    for _ in range(NUM_SHUFFLES):
        neighbors = puzzle.get_neighbors(state)
        state, op = neighbors[random.randrange(0, len(neighbors))]
    all_puzzles.append(state)
print(all_puzzles)