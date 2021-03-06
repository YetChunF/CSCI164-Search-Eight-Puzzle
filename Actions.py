from puzzle import PuzzleState


def subNodes(node):

    global NodesExpanded
    NodesExpanded = 0
    NodesExpanded = NodesExpanded+1

    nextPaths = []
    nextPaths.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for procPaths in nextPaths:
        if(procPaths.state!=None):
            nodes.append(procPaths)
    return nodes


def move(state, direction):
    #generate a copy
    newState = state[:]
    
    #obtain poss of 0
    index = newState.index(0)

    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[0]
            newState[0]=newState[3]
            newState[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[0]
            newState[0]=newState[1]
            newState[1]=temp
        return newState      
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[1]
            newState[1]=newState[4]
            newState[4]=temp
        if(direction==3):
            temp=newState[1]
            newState[1]=newState[0]
            newState[0]=temp
        if(direction==4):
            temp=newState[1]
            newState[1]=newState[2]
            newState[2]=temp
        return newState    
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[2]
            newState[2]=newState[5]
            newState[5]=temp
        if(direction==3):
            temp=newState[2]
            newState[2]=newState[1]
            newState[1]=temp
        if(direction==4):
            return None
        return newState
    if(index==3):
        if(direction==1):
            temp=newState[3]
            newState[3]=newState[0]
            newState[0]=temp
        if(direction==2):
            temp=newState[3]
            newState[3]=newState[6]
            newState[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[3]
            newState[3]=newState[4]
            newState[4]=temp
        return newState
    if(index==4):
        if(direction==1):
            temp=newState[4]
            newState[4]=newState[1]
            newState[1]=temp
        if(direction==2):
            temp=newState[4]
            newState[4]=newState[7]
            newState[7]=temp
        if(direction==3):
            temp=newState[4]
            newState[4]=newState[3]
            newState[3]=temp
        if(direction==4):
            temp=newState[4]
            newState[4]=newState[5]
            newState[5]=temp
        return newState
    if(index==5):
        if(direction==1):
            temp=newState[5]
            newState[5]=newState[2]
            newState[2]=temp
        if(direction==2):
            temp=newState[5]
            newState[5]=newState[8]
            newState[8]=temp
        if(direction==3):
            temp=newState[5]
            newState[5]=newState[4]
            newState[4]=temp
        if(direction==4):
            return None
        return newState
    if(index==6):
        if(direction==1):
            temp=newState[6]
            newState[6]=newState[3]
            newState[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[6]
            newState[6]=newState[7]
            newState[7]=temp
        return newState
    if(index==7):
        if(direction==1):
            temp=newState[7]
            newState[7]=newState[4]
            newState[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[7]
            newState[7]=newState[6]
            newState[6]=temp
        if(direction==4):
            temp=newState[7]
            newState[7]=newState[8]
            newState[8]=temp
        return newState
    if(index==8):
        if(direction==1):
            temp=newState[8]
            newState[8]=newState[5]
            newState[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[8]
            newState[8]=newState[7]
            newState[7]=temp
        if(direction==4):
            return None
        return newState


#---------- 15 Puzzles ----------#
# def move(state, direction):
#     #generate a copy
#     newState = state[:]
    
#     #obtain poss of 0
#     index = newState.index("0")

#     if(index==0):
#         if(direction==1):
#             return None
#         if(direction==2):
#             temp=newState[0]
#             newState[0]=newState[4]
#             newState[4]=temp
#         if(direction==3):
#             return None
#         if(direction==4):
#             temp=newState[0]
#             newState[0]=newState[1]
#             newState[1]=temp
#         return newState      
#     if(index==1):
#         if(direction==1):
#             return None
#         if(direction==2):
#             temp=newState[1]
#             newState[1]=newState[5]
#             newState[5]=temp
#         if(direction==3):
#             temp=newState[1]
#             newState[1]=newState[0]
#             newState[0]=temp
#         if(direction==4):
#             temp=newState[1]
#             newState[1]=newState[2]
#             newState[2]=temp
#         return newState    
#     if(index==2):
#         if(direction==1):
#             return None
#         if(direction==2):
#             temp=newState[2]
#             newState[2]=newState[6]
#             newState[6]=temp
#         if(direction==3):
#             temp=newState[2]
#             newState[2]=newState[1]
#             newState[1]=temp
#         if(direction==4):
#             temp=newState[2]
#             newState[2]=newState[3]
#             newState[3]=temp
#         return newState
#     if(index==3):
#         if(direction==1):
#             return None
#         if(direction==2):
#             temp=newState[3]
#             newState[3]=newState[7]
#             newState[7]=temp
#         if(direction==3):
#             temp=newState[3]
#             newState[3]=newState[2]
#             newState[2]=temp
#         if(direction==4):
#             return None
#         return newState
#     if(index==4):
#         if(direction==1):
#             temp=newState[4]
#             newState[4]=newState[0]
#             newState[0]=temp
#         if(direction==2):
#             temp=newState[4]
#             newState[4]=newState[8]
#             newState[8]=temp
#         if(direction==3):
#             return None
#         if(direction==4):
#             temp=newState[4]
#             newState[4]=newState[5]
#             newState[5]=temp
#         return newState
#     if(index==5):
#         if(direction==1):
#             temp=newState[5]
#             newState[5]=newState[1]
#             newState[1]=temp
#         if(direction==2):
#             temp=newState[5]
#             newState[5]=newState[9]
#             newState[9]=temp
#         if(direction==3):
#             temp=newState[5]
#             newState[5]=newState[4]
#             newState[4]=temp
#         if(direction==4):
#             temp=newState[5]
#             newState[5]=newState[6]
#             newState[6]=temp
#         return newState
#     if(index==6):
#         if(direction==1):
#             temp=newState[6]
#             newState[6]=newState[2]
#             newState[2]=temp
#         if(direction==2):
#             temp=newState[6]
#             newState[6]=newState[10]
#             newState[10]=temp
#         if(direction==3):
#             temp=newState[6]
#             newState[6]=newState[5]
#             newState[5]=temp
#         if(direction==4):
#             temp=newState[6]
#             newState[6]=newState[7]
#             newState[7]=temp
#         return newState
#     if(index==7):
#         if(direction==1):
#             temp=newState[7]
#             newState[7]=newState[3]
#             newState[3]=temp
#         if(direction==2):
#             temp=newState[7]
#             newState[7]=newState[11]
#             newState[11]=temp
#         if(direction==3):
#             temp=newState[7]
#             newState[7]=newState[6]
#             newState[6]=temp
#         if(direction==4):
#             return None
#         return newState
#     if(index==8):
#         if(direction==1):
#             temp=newState[8]
#             newState[8]=newState[4]
#             newState[4]=temp
#         if(direction==2):
#             temp=newState[8]
#             newState[8]=newState[12]
#             newState[12]=temp
#         if(direction==3):
#             return None
#         if(direction==4):
#             temp=newState[8]
#             newState[8]=newState[9]
#             newState[9]=temp
#         return newState
#     if(index==9):
#         if(direction==1):
#             temp=newState[9]
#             newState[9]=newState[5]
#             newState[5]=temp
#         if(direction==2):
#             temp=newState[9]
#             newState[9]=newState[13]
#             newState[13]=temp
#         if(direction==3):
#             temp=newState[9]
#             newState[9]=newState[8]
#             newState[8]=temp
#         if(direction==4):
#             temp=newState[9]
#             newState[9]=newState[10]
#             newState[10]=temp
#         return newState
#     if(index==10):
#         if(direction==1):
#             temp=newState[10]
#             newState[10]=newState[6]
#             newState[6]=temp
#         if(direction==2):
#             temp=newState[10]
#             newState[10]=newState[14]
#             newState[14]=temp
#         if(direction==3):
#             temp=newState[10]
#             newState[10]=newState[9]
#             newState[9]=temp
#         if(direction==4):
#             temp=newState[10]
#             newState[10]=newState[11]
#             newState[11]=temp
#         return newState
#     if(index==11):
#         if(direction==1):
#             temp=newState[11]
#             newState[11]=newState[7]
#             newState[7]=temp
#         if(direction==2):
#             temp=newState[11]
#             newState[11]=newState[15]
#             newState[15]=temp
#         if(direction==3):
#             temp=newState[11]
#             newState[11]=newState[10]
#             newState[10]=temp
#         if(direction==4):
#             return None
#         return newState
#     if(index==12):
#         if(direction==1):
#             temp=newState[12]
#             newState[12]=newState[8]
#             newState[8]=temp
#         if(direction==2):
#             return None
#         if(direction==3):
#             return None
#         if(direction==4):
#             temp=newState[12]
#             newState[12]=newState[13]
#             newState[13]=temp
#         return newState
#     if(index==13):
#         if(direction==1):
#             temp=newState[13]
#             newState[13]=newState[9]
#             newState[9]=temp
#         if(direction==2):
#             return None
#         if(direction==3):
#             temp=newState[13]
#             newState[13]=newState[12]
#             newState[12]=temp
#         if(direction==4):
#             temp=newState[13]
#             newState[13]=newState[14]
#             newState[14]=temp
#         return newState
#     if(index==14):
#         if(direction==1):
#             temp=newState[14]
#             newState[14]=newState[10]
#             newState[10]=temp
#         if(direction==2):
#             return None
#         if(direction==3):
#             temp=newState[14]
#             newState[14]=newState[13]
#             newState[13]=temp
#         if(direction==4):
#             temp=newState[14]
#             newState[14]=newState[15]
#             newState[15]=temp
#         return newState
#     if(index==15):
#         if(direction==1):
#             temp=newState[15]
#             newState[14]=newState[11]
#             newState[11]=temp
#         if(direction==2):
#             return None
#         if(direction==3):
#             temp=newState[15]
#             newState[15]=newState[14]
#             newState[14]=temp
#         if(direction==4):
#             return None
#         return newState