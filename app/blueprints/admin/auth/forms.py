from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import ValidationError, DataRequired


class LoginForm(FlaskForm):
    # TODO Revise validation rule for username
    def validate_username(form, field):
        if len(field.data) < 4:
            raise ValidationError('Email Address must be atleast 4 char long.')
    username = EmailField('Email Address', validators=[DataRequired()])
    # TODO Revise validation rule for password

    def validate_password(form, field):
        if len(field.data) < 3:
            raise ValidationError('Password must be atleast 4 char long.')
    password = PasswordField('Password', validators=[DataRequired()])
