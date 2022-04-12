from puzzle import PuzzleState
from Actions import subNodes


def depth_first_search(startState, goalState):

    global GoalNode, numberOfNodes

    numberOfNodes = 0
    boardVisited = set()
    stack = list([PuzzleState(startState, None, None, 0, 0, 0)])

    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        if node.state == goalState:
            GoalNode = node
            return stack
        #inverse the order of next paths for execution porpuses
        possiblePaths = reversed(subNodes(node))
        numberOfNodes += 1
        for path in possiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)