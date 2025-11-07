from flask import Blueprint, request, current_app
from src.controllers.auth_controller import register_user, login_user
from src.extensions import db

#Blueprint for authentication routes
auth_blueprint = Blueprint('auth', __name__)

#request.json parses JSON body sent by client
#Calls register_user() from the controller
#Response returned to client (browser/fetch)
@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data, db)

#Similar but login returns JWT if credentials are correct
@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    secret_key = current_app.config['SECRET_KEY']
    return login_user(data, db, secret_key)



