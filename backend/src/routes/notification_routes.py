from flask import Blueprint
from src.controllers.notification_controller import (
    get_notifications,
    get_unread_notifications,
    mark_as_read,
    mark_all_as_read,
    delete_notification
)
from src.middleware.auth_middleware import token_required
from flask import request

notification_blueprint = Blueprint('notifications', __name__)

@notification_blueprint.route('', methods=['GET'])
@token_required
def get_notifications_route():
    return get_notifications(request.user_id)

@notification_blueprint.route('/unread', methods=['GET'])
@token_required
def get_unread_notifications_route():
    return get_unread_notifications(request.user_id)

@notification_blueprint.route('/<int:notif_id>/read', methods=['PUT'])
@token_required
def mark_as_read_route(notif_id):
    return mark_as_read(request.user_id, notif_id)

@notification_blueprint.route('/read-all', methods=['PUT'])
@token_required
def mark_all_as_read_route():
    return mark_all_as_read(request.user_id)

@notification_blueprint.route('/<int:notif_id>', methods=['DELETE'])
@token_required
def delete_notification_route(notif_id):
    return delete_notification(request.user_id, notif_id)