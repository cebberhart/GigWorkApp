from src.extensions import db
#Placeholder User model - represents database table

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    role = db.Column(db.String(50), nullable = False)

#SQLAlchemy maps Python classes to db tables
#primary_key = true -> automatically increments/uniquesly identifies users
#nullable = false -> cannot be left empty
#unique = True -> prevents duplicate emails
#SQLAlchemy automatically generates SQL behind the scenes