import collections 

class Point:
    def __init__(self, parent, x, y, rank):
        self.parent = parent
        self.x = x
        self.y = y
        self.rank = rank
        self.direction = "none"
    
    def get_symbol(self, board):
        return board[self.y][self.x]

    def get_neighbors(self, board, height, width):
        neighbors = []

        if self.y > 0:
            up = Point(self, self.x, self.y - 1, self.rank + 1)
            up.direction = "up"
            neighbors.append(up)

        if self.y < (height - 1):
            down = Point(self, self.x, self.y + 1, self.rank + 1)
            down.direction = "down"
            neighbors.append(down)

        if self.x > 0:
            left = Point(self, self.x - 1, self.y, self.rank + 1)
            left.direction = "left"
            neighbors.append(left)

        if self.x < (width - 1):
            right = Point(self, self.x + 1, self.y, self.rank + 1)
            right.direction = "right"
            neighbors.append(right)

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
    top = _open.popleft()
    while top.get_symbol(board) != "F":
        for neighbor in top.get_neighbors(board, height, width):
            if neighbor in _open:
                for value in tuple(_open):
                    if value == neighbor:
                        if value.rank > neighbor.rank:
                            _open.remove(value)
                            _open.append(neighbor)
            elif neighbor in closed:
                for value in tuple(closed):
                    if value == neighbor:
                        if value.rank > neighbor.rank:
                            closed.remove(value)
                            _open.append(neighbor)
            else:
                _open.append(neighbor)
        top = _open.popleft()
    return top.get_move("initial")

def get_food(board, you_x, you_y, height, width):
    return a_star(board, you_x, you_y, height, width)