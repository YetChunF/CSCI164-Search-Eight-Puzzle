# #Iterative Deepening Depth First Search 

# from DFS import depth_first_search
# from puzzle import puzzle
# from Node import node 
# import queue

# def dfs(initial_state, limit):
#     NNode = node(initial_state.initial[:], None, "", 0, initial_state.initial.index("0"))
#     frontier = queue.LifoQueue(0)
#     frontier.put(NNode)
#     reached = {}
#     nodesExpanded = 0 
#     while not frontier.empty():
#         NNode = frontier.get()
#         hState = ''.join(NNode.state)
#         if initial_state.isGoal(NNode.state):
#             return(NNode, nodesExpanded)
#         elif NNode.path_cost + 1 > limit:
#             continue
#         elif not reached.get(hState):
#             nodesExpanded += 1
#             reached[hState] = True 
#             for child in initial_state.expandNode(NNode):
#                 frontier.put(child)
#     return(limit, nodesExpanded)

# def iterative_deepening_dfs(initial_state, max_depth):
#     for i in range(1, max_depth):
#         (NNode, nodesExpanded) = depth_first_search(initial_state, i)
#         if (isinstance(NNode, node)) or not NNode == i:
#             return (NNode, nodesExpanded)
#     return(node("Failure", None, None, None, None), nodesExpanded)
     


