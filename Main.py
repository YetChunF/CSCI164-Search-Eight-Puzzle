import argparse
import BFS
import DFS
import IDDFS


def main():
     
    GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
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
        print("Cost: ", len(bfsMoves))
        print("Nodes expanded: ", BFS.numberOfPaths)

    elif(function == "dfs"):
        DFS.depth_first_search(InitialState, GoalState)

        dfsNode = DFS.GoalNode
        dfsMoves = []

        while InitialState != dfsNode.state:
            if dfsNode.move == 1:
                path = 'U'
            if dfsNode.move == 2:
                path = 'D'
            if dfsNode.move == 3:
                path = 'L'
            if dfsNode.move == 4:
                path = 'R'
            dfsMoves.insert(0, path)
            dfsNode = dfsNode.parent

        #Print results.
        print("Path: ", dfsMoves)
        print("Cost: ", len(dfsMoves))
        print("Nodes Expanded: ", DFS.numberOfNodes)

    elif(function == "iddfs"):
        maxDepth = 100
        result = IDDFS.iterative_deepening_depth_first_search(InitialState, GoalState, maxDepth)

        IDDFS.iterative_deepening_depth_first_search(InitialState, GoalState, 100)
        iddfsNode = IDDFS.GoalNode
        iddfsMoves = []

        if result:
            while InitialState != iddfsNode.state:
                if iddfsNode.move == 1:
                    path = 'U'
                if iddfsNode.move == 2:
                    path = 'D'
                if iddfsNode.move == 3:
                    path = 'L'
                if iddfsNode.move == 4:
                    path = 'R'
                iddfsMoves.insert(0, path)
                iddfsNode = iddfsNode.parent
        else:
            print("Can't find the goal state within the height of 100")

        #Print results.
        print("path: ", iddfsMoves)
        print("cost: ", len(iddfsMoves))
        print("nodes expanded: ", IDDFS.numberOfNodes)

    # if(function=="ast"):
    #     ast(InitialState) 

if __name__ == '__main__':
    main()
