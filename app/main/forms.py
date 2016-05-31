from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError
from wtforms.validtors import Required, Length, Email, Regexp

class LoginForm(Form):
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')
