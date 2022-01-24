from distutils.debug import DEBUG
import os
import sys
from flask import Flask, render_template, g, current_app
from flask_bootstrap import Bootstrap4
from flask_wtf.csrf import CSRFProtect
from importlib import import_module
import time


csrf = CSRFProtect()
bootstrap = Bootstrap4()


def handler_404():
    with current_app.app_context():
        if hasattr(g, 'user') and getattr(g, 'user')[2] == 'ADMIN':
            return render_template('views/public-site/error/404.html')
        else:
            return render_template('views/admin/error/404.html')


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    root_dir = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

    app.config.from_mapping(
        # 'ENV': 'development', 'DEBUG': True, 'TESTING': False,
        # FLASK_ENV='development',
        # DEBUG=True,
        # FLASK_DEBUG=True,
        
        ROOT_PATH=os.path.basename(os.path.dirname(os.path.abspath(__file__))),
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite3'),
        TIMEZONE='Asia/Dhaka',
        BOOTSTRAP_SERVE_LOCAL=True,
        SITE_NAME='BoilerXL'
    )

    app.config.from_pyfile('config.py', silent=True)

    csrf.init_app(app)
    bootstrap.init_app(app)

    from . import db
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return handler_404()

    # import and register blueprints
    for module_name in ['admin.auth', 'admin.index', 'admin.post', 'admin.menu', 'public-site']:
        module = import_module(
            '{}.blueprints.{}'.format(root_dir, module_name)
        )
        app.register_blueprint(module.bp)

    return app
