# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.users import Users
from .api.users_id import UsersId
from .api.ping import Ping


routes = [
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=UsersId, urls=['/users/<int:id>'], endpoint='users_id'),
    dict(resource=Ping, urls=['/ping'], endpoint='ping'),
]