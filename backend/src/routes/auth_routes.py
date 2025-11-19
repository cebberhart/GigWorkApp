from flask import Blueprint
from src.controllers.auth_controller import register, login

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register_route():
    return register()

@auth_blueprint.route('/login', methods=['POST'])
def login_route():
    return login()



