import astar
import animate

solutions = []
for p in astar.four_board_ez:
    print(f"Solving {p}")
    goal_state = "".join(sorted([c for c in p]))
    sol, _ = astar.a_star(p, goal_state)
    print(f"Solution: {sol}")

    f = open(f"solutions/{p}.txt", "w")
    for state in sol:
        f.write(f"{state}\n")
    f.close()

