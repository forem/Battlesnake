import collections 

class Point:
    def __init__(self, board, x, y, width, height, rank = 0, direction = "none", parent = 'none'):
        self.board = board
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rank = rank
        self.direction = direction
        self.parent = parent
    
    def get_symbol(self):
        return self.board[self.y][self.x]

    def check_safe(self):
        safe = ['F', '.', 'T', 't']
        return self.get_symbol() in safe

    def get_neighbors(self):
        neighbors = []

        if self.y > 0:
            up = Point(self.board, self.x, self.y - 1, self.width, self.height, self.rank + 1, "up", self)
            if up.check_safe():
                neighbors.append(up)
        if self.y < (self.height - 1):
            down = Point(self.board, self.x, self.y + 1, self.width, self.height, self.rank + 1, "down", self)
            if down.check_safe():
                neighbors.append(down)
        if self.x < (self.width - 1):
            right = Point(self.board, self.x + 1, self.y, self.width, self.height, self.rank + 1, "right", self)
            if right.check_safe():
                neighbors.append(right)
        if self.x > 0:
            left = Point(self.board, self.x - 1, self.y, self.width, self.height, self.rank + 1, "left", self)
            if left.check_safe():
                neighbors.append(left)

        return neighbors

    def get_move(self, prev_move = "none"):
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

def a_star(board, you_x, you_y, height, width, target):
    _open = collections.deque([Point(board, you_x, you_y, width, height)])
    closed = set()
    while True:
        try:
            top = _open.popleft()
        except:
            return []
        if top.get_symbol() == target:
            break
        closed.add(top)
        neighbors = top.get_neighbors()
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
    return top.get_move()

def get_food(board, you_x, you_y, height, width):
    return a_star(board, you_x, you_y, height, width, 'F')

def chase_tail(board, you_x, you_y, height, width):
    return a_star(board, you_x, you_y, height, width, 'T')