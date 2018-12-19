# -*- coding: utf-8 -*-
""" REST API - Endpoint routing

    Author(s): Adam Mitchell, adam@think-engineer.com
"""
from flask import current_app, request
from flask_rebar import Rebar, response


rebar = Rebar()
registry = rebar.create_handler_registry()


@registry.handles(
    rule='/hello',
    method='GET'
)
def get_hello():
    return response(
        data={'message': 'Hello, Adam!'},
        status_code=200
    )