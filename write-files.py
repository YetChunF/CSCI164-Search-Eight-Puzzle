import astar
import time
from animate import puzzle
import animate

all_puzzles = ["4123875BA906CDEF"]

f = open(f"solutions/others-fifteen-solutions.txt", "w")

solutions = []
for p in all_puzzles:
    init_state = [c for c in p]
    goal_state = sorted(init_state)
    puzzle.set_board_size(int((len(init_state))**(1/2)))
    print(f"Puzzle: {p} Solution: {''.join(goal_state)}")
    current_time = time.time()
    sol, _ = astar.a_star(init_state, goal_state)
    time_elapsed = time.time() - current_time
    print(f"Solution: {sol}")
    animate.run_anim_moves(p, sol)

    f.write(f"Puzzle: {p} Time: {round(time_elapsed, 2)}s Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

