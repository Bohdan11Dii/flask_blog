from flask_login import UserMixin

from blog import db, login_manager
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

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


