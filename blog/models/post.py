from datetime import datetime
from blog import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_post = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_post}')"