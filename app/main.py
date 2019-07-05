import json
import os
import bottle

try:
    from board import *
except:
    from .board import *
from logic import *

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    print(json.dumps(data))

    return start_response()


@bottle.post('/move')
def move():
    data = bottle.request.json

    height, width = data["board"]["height"], data["board"]["width"]
    food = data["board"]["food"]
    you_health, you_body = data["you"]["health"], data["you"]["body"]
    you_x, you_y = you_body[0]["x"], you_body[0]["y"]
    you_id = data["you"]["id"]
    snakes = data["board"]["snakes"]

    board = Board(height, width, food, you_body, snakes, you_id)

    move = decide_move(board.board, height, width, you_x, you_y, you_health, you_body)

    board.print_board()
    print(f'x: {you_x + 1}')
    print(f'y: {you_y + 1}')
    print(f'move: {move}')
    print(f'health: {you_health}')

    return move_response(move)


@bottle.post('/end')
def end():
    data = bottle.request.json

    # print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
