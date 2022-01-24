"""
Blueprint for Menu management
"""
from email.policy import default
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .forms import UpdateMenuForm
from ..auth import login_required
from ....db import get_db, find_or_abort


bp = Blueprint('menu', __name__, url_prefix='/admin/menu')


@bp.route('/')
@login_required
def index():
    db = get_db()
    sql = (
        'SELECT p.id, p.created, p.slug, p.menu_name, p.menu_position, p.menu_visibility, u.user_name'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    )
    menus = db.execute(sql).fetchall()
    return render_template('views/admin/menu/index.html', posts=menus)


@bp.route('/update/<id>', methods=('GET', 'POST'))
@login_required
def update(id):
    form = UpdateMenuForm()
    

    db = get_db()
    menu = db.execute(
        'SELECT p.id, p.created, p.slug, p.menu_name, p.menu_position, p.menu_visibility, u.user_name'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchall()
    
    if len(menu) == 0:
        abort(404)

    form.menu_position.choices = [
        [pp[0], pp[0]] for pp in
        db.execute(
            'SELECT DISTINCT menu_position FROM post order by 1'
        ).fetchall()
    ]
    
    form.menu_visibility.choices = [(1, 'Yes'), (0, 'No')]

    if form.validate_on_submit():
        menu_with_same_position = db.execute(
            'SELECT id FROM post WHERE menu_position = ?',
            (form.menu_position.data,)
        ).fetchone()

        if menu_with_same_position is not None and menu[0]["id"] != menu_with_same_position[0]:
            db.execute(
                'UPDATE post SET menu_position = ? WHERE id = ?',
                (menu[0]["menu_position"], menu_with_same_position[0], )
            )
        db.execute(
            'UPDATE post SET menu_name = ?, menu_position = ?, menu_visibility = ?'
            ' WHERE id = ?',
            (form.menu_name.data, form.menu_position.data,
             form.menu_visibility.data, form.id.data)
        )
        db.commit()
        flash('Menu updated', 'success')
        return redirect(url_for('menu.index', id=form.id.data))



    if request.method == 'GET':
        form.menu_name.data = menu[0]["menu_name"]
        form.menu_position.data = menu[0]["menu_position"]
        form.menu_visibility.data = menu[0]["menu_visibility"]
        form.id.data = menu[0]["id"]
    return render_template('views/admin/menu/update.html', form=form)



#     form.visible.choices = [(1, 'Yes'), (0, 'No')]

#     if form.validate_on_submit():
#         post_with_same_position = db.execute(
#             'SELECT id FROM post WHERE post_position = ?',
#             (form.post_position.data,)
#         ).fetchone()

#         if post_with_same_position is not None and post[0]["id"] != post_with_same_position[0]:
#             db.execute(
#                 'UPDATE post SET post_position = ? WHERE id = ?',
#                 (post[0]["post_position"], post_with_same_position[0], )
#             )
#         db.execute(
#             'UPDATE post SET slug = ?, post_position = ?, visible = ?, post = ?'
#             ' WHERE id = ?',
#             (form.slug.data, form.post_position.data,
#              form.visible.data, form.post.data, form.id.data)
#         )
#         db.commit()
#         return redirect(url_for('menu.index', id=form.id.data))

#     if request.method == 'GET':
#         form.slug.data = post[0]["slug"]
#         form.post_position.data = post[0]["post_position"]
#         form.visible.data = post[0]["visible"]
#         form.post.data = post[0]["post"]
#         form.id.data = post[0]["id"]

    # return render_template('views/admin/menu/update.html', form=form)
