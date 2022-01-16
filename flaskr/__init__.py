import os, sys
from flask import Flask, render_template


from flask_bootstrap import Bootstrap4
bootstrap = Bootstrap4()
        

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('views/error/404.html')

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

    bootstrap.init_app(app)

    from . import db
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Ello, Wald! Enjoy!'

    from . import auth
    app.register_blueprint(auth.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)

    from . import admin
    app.register_blueprint(admin.bp)
    


    return app
