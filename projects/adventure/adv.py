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

    queue = deque()
    stack = deque()
    stack.append(starting_location)
    
    visited = {}
    waiting_visit = {}
    
    number_of_visits = 0
    
    opposites = [('n', 's'), ('e', 'w'), ('w', 'e'), ('s', 'n')]
    
    # if len(visited) < 8 and len(visited) > 1:
    #     stack.append(queue.popleft())
    #     while len(stack) > 0:
    #         print("in while loop")
    #         current = stack.pop()
    #         if current not in visited:
    #             visited[current] = number_of_visits + 1
            
    #         directions = player.current_room.get_exits()
            
    #         random_direction = random.choice(directions)
            
    #         if len(directions) == 1:
    #             traversal_path.append(random_direction)
    #             player.travel(random_direction)
    #             if player.current_room.id in visited and len(queue) > 0:
                    
    #                 stack.append(queue.popleft())
    #             elif player.current_room.id in visited:
    #                 continue
    #             else:
    #                 stack.append(player.current_room.id)
                
            
    #         elif len(directions) == 2:
    #             for direction in directions:
    #                 if len(traversal_path) < 1:
    #                     break
    #                 if (random_direction, traversal_path[-1]) in opposites:
    #                     while (random_direction, traversal_path[-1]) in opposites:
    #                           random_direction = random.choice(directions)
    #             traversal_path.append(random_direction)
    #             player.travel(random_direction)
    #             stack.append(player.current_room.id)
            
    #         elif len(directions) > 2:
    #             for direction in directions:
    #                 if len(traversal_path) < 1:
    #                     break
    #                 if random_direction == direction:
    #                     continue
    #                 elif (random_direction, traversal_path[-1]) in opposites:
    #                     while (random_direction, traversal_path[-1]) in opposites:
    #                           random_direction = random.choice(directions)
    #             queue.append(current)
    #             waiting_visit[current] = direction
    #             traversal_path.append(random_direction)
    #             player.travel(random_direction)
    #             stack.append(player.current_room.id)
    # else:
    while len(stack) > 0 and len(visited) < 500:
        current = stack.pop()
        player.current_room.id = current
        
        if current not in visited:
            visited[current] = number_of_visits + 1
        
        directions = player.current_room.get_exits()
        
        random_direction = random.choice(directions)
        
        if len(directions) == 1:
            traversal_path.append(random_direction)
            player.travel(random_direction)
            if player.current_room.id in visited and len(queue) > 0:
                
                stack.append(queue.popleft())
            elif player.current_room.id in visited:
                continue
            else:
                stack.append(player.current_room.id)
            
        
        elif len(directions) == 2:
            for direction in directions:
                if len(traversal_path) < 1:
                    break
                if (random_direction, traversal_path[-1]) in opposites:
                    while (random_direction, traversal_path[-1]) in opposites:
                            random_direction = random.choice(directions)

            traversal_path.append(random_direction)
            player.travel(random_direction)
            stack.append(player.current_room.id)
        
        elif len(directions) > 2:
            for direction in directions:
                if len(traversal_path) < 1:
                    break
                if random_direction == direction:
                    continue
                elif (random_direction, traversal_path[-1]) in opposites:
                    while (random_direction, traversal_path[-1]) in opposites:
                            random_direction = random.choice(directions)
            queue.append(current)
            waiting_visit[current] = direction
            traversal_path.append(random_direction)
            player.travel(random_direction)
            stack.append(player.current_room.id)
            
                       
        
                    

        
        ## create a queue
        ## if room has more than two directions(not going backward and jsut contionuing forward)
            ## queue room id and get neighbor for bfs when the dft ends
        
        # traversal_path.append() ## push direction went

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
