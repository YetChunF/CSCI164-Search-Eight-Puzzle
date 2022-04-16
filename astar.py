import pygame
import priority
import math
import sys

SCREEN_HEIGHT = 500
SCREEN_WIDTH =  500
BOARD_PADDING = 120
BACKGROUND_COLOR = (0, 0, 0)
TILE_COLOR = (218, 182, 150)
FONT_COLOR = (67, 38, 29)
TILE_SIZE = 70
FRAME_RATE = 200

class puzzle:
    def __init__(self, initial_state: str, goal_state: str) -> None:
        self.state = [c for c in initial_state]
        self.goal = goal_state
        self.boardSize = int(math.sqrt(len(self.state)))
        self.space_pos = self.state.index("0")
    # Swaps two values in the state list
    def __swap(self, index_1: int, index_2: int) -> None:
        (self.state[index_1], self.state[index_2]) = (self.state[index_2], self.state[index_1])
    # Attempts to perform one of the following operations: U, D, L, R. Returns the new state.
    def move(self, choice: str, verbose:bool=False) -> str:
        if verbose:
            print(f"Attempted move: {choice}")
        if choice == "D" and self.space_pos + self.boardSize < len(self.state):
            self.__swap(self.space_pos, self.space_pos + self.boardSize)
            self.space_pos = self.space_pos + self.boardSize
        elif choice == "U" and self.space_pos - self.boardSize >= 0:
            self.__swap(self.space_pos, self.space_pos - self.boardSize)
            self.space_pos = self.space_pos - self.boardSize
        elif choice == "R" and self.space_pos % self.boardSize < self.boardSize - 1:
            self.__swap(self.space_pos, self.space_pos + 1)
            self.space_pos = self.space_pos + 1
        elif choice == "L" and self.space_pos % self.boardSize > 0:
            self.__swap(self.space_pos, self.space_pos - 1)
            self.space_pos = self.space_pos - 1
        else:
            if verbose:
                print(f"That's an illegal move, sir. Attempted move: {choice}")
        return self.get_state()
    # Returns current board state as a string
    def get_state(self) -> str:
        return "".join(self.state)
    # Prints ascii version of the board state to console.
    def print_ascii(self) -> None:
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(f"{self.state[j + i * self.boardSize]} ", end="")
            print()
    # Draws the board on the specified screen.
    def draw(self, screen: pygame.Surface) -> None:
        for tile_index in range(len(self.state)):
            i = int(tile_index / self.boardSize)
            j = tile_index % self.boardSize
            tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
            tile.fill(TILE_COLOR)
            pygame.draw.rect(tile, FONT_COLOR, (0, 0, TILE_SIZE, TILE_SIZE), 1)
            if self.state[tile_index] != "0":
                tile.blit(font.render(self.state[tile_index], True, FONT_COLOR), (5, 5))
            screen.blit(tile, (BOARD_PADDING + j * TILE_SIZE, BOARD_PADDING + i * TILE_SIZE))
    # Gets all neighbors for a specified state.
    @staticmethod
    def get_neighbors(state: str):
        space_pos = state.index("0")
        boardSize = int((len(state))**(1/2))
        possible_states = []
        if space_pos + boardSize < len(state):
            new_state = [c for c in state]
            (new_state[space_pos], new_state[space_pos + boardSize]) = (new_state[space_pos + boardSize], new_state[space_pos])
            possible_states.append(("".join(new_state), "D"))
        if space_pos - boardSize >= 0:
            new_state = [c for c in state]
            (new_state[space_pos], new_state[space_pos - boardSize]) = (new_state[space_pos - boardSize], new_state[space_pos])
            possible_states.append(("".join(new_state), "U"))
        if space_pos % boardSize < boardSize - 1:
            new_state = [c for c in state]
            (new_state[space_pos], new_state[space_pos + 1]) = (new_state[space_pos + 1], new_state[space_pos])
            possible_states.append(("".join(new_state), "R"))
        if space_pos % boardSize > 0:
            new_state = [c for c in state]
            (new_state[space_pos], new_state[space_pos - 1]) = (new_state[space_pos - 1], new_state[space_pos])
            possible_states.append(("".join(new_state), "L"))
        return possible_states
        # Gets all neighbors for a specified state.
    @staticmethod
    def get_prev(state: str, choice: str):
        space_pos = state.index("0")
        boardSize = int((len(state))**(1/2))
        new_state = [c for c in state]
        if (choice == "U") and (space_pos + boardSize < len(state)):
            (new_state[space_pos], new_state[space_pos + boardSize]) = (new_state[space_pos + boardSize], new_state[space_pos])
        if (choice == "D") and (space_pos - boardSize >= 0):
            (new_state[space_pos], new_state[space_pos - boardSize]) = (new_state[space_pos - boardSize], new_state[space_pos])
        if (choice == "L") and (space_pos % boardSize < boardSize - 1):
            (new_state[space_pos], new_state[space_pos + 1]) = (new_state[space_pos + 1], new_state[space_pos])
        if (choice == "R") and (space_pos % boardSize > 0):
            (new_state[space_pos], new_state[space_pos - 1]) = (new_state[space_pos - 1], new_state[space_pos])
        return "".join(new_state)
    # Calculates the out of place heuristic function.
    @staticmethod
    def ooph(state: str, goal: str) -> int:
        return sum(list(map(lambda a, b: int(a==b), state, goal)))
    @staticmethod
    def manh(state: str, goal: str) -> float:
        boardSize = int((len(state))**(1/2))
        man_dist = 0
        for tile_source in range(len(state)):
            source_i, source_j = int(tile_source / boardSize), tile_source % boardSize
            tile_dest = goal.index(state[tile_source])
            dest_i, dest_j = int(tile_dest / boardSize), tile_dest % boardSize
            man_dist += math.sqrt((source_i - dest_i)**2 + (source_j - dest_j)**2)
        return man_dist

# A* Algorithm Implementation
def a_star(puzz: puzzle):
    curr_node = puzz.get_state()
    frontier = priority.PQ()
    frontier.push(curr_node, puzzle.ooph(curr_node, puzz.goal))
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
        if curr_node == puzz.goal:
            solution = []
            _current = curr_node
            while parent_map[_current] != "":
                solution.append(parent_map[_current])
                _current = puzzle.get_prev(_current, parent_map[_current])
            solution.reverse()
            return solution, num_explored
        for child_node, op in puzzle.get_neighbors(curr_node):
            path_costs[child_node] = path_costs[curr_node] + 1
            priority_cost = path_costs[child_node] + puzzle.manh(child_node, puzz.goal)
            if (not child_node in explored) and (not frontier.is_in(child_node)):
                frontier.push(child_node, priority_cost)
                parent_map[child_node] = op
            elif (frontier.is_in(child_node)) and (frontier.get_cost(child_node) > priority_cost):
                frontier.set_cost(child_node, priority_cost)
                parent_map[child_node] = op

# Iterative Deepening Depth First Search
def iddfs(puzz: puzzle):
    depth = 1
    result = None
    while not result:
        result = ldfs(puzz.get_state(), puzz.goal, 0, depth)
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
def ida_star(puzz: puzzle):
    bound = puzzle.manh(puzz.get_state(), puzz.goal)
    path = [puzz.get_state()]
    while True:
        result = la_star(path, puzz.goal, 0, bound)
        if result == "FOUND":
            return path, bound
        if result == math.inf:
            return None
        bound = result
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

sample_p = puzzle("462301587", "012345678")
result, fbound = ida_star(sample_p)
print(result)

sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Map")
    screen.fill(BACKGROUND_COLOR)

    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 48)

    move_list = []
    puzz = puzzle("012345678", "012345678")
    pygame.display.update()

    ticks = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        current_ticks = pygame.time.get_ticks()
        if current_ticks > ticks + FRAME_RATE:
            ticks = current_ticks
            if move_list:
                m = move_list.pop(0)
                puzz.move(m)
            else:
                if small_puzzles:
                    new_start_state = small_puzzles.pop()
                    new_end_state = "".join(sorted([c for c in new_start_state]))
                    print(f"New puzzle started! Puzzle: {new_start_state} Goal: {new_end_state}")
                    puzz = puzzle(new_start_state, new_end_state)
                    puzz.draw(screen)
                    pygame.display.update()
                    move_list, num_explored = a_star(puzz)
                    print(f"Puzzle solved! Total nodes explored: {num_explored}. Solution: {''.join(move_list)}")
                else:
                    print("Finished all puzzles.")
                    sys.exit()
            puzz.draw(screen)
            pygame.display.update()
    pygame.quit()
