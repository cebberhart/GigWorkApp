#Import Flask & blueprint objects from route files
#Import blueprints (modules that organize routes by functionality)
#Import database URL and secret key from config.py
from flask import Flask, render_template
from config.config import DATABASE_URL, SECRET_KEY
from src.extensions import db
from src.routes.auth_routes import auth_blueprint
from src.routes.gig_routes import gig_blueprint
from src.routes.review_routes import review_blueprint

#Create Flask app instance
#Creates Flask web server
#__name__ - special Python variable that represents the current files name
#Flask uses __name__ to know where to look for templates and static files
app = Flask(__name__)

#Used to load configuration settings from config.py
#silent = True - prevents errors if config.py incomplete (or missing)
#This is where app-wide settings are stord - any part of app can access app.config
app.config.from_pyfile('../config/config.py', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL #Tells SQLAlchemy which database to connect to
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Saves memory - dont need to track every change in the ORM
app.config['SECRET_KEY'] = SECRET_KEY #Used to sign JWTs and session data

#Initialize SQLAlchemy with app to handle database operations
#init_app(app) links database object to Flask app
#Sort of like pluggin in database into Flask engine
db.init_app(app)

#Register blueprints for different modules
#Note: blueprints help organize routes into separate files/modules
#URL prefixes mean /auth/register maps to auth_routes.py, /gigs/ mapes to gig_routes.py, etc
app.register_blueprint(auth_blueprint, url_prefix='/auth') 
app.register_blueprint(review_blueprint, url_prefix='/reviews')
app.register_blueprint(gig_blueprint, url_prefix='/gigs')

#Decorator - tells Flask "when someone visits /, run function below"
#Any routes should have function decorator
@app.route('/')
def home():
    return {"message": "Backend is running!"}

#Test HTML page
#Decorator - works same as above
@app.route('/test')
def test_page():
    return render_template('test_backend.html')

#/ route - simple JSON to check the backend is running
#/test route - serves HTML page to visually test backend

#Run Flask server if executed directly
#db.create_all() - reads SQLAlchemy models and creates tables in database
#app.run(debug=True) - starts the server - debug mode gives live reloads and detailed error pages
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)


#Flask app (app) -> main engine which serves web app
#Blueprints -> organize routes like /auth, /gigs, etc
#Database (db) -> handles data storage using SQLAlchemy
#Routes - map URLs to functions (API endpoints)
#Test page - allows to visually interact with backend
#JWT/Secret key - secure routes