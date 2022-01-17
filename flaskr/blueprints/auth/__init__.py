import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import ValidationError, DataRequired
from flaskr.db import get_db


class LoginForm(FlaskForm):
    # TODO Set validation rule for username
    def validate_username(form, field):
        if len(field.data) < 4:
            raise ValidationError('Email Address must be atleast 4 char long.')
    username = EmailField('Email Address', validators=[DataRequired()])
    # TODO Set validation rule for password

    def validate_password(form, field):
        if len(field.data) < 3:
            raise ValidationError('Password must be atleast 4 char long.')
    password = PasswordField('Password', validators=[DataRequired()])


bp = Blueprint('auth', __name__, url_prefix='/admin/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # TODO: Push error in WTForms validation
        if user is None:
            error = 'Incorrect email address.'
            form.username.errors.append(error)
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
            form.password.errors.append(error)

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            flash('Login Successful', 'success')
            return redirect(url_for('admin.index'))

        flash(error, 'danger')

    return render_template('views/auth/login.html', form=form)

# TODO: Refactor register method
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error, 'danger')

    return render_template('views/auth/register.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
