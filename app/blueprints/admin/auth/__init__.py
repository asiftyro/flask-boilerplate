import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from ....db import get_db
from .forms import LoginForm


bp = Blueprint('auth', __name__, url_prefix='/admin/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if g.user:
        flash("User " + g.user['user_name'] + ' is already logged in.', 'info')
        return redirect(url_for('admin.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE user_name = ?', (username,)
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

    return render_template('views/admin/auth/login.html', form=form)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    # TODO: Refactor register method
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
                    "INSERT INTO user (user_name, password) VALUES (?, ?)",
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
            'SELECT id, user_name, user_type FROM user WHERE id = ?', (user_id,)
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
