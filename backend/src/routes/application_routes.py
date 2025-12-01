from flask import Blueprint, request
from src.controllers.application_controller import (
    create_application,
    get_applications,
    get_application,
    update_application,
    delete_application,
)
from src.middleware.auth_middleware import token_required

application_blueprint = Blueprint('applications', __name__)

@application_blueprint.route('', methods=['POST'])
@token_required
def create_application_route():
    return create_application(request.user_id)

@application_blueprint.route('', methods=['GET'])
@token_required
def get_applications_route():
    return get_applications(request.user_id)

@application_blueprint.route('/<int:app_id>', methods=['GET'])
@token_required
def get_application_route(app_id):
    return get_application(request.user_id, app_id)

@application_blueprint.route('/<int:app_id>', methods=['PUT'])
@token_required
def update_application_route(app_id):
    return update_application(request.user_id, app_id)

@application_blueprint.route('/<int:app_id>', methods=['DELETE'])
@token_required
def delete_application_route(app_id):
    return delete_application(request.user_id, app_id)

