from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Login form."""
    user_name = StringField("Username", validators=[DataRequired()])
    pass_word = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    user_name = StringField("User name", validators=[DataRequired()])
    pass_word = PasswordField("Password", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
