#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:15:25
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New password', [DataRequired()])

