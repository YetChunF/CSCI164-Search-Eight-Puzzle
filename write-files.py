import astar
import time
from animate import puzzle
import random

NUM_PUZZLES = 10
NUM_SHUFFLES = 1000000
INITIAL_STATE = "012345678"

moves = "ULDR"
all_puzzles = []
for _ in range(NUM_PUZZLES):
    state = INITIAL_STATE
    for _ in range(NUM_SHUFFLES):
        neighbors = puzzle.get_neighbors(state)
        state, op = neighbors[random.randrange(0, len(neighbors))]
    all_puzzles.append(state)
print(all_puzzles)

f = open(f"solutions/hard-eight-solutions.txt", "w")

solutions = []
for p in all_puzzles:
    print(f"Solving {p}")
    goal_state = "".join(sorted([c for c in p]))
    current_time = time.time()
    sol, _ = astar.a_star(p, goal_state)
    time_elapsed = time.time() - current_time
    print(f"Solution: {sol}")

    f.write(f"Puzzle: {p} Time: {round(time_elapsed, 2)}s Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

