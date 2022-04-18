import astar
import animate

solutions = []
for p in astar.four_board_ez:
    goal = "".join(sorted([x for x in p]))
    s, fbound = astar.a_star(p, goal)
    print(s)
    solutions.append(s)
    
    f = open(f"solutions/{p}.txt", "w")
    for state in s:
        f.write(f"{state}\n")
    f.close()
animate.run_animations(solutions)