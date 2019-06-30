
def empty_board(height, width):
    board = []

    for h in range(height):
        row = []
        for w in range(width):
            row.append('0')
        board.append(row)
    return board

def add_food(board, food):
    for f in food:
        x_coord = f['x']
        y_coord = f['y']
        board[y_coord][x_coord] = 'F'
    return board

def add_you(board, body):
    for b in body:
        x_coord = b['x']
        y_coord = b['y']
        board[y_coord][x_coord] = 'Y'
    return board

def print_board(board):

    x_label = 1
    print("  ", end =" ")
    for coord in board[0]:
        if x_label < 10:
            print(x_label, end ="  ")
        else:
            print(x_label, end=" ")
        x_label += 1
    print()

    y_label = 1
    for x in board:
        if y_label < 10:
            print(y_label, end ="  ")
        else:
            print(y_label, end =" ")

        for coord in x:
            print(coord, end ="  ")
        print()
        y_label += 1