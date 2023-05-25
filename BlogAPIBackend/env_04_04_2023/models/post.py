from db import db
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func


class PostModel(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    image_path = db.Column(db.String(250), nullable=False)
    filename = db.Column(db.String(250), nullable=False)
    created_date = db.Column(TIMESTAMP(timezone=True),
                             nullable=False, server_default=func.now())

    user = db.relationship('UserModel', backref=db.backref('post', lazy=True))

    def __repr__(self):
        return '<Title %r>' % self.title
