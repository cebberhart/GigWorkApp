from flask import request, jsonify
from src.extensions import db
from src.models.user_model import User
import jwt
import os
from datetime import datetime, timedelta

JWT_SECRET = os.getenv('JWT_SECRET', 'verysecretkey')


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def register():
    try:
        data = request.get_json()

        # Validation
        if not data.get('email') or not data.get('password') or not data.get('name') or not data.get('role'):
            return {'error': 'Missing required fields: name, email, password, role'}, 400

        if User.query.filter_by(email=data['email']).first():
            return {'error': 'Email already exists'}, 409

        if len(data['password']) < 6:
            return {'error': 'Password must be at least 6 characters'}, 400

        if data['role'] not in ['client', 'worker']:
            return {'error': 'Role must be "client" or "worker"'}, 400

        # Create user
        user = User(
            name=data['name'],
            email=data['email'],
            role=data['role']
        )
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()

        token = generate_token(user.id)

        return {
            'message': 'User registered successfully',
            'user': user.to_dict(),
            'token': token
        }, 201

    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500


def login():
    try:
        data = request.get_json()

        if not data.get('email') or not data.get('password'):
            return {'error': 'Email and password required'}, 400

        user = User.query.filter_by(email=data['email']).first()

        if not user or not user.check_password(data['password']):
            return {'error': 'Invalid email or password'}, 401

        token = generate_token(user.id)

        return {
            'message': 'Login successful',
            'user': user.to_dict(),
            'token': token
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500