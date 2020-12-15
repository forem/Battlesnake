import json
import random
from bottle import HTTPResponse


def ping_response():
    return HTTPResponse(
        status=200
    )


def start_response():

    return HTTPResponse(
        status=200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
            "color": random.choice(["#DBAF34", "#739071"]),
            "headType": "dead",
            "tailType": "shac-coffee"
        })
    )


def move_response(move):
    assert move in ['up', 'down', 'left', 'right'], \
        "Move must be one of [up, down, left, right]"

    return HTTPResponse(
        status=200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
            "move": move
        })
    )


def end_response():
    return HTTPResponse(
        status=200
    )
