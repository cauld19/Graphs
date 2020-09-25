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


def solution_attempt(world, starting_location):
    
    ## at starting room choose random direction
        ## at each room check to see number of directions
            ## if greater than 2 store in queue the room_id and direction
            ## that is not the opposite direction of the way headed
        ## DFT until room.exits has only one direction(returning backwards)
            ## look in queue and take most recent saved room id and direction
            ## DFT traverse through that 
        ## store every direction taken and return that
    traversal_path_rooms = {}
    queue = deque()
    stack = deque()
    stack.append(starting_location)
    
    visited = {}

    print(stack)
    
    opposites = [('n', 's'), ('e', 'w'), ('w', 'e'), ('s', 'n')]
    

    while len(stack) > 0 and len(visited) < 500:

        current = stack.pop()
        player.current_room.id = current
        
        
        directions = player.current_room.get_exits()
        print(directions)
        print(visited)
        
        random_direction = random.choice(directions)
        
        if current not in visited:
            # print("here")
            # if len(directions) == 1:
            #     traversal_path_rooms[current].append(random_direction)
            #     traversal_path.append(random_direction)
            #     player.travel(random_direction)
            #     stack.append(player.current_room.id)
                
                
            if len(directions) == 1: ## if only one way to go at end of traversal, take what was in queue and put to stack
                stack.append(queue.popleft)
                
                
            elif len(directions) == 2: ## if two directions to go
                if len(traversal_path) > 0 and (random_direction, traversal_path[-1]) in opposites: ## make sure random way to go is not backwards where you came from
                    while (random_direction, traversal_path[-1]) in opposites:
                        # print(traversal_path[-1])
                        random_direction = random.choice(directions)
                        
                traversal_path_rooms[current] = random_direction
                traversal_path.append(random_direction)
                player.travel(random_direction)
                stack.append(player.current_room.id)
                
            elif len(directions) > 2: ## if greater than two directions make sure not going back where you came from
                
                if len(traversal_path) > 0 and (random_direction, traversal_path[-1]) in opposites:
                    while (random_direction, traversal_path[-1]) in opposites:
                        random_direction = random.choice(directions)
                        print("are you stuck here")
                visited[current] = 1
                traversal_path_rooms[current] = random_direction
                traversal_path.append(random_direction)
                queue.appendleft(current)
                player.travel(random_direction)
                stack.append(player.current_room.id)

                
                
        elif current in visited:
            if current in traversal_path_rooms:
                for key, value in traversal_path_rooms.items():
                    if current == key:
                        if value in directions:
                            directions.remove(value)
                visited[current] += 1            
                random_direction = random.choice(directions)
                traversal_path_rooms[current] = random_direction
                traversal_path.append(random_direction)
                player.travel(random_direction)
                stack.append(player.current_room.id)
                
                directions = player.current_room.get_exits()
                if visited[current] < len(directions):
                    queue.appendleft(current)
            

                
        # if len(directions) == 1:
        #     traversal_path.append(random_direction)
        #     player.travel(random_direction)
        #     if player.current_room.id in visited and len(queue) > 0:
                
        #         stack.append(queue.popleft())
        #     elif player.current_room.id in visited:
        #         continue
        #     else:
        #         stack.append(player.current_room.id)
            
        
        # elif len(directions) == 2:
        #     for direction in directions:
        #         if len(traversal_path) < 1:
        #             break
        #         if (random_direction, traversal_path[-1]) in opposites:
        #             while (random_direction, traversal_path[-1]) in opposites:
        #                     random_direction = random.choice(directions)

        #     traversal_path.append(random_direction)
        #     player.travel(random_direction)
        #     stack.append(player.current_room.id)
        
        # elif len(directions) > 2:
        #     for direction in directions:
        #         if len(traversal_path) < 1:
        #             break
        #         if random_direction == direction:
        #             continue
        #         elif (random_direction, traversal_path[-1]) in opposites:
        #             while (random_direction, traversal_path[-1]) in opposites:
        #                     random_direction = random.choice(directions)
        #     queue.append(current)
        #     waiting_visit[current] = direction
        #     traversal_path.append(random_direction)
        #     player.travel(random_direction)
        #     stack.append(player.current_room.id)
            
                       
        
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
