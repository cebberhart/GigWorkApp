from flask import request
from src.extensions import db
from src.models.application_model import Application
from src.models.gig_model import Gig
from src.models.user_model import User


def create_application(user_id):
    try:
        data = request.get_json()
        user = User.query.get(user_id)

        # Only workers can apply
        if user.role != 'worker':
            return {'error': 'Only workers can apply for gigs'}, 403

        if not data.get('gig_id'):
            return {'error': 'gig_id required'}, 400

        gig = Gig.query.get(data['gig_id'])
        if not gig:
            return {'error': 'Gig not found'}, 404

        # Check if already applied
        existing = Application.query.filter_by(gig_id=data['gig_id'], worker_id=user_id).first()
        if existing:
            return {'error': 'Already applied to this gig'}, 409

        application = Application(
            gig_id=data['gig_id'],
            worker_id=user_id,
            message=data.get('message', '')
        )

        db.session.add(application)
        db.session.commit()

        return {'message': 'Application submitted', 'application': application.to_dict()}, 201

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def get_applications(user_id):
    try:
        user = User.query.get(user_id)

        # Workers see their own applications
        if user.role == 'worker':
            applications = Application.query.filter_by(worker_id=user_id).all()

        # Clients see applications on their gigs
        elif user.role == 'client':
            client_gigs = Gig.query.filter_by(client_id=user_id).all()
            gig_ids = [gig.id for gig in client_gigs]
            applications = Application.query.filter(Application.gig_id.in_(gig_ids)).all()

        else:
            return {'error': 'Unauthorized'}, 403

        return {
            'applications': [app.to_dict() for app in applications]
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500


def get_application(user_id, app_id):
    try:
        app = Application.query.get(app_id)

        if not app:
            return {'error': 'Application not found'}, 404

        # Worker can view their own application
        if app.worker_id != user_id and app.gig.client_id != user_id:
            return {'error': 'Unauthorized'}, 403

        return app.to_dict(), 200

    except Exception as e:
        return {'error': str(e)}, 500


def update_application(user_id, app_id):
    try:
        app = Application.query.get(app_id)

        if not app:
            return {'error': 'Application not found'}, 404

        # Only gig owner (client) can update
        if app.gig.client_id != user_id:
            return {'error': 'Unauthorized'}, 403

        data = request.get_json()

        if 'status' in data and data['status'] in ['accepted', 'rejected', 'completed']:
            app.status = data['status']

        db.session.commit()

        return {'message': 'Application updated', 'application': app.to_dict()}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def delete_application(user_id, app_id):
    try:
        app = Application.query.get(app_id)

        if not app:
            return {'error': 'Application not found'}, 404

        # Worker can delete their own application, or client can delete from their gig
        if app.worker_id != user_id and app.gig.client_id != user_id:
            return {'error': 'Unauthorized'}, 403

        db.session.delete(app)
        db.session.commit()

        return {'message': 'Application deleted'}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500