from flask import Blueprint

#Blueprint - for review-relaed routes
review_blueprint = Blueprint('reviews', __name__)

@review_blueprint.route('/', methods=['GET'])
def list_reviews():
    #Response placeholder
    return {"message": "List reviews endpoint placeholder"}

@review_blueprint.route('/', methods=['POST'])
def create_review():
    #Response placeholder
    return {"message": "Create review endpoint placeholder"}
