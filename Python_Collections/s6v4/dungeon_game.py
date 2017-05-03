import os
import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


monster, door, player = get_locations()

while True:
    valid_moves = get_moves(player)
    clear_screen()
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player))
    print("You can move {}".format(", ".join(valid_moves)))
    print("Enter QUIT to quit")
    
    move = input("> ")
    move = move.upper()
    
    if move == 'QUIT':
        break
    if move in valid_moves:
        player = move_player(player, move)
    else:
        print("\n ** Walls are hard! Don't run into them! **\n")
        continue
        
    # Good move? Change the player position
    # Bad move? Don't change anything!
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around