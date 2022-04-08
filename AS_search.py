from puzzle import puzzle
from Node import node
from queue import PriorityQueue 
import heuristics

def a_star_search(initial_state, heuristic):
    node = node(initial_state.initial[:], None,"",0,initial_state.initial.index("0"))
    frontier = PriorityQueue(0)
    frontier.put((node.path_cost + heuristic(node.state, initial_state.goalState), node.path_cost, node))
    reached = {''.join(node.state): 0}
    nodesExpanded = 0

    while not frontier.empty(): 
        (val, val2, node) = frontier.get()
        if initial_state.isGoal(node.state):
            return(node, nodesExpanded)
        nodesExpanded += 1 
        for child in initial_state.expandNode(node):
            hState = ''.join(child.state)
            if not reached.get(hState) or child.path_cost < reached.get(hState):
                reached[hState] = child.path_cost
                frontier.put((child.path_cost + heuristic(child.state, puzzle.goalState), child.path_cost, child))
    return(Node("Failure", None, None, None, None), nodesExpanded)