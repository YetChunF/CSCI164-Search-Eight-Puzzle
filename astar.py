from animate import puzzle
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

class qnode:
    def __init__(self, state: float, priority: float=math.inf, p_op: str="N", p_cost: float=math.inf):
        self.state = state
        self.priority = priority
        self.parent_op = p_op
        self.path_cost = p_cost
    def __eq__(self, __o: object) -> bool:
        return self.state == __o.state

# A* Algorithm Implementation
def a_star(start_state: str, goal_state: str):
    frontier = [qnode(start_state, puzzle.manh(start_state, goal_state), "", 0)]
    explored = []
    num_explored = 0
    while frontier:
        frontier.sort(key=lambda obj: obj.priority)
        curr_node = min(frontier, key=lambda obj: obj.priority)
        frontier.remove(curr_node)
        # print(f"Node: {curr_node.state} {curr_node.priority} {curr_node.path_cost}")
        num_explored += 1
        if num_explored % 5000 == 0:
            print(f"Explored {num_explored} nodes...")
        explored.append(curr_node)
        if curr_node.state == goal_state:
            solution = []
            _current = curr_node
            while _current.parent_op != "":
                solution.append(_current.state)
                _current = explored[explored.index(qnode(puzzle.get_prev(_current.state, _current.parent_op)))]
            solution.append(_current.state)
            solution.reverse()
            return solution, num_explored
        for child_state, op in puzzle.get_neighbors(curr_node.state):
            h = puzzle.manh(child_state, goal_state)
            child_node = qnode(child_state, curr_node.path_cost + 1 + h, op, curr_node.path_cost + 1)
            if (not child_node in explored) and (not child_node in frontier):
                frontier.append(child_node)
            elif (child_node in frontier) and (frontier[frontier.index(child_node)].priority > child_node.priority):
                frontier[frontier.index(child_node)].priority = child_node.priority

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