from Puzzle import PuzzleState
from Actions import subNodes


def depth_first_search_utils(state, goalState, depth):

    global GoalNode, numberOfNodes

    numberOfNodes = 0
    visited = set()
    stack = list([PuzzleState(state, None, None, 0, 0, 0)])

    while stack:
        node = stack.pop()
        visited.add(node.map)
        if node.state == goalState:
            GoalNode = node
            return stack
        elif depth < 0:
            continue
        else:
            #inverse the order of next paths for execution porpuses
            possiblePaths = reversed(subNodes(node))
            numberOfNodes += 1
            for path in possiblePaths:
                if path.map not in visited:
                    stack.append(path)
                    visited.add(path.map)
        depth -= 1


def iterative_deepening_depth_first_search(state, goal, depth):

    global GoalNode, numberOfNodes, node

    # Repeatedly depth-limit search till the maximum depth
    for i in range(depth):
        result = depth_first_search_utils(state, goal, i)
        if result:
            return (result, GoalNode)
    return []
