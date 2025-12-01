from flask import request
from src.extensions import db
from src.models.notification_model import Notification


def get_notifications(user_id):
    try:
        # Get all notifications for this user
        notifications = Notification.query.filter_by(user_id=user_id).order_by(
            Notification.created_at.desc()
        ).all()

        return {
            'notifications': [notif.to_dict() for notif in notifications],
            'unread_count': len([n for n in notifications if not n.read_flag])
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500


def get_unread_notifications(user_id):
    try:
        # Get only unread notifications
        notifications = Notification.query.filter_by(
            user_id=user_id,
            read_flag=False
        ).order_by(Notification.created_at.desc()).all()

        return {
            'notifications': [notif.to_dict() for notif in notifications],
            'count': len(notifications)
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500


def mark_as_read(user_id, notif_id):
    try:
        notif = Notification.query.get(notif_id)

        if not notif:
            return {'error': 'Notification not found'}, 404

        # Only owner can mark as read
        if notif.user_id != user_id:
            return {'error': 'Unauthorized'}, 403

        notif.read_flag = True
        db.session.commit()

        return {'message': 'Notification marked as read', 'notification': notif.to_dict()}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def mark_all_as_read(user_id):
    try:
        # Mark all unread notifications as read
        unread = Notification.query.filter_by(user_id=user_id, read_flag=False).all()

        for notif in unread:
            notif.read_flag = True

        db.session.commit()

        return {
            'message': f'Marked {len(unread)} notifications as read',
            'count': len(unread)
        }, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def delete_notification(user_id, notif_id):
    try:
        notif = Notification.query.get(notif_id)

        if not notif:
            return {'error': 'Notification not found'}, 404

        # Only owner can delete
        if notif.user_id != user_id:
            return {'error': 'Unauthorized'}, 403

        db.session.delete(notif)
        db.session.commit()

        return {'message': 'Notification deleted'}, 200

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500

