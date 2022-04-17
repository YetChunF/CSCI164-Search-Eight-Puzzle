from puzzle import PuzzleState
from collections import deque
from Actions import subNodes


def breath_first_search(initialState, goalState):

    global GoalNode, numberOfPaths

    boardVisited= set()
    Queue = deque([PuzzleState(initialState, None, None, 0, 0, 0)])
    numberOfPaths = 0

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == goalState:
            GoalNode = node
            return Queue
        possiblePaths = subNodes(node)
        numberOfPaths += 1
        for path in possiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)