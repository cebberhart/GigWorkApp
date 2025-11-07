from src.extensions import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    worker_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    gig_id = db.Column(db.Integer, db.ForeignKey('gig.id'), nullable = False)
    status = db.Column(db.String(50), default = 'Pending')

# Pending, Accepted, Rejected