from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired




class SiteInfoForm(FlaskForm):
    name = StringField('Site Name', validators=[DataRequired()])
    title = StringField('Site Title', validators=[DataRequired()])
    tagline = StringField('Site Tagline', validators=[DataRequired()])
    description = TextAreaField('Site Description', validators=[DataRequired()])
    copyright = StringField('Copyright line', validators=[DataRequired()])
    fqdns = TextAreaField('FQDNs, comma separated', validators=[DataRequired()])
    enabled = BooleanField('Enabled')
    submit = SubmitField('Submit')
