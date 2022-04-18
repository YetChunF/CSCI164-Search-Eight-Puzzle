import astar
import animate

f = open(f"solutions/eight-puzzle-solutions.txt", "w")

solutions = []
for p in astar.small_puzzles:
    print(f"Solving {p}")
    goal_state = "".join(sorted([c for c in p]))
    sol, _ = astar.a_star(p, goal_state)
    print(f"Solution: {sol}")

    f.write(f"Puzzle: {p} Solution: ")
    for state in sol:
        f.write(f"{state}")
    f.write("\n")

f.close()

