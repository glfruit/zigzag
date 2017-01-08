#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-08 19:45:39
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from flask import Blueprint

mod_home = Blueprint('home', __name__, url_prefix='/')


@mod_home.route('/')
def index():
    return "Website index page"
