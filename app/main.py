import json
import os
import bottle

from board import *
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

    # print(json.dumps(data))

    height, width = data["board"]["height"], data["board"]["width"]
    you_x, you_y = data["you"]["body"][0]["x"], data["you"]["body"][0]["y"] 
    board = empty_board(height, width)
    board = add_food(board, data["board"]["food"])
    board = add_you(board, data["you"]["body"])
    # food = data["board"]["food"]

    print_board(board)
    print('x: ' + str(you_x + 1))
    print('y: ' + str(you_y + 1))

    move = decide_move(board, height, width, you_x, you_y, data["you"]["health"])
    print('move: ' + str(move))
    print('health: ' + str(data["you"]["health"]))

    return move_response(move)


@bottle.post('/end')
def end():
    data = bottle.request.json

    print(json.dumps(data))

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
