from flask import request
from src.extensions import db
from src.models.gig_model import Gig
from src.models.user_model import User


def create_gig(user_id):
    try:
        data = request.get_json()
        user = User.query.get(user_id)

        if user.role != 'client':
            return {'error': 'Only clients can post gigs'}, 403

        if not data.get('title') or not data.get('description') or not data.get('location') or not data.get('payment'):
            return {'error': 'Missing required fields'}, 400

        gig = Gig(
            client_id=user_id,
            title=data['title'],
            description=data['description'],
            location=data['location'],
            payment=data['payment']
        )

        db.session.add(gig)
        db.session.commit()

        return {'message': 'Gig created successfully', 'gig': gig.to_dict()}, 201

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def get_gigs():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 20

        query = Gig.query.filter_by(status='open')

        location = request.args.get('location')
        if location:
            query = query.filter_by(location=location)

        payment_min = request.args.get('payment_min', type=float)
        if payment_min:
            query = query.filter(Gig.payment >= payment_min)

        gigs = query.paginate(page=page, per_page=per_page)

        return {
            'gigs': [gig.to_dict() for gig in gigs.items],
            'total': gigs.total,
            'pages': gigs.pages,
            'current_page': page
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500


def get_gig(gig_id):
    try:
        gig = Gig.query.get(gig_id)

        if not gig:
            return {'error': 'Gig not found'}, 404

        return gig.to_dict(include_applications=True), 200

    except Exception as e:
        return {'error': str(e)}, 500


def update_gig(user_id, gig_id):
    try:
        gig = Gig.query.get(gig_id)

        if not gig:
            return {'error': 'Gig not found'}, 404

        if gig.client_id != user_id:
            return {'error': 'Unauthorized'}, 403

        data = request.get_json()

        if 'title' in data:
            gig.title = data['title']
        if 'description' in data:
            gig.description = data['description']
        if 'location' in data:
            gig.location = data['location']
        if 'payment' in data:
            gig.payment = data['payment']
        if 'status' in data:
            gig.status = data['status']

        db.session.commit()

        return {'message': 'Gig updated', 'gig': gig.to_dict()}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def delete_gig(user_id, gig_id):
    try:
        gig = Gig.query.get(gig_id)

        if not gig:
            return {'error': 'Gig not found'}, 404

        if gig.client_id != user_id:
            return {'error': 'Unauthorized'}, 403

        gig.status = 'closed'
        db.session.commit()

        return {'message': 'Gig deleted'}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500