# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Users(Resource):

    def get(self):
        print(g.headers)
        user1 = {"id": "1", "firstName": "Brandon", "lastName": "Brown"}
        user2 = {"id": "2", "firstName": "Daniel", "lastName": "Aquino"}
        return [user1, user2], 200, None

    def post(self):
        print(g.json)
        print(g.headers)

        return {}, 201, None