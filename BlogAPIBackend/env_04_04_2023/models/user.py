from sqlalchemy import TIMESTAMP, func

from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    subname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    image_path = db.Column(db.String(256), nullable=True)
    created_date = db.Column(TIMESTAMP(timezone=True),
                             nullable=False, server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username
