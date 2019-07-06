import random

from .a_star import *

def avoid_self_and_borders_randomly(board, height, width, you_x, you_y):
    directions = list()
    safe = ['F', '.', 'T', 't']

    if you_y < (height - 1):
        if (board[you_y + 1][you_x] in safe):
            directions.append('down')
    if you_y > 0:
        if (board[you_y - 1][you_x] in safe):
            directions.append('up')
    if you_x > 0:
        if (board[you_y][you_x - 1] in safe):
            directions.append('left')
    if you_x < (width - 1):
        if (board[you_y][you_x + 1] in safe):
            directions.append('right')

    if len(directions) == 0:
        print('Guaranteed loss')
        return 'down'

    return random.choice(directions)

def decide_move(board, height, width, you_x, you_y, you_health, you_body, snakes):

    can_chase_tail = True

    for snake in snakes:
        if snake["health"] >= you_health:
            can_chase_tail = False
            break

    if (you_health >= 50) and can_chase_tail:
        move = chase_tail(board, you_x, you_y, height, width)
        if len(move) == 0:
            print("Can't chase tail")
            return avoid_self_and_borders_randomly(board, height, width, you_x, you_y)
        return move
    else:
        move = get_food(board, you_x, you_y, height, width)
        if len(move) == 0:
            print("Can't eat")
            return avoid_self_and_borders_randomly(board, height, width, you_x, you_y)
        return move

