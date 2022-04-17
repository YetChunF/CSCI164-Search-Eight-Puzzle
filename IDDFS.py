from Puzzle import PuzzleState
from Actions import subNodes
import queue


def depth_first_search(startState, goalState, maxDepth):

    node = PuzzleState(startState, None, None, 0, 0, 0)
    # make a LIFO queue with infinite size
    frontier = queue.LifoQueue(0)
    frontier.put(node)
    numberOfNodes = 0
    # dictionary to set true to the visited node
    # false to node that haven't been visited
    visited = {}

    while not frontier.empty():
        # get the last element
        node = frontier.get()
        # convert the state to string
        currentState = ''.join(str(v) for v in node.state)

        # if the state is equal to goalState, return the results
        if node.state == goalState:
            return (node, numberOfNodes)

        # don't expand node if the depth exceed maxDepth
        elif node.depth + 1 > maxDepth:
            continue

        # put the current node into the dictionary and set it to True
        # if the state have not been visited
        elif not visited.get(currentState):
            numberOfNodes += 1
            visited[currentState] = True

            # expand the node
            for child in subNodes(node):
                frontier.put(child)

    return (0, numberOfNodes)


def iterative_deepening_depth_first_search(state, goal, depth):

    fail = "Can't find the goal within the depth"

    # Repeatedly depth-limit search till the maximum depth
    for i in range(depth):
        (node, numberofNodes) = depth_first_search(state, goal, i)
        if (isinstance(node, PuzzleState)):
            return (node, numberofNodes)
    return (fail, numberofNodes)


iterative_deepening_depth_first_search([1,2,3,4,0,6,5,7,8],"0,1,2,3,4,5,6,7,8",10)
