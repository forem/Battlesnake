import collections 

class Point:
    def __init__(self, parent, x, y, rank):
        self.parent = parent
        self.x = x
        self.y = y
        self.rank = rank
        self.direction = "none"
    
    def get_symbol(self, board):
        return str(board[self.y][self.x])

    def get_neighbors(self, board, height, width):
        neighbors = []

        if self.y > 0:
            up = Point(self, self.x, self.y - 1, self.rank + 1)
            up.direction = "up"
            if (up.get_symbol(board) == '.') or (up.get_symbol(board) == 'F'):
                neighbors.append(up)

        if self.y < (height - 1):
            down = Point(self, self.x, self.y + 1, self.rank + 1)
            down.direction = "down"
            if (down.get_symbol(board) == '.') or (down.get_symbol(board) == 'F'):
                neighbors.append(down)

        if self.x < (width - 1):
            right = Point(self, self.x + 1, self.y, self.rank + 1)
            right.direction = "right"
            if (right.get_symbol(board) == '.') or (right.get_symbol(board) == 'F'):
                neighbors.append(right)

        if self.x > 0:
            left = Point(self, self.x - 1, self.y, self.rank + 1)
            left.direction = "left"
            if (left.get_symbol(board) == '.') or (left.get_symbol(board) == 'F'):
                neighbors.append(left)
        
        return neighbors

    def get_move(self, prev_move):
        if self.direction == "none":
            return prev_move
        else:
            return self.parent.get_move(self.direction)

    def __eq__(self, other):
        if isinstance(other, Point):
            equal = (self.x == other.x) and (self.y == other.y)
            return equal
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))

def a_star(board, you_x, you_y, height, width):
    _open = collections.deque([])
    _open.append(Point('none', you_x, you_y, 0))
    closed = set()
    top = ""
    while True:
        try:
            top = _open.popleft()
        except:
            return []
        if top.get_symbol(board) == 'F':
            break
        closed.add(top)
        neighbors = top.get_neighbors(board, height, width)
        if len(neighbors) > 0:
            for neighbor in neighbors:
                in_open, in_closed = False, False
                for value in tuple(_open):
                    if value == neighbor:
                        if value.rank > neighbor.rank:
                            _open.remove(value)
                        else:
                            in_open = True                            
                for value in tuple(closed):
                    if value == neighbor:
                        if value.rank > neighbor.rank:
                            closed.remove(value)
                        else:
                            in_closed = True
                if (not in_open) and (not in_closed):
                    _open.append(neighbor)
    return top.get_move("initial")

def get_food(board, you_x, you_y, height, width):
    return a_star(board, you_x, you_y, height, width)
