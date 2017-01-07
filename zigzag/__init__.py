# coding=utf-8
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

# FIXME:
# 根据http://www.cnblogs.com/txw1958/archive/2011/10/21/2220636.html重构日志初始化代码
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile("config.py")

app.debug = True
toolbar = DebugToolbarExtension(app)

# common error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# logging initialization
handler = TimedRotatingFileHandler('zigzag.log', when='d', backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
app.logger.addHandler(console)

# database initialiation
db = SQLAlchemy(app)

# i18n
babel = Babel(app)

# flask-bootstrap config
Bootstrap(app)
# app.extensions['bootstrap']['cdns']['twitter'] = WebCDN('//cdn.bootcss.com/bootstrap/3.3.0/css/')

# register blueprints
from zigzag.mod_auth.controllers import mod_auth as auth_module
from zigzag.mod_survey.controllers import mod_survey as survey_module

app.register_blueprint(auth_module)
app.register_blueprint(survey_module)
