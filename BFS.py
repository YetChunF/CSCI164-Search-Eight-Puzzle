from lib2to3.pytree import Node
from puzzle import puzzle
from Node import node
import queue


def breath_first_search(initial_state):
    NNode = node(initial_state.initial[:], None, "", 0, initial_state.initial.index("0"))
    frontier = queue.Queue(0)
    frontier.put(NNode)
    reached = {''.join(NNode.state): True}
    nodesExpanded = 0
    while not frontier.empty():
        NNode = frontier.get()
        nodesExpanded += 1
        for child in initial_state.expandNode(NNode):
            hState = ''.join(child.state)
            if initial_state.isGoal(child.state):
                return (child, nodesExpanded)
            if not reached.get(hState):
                reached[hState] = True
                frontier.put(child)
    return(NNode("Failure", None, None, None, None), nodesExpanded)
