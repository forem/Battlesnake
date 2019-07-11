import random

from a_star import *

def avoid_self_and_borders_randomly(variables, safe):
    board = variables.board
    height = variables.height
    width = variables.width
    you_x = variables.you_x
    you_y = variables.you_y
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

def decide_move(variables):
    board = variables.board
    height = variables.height
    width = variables.width
    you_x = variables.you_x
    you_y = variables.you_y
    you_health = variables.you_health
    you_body = variables.you_body
    snakes = variables.snakes
    you_id = variables.you_id

    you_size = len(you_body)
    can_chase_tail = True
    for snake in snakes:
        if (snake["health"] >= you_health) or (len(snake["body"]) >= you_size):
            if snake["id"] != you_id:
                can_chase_tail = False
                break

    if (you_health >= 55) and can_chase_tail:
        move = chase_tail(variables)
        if len(move) == 0:
            move2 = get_food(variables)
            if len(move2) == 0:
                move3 = avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't'])
                if len(move3) == 0:
                    move4 = chase_tail(variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move4) == 0:
                        move5 = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
                        if len(move5) == 0:
                            return avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
                        return move5
                    return move4
                return move3
            return move2
        return move
    elif you_health < 30:
        move = get_food(variables)
        if len(move) == 0:
            move2 = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
            if len(move2) == 0:
                move3 = chase_tail(variables)
                if len(move3) == 0:
                    move4 = avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't'])
                    if len(move4) == 0:
                        return avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
                    return move4
                return move3
            return move2
        return move
    else:
        move = get_food(variables)
        if len(move) == 0:
            move2 = chase_tail(variables)
            if len(move2) == 0:
                move3 = avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't'])
                if len(move3) == 0:
                    move4 = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move4) == 0:
                        return avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
                    return move4
                return move3
            return move2
        return move

