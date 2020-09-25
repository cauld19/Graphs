from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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

def give_opposite_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'



def solution_attempt(world, starting_location):
    
    
    stack = deque()
    stack.append(starting_location)
    previous_room = []
    
    
    
    visited = {}



    
    

    while len(visited) < 3:
        print(visited)
        print(stack)
        current = stack.pop()
        
        previous_room.append(current)
        
        directions = player.current_room.get_exits()
        random_direction = random.choice(directions)

        if current not in visited:
            visited[current] = dict.fromkeys(directions, "?")
            

        if len(directions) == 1:
       
            player.travel(random_direction) ## move to next room
            visited[current][random_direction] = player.current_room.id ## set first room
            
            opposite_direction = give_opposite_direction(random_direction) ## function to give opposite direction
            
            directions = player.current_room.get_exits() ## new directions for next room
            print(visited)
            visited[player.current_room.id] = dict.fromkeys(directions, "?") ## create new room       
            print(visited)         
            visited[player.current_room.id][opposite_direction] = current ## set current room with previous rooms direction
            print(visited)
            
            stack.append(player.current_room.id) ## add new room to stack
            traversal_path.append(random_direction) ## add path to traversal

            
            
        elif len(directions) == 2: ## if two directions to go
            
            for key, value in visited[player.current_room.id].items(): ## find room direction with ? and set direction to it
                
                if value == '?':
                    random_direction = key
                    print(random_direction, "wtf")
                    
            player.travel(random_direction) ## move to next room
            visited[current][random_direction] = player.current_room.id ## set room
            
            opposite_direction_two = give_opposite_direction(random_direction)
            
            visited[player.current_room.id] = dict.fromkeys(directions, "?")
            
            visited[player.current_room.id][opposite_direction_two] = current ## set current room with previous rooms direction
            
            stack.append(player.current_room.id) ## add new room to stack
            traversal_path.append(random_direction) ## add path to traversal
            
                

                
            # elif len(directions) >= 3: ## if greater than two directions make sure not going back where you came from
            #     print("more than three directions")
            #     if len(traversal_path) > 0 and (random_direction, traversal_path[-1]) in opposites:
            #         while (random_direction, traversal_path[-1]) in opposites:
            #             random_direction = random.choice(directions)
                        
                
                
            #     traversal_path.append(random_direction)
            #     queue.appendleft(current)
            #     player.travel(random_direction)
            #     stack.append(player.current_room.id)

                
                
        # elif current in visited:
        #     print("in visited")
            
        #     # print(current, "pre removing", directions)
             
        #     # if current in rooms_with_many_connections:
        #     #     for key, value in rooms_with_many_connections.items():
        #     #         print("key/value", key,value)
        #     #         for i in value:
        #     #             print("values in i", i, "directions:", directions) 
        #     #             if current == key:
        #     #                 if i in directions:
        #     #                     directions.remove(i)
        #     #                     print(directions)
                                
                            
        #     random_direction = random.choice(directions)
        #     player.travel(random_direction)
        #     traversal_path.append(random_direction)
        #     stack.append(player.current_room.id)
            
        #     directions = player.current_room.get_exits()
    print(traversal_path)
    print(visited)
            
                       
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
