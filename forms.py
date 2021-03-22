from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SentimentForm(FlaskForm):
	sent_inp = StringField('Feedback',
							validators = [DataRequired()])
	submit = SubmitField('Get Result')

class ResultForm(FlaskForm):

	submit = SubmitField('Try Again?')	