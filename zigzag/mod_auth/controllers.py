#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:03:42
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from flask import Blueprint, redirect, render_template

from .forms import LoginForm

mod_auth = Blueprint("auth", __name__, url_prefix="/auth")

@mod_auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: 实现登录功能
        return redirect('/')
    return render_template('auth/login.html', form=form)
