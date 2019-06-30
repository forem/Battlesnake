import random

def avoid_borders(directions, height, width, you_x, you_y):
    if you_y > height:
        directions.remove('down')
    if you_y == 0:
        directions.remove('up')
    if you_x > width:
        directions.remove('right')
    if you_y == 0:
        directions.remove('left')
    return directions

def decide_move(board, height, width, you_x, you_y):
    directions = ['up', 'down', 'left', 'right']
    directions = avoid_borders(directions, height, width, you_x, you_y)
    if len(directions) == 0:
        return 'down'
    return random.choice(directions)
