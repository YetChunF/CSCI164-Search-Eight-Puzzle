import pygame
import priority

SCREEN_HEIGHT = 400
SCREEN_WIDTH =  400
BOARD_PADDING = 120
BACKGROUND_COLOR = (0, 0, 0)
TILE_COLOR = (218, 182, 150)
FONT_COLOR = (67, 38, 29)
TILE_SIZE = 50
FRAME_RATE = 200

class puzzle:
    def __init__(self, initial_state: str, goal_state: str) -> None:
        self.state = [c for c in initial_state]
        self.goal = goal_state
        self.boardSize = int((len(self.state))**(1/2))
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
            i = int(tile_index / 3)
            j = tile_index % 3
            tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
            tile.fill(TILE_COLOR)
            pygame.draw.rect(tile, FONT_COLOR, (0, 0, TILE_SIZE, TILE_SIZE), 1)
            if self.state[tile_index] != "0":
                tile.blit(font.render(self.state[tile_index], True, FONT_COLOR), (5, 5))
            screen.blit(tile, (BOARD_PADDING + j * TILE_SIZE, BOARD_PADDING + i * TILE_SIZE))
    # Gets all neighbors for a specified state.
    @staticmethod
    def get_neighbors(state: str) -> list[str]:
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
    def get_prev(state: str, choice: str) -> list[str]:
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
        return sum(list(map(lambda a, b: (1 if a == b else 0), state, goal)))

# A* with Out-Of-Place heuristic
def astar_oop(puzz: puzzle) -> list[str]:
    curr_node = puzz.get_state()
    frontier = priority.PQ()
    frontier.push(curr_node, puzzle.ooph(curr_node, puzz.goal))
    parent_map = {curr_node: ""}
    path_costs = {curr_node: 0}
    explored = set()
    num_explored = 0
    while not frontier.is_mt():
        curr_node, curr_cost = frontier.pop()
        num_explored += 1
        print(curr_node, curr_cost)
        explored.add(curr_node)
        if curr_node == puzz.goal:
            return parent_map, num_explored
        for child_node, op in puzzle.get_neighbors(curr_node):
            path_costs[child_node] = path_costs[curr_node] + 1
            priority_cost = path_costs[child_node] + puzzle.ooph(child_node, puzz.goal)
            if (not child_node in explored) and (not frontier.is_in(child_node)):
                frontier.push(child_node, priority_cost)
                parent_map[child_node] = op
            elif (frontier.is_in(child_node)) and (frontier.get_cost(child_node) > priority_cost):
                frontier.set_cost(child_node, priority_cost)
                parent_map[child_node] = op

# A* with Manhattan Distance heuristic
def astar_man_dist(puzz: puzzle):
    pass

puzz = puzzle("160273485", "012345678")
pmap, num_explored = astar_oop(puzz)
print(f"Nodes explored: {num_explored}")
move_list = []
curr = "012345678"
while pmap[curr] != "":
    move_list.append(pmap[curr])
    curr = puzzle.get_prev(curr, pmap[curr])
move_list.reverse()
print(move_list)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Map")
    screen.fill(BACKGROUND_COLOR)

    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 48)

    puzz.draw(screen)

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
            print(f"ticks: {ticks}")
            if move_list:
                m = move_list.pop(0)
                puzz.move(m)
            puzz.draw(screen)
            pygame.display.update()
    pygame.quit()
