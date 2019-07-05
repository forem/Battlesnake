class Board:

    def __init__(self, height, width, food, you_body, snakes, you_id):
        self.create_empty_board(height, width)
        self.add_food(food)
        self.add_you(you_body)
        self.add_others(snakes, you_id)

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
