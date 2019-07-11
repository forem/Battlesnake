import random

from .a_star import *
from .point import *

def avoid_self_and_borders_randomly(variables, safe = ['F', '.', 'T', 't']):
    you_x = variables.you_x
    you_y = variables.you_y
    point = Point(variables, you_x, you_y, safe)
    directions = list()

    for neighbor in point.get_neighbors():
        directions.append(neighbor.direction)

    if len(directions) == 0:
        return directions
    return random.choice(directions)

def favor_chase_tail(variables):
    move = chase_tail(variables)
    if len(move) == 0:
        move = get_food(variables)
        if len(move) == 0:
            move = avoid_self_and_borders_randomly(variables)
            if len(move) == 0:
                move = chase_tail(variables, ['F', '.', 'T', 't', '!', '*'])
                if len(move) == 0:
                    move = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move) == 0:
                        move = avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
    return move

def heavily_favor_get_food(variables):
    move = get_food(variables)
    if len(move) == 0:
        move = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
        if len(move) == 0:
            move = chase_tail(variables)
            if len(move) == 0:
                move = chase_tail(variables, ['F', '.', 'T', 't', '!', '*'])
                if len(move) == 0:
                    move = avoid_self_and_borders_randomly(variables)
                    if len(move) == 0:
                        move =  avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
    return move

def favor_get_food(variables):
    move = get_food(variables)
    if len(move) == 0:
        move = chase_tail(variables)
        if len(move) == 0:
            move = avoid_self_and_borders_randomly(variables)
            if len(move) == 0:
                move = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
                if len(move) == 0:
                    move = chase_tail(variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move) == 0:
                        move = avoid_self_and_borders_randomly(variables, ['F', '.', 'T', 't', '!', '*'])
    return move


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
        if len(snake["body"]) >= you_size:
            if snake["id"] != you_id:
                can_chase_tail = False
                break

    if (you_health >= 55) and can_chase_tail:
        move = favor_chase_tail(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move
    elif you_health < 30:
        move = heavily_favor_get_food(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move
    else:
        move = favor_get_food(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move
 
    return random.choice(['up', 'down', 'left', 'right'])

