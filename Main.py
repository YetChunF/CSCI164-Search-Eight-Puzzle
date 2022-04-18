import argparse
import string
import BFS
import DFS
import IDDFS
from Puzzle import PuzzleState


def main():
     
    GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    GoalState15 = ["1234567890ABCDEF"]
    
    #Obtain information from calling parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('method')
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")

    #Build initial board state
    InitialState = [] #Take in 8 data 
    InitialState.append(int(data[0]))
    InitialState.append(int(data[1]))
    InitialState.append(int(data[2]))
    InitialState.append(int(data[3]))
    InitialState.append(int(data[4]))
    InitialState.append(int(data[5]))
    InitialState.append(int(data[6]))
    InitialState.append(int(data[7]))
    InitialState.append(int(data[8]))

    function = args.method

    if(function == "bfs"):
        BFS.breath_first_search(InitialState, GoalState)

        bfsNode = BFS.GoalNode
        bfsMoves = []

        while InitialState != bfsNode.state:
            if bfsNode.move == 1:
                path = 'U'
            if bfsNode.move == 2:
                path = 'D'
            if bfsNode.move == 3:
                path = 'L'
            if bfsNode.move == 4:
                path = 'R'
            bfsMoves.insert(0, path)
            bfsNode = bfsNode.parent

        #Print results
        print("Path: ", bfsMoves)
        print("Number of Moves: ", len(bfsMoves))
        print("Nodes expanded: ", BFS.numberOfPaths)

    elif(function == "dfs"):
        (node, nNode) = DFS.depth_first_search(InitialState, GoalState)

        # dfsNode = DFS.GoalNode
        dfsMoves = []

        while InitialState != node.state:
            if node.move == 1:
                path = 'U'
            if node.move == 2:
                path = 'D'
            if node.move == 3:
                path = 'L'
            if node.move == 4:
                path = 'R'
            dfsMoves.insert(0, path)
            node = node.parent

        #Print results.
        print("Path: ", dfsMoves)
        print("Number of moves: ", len(dfsMoves))
        print("Nodes expanded: ", nNode)

    elif(function == "iddfs"):
        maxDepth = 100
        (node, nNode) = IDDFS.iterative_deepening_depth_first_search(InitialState, GoalState, maxDepth)

        iddfsMoves = []

        if isinstance(node, PuzzleState):
            while InitialState != node.state:
                if node.move == 1:
                    path = 'U'
                if node.move == 2:
                    path = 'D'
                if node.move == 3:
                    path = 'L'
                if node.move == 4:
                    path = 'R'
                iddfsMoves.insert(0, path)
                node = node.parent

            #Print results.
            print("Path: ", iddfsMoves)
            print("Number of moves: ", len(iddfsMoves))
            print("Nodes expanded: ", nNode)

        else:
            print(node)

if __name__ == '__main__':
    main()

