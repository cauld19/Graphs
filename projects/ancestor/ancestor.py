from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    
    s = Stack()
    s.push(starting_node)
    levels = -1
    ancestors_obj = {}

    while s.size() > 0:
        levels += 1
        current = s.pop()
        ancestors_obj[current] = levels
        for i in ancestors[:]:
            if current == i[1]:
                s.push(i[0])
       
    ancestors_obj.pop(starting_node)

    if len(ancestors_obj) < 1:
            return  -1
    else:        
        for k,v in ancestors_obj.items():
            if len(ancestors_obj) < 2:
                return k
            elif len(ancestors_obj) == 2:
                return max(ancestors_obj, key=ancestors_obj.get)
            else:
                return max(ancestors_obj, key=ancestors_obj.get)
        


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,3))
    