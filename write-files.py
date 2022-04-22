import astar
import time

to_solve = ['865102473', '632754180', '140386527', '142607358']

f = open(f"solutions/hard-eight-solutions.txt", "w")

solutions = []
for p in to_solve:
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

