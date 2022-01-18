from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Regexp, Length
from ...db import get_db


class CreatePostForm(FlaskForm):
    def validate_slug(form, field):
        db = get_db()
        slug = db.execute(
            'SELECT slug FROM post WHERE slug = ?', (field.data,)
        ).fetchone()
        if slug is not None:
            raise ValidationError('Slug exists. This field must be Unique')

    slug = StringField('Slug', validators=[DataRequired(), Regexp(
        regex=r'^[a-zA-Z0-9\-]+$'), Length(max=128)])
    post = TextAreaField('Post Content', validators=[DataRequired()])
