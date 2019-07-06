from .point import *

class Board:

    def __init__(self, height, width, food, you_body, snakes, you_id):
        self.create_empty_board(height, width)
        self.add_food(food)
        self.add_you(you_body)
        self.add_others(snakes, you_id)
        self.flood_flow_get_deadends(Point(self.board, you_body[0]['x'], you_body[0]['y'], width, height))

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
        for b in you_body:
            x_coord = b['x']
            y_coord = b['y']
            self.board[y_coord][x_coord] = 'Y'

        head = you_body[0]
        head_x_coord = head['x']
        head_y_coord = head['y']
        self.board[head_y_coord][head_x_coord] = 'H'

        if len(you_body) > 3:
            tail = you_body[-1]
            tail_x_coord = tail['x']
            tail_y_coord = tail['y']
            self.board[tail_y_coord][tail_x_coord] = 'T'

    
    def add_others(self, snakes, you_id):
        for snake in snakes:
            if snake["id"] == you_id:
                continue
            for b in snake["body"]:
                x_coord = b['x']
                y_coord = b['y']
                self.board[y_coord][x_coord] = 'o'
                
            head = snake["body"][0]
            head_x_coord = head['x']
            head_y_coord = head['y']
            self.board[head_y_coord][head_x_coord] = 'h'

            tail = snake["body"][-1]
            tail_x_coord = tail['x']
            tail_y_coord = tail['y']
            self.board[tail_y_coord][tail_x_coord] = 't'

    def flood_flow_get_deadends(self, point):
        if (not point.check_safe()) or (point.get_symbol() == 'H'):
            return
        safe_neighbors = 0
        for neighbor in point.get_neighbors():
            if neighbor.check_safe():
                safe_neighbors += 1
                self.flood_flow_get_deadends(point)
        if safe_neighbors <= 1:
            self.board[point.y][point.x] = 'x'


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
