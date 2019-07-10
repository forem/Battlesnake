from collections import deque

from .point import *

class Board:

    def __init__(self, height, width, food, you_body, snakes, you_id, you_health):
        self.create_empty_board(height, width)
        self.add_food(food)
        self.add_you(you_body)
        self.add_others(snakes, you_body, you_id, width, height)
        self.flood_board = self.board
        self.flood_flowed = list()
        self.flood_flow_get_deadends(Point(self.board, you_body[0]['x'], you_body[0]['y'], width, height))
        if you_health < 30:
            self.add_food(food)

    def create_empty_board(self, height, width):
        board = []
        for h in range(height):
            board.append(['.'] * width)
        self.board = board

    def add_food(self, food):
        for f in food:
            x_coord = f['x']
            y_coord = f['y']
            self.board[y_coord][x_coord] = 'F'

    def add_you(self, you_body):
        coords = set()
        duplicates = False
        for b in you_body:
            x_coord = b['x']
            y_coord = b['y']
            if (x_coord, y_coord) in coords:
                duplicates = True
            coords.add((x_coord, y_coord))
            self.board[y_coord][x_coord] = 'Y'

        head = you_body[0]
        head_x_coord = head['x']
        head_y_coord = head['y']
        self.board[head_y_coord][head_x_coord] = 'H'

        if (len(you_body) > 3) and not duplicates:
            tail = you_body[-1]
            tail_x_coord = tail['x']
            tail_y_coord = tail['y']
            self.board[tail_y_coord][tail_x_coord] = 'T'

    
    def add_others(self, snakes, you_body, you_id, width, height):
        you_size = len(you_body)
        for snake in snakes:
            if snake["id"] == you_id:
                continue

            coords = set()
            duplicates = False

            for b in snake["body"]:
                x_coord = b['x']
                y_coord = b['y']
                if (x_coord, y_coord) in coords:
                    duplicates = True
                coords.add((x_coord, y_coord))
                self.board[y_coord][x_coord] = 'o'
                
            head = snake["body"][0]
            head_x_coord = head['x']
            head_y_coord = head['y']
            self.board[head_y_coord][head_x_coord] = 'h'

            if not duplicates:
                tail = snake["body"][-1]
                tail_x_coord = tail['x']
                tail_y_coord = tail['y']
                self.board[tail_y_coord][tail_x_coord] = 't'

            if len(snake["body"]) >= you_size:
                for neighbor in Point(self.board, head_x_coord, head_y_coord, width, height).get_neighbors():
                    self.board[neighbor.y][neighbor.x] = '*'


    def flood_flow_get_deadends(self, point):
        self.flood_flowed.append(point)
        point.board = self.flood_board
        if (not point.check_safe()) and (not self.board[point.y][point.x] == 'H'):
            return
        for neighbor in point.get_neighbors():
            if not neighbor in self.flood_flowed:
                self.flood_flow_get_deadends(neighbor)
        if (len(point.get_neighbors()) <= 1) and (not self.board[point.y][point.x] in ['H', 'T', 't']):
            self.board[point.y][point.x] = '!'
            if(not point.parent == 'none'):
                self.flood_flow_get_deadends_again(point.parent)

    def flood_flow_get_deadends_again(self, point):
        point.board = self.flood_board
        if (not point.check_safe()) and (not self.board[point.y][point.x] == 'H'):
            return
        if (len(point.get_neighbors()) == 0) and (not self.board[point.y][point.x] in ['H', 'T', 't']):
            self.board[point.y][point.x] = '!'
            if(not point.parent == 'none'):
                self.flood_flow_get_deadends_again(point.parent)

    def print_board(self):

        x_label = 1
        print("  ", end =" ")
        for coord in self.board[0]:
            if x_label < 10:
                print(x_label, end ="  ")
            else:
                print(x_label, end=" ")
            x_label += 1
        print()

        y_label = 1
        for x in self.board:
            if y_label < 10:
                print(y_label, end ="  ")
            else:
                print(y_label, end =" ")

            for coord in x:
                print(coord, end ="  ")
            print()
            y_label += 1
