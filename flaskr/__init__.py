import os, sys
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_wtf.csrf import CSRFProtect
from importlib import import_module
import time

# print(time.strftime('%Y-%m-%d %H:%M:%S')) # before timezone change
os.environ['TZ'] = 'Asia/Dhaka' # set new timezone
time.tzset()
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # after timezone change

csrf = CSRFProtect()
bootstrap = Bootstrap4()
        

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        BOOTSTRAP_SERVE_LOCAL=True,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    csrf.init_app(app)
    bootstrap.init_app(app)

    from . import db
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('views/error/404.html')

    @app.route('/')
    def hello():
        return 'Ello, Wald! Enjoy!'

    # import and register blueprints
    root_dir = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    for module_name in ('auth', 'admin'):
        module = import_module('{}.blueprints.{}'.format(root_dir, module_name))
        app.register_blueprint(module.bp)
    
    return app
