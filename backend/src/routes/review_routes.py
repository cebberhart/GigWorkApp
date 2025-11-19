from flask import Blueprint, request
from src.controllers.review_controller import create_review
from src.middleware.auth_middleware import token_required

review_blueprint = Blueprint('reviews', __name__)

@review_blueprint.route('', methods=['POST'])
@token_required
def create_review_route():
    return create_review(request.user_id)