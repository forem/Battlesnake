import random

from .a_star import *

def avoid_self_and_borders_randomly(board, height, width, you_x, you_y, safe):
    directions = list()

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
        return directions
    return random.choice(directions)

def decide_move(board, height, width, you_x, you_y, you_health, you_body, snakes, you_id):

    can_chase_tail = True

    for snake in snakes:
        if snake["health"] >= you_health:
            if snake["id"] != you_id:
                can_chase_tail = False
                break

    if (you_health >= 50) and can_chase_tail:
        move = chase_tail(board, you_x, you_y, height, width)
        if len(move) == 0:
            move2 = get_food(board, you_x, you_y, height, width)
            if len(move2) == 0:
                move3 = avoid_self_and_borders_randomly(board, height, width, you_x, you_y, ['F', '.', 'T', 't'])
                if len(move3) == 0:
                    return avoid_self_and_borders_randomly(board, height, width, you_x, you_y, ['F', '.', 'T', 't', '*'])
                return move3
            return move2
        return move
    else:
        move = get_food(board, you_x, you_y, height, width)
        if len(move) == 0:
            move2 = chase_tail(board, you_x, you_y, height, width)
            if len(move2) == 0:
                move3 = avoid_self_and_borders_randomly(board, height, width, you_x, you_y, ['F', '.', 'T', 't'])
                if len(move3) == 0:
                    return avoid_self_and_borders_randomly(board, height, width, you_x, you_y, ['F', '.', 'T', 't', '*'])
                return move3
            return move2
        return move

