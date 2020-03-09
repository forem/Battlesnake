import json
import os
import bottle

from .variables import *
from .board import *
from .logic import *
from .api import ping_response, start_response, move_response, end_response


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

    variables = Variables(data)
    board = Board(variables)
    move = decide_move(variables)

    board.print_board()
    print(f'move: {move}')
    print(f'health: {variables.you_health}')

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
