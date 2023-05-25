from db import db
from sqlalchemy import TIMESTAMP, CheckConstraint
from sqlalchemy.sql import func


class BatchJobs(db.Model):
    __tablename__ = "batch_jobs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    file_path = db.Column(db.String)
    status = db.Column(db.String)
    created_date = db.Column(TIMESTAMP(timezone=True),
                             nullable=False, server_default=func.now())
    updated_date = db.Column(TIMESTAMP(timezone=True))
    __table_args__ = (
        CheckConstraint(
            status.in_(['in-progress', 'completed']), 
            name='status_check'
        ),
    )