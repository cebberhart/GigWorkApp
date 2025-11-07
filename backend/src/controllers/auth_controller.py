from src.models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

def register_user(data, db):
    if User.query.filter_by(email=data['email']).first():
        return {"message": "Email already registered"}, 400
    
    hashed_pw = generate_password_hash(data['password'])
    user = User(email=data['email'], password=hashed_pw, role=data.get('role', 'Client'))
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully"}, 201

def login_user(data, db, secret_key):
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return {"message": "Invalid email or password"}, 401
    
    token = jwt.encode(
        {"user_id": user.id, "exp": datetime.utcnow() + timedelta(hours = 24)},
        secret_key,
        algorithm = "HS256"
    )
    return {"token": token, "user": {"id": user.id, "email": user.email, "role": user.role}}, 200