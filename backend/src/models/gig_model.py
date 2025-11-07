from src.extensions import db
from datetime import datetime

class Gig(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text, nullable = False)
    title = db.Column(db.String(300), nullable = False)
    payment = db.Column(db.Float, nullable = False)
    location = db.Column(db.String(300))
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    applications = db.relationship('Application', backref='gig', lazy=True)
    reviews = db.relationship('Review', backref='gig', lazy=True)
    