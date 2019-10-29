from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    # creating app configurations
    app.config.get_config_option("sqlalchemy.url")
    app.config['SECRET_KEY'] = '12345'

    # configure UploadSet


    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering the auth Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    return app
