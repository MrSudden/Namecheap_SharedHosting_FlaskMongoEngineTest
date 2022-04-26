from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, IntegerField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo

# without space cleaning
def clean_data():
	def _clean_data(form, field):
		val = field.data
		if "\'" in val or "\"" in val or "<" in val or '*' in val or '>' in val or " " in val:
			raise ValidationError('please enter an appropriate input with no special characters and spaces within e.g TESTING')
	return _clean_data

# with space cleaning
def clean_data_wspaces():
	def _clean_data(form, field):
		val = field.data
		if "\'" in val or "\"" in val or "<" in val or '*' in val or '>' in val:
			raise ValidationError('please enter an appropriate input with no special characters e.g Testing testing...')
	return _clean_data

class ClassName(FlaskForm):
    pass