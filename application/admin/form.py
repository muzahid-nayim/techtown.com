# In application/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class AddBrandForm(FlaskForm):
    name = StringField('Brand', validators=[DataRequired()])
    logo = FileField('Brand Logo') 
    submit = SubmitField('Add Brand')


class EditBrandForm(FlaskForm):
    name = StringField('Brand', validators=[DataRequired()])
    logo = FileField('Brand Logo') 
    submit = SubmitField('Update Brand')
