# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import user


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(
        user.bp,
        url_prefix='/user')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)