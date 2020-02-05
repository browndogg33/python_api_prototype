# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Ping(Resource):

    def get(self):
        ping = {"ping": "UP"}
        return ping, 200, None