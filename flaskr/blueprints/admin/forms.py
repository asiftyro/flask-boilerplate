from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Regexp, Length
from ...db import get_db


class UpdatePostForm(FlaskForm):
    def validate_slug(form, field):
        db = get_db()
        post = db.execute(
            'SELECT id, slug FROM post WHERE slug = ?', (field.data,)
        ).fetchone()
        if post is not None and int(post["id"]) != int(form.data["id"]):
            raise ValidationError('Slug exists. This field must be Unique')

    slug = StringField('Slug', validators=[DataRequired(),
                                           Regexp(regex=r'^[a-zA-Z0-9\-]+$'),
                                           Length(max=128)])
    post_position = SelectField("Position", coerce=int)
    visible = SelectField("Visibility",  coerce=int)
    post = TextAreaField('Post Content', validators=[DataRequired()])
    id = HiddenField()


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
