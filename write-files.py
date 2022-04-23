import astar
import time
from animate import puzzle
import animate
import random

all_puzzles = ["237416B8590CDAEF"]

f = open(f"solutions/others-fifteen-solutions.txt", "w")

solutions = []
for p in all_puzzles:
    goal_state = "".join(sorted([c for c in p]))
    print(f"Puzzle: {p} Solution: {goal_state}")
    current_time = time.time()
    sol, _ = astar.a_star(p, goal_state)
    time_elapsed = time.time() - current_time
    print(f"Solution: {sol}")
    animate.run_anim_moves(p, sol)

    f.write(f"Puzzle: {p} Time: {round(time_elapsed, 2)}s Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

