from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Regexp, Length
from ....db import get_db


class UpdateMenuForm(FlaskForm):
    def validate_menu_name(form, field):
        if form.menu_visibility.data==1 and not field.data:
            raise ValidationError('Menu name is required if it is visible')
        
        db = get_db()
        post = db.execute(
            'SELECT id, menu_name FROM post WHERE menu_name = ? and id <> ?', (field.data, form.id.data,)
        ).fetchone()

        if post and post[1]:
            raise ValidationError('Menu exists. This field must be Unique')

    menu_name = StringField('Menu Name', validators=[
        Regexp(regex=r'^$|^[a-zA-Z0-9\-\s]+$', message='Must contain only Alphanumeric, Space and Hyphen characters'),
        Length(max=128)
    ])
    menu_position = SelectField("Position", coerce=int)
    menu_visibility = SelectField("Visibile",  coerce=int)
    id = HiddenField()
