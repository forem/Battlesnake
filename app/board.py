
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

def print_board(board):
    for x in board:
        for coord in x:
            print(coord, end =" ")
        print()