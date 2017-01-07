#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-07 10:11:42
# @Author  : Fruit Lee (glfruit80@gmail.com)
# @Link    : http://glfruit.me
# @Version : $Id$

from zigzag import db
from zigzag.models import Entity


class Survey(Entity):
    title = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.String(300), index=True)
    questions = db.relationship('Question', backref='survey', lazy='dynamic')

    def __repr__(self):
        return "<Survey %r>" % (self.title)

# TODO: 增加是否类型、单选类型和多选类型问题


class Question(Entity):    
    title = db.Column(db.String(200), index=True, unique=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    question_type = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_on': question_type,
        'polymorphic_identity': 'question'
    }

    def __repr__(self):
        return "<Question %r>" % (self.title)


class BooleanQuestion(Question):
    __mapper_args__ = {
        'polymorphic_identity': 'boolean_question'
    }
