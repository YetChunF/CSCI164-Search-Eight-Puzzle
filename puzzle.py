from lib2to3.pytree import Node
import math
from Node import node 

class puzzle():


	actionDict = {"L":"R", "R":"L", "U":"D", "D":"U"}

	def __init__(self, initial, goal):
		self.initial = initial[:]
		self.boardSize = math.sqrt(len(goal))
		self.goalState = goal[:]

	def isGoal(self, state) -> bool:
		return ''.join(state) == ''.join(self.goalState)

	def action_cost(self, state, action, newState) -> int:
		return 1

	def expandNode(self, node):
		retList = []
		for act in puzzle.actionDict.keys():
			tempList = list(node.state)
			puzzle.executeAction(tempList, act, node.zeroIndex)
			cost = node.path_cost + self.action_cost(node.state, act, tempList)
			retList.append(Node(tempList, node, act, cost, tempList.index("0")))
		return retList

	def printSolutionMetrics(node, expandedNodes, functionName, originalState):
		nodePath = puzzle.buildNodePath(node)

		print(f'{"Function Name: ":22}', functionName)
		print(f'{"Final State: ":22}', ''.join(node.state))
		print(f'{"Nodes Expanded: ":22}', expandedNodes)
		if node.state != "Failure":
			print(f'{"Action Set: ":22}', ''.join(nodePath))
			print(f'{"Path Cost: ":22}', len(nodePath))
			print(f'{"Original State: ":22}', originalState)
			finalState = list(originalState)
			puzzle.executeActionList(finalState, nodePath)
			print(f'{"Path Verification":22}', ''.join(finalState))


	def buildNodePath(node):
		nodePath = [node.action]
		tempNode = node.parent
		while tempNode != None:
			nodePath.append(tempNode.action)
			tempNode = tempNode.parent

		nodePath.reverse()
		return nodePath 


	# Used to get the reversed Move sequence from a given sequence
	def getInvertedActions(actions):
		retList = []
		for act in actions:
			retList.append(puzzle.actionDict.get(act))
		retList.reverse()
		return retList


	"""
		All functions below are for executing Move Sequences on an Entered Puzzle State
	"""
	def executeActionList(state, actions):
		for act in ''.join(actions).lower():
			puzzle.executeAction(state, act, state.index("0"))

	def executeAction(state, action, zIndex):
		boardSize = int(math.sqrt(len(state)))
		if puzzle.isValidMove(state, action, zIndex):
			if action == "U":
				puzzle.swap(zIndex, zIndex - boardSize, state)
			elif action == "D":
				puzzle.swap(zIndex, zIndex + boardSize, state)
			elif action == "L":
				puzzle.swap(zIndex, zIndex - 1, state)
			elif action == "R":
				puzzle.swap(zIndex, zIndex + 1, state)

	def isValidMove(state, action, zIndex):	
		if not puzzle.actionDict.get(action):
			return False
		boardSize = int(math.sqrt(len(state)))
		if action == "U":
			return zIndex > (boardSize - 1)
		elif action == "D":
			return (zIndex//boardSize) < (boardSize - 1)
		elif action == "L":
			return (zIndex%boardSize) > 0
		elif action == "R":
			return zIndex%boardSize < (boardSize - 1)

	def swap(zIndex, moveToIndex, state):
		temp = state[moveToIndex]
		state[moveToIndex] = state[zIndex]
		state[zIndex] = temp