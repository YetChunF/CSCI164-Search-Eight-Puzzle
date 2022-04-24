import astar
import time
from animate import puzzle
import random

# Constants

NUM_PUZZLES = 5
NUM_SHUFFLES = 10
INITIAL_STATE = "123456780"
SAVE_FILE_NAME = "my-solutions.txt"

# MAIN

puzzle.set_board_size(int((len(INITIAL_STATE))**(1/2)))
initial_state = [c for c in INITIAL_STATE]
moves = "ULDR"
all_puzzles = []
for _ in range(NUM_PUZZLES):
    state = initial_state[:]
    for _ in range(NUM_SHUFFLES):
        neighbors = puzzle.get_neighbors(state)
        state, op = neighbors[random.randrange(0, len(neighbors))]
    all_puzzles.append(state)

f = open(f"solutions/{SAVE_FILE_NAME}", "w")

solutions = []
for p in all_puzzles:
    p_str = ''.join(p)
    print(f"Solving {p_str}")
    goal_state = initial_state[:]
    current_time = time.time()
    sol, n = astar.a_star(p, goal_state)
    time_elapsed = time.time() - current_time
    print(f"Puzzle: {p_str} Time: {round(time_elapsed, 2)}s Solution: {''.join(sol)}\n")
    f.write(f"Puzzle: {p_str} Time: {round(time_elapsed, 2)}s Solution: {''.join(sol)}\n")

f.close()