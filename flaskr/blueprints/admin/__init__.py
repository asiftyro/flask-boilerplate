from email.policy import default
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .forms import CreatePostForm
from ..auth import login_required
from ...db import get_db


bp = Blueprint('admin', __name__, url_prefix='/admin')

# TODO: write admin/ backend


@bp.route('/')
@login_required
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('views/admin/index.html')

# TODO: write admin/post backend


@bp.route('/post', defaults={'id': None})
@bp.route('/post/<id>')
@login_required
def post_index(id):
    db = get_db()
    posts = db.execute(
        'SELECT p.id, p.created, p.slug, p.visible, p.post_position, p.menu_name, p.menu_position, p.menu_visibility, u.username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('views/admin/post/index.html', posts=posts)

# TODO:FIX : write admin/post/create backend


@bp.route('/post/create', methods=('GET', 'POST'))
@login_required
def post_create():
    form = CreatePostForm()
    if form.validate_on_submit():
        slug = form.slug.data
        post = form.post.data
        db = get_db()
        db.execute(
            'INSERT INTO post (slug, post, author_id)'
            ' VALUES (?, ?, ?)',
            (slug, post, g.user['id'])
        )
        db.commit()
        return redirect(url_for('admin.post_index'))
    return render_template('views/admin/post/create.html', form=form)

# TODO: write admin/post/update backend


@bp.route('/post/update/<id>')
@login_required
def post_update(id):
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('views/admin/post/update.html', posts=posts)

# TODO: write admin/post/delete backend


@bp.route('/post/delete')
@login_required
def post_delete():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('views/admin/post/delete.html')
