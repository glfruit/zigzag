#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:11:55
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SurveyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Survey Description')

