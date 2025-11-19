from flask import request
from src.extensions import db
from src.models.review_model import Review
from src.models.gig_model import Gig
from src.models.user_model import User


def create_review(user_id):
    try:
        data = request.get_json()
        user = User.query.get(user_id)

        if user.role != 'client':
            return {'error': 'Only clients can leave reviews'}, 403

        if not data.get('gig_id') or not data.get('rating'):
            return {'error': 'gig_id and rating required'}, 400

        if not 1 <= data['rating'] <= 5:
            return {'error': 'Rating must be between 1 and 5'}, 400

        gig = Gig.query.get(data['gig_id'])
        if not gig or gig.client_id != user_id:
            return {'error': 'Unauthorized or gig not found'}, 404

        review = Review(
            gig_id=data['gig_id'],
            reviewer_id=user_id,
            rating=data['rating'],
            text=data.get('text', '')
        )

        db.session.add(review)
        db.session.commit()

        return {'message': 'Review created', 'review': review.to_dict()}, 201

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500