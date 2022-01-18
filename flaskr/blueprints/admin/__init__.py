from email.policy import default
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .forms import CreatePostForm, UpdatePostForm
from ..auth import login_required
from ...db import get_db


bp = Blueprint('admin', __name__, url_prefix='/admin')

# TODO: write admin/ backend
@bp.route('/')
@login_required
def index():
    return render_template('views/admin/index.html')


@bp.route('/post', defaults={'id': None})
@bp.route('/post/<id>')
@login_required
def post_index(id):
    db = get_db()
    if id is None:
        posts = db.execute(
            'SELECT p.id, p.created, p.slug, p.visible, p.post_position, p.menu_name, p.menu_position, p.menu_visibility, u.username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
        return render_template('views/admin/post/index.html', posts=posts)
    else:
        post = db.execute(
            'SELECT p.id, p.created, p.slug, p.visible, p.post_position, p.menu_name, p.menu_position, p.menu_visibility, u.username, p.post'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' WHERE p.id = ?',
            (id,)
        ).fetchall()
        if len(post) == 0:
            abort(404)
        return render_template('views/admin/post/view.html', post=post[0])


@bp.route('/post/create', methods=('GET', 'POST'))
@login_required
def post_create():
    form = CreatePostForm()
    if form.validate_on_submit():
        slug = form.slug.data
        post = form.post.data
        db = get_db()
        row = db.execute(
            'SELECT MAX(post_position) FROM post'
        ).fetchone()
        new_post_position = 1 if row[0] is None else row[0] + 1
        cur = db.execute(
            'INSERT INTO post (slug, post, author_id, post_position)'
            ' VALUES (?, ?, ?, ?)',
            (slug, post, g.user['id'], new_post_position)
        )
        db.commit()
        return redirect(url_for('admin.post_index', id=cur.lastrowid))
    return render_template('views/admin/post/create.html', form=form)


@bp.route('/post/update/<id>', methods=('GET', 'POST'))
@login_required
def post_update(id):
    db = get_db()
    post = db.execute(
        'SELECT p.id, p.created, p.slug, p.visible, p.post_position, p.menu_name, p.menu_position, p.menu_visibility, u.username, p.post'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchall()
    if len(post) == 0:
        abort(404)

    form = UpdatePostForm()
    form.post_position.choices = [
        [pp[0], pp[0]] for pp in
        db.execute(
            'SELECT DISTINCT post_position FROM post order by 1'
        ).fetchall()
    ]
    form.visible.choices = [(1, 'Yes'), (0, 'No')]
    
    if form.validate_on_submit():
        post_with_same_position = db.execute(
            'SELECT id FROM post WHERE post_position = ?',
            (form.post_position.data,)
        ).fetchone()

        if post_with_same_position is not None and post[0]["id"]!=post_with_same_position[0]: 
            db.execute(
                'UPDATE post SET post_position = ? WHERE id = ?',
                (post[0]["post_position"], post_with_same_position[0], )
            )
        db.execute(
            'UPDATE post SET slug = ?, post_position = ?, visible = ?, post = ?'
            ' WHERE id = ?',
            (form.slug.data, form.post_position.data, form.visible.data, form.post.data, form.id.data)
        )
        db.commit()
        return redirect(url_for('admin.post_index',id=form.id.data))

    if request.method == 'GET':
        form.slug.data = post[0]["slug"]
        form.post_position.data = post[0]["post_position"]
        form.visible.data = post[0]["visible"]
        form.post.data = post[0]["post"]
        form.id.data = post[0]["id"]

    return render_template('views/admin/post/update.html', form=form)
