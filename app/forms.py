
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CarForm(FlaskForm):
    image_url = StringField('Image URL', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=5)])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Car')
