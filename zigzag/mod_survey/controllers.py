#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:01:40
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from flask import Blueprint, request, redirect, render_template, url_for, flash


from zigzag import app, db

from .models import Survey
from .forms import SurveyForm

mod_survey = Blueprint("survey", __name__, url_prefix="/survey")


@mod_survey.route('/')
def index():
    return redirect(url_for('survey.survey_list'))


@mod_survey.route('/create', methods=['GET', 'POST'])
def survey_create():
    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey()
        survey.title = request.form['title']
        survey.description = request.form['description']
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('survey.survey_list'))

    if app.config['DEBUG']:
        flash(form.errors, 'error')

    return render_template('survey/create.html', form=form)


@mod_survey.route('/list', methods=['GET'])
def survey_list():
    surveys = Survey.query.all()
    return render_template('survey/list.html', surveys=surveys)


@mod_survey.route('/<survey_id>', methods=['GET'])
def survey_show(survey_id):
    survey = Survey.query.get(survey_id)  # FIXME:处理id不存在的情况
    return render_template('survey/show.html', survey=survey)
