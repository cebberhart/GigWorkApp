from flask import Blueprint

gig_blueprint = Blueprint('gigs', __name__)

@gig_blueprint.route('/', methods=['GET'])
def list_gigs():
    #Response placeholder
    return {"message": "List gigs endpoint placeholder"}

@gig_blueprint.route('/', methods=['POST'])
def create_gig():
    #Response placeholder
    return {"message": "Create gig endpoint placeholder"}

