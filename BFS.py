from lib2to3.pytree import Node
from puzzle import puzzle
from Node import node
import queue 

def breath_first_search(initial_state):
    node = Node(puzzle.initial[:], None, "",0, puzzle.initial.index("0"))
    frontier = queue.Queue(0)
    frontier.put(node)
    reached = {''.join(node.state) : True}
    nodesExpanded = 0 
    while not frontier.empty(): 
        node = frontier.get()
        nodesExpanded += 1 
        for child in puzzle.expandNode(node):
            hState = ''.join(child.state)
            if puzzle.isGoal(child.state): 
                return (child, nodesExpanded)
            if not reached.get(hState):
                reached[hState] = True 
                frontier.put(child)
    return(Node("Failure", None, None, None, None), nodesExpanded)

