from db import db
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func


class FollowerModel(db.Model):
    __tablename__ = "follower"

    id = db.Column(db.Integer, primary_key=True)
    leader_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    follower_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_date = db.Column(TIMESTAMP(timezone=True),
                             nullable=False, server_default=func.now())
    following = db.Column(db.Boolean, default=False, nullable=False)
    block = db.Column(db.Boolean, default=False, nullable=False)
    updated_date = db.Column(TIMESTAMP(timezone=True))

    __table_args__ = (db.UniqueConstraint('leader_user_id', 'follower_user_id'),)
