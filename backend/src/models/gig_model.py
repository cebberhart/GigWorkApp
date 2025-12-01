from src.extensions import db
from datetime import datetime


class Gig(db.Model):
    __tablename__ = 'gigs'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    payment = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='open')  # 'open', 'in_progress', 'completed', 'closed'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications = db.relationship('Application', backref='gig', cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref='gig', cascade='all, delete-orphan')

    def to_dict(self, include_applications=False):
        data = {
            'id': self.id,
            'client_id': self.client_id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'payment': self.payment,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'client': self.client.to_dict()
        }
        if include_applications:
            data['applications'] = [app.to_dict() for app in self.applications]
        return data