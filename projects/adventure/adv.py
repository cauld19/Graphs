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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

def solution_attempt_recursive(unexplored_room, visited = None):
    
    if visited is None:
        visited = set()
    
    visited.add(unexplored_room.id) ## add current room to visited
    
    route = []
        
        
        
    
    
    for way in unexplored_room.get_exits(): ## get each direction possible from current room
        print(unexplored_room.id)
        next_unexplored_room = unexplored_room.get_room_in_direction(way) ## get each room from direction available for current unexplored room
        # print(next_unexplored_room, "next room")
        
        
        if next_unexplored_room.id not in visited: ## if the next room is not in visited use recursive
            
            room_recursive = solution_attempt_recursive(next_unexplored_room, visited)
            
            if len(unexplored_room.get_exits()) == 1: ##if length of rooms directions is 1(dead end) add way and reverse to path
                order = [way, give_opposite_direction(way)]
                
            else: ## if room has more than one direction add direction, recursive, and opposite to return
                order = [way] + room_recursive + [give_opposite_direction(way)]
               
        
            route = route + order

    
    
    return route
        
        
traversal_path = solution_attempt_recursive(player.current_room)

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
