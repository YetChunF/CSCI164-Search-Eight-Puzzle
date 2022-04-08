from lib2to3.pytree import Node
from puzzle import puzzle
from Node import node
import queue 

def depth_first_search(initial_state): 
    node = Node(puzzle.initial[:], None, "", 0, puzzle.initial.index("0"))
    frontier = queue.LIFO_queue(0)
    frontier.put(node)
    reached = {}
    nodesExpanded = 0
    while not frontier.empty():
        node = frontier.get()
        hState = ''.join(node.state)
        if puzzle.isGoal(node.state):
            return (node, nodesExpanded)
        elif node.path_cost + 1 > 30: 
            continue
        elif not reached.get(hState):
            nodesExpanded += 1 
            reached[hState] = True 
            for child in puzzle.expandNode(node):
                frontier.put(child)
    return(Node("Failure", None, None, None, None), nodesExpanded)
