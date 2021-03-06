import pygame
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
    board_size = 3
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
            font = pygame.font.SysFont(None, 48)
            if self.state[tile_index] != "0":
                tile.blit(font.render(self.state[tile_index], True, FONT_COLOR), (5, 5))
            screen.blit(tile, (BOARD_PADDING + j * TILE_SIZE, BOARD_PADDING + i * TILE_SIZE))
    @staticmethod
    def set_board_size(new_size):
        puzzle.board_size = new_size
    @staticmethod
    def draw_state(state: list, screen: pygame.Surface) -> None:
        for tile_index in range(len(state)):
            i = int(tile_index / puzzle.board_size)
            j = tile_index % puzzle.board_size
            tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
            tile.fill(TILE_COLOR)
            pygame.draw.rect(tile, FONT_COLOR, (0, 0, TILE_SIZE, TILE_SIZE), 1)
            font = pygame.font.SysFont(None, 48)
            if state[tile_index] != "0":
                tile.blit(font.render(state[tile_index], True, FONT_COLOR), (5, 5))
            screen.blit(tile, (BOARD_PADDING + j * TILE_SIZE, BOARD_PADDING + i * TILE_SIZE))
    # Gets all neighbors for a specified state.
    @staticmethod
    def get_neighbors(state: list) -> list:
        space_pos = state.index("0")
        possible_states = []
        if space_pos + puzzle.board_size < len(state):
            new_state = state[:]
            (new_state[space_pos], new_state[space_pos + puzzle.board_size]) = (new_state[space_pos + puzzle.board_size], new_state[space_pos])
            possible_states.append((new_state, "D"))
        if space_pos - puzzle.board_size >= 0:
            new_state = state[:]
            (new_state[space_pos], new_state[space_pos - puzzle.board_size]) = (new_state[space_pos - puzzle.board_size], new_state[space_pos])
            possible_states.append((new_state, "U"))
        if space_pos % puzzle.board_size < puzzle.board_size - 1:
            new_state = state[:]
            (new_state[space_pos], new_state[space_pos + 1]) = (new_state[space_pos + 1], new_state[space_pos])
            possible_states.append((new_state, "R"))
        if space_pos % puzzle.board_size > 0:
            new_state = state[:]
            (new_state[space_pos], new_state[space_pos - 1]) = (new_state[space_pos - 1], new_state[space_pos])
            possible_states.append((new_state, "L"))
        return possible_states
        # Gets all neighbors for a specified state.
    @staticmethod
    def get_prev(state: list, choice: str):
        space_pos = state.index("0")
        new_state = state[:]
        if (choice == "U") and (space_pos + puzzle.board_size < len(state)):
            (new_state[space_pos], new_state[space_pos + puzzle.board_size]) = (new_state[space_pos + puzzle.board_size], new_state[space_pos])
        if (choice == "D") and (space_pos - puzzle.board_size >= 0):
            (new_state[space_pos], new_state[space_pos - puzzle.board_size]) = (new_state[space_pos - puzzle.board_size], new_state[space_pos])
        if (choice == "L") and (space_pos % puzzle.board_size < puzzle.board_size - 1):
            (new_state[space_pos], new_state[space_pos + 1]) = (new_state[space_pos + 1], new_state[space_pos])
        if (choice == "R") and (space_pos % puzzle.board_size > 0):
            (new_state[space_pos], new_state[space_pos - 1]) = (new_state[space_pos - 1], new_state[space_pos])
        return new_state
    # Calculates the out of place heuristic function.
    @staticmethod
    def ooph(state: list, goal: str) -> int:
        return sum(list(map(lambda a, b: int(a==b), state, goal)))
    @staticmethod
    def manh(state: list, goal: str) -> float:
        man_dist = 0
        for tile_source in range(len(state)):
            source_i, source_j = int(tile_source / puzzle.board_size), tile_source % puzzle.board_size
            tile_dest = goal.index(state[tile_source])
            dest_i, dest_j = int(tile_dest / puzzle.board_size), tile_dest % puzzle.board_size
            man_dist += math.sqrt((source_i - dest_i)**2 + (source_j - dest_j)**2)
        return man_dist

# Animation function. Simply provide a list containing lists of states.
def run_animations(solutions: list):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Map")
    screen.fill(BACKGROUND_COLOR)

    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 30)
    
    states = []
    ticks = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        current_ticks = pygame.time.get_ticks()
        if current_ticks > ticks + FRAME_RATE:
            ticks = current_ticks
            if states:
                puzzle.draw_state(states.pop(0), screen)
            else:
                if solutions:
                    states = solutions.pop(0)
                    pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, BOARD_PADDING))
                    screen.blit(font.render(f"Solving puzzle: {states[0]}", True, (255, 255, 255)), (5, 5))
                else:
                    running = False
            pygame.display.update()
    pygame.quit()

def run_anim_moves(initial_state: str, move_list: list):
    goal_state = "".join(sorted([c for c in initial_state]))
    p = puzzle(initial_state, goal_state)
    s = [p.get_state()]
    for move in move_list:
        p.move(move)
        s.append(p.get_state())
    run_animations([s])