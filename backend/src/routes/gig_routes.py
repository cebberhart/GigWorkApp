from flask import Blueprint, request
from src.controllers.gig_controller import create_gig, get_gigs, get_gig, update_gig, delete_gig
from src.middleware.auth_middleware import token_required

gig_blueprint = Blueprint('gigs', __name__)

@gig_blueprint.route('', methods=['POST'])
@token_required
def create_gig_route():
    return create_gig(request.user_id)

@gig_blueprint.route('', methods=['GET'])
def get_gigs_route():
    return get_gigs()

@gig_blueprint.route('/<int:gig_id>', methods=['GET'])
def get_gig_route(gig_id):
    return get_gig(gig_id)

@gig_blueprint.route('/<int:gig_id>', methods=['PUT'])
@token_required
def update_gig_route(gig_id):
    return update_gig(request.user_id, gig_id)

@gig_blueprint.route('/<int:gig_id>', methods=['DELETE'])
@token_required
def delete_gig_route(gig_id):
    return delete_gig(request.user_id, gig_id)