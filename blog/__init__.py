from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from configurations.config import Config

from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = "info"

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from blog.routes.users_routs import users_bp
    from blog.routes.posts_routes import posts_bp
    from blog.routes.main_routes import main_bp
    from blog.errors.handlers import errors

    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors)

    return app
