from animate import puzzle
import priority
import math

small_puzzles = [
    "160273485",
    "462301587",
    "821574360",
    "840156372",
    "530478126",
    "068314257",
    "453207186",
    "128307645",
    "035684712",
    "684317025",
    "028514637",
    "618273540",
    "042385671",
    "420385716",
    "054672813",
    "314572680",
    "637218045",
    "430621875",
    "158274036",
    "130458726"
]

four_board_ez = [
    "16235A749C08DEBF",
    "0634217859ABDEFC",
    "012456379BC8DAEF",
    "51246A38097BDEFC",
    "12345678D9CFEBA0"
]

four_board_hard = [
    "71A92CE03DB4658F",
    "02348697DF5A1EBC",
    "39A1D0EC7BF86452",
    "EAB480FC19D56237",
    "7DB13C52F46E80A9"
]

# A* Algorithm Implementation
def a_star(start_state: str, goal_state: str):
    curr_node = start_state
    frontier = priority.PQ()
    frontier.push(curr_node, puzzle.manh(curr_node, goal_state))
    parent_map = {curr_node: ""}
    path_costs = {curr_node: 0}
    explored = set()
    num_explored = 0
    while not frontier.is_mt():
        curr_node, _ = frontier.pop()
        num_explored += 1
        if num_explored % 5000 == 0:
            print(f"Explored {num_explored} nodes...")
        explored.add(curr_node)
        if curr_node == goal_state:
            solution = []
            _current = curr_node
            while parent_map[_current] != "":
                solution.append(_current)
                _current = puzzle.get_prev(_current, parent_map[_current])
            solution.append(_current)
            solution.reverse()
            return solution, num_explored
        for child_node, op in puzzle.get_neighbors(curr_node):
            path_costs[child_node] = path_costs[curr_node] + 1
            priority_cost = path_costs[child_node] + puzzle.manh(child_node, goal_state)
            if (not child_node in explored) and (not frontier.is_in(child_node)):
                frontier.push(child_node, priority_cost)
                parent_map[child_node] = op
            elif (frontier.is_in(child_node)) and (frontier.get_cost(child_node) > priority_cost):
                frontier.set_cost(child_node, priority_cost)
                parent_map[child_node] = op

# Iterative Deepening Depth First Search
def iddfs(start_state: str, goal_state: str):
    depth = 1
    result = None
    while not result:
        result = ldfs(start_state, goal_state, 0, depth)
        if result:
            return result
        depth += 1
        print(f"Increasing depth to {depth}")
    return None

# Limited DFS
def ldfs(curr_node, goal_node, current_depth, max_depth):

    if curr_node == goal_node:
        print(f"Found goal node {curr_node} at depth {current_depth} with max depth {max_depth}")
        return curr_node
    if current_depth == max_depth:
        return None
    
    for child_node, _ in puzzle.get_neighbors(curr_node):
        result = ldfs(child_node, goal_node, current_depth + 1, max_depth)
        if result:
            return result
    return None

# Iterative Deepening A*
def ida_star(start_state: str, goal_state: str, verbose:bool=False):
    bound = puzzle.manh(start_state, goal_state)
    path = [start_state]
    while True:
        result = la_star(path, goal_state, 0, bound)
        if result == "FOUND":
            return path, bound
        if result == math.inf:
            return None
        bound = result
        if verbose:
            print(f"Increasing bound to {bound}.")

# Limited A* Search
def la_star(path: list, goal_node: str, g, bound: float):
    node = path[-1]
    f = g + puzzle.manh(node, goal_node)
    if f > bound:
        return f
    if node == goal_node:
        print(f"Found goal node {node} at depth {g} with max depth {bound}")
        return "FOUND"
    m = math.inf
    for child_node, _ in puzzle.get_neighbors(node):
        if not child_node in path:
            path.append(child_node)
            result = la_star(path, goal_node, g + 1, bound)
            if result == "FOUND":
                return "FOUND"
            if result < m:
                m = result
            path.pop()
    return m