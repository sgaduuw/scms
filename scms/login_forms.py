from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SALoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class CreateAdminForm(FlaskForm):
    new_first_name = StringField('First Name', validators=[DataRequired()])
    new_last_name = StringField('Last Name', validators=[DataRequired()])
    new_username = StringField('Username', validators=[DataRequired()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create admin')

class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
