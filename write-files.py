import astar

to_solve = ['865102473', '632754180', '140386527', '142607358']

f = open(f"solutions/hard-eight-solutions.txt", "w")

solutions = []
for p in to_solve:
    print(f"Solving {p}")
    goal_state = "".join(sorted([c for c in p]))
    sol, _ = astar.a_star(p, goal_state)
    print(f"Solution: {sol}")

    f.write(f"Puzzle: {p} Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

