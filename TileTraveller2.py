import random
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO =  'n'
COUNTER_LIST = [True, 0]

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

"""
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    print("Direction:", direction.lower())
    """

def pull_a_lever(purse, col, row):
    if (col == 1 and row == 2):
        if purse[1][0]:
            choice = random.choice([YES, NO])
            print("Pull a lever (y/n):", choice.lower())
            
            if choice in YES:
                purse[0] += 1
                print("You received 1 coin, your total is now {}.".format(purse[0]))
                return purse
            elif choice in NO:
                return purse
        else:
            return purse
    elif (col == 2 and row == 2):
        if purse[1][1]:
            choice = random.choice([YES, NO])
            print("Pull a lever (y/n):", choice.lower())
            if choice in YES:
                purse[0] += 1
                print("You received 1 coin, your total is now {}.".format(purse[0]))
                return purse
            elif choice in NO:
                return purse
        else:
            return purse
    elif (col == 2 and row == 3):
        if purse[1][2]:
            choice = random.choice([YES, NO])
            print("Pull a lever (y/n):", choice.lower())
            if choice in YES:
                purse[0] += 1
                print("You received 1 coin, your total is now {}.".format(purse[0]))
                return purse
            elif choice in NO:
                return purse
        else:
            return purse
    elif (col == 3 and row == 2):
        if purse[1][3]:
            choice = random.choice([YES, NO])
            print("Pull a lever (y/n):", choice.lower())
            if choice in YES:
                purse[0] += 1
                print("You received 1 coin, your total is now {}.".format(purse[0]))
                return purse
            elif choice in NO:
                return purse
        else:
            return purse
    return purse

        
def find_directions(col, row, purse):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        purse = pull_a_lever(purse, col, row)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        purse = pull_a_lever(purse, col, row)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        purse = pull_a_lever(purse, col, row)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        purse = pull_a_lever(purse, col, row)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, purse

def play_one_move(col, row, valid_directions, purse):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    print("Direction:", direction.lower())
    
    if not direction in valid_directions:
        if (col == 1 and row == 2):
            purse[1][0] = False
        elif (col == 2 and row == 2):
            purse[1][1] = False
        elif (col == 2 and row == 3):
            purse[1][2] = False
        elif (col == 3 and row == 2):
            purse[1][3] = False

        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        purse[1] = [True, True, True, True]

    purse[2] += 1
    return victory, col, row, purse

def main():
    victory = False
    purse = [0, [True, True, True, True], 0]
    row = 1
    col = 1
    seed = int(input("Input seed: "))
    random.seed(seed)

    while not victory:
        valid_directions, purse = find_directions(col, row, purse)
        print_directions(valid_directions)
        victory, col, row, purse = play_one_move(col, row, valid_directions, purse)
    print("Victory! Total coins {}. Moves {}.".format(purse[0],purse[2]))

def play():
    play_choice = input("Play again (y/n): ")
    while play_choice in YES:
        main()
        play_choice = input("Play again (y/n): ")

# The main program starts here
main()
play()