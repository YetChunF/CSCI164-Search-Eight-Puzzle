import argparse
import string

from pygame import init
import BFS
import DFS
import IDDFS
import astar
from Puzzle import PuzzleState
import animate


def main():
     
    GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #---------- 15 Puzzles ----------#
    # GoalStateLong = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
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

    #---------- 15 Puzzles ----------#
    # InitialStateLong = [] #Take in 8 data 
    # InitialStateLong.append(str(data[0]))
    # InitialStateLong.append(str(data[1]))
    # InitialStateLong.append(str(data[2]))
    # InitialStateLong.append(str(data[3]))
    # InitialStateLong.append(str(data[4]))
    # InitialStateLong.append(str(data[5]))
    # InitialStateLong.append(str(data[6]))
    # InitialStateLong.append(str(data[7]))
    # InitialStateLong.append(str(data[8]))
    # InitialStateLong.append(str(data[9]))
    # InitialStateLong.append(str(data[10]))
    # InitialStateLong.append(str(data[11]))
    # InitialStateLong.append(str(data[12]))
    # InitialStateLong.append(str(data[13]))
    # InitialStateLong.append(str(data[14]))
    # InitialStateLong.append(str(data[15]))

    function = args.method

    if(function == "bfs"):
        BFS.breath_first_search(InitialState, GoalState)
        #---------- 15 Puzzles ----------#
        # BFS.breath_first_search(InitialStateLong, GoalStateLong)

        bfsNode = BFS.GoalNode
        bfsMoves = []

        # while InitialStateLong != node.state:   # 15 Puzzles
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

        # Puzzle Animation
        init_state = "".join([str(c) for c in InitialState])
        animate.run_anim_moves(init_state, bfsMoves)

    elif(function == "dfs"):
        (node, nNode) = DFS.depth_first_search(InitialState, GoalState)
        #---------- 15 Puzzles ----------#
        # (node, nNode) = DFS.depth_first_search(InitialStateLong, GoalStateLong)

        # dfsNode = DFS.GoalNode
        dfsMoves = []

        # while InitialStateLong != node.state:   # 15 Puzzles
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

        # Puzzle Animation
        init_state = "".join([str(c) for c in InitialState])
        animate.run_anim_moves(init_state, dfsMoves)

    elif(function == "iddfs"):
        maxDepth = 100
        (node, nNode) = IDDFS.iterative_deepening_depth_first_search(InitialState, GoalState, maxDepth)
        #---------- 15 Puzzles ----------#
        # (node, nNode) = IDDFS.iterative_deepening_depth_first_search(InitialStateLong, GoalStateLong, maxDepth)

        iddfsMoves = []

        if isinstance(node, PuzzleState):
            # while InitialStateLong != node.state:   # 15 Puzzles
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

            # Puzzle Animation
            init_state = "".join([str(c) for c in InitialState])
            animate.run_anim_moves(init_state, iddfsMoves)
    
    elif(function == "astar"):
        init_state = "".join([str(c) for c in InitialState])
        goal_state = "".join([str(c) for c in GoalState])
        s, num_explored = astar.a_star(init_state, goal_state)
        print (s)
        # Puzzle Animation
        animate.run_anim_moves(init_state, s)
    
    elif(function == "idastar"):
        init_state = "".join([str(c) for c in InitialState])
        goal_state = "".join([str(c) for c in GoalState])
        s, fbound = astar.ida_star(init_state, goal_state)
        print (s)
        #animate.run_animations([s])
        

    
    else:
        print(node)

if __name__ == '__main__':
    main()

