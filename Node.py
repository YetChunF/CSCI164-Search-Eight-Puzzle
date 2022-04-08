class node:
    def __init__(self, state, parent, action, path_cost, zeroIndex):
        self.state = state 
        self.parent = parent 
        self.action = action 
        self.path_cost = path_cost 
        self.zeroIndex = zeroIndex 
    
    def __lesser__(self,other): 
        if not other or not self: 
            return False 
        else: 
            return self.path_cost < other.path_cost
    
    def __equals__(self,other):
        if not other or not self: 
            return False 
        else: 
            return self.path_cost == other.path_cost
    
    def __greater__(self, other): 
        if not other or not self: 
            return False 
        else: 
            return self.path_cost > other.path_cost