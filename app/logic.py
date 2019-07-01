import random

from get_food import *

def avoid_self_and_borders(board, directions, height, width, you_x, you_y):
    try:
        if (board[you_y + 1][you_x] == 'Y'):
            directions.remove('down')
    except:
        directions.remove('down')
    try:
        if (board[you_y - 1][you_x] == 'Y') or (you_y == 0):
            directions.remove('up')
    except:
        directions.remove('up')
    
    try:
        if (board[you_y][you_x - 1] == 'Y') or (you_x == 0):
            directions.remove('left')
    except:
        directions.remove('left')

    try:
        if (board[you_y][you_x + 1] == 'Y'):
            directions.remove('right')
    except:
        directions.remove('right')

    return directions

def decide_move(board, height, width, you_x, you_y, health):
    if False: #health > 50:
        directions = ['up', 'down', 'left', 'right']
        directions = avoid_self_and_borders(board, directions, height, width, you_x, you_y)
        if len(directions) == 0:
            print('Guaranteed loss')
            return 'down'
        print('Options:', directions)
        return random.choice(directions)
    else:
        print("It's A* time, baby!*******************************************************************************************")
        move = get_food(board, you_x, you_y, height, width)
        if len(move) == 0:
            print("Can't eat")
            directions = ['up', 'down', 'left', 'right']
            directions = avoid_self_and_borders(board, directions, height, width, you_x, you_y)
            if len(directions) == 0:
                print('Guaranteed loss')
                return 'down'
            print('Options:', directions)
            return random.choice(directions)
        return move

