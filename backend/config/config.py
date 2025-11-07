import os

#Configuration settings for Flask app
#Can add more settings later - ie, SECRET_KEY, etc for authentication

#Database URI
DATABASE_URL = 'sqlite:///gigapp.db'

#Flask secret key for JWT signing
SECRET_KEY = os.environ.get("JWT_SECRET", "verysecretkey")

#Debug Mode (should be True during development)
DEBUG = True