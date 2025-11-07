from src.extensions import db
from datetime import datetime

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gig_id = db.Column(db.Integer, db.ForeignKey('gig.id'), nullable = False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    