# Yet Chun Fong 300376480 
# CSCI 164 Spring 2022 Search w/ Eight Puzzle 

import sys
import random as rd
from random import choice
import time
import itertools

class Node: 
    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action 
        self.path_cost = path_cost 
        self.depth = 0 
        if parent: 
            self.depth = parent.depth + 1

    def Expand(self,problem): 
        return[self.Child_Node(problem,action) for action in problem.action(self.state)]

    def Child_Node(self,problem,action):
        next_state = problem.Result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self): 
        return [node.action for node in self.path()[1:]] 
    
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent 
        return list(reversed(path_back)) 

#Breadth-First Search 
def BFS(set):
    global node 
    frontier = list([node]) #FIFO 
    explored = list()   #Contain explored nodes 

    while frontier: 
        node = frontier.pop(0)  #FIFO
        if node.state not in explored: 
            explored.append(node.state)
        for action in set.action(node.state):
            child = node.Child_Node(set, action)
            if(child not in explored or child not in frontier):
                return child 
            frontier.append(child)

#Depth-First Search
def DFS(set):
    global node 
    frontier = list([node]) #LIFO 
    explored = list()

    while frontier: 
        node= frontier.pop()
        if node.state not in explored: 
            explored.append(node.state)
        for action in set.action(node.state): 
            child = node.Child_Node(set, action)
            if(child not in explored or child not in frontier):
                if(set.goal_test(child.state)):
                    return child 
                frontier.append(child)

#Uniform Cost Search 
def UCS(set): 
    global node 
    frontier = list([node])
    explored = list()

    while frontier: 
        print(len(frontier))
        node = frontier.pop(frontier.index(min(frontier, 
            key = lambda path_cost : node.path_cost)))
        if(set.goal_test(node.state)):
            return node
        if node.state not in explored: 
            explored.append(node.state)
        for action in set.action(node.state):
            child = node.Child_Node(set, action)
            if(child not in explored or child not in frontier):
                frontier.append(child)
            elif(child in frontier): 
                for i in frontier: 
                    if i == child and child.path < i.path:
                        frontier[i] = child

def Depth_Limit_Search(node, problem, limit): 
    frontier = list([node]) #LIFO
    explored = list()   #Contains the explored nodes
    explored_depth = list() #Contains the depth of explored nodes 

    while frontier: 
        node = frontier.pop()
        if node.state not in explored:
            explored.append(node.state)
            explored_depth.append(node.depth)
        if problem.goal_test(node.state):
            return node 
        else:
            for child in node.Expand(problem):
                if child.depth <= limit: 
                    if child not in frontier: 
                        if child.state not in explored: 
                            if problem.goal_test(child.state):
                                return child 
                            else: frontier.append(child)
                        elif explored_depth[explored.index(child.state)] > child.depth:
                            explored_depth[explored.index(child.state)] = child.depth
                            if problem.goal_test(child.state):
                                return child 
                            else: frontier.append(child)
                else: break
        return None

def IDLS(problem, node): 
    depthlimit = 0 
    #Use itertools to run the endless loop 
    for depthlimit in itertools.count(): 
        result = Depth_Limit_Search(node, problem, limit=depthlimit)
        if result != None: 
            break 
    return result 

class EightPuzzleProblem:
    def __init__(self, initial, goal = (0,1,2,3,4,5,6,7,8)): 
        self.initial = initial 
        self.goal = goal 

    def action(self, state): 
        possible_actions = ['UP','DOWN','LEFT','RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove ('LEFT')
        if index_blank_square < 3: 
            possible_actions.remove ('UP')
        if index_blank_square % 3 == 2: 
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def path_cost(self, c, state1, action, state2):
        return c + 1 

    def goal_test(self,state): 
        return state == self.goal 

    def find_blank_square(self, state): 
        return state.index(0)

    def Result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]
        return tuple(new_state)

    def random(problem, random_level):
        x = rd.randint(20, random_level)
        node = Node(problem.goal)
        explored = set() 
        explored.add(node.state)
        while x > 0: 
            temp = choice(node.Expand(problem))
            while temp.state in explored: 
                temp = choice(node.Expand(problem))
                while temp.state in explored: 
                    temp = choice(node.Expand(problem))
                node = temp 
                explored.add(node)
                x = x - 1
        return node  
    
    def solve(initialState): 
        problem = EightPuzzleProblem(initial= None, goal = (0, 1, 2, 3 ,4 ,5 ,6 ,7 ,8))
        problem.intial = initialState 

        node = Node(problem.initial)

        start = time.time()
        result = IDLS(problem, node)

        end = time.time()

        yield result.solution()
        yield end-start

if __name__ == '__main__': 
    problem = EightPuzzleProblem(initial=(1,8,2,3,0,5,4,7,6), goal=(0, 1, 2, 3, 4, 5, 6, 7, 8))
    node = Node(problem.initial)
    result = IDLS(problem, node)
    print(result.solution())   