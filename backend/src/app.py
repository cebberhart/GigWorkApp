#Import Flask & blueprint objects from route files
from flask import Flask
from routes.auth_routes import auth_blueprint
from routes.gig_routes import gig_blueprint
from routes.review_routes import review_blueprint

#Create Flask app instance
app = Flask(__name__)

#Used to load configuration settings from config.py
#silent = True - prevents errors if config.py incomplete (or missing)
app.config.from_pyfile('../config/config.py', silent=True)

#Register blueprints for different modules
#Note: blueprints help organize routes into separate files/modules
app.register_blueprint(auth_blueprint, url_prefix='/auth') 
app.register_blueprint(review_blueprint, url_prefix='/reviews')
app.register_blueprint(gig_blueprint, url_prefix='/gigs')

@app.route('/')
def home():
    return {"message": "Backend is running!"}

#Run Flask server if executed directly
if __name__ == '__main__':
    app.run(debug = True)


