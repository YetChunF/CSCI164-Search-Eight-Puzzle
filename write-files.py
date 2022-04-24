import astar
import time
from animate import puzzle
import animate

SAVE_FILE_NAME = "others-solutions.txt"
all_puzzles = ["045372816", "721804356", "237416B8590CDAEF", "132456879ABCDE0F"]

f = open(f"solutions/{SAVE_FILE_NAME}", "w")

solutions = []
for p in all_puzzles:
    init_state = [c for c in p]
    goal_state = sorted(init_state)
    goal_state.pop(0)
    goal_state.append("0")
    print(goal_state)
    puzzle.set_board_size(int((len(init_state))**(1/2)))
    print(f"Puzzle: {p} Solution: {''.join(goal_state)}")
    current_time = time.time()
    sol, n = astar.a_star(init_state, goal_state)
    time_elapsed = time.time() - current_time
    print(f"Solution: {sol}")

    f.write(f"Puzzle: {p} Nodes: {n} Time: {round(time_elapsed, 2)}s Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

