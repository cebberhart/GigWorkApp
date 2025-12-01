from src.extensions import db
from datetime import datetime


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'application_received', 'application_accepted', etc.
    payload = db.Column(db.JSON)  # Extra data (gig_id, worker_name, etc.)
    read_flag = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.type,
            'payload': self.payload,
            'read_flag': self.read_flag,
            'created_at': self.created_at.isoformat()
        }

