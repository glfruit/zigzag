from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

from flask_babel import gettext, _

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('New password',[DataRequired(), EqualTo('confirm', message = _('Passwords must match'))])
	confirm = PasswordField('Repeat Password')