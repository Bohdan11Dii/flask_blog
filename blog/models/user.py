from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer, SignatureExpired, BadSignature
from blog import db, login_manager
from blog import create_app
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    image_file = Column(String(50), nullable=False, default='default.jpg')
    password = Column(String(100), nullable=False)

    post = relationship("Post", backref="author", lazy=True)

    def get_reset_token(self):
        s = Serializer(create_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(create_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expires_sec)
        except SignatureExpired:
            # токен прострочений
            return None
        except BadSignature:
            # токен зламаний або некоректний
            return None
        return User.query.get(data['user_id'])

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
