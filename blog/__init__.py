from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f1933f4bb571854a19f6624cd7991ff1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

# # 🔑 імпортуй моделі ТУТ, щоб вони зареєструвалися в metadata
# from blog.models.user import User
# from blog.models.post import Post

# імпортуємо та реєструємо блупринти
from blog.routes import blog_routes



