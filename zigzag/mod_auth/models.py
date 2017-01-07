#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:13:53
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from zigzag import db
from zigzag.models import Entity


class User(Entity):
    __tablename__ = 'auth_user'

    username = db.Column(db.String(200), index=True,
                         unique=True, nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False,
                      unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
