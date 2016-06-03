from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class LoginForm(Form):
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')

class BlogForm(Form):
    title = StringField(validators=[Required()], render_kw={"placeholder": "Put title here"})
    body = TextAreaField(validators=[Required()], render_kw={"placeholder": "What's on your mind?"})
    submit = SubmitField('Submit')

class JournalForm(Form):
    event = StringField("", validators=[Required()], render_kw={"placeholder": "Event Name"})
    costtime = StringField("", validators=[Required()], render_kw={"placeholder": "Time Cost"})
    submit = SubmitField('Add')
