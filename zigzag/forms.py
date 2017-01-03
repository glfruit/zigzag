from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from flask_babel import gettext, _

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('New password',[DataRequired()])

class SurveyForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()])
	description = PasswordField('Survey Description')