from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

current_location = None

def give_opposite_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'
    
    """
    if has 1 direciton go that way
    if has two directions go opposite from lat went direction
    if has three ways:
        check if one of the wways is '?' and go there
        if no way are '?'
            add the two direcitons that are not the previously went direction
    if has four ways:
        repeat the same for three ways but with an ectra direction
    
    
    
    """
    
def bfs(word, visited_rooms, starting_location, stack):
    queue = deque()
    stack = stack

    if len(stack) > 0:
        stack.pop() ## remove any room left in stack before running bfs
        
    visited = visited_rooms
    queue.appendleft(starting_location)
    
    
    
    # print("--------------------in bfs---------------------------")

    searching_unexplored_direction = True
    
    while searching_unexplored_direction is True:
        print(len(traversal_path)) 
        print("queue in bfs:", queue)
        current = queue.popleft()
        # print("visited in bfs", visited)
        # print(current)
        current_room = visited[current]
        # print("current room", current_room)
        
        ## one direction option availabel
            
        if len(current_room) == 1:
            for key, value in current_room.items():
                # print("one room bfs")
                traversal_path.append(key)
                player.travel(key)
                queue.appendleft(player.current_room.id)
                searching_unexplored_direction = True
                
        ## two direction options available
                
        elif len(current_room) == 2:
            # print(player.current_room.id)
            # print("here")
            new_directions_to_go = []
            opposite_direction = give_opposite_direction(traversal_path[-1])
            # print(current_room)
            for key, value in current_room.items():
                # print(key)
            
                if key == opposite_direction:
                    continue
                else:
                    new_directions_to_go.append(key)
                    for new_direction in new_directions_to_go:
                        # print(new_direction)
                        traversal_path.append(new_direction)
                        player.travel(new_direction)
                        queue.appendleft(player.current_room.id)
                new_directions_to_go.clear()
                searching_unexplored_direction = True
            
        ## three or four direction options available
            
        elif len(current_room) > 2:
            # print("len(directions) > 2")
            # print("player current room", player.current_room.id)
            # print("length of queue", len(queue))
            
            sort_orders = sorted(current_room.items(), key=lambda x: x[1])
            
            
            for key, value in sort_orders:
                # print(key,value)
                if value == -1: ## if it finds a -1 (unexplored value) then push to stack and break
                    # print("if value is not known", key)
                    stack.append(player.current_room.id)
                    searching_unexplored_direction = False
                    break
                else: ## add all of its immediate neighbors to the queue
                    if len(visited[value]) > 3:
                        queue.appendleft(value)
                  
            
            if len(queue) > 0:
                for k,v in sort_orders:
                    if queue[0] == v:
                        traversal_path.append(k)
                        player.travel(k)
                        searching_unexplored_direction = True
                            
            
                    

                
            
            
                    
                    
            

    



def solution_attempt(world, starting_location):
    
    queue = deque()
    stack = deque()
    stack.append(starting_location)
    
    
    visited = {}
    coming_from_bfs = False

    while len(visited) < 18:
        # print("------------------------in dft--------------------------")
        # print(stack)
        coming_from_bfs = False
        current = stack.pop()
        
        directions = player.current_room.get_exits()
        random_direction = random.choice(directions)
        opposite_direction = give_opposite_direction(random_direction)  
        
        if len(directions) == 1 and len(visited) > 0:
            coming_from_bfs = True
            bfs(world, visited, current, stack)
            

        if len(directions) == 1:
            # print("------------------------in dft one direction--------------------------")
            
            if coming_from_bfs is True:
                continue
           
            current = player.current_room.id
            if current not in visited:
                visited[current] = dict.fromkeys(directions, -1)
            
            player.travel(random_direction) ## move to next room
            visited[current][random_direction] = player.current_room.id ## set first room
            
            
            opposite_direction = give_opposite_direction(random_direction) ## function to give opposite direction
            
            directions = player.current_room.get_exits() ## new directions for next room
            
            if player.current_room.id not in visited:
                visited[player.current_room.id] = dict.fromkeys(directions, -1)
                  
            visited[player.current_room.id][opposite_direction] = current ## set current room with previous rooms direction
                       
            stack.append(player.current_room.id) ## add new room to stack
            traversal_path.append(random_direction) ## add path to traversal
            
            
            

            
            
        elif len(directions) == 2: ## if two directions to go
            # print("------------------------in dft 2 direction--------------------------")
            if coming_from_bfs is True:
                continue
            
            if current not in visited:
                # print(directions)
                visited[current] = dict.fromkeys(directions, -1)
                
            
            
            for key, value in visited[player.current_room.id].items(): ## find room direction with ? and set direction to it
                
                if value == -1:
                    random_direction = key
                    
            player.travel(random_direction) ## move to next room
            visited[current][random_direction] = player.current_room.id ## set room
            
            opposite_direction_two = give_opposite_direction(random_direction)
            
            directions = player.current_room.get_exits() ## new directions for next room
            
            if player.current_room.id not in visited:
                visited[player.current_room.id] = dict.fromkeys(directions, -1) ## create new room
                
             
            
            visited[player.current_room.id][opposite_direction_two] = current ## set current room with previous rooms direction
            # print(visited[player.current_room.id])
            stack.append(player.current_room.id) ## add new room to stack
            traversal_path.append(random_direction) ## add path to traversal
            
                

        elif len(directions) > 2: ## if possible directions is greater than two
            # print("------------------------in dft 3 or 4 direction--------------------------")
            if coming_from_bfs is True:
                continue

            if current not in visited:
                visited[current] = dict.fromkeys(directions, -1)
                
            for key, value in visited[player.current_room.id].items(): ## find room direction with ? and set direction to it
                
                if value == -1:
                    random_direction = key
                    
                    break
                
            player.travel(random_direction) ## move to next room
            visited[current][random_direction] = player.current_room.id ## set first room
            
            opposite_direction = give_opposite_direction(random_direction) ## function to give opposite direction
            
            directions = player.current_room.get_exits() ## new directions for next room
            
            visited[player.current_room.id] = dict.fromkeys(directions, -1) ## create new room       
                    
            visited[player.current_room.id][opposite_direction] = current ## set current room with previous rooms direction
            
            
            stack.append(player.current_room.id) ## add new room to stack
            traversal_path.append(random_direction) ## add path to traversal
            
    print(len(traversal_path))       
    # print(traversal_path)
    # print("bottom of solution function", visited)
            
                       
solution_attempt(world, player.current_room.id)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
