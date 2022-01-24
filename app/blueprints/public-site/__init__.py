from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from ...auth import login_required
# from ....db import get_db


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
    # TODO: write public site home

    return render_template('views/public-site/index.html')
