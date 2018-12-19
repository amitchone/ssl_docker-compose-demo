# -*- coding: utf-8 -*-
""" REST API - Endpoint routing

    Author(s): Adam Mitchell, adam@think-engineer.com
"""
from flask import current_app, request
from flask_rebar import Rebar, response


rebar = Rebar()
registry = rebar.create_handler_registry()


@registry.handles(
    rule='/',
    method='GET'
)
def get_index():
    return response(
        data={'message': 'Hello, Being!'},
        status_code=200
    )