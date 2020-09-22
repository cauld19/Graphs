from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    
    s = Stack() ## create Stack for DFT
    s.push(starting_node) ## add starting node to stack
    levels = -1 ## set level to -1, to keep track of how many connections back the starting node is from its original node
    ancestors_obj = {} ## store key, value pair of node-level that is connected to starting node

    while s.size() > 0: ## iterate while theres something left in Stack
        levels += 1 ## add one to level with each traversal 
        current = s.pop() ## current node is the most recent on Stack
        ancestors_obj[current] = levels ## add current node to object with its level
        for i in ancestors: ## find all connected nodes to current node and push to stack
            if current == i[1]:
                s.push(i[0])
       
    ancestors_obj.pop(starting_node) ## remove starting node ancestors object
    
    if len(ancestors_obj) < 1: ## if no nodes connected
            return  -1
    else:        
        for k,v in ancestors_obj.items():
            if len(ancestors_obj) < 2: ## if only one node
                return k
            elif len(ancestors_obj) == 2: ## if two nodes return higher value / if the same return lower key
                return max(ancestors_obj, key=ancestors_obj.get)
            else:
                return max(ancestors_obj, key=ancestors_obj.get) ## return node with highest value (level)
        


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors,3)
    