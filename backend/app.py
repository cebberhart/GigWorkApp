from flask_cors import CORS
from flask import Flask, render_template
from config.config import DATABASE_URL, SECRET_KEY
from src.extensions import db
from src.routes.application_routes import application_blueprint
from src.models.notification_model import Notification
from src.routes.notification_routes import notification_blueprint
from src.middleware.auth_middleware import token_required

# Import all models FIRST (before routes)
from src.models.user_model import User
from src.models.gig_model import Gig
from src.models.application_model import Application
from src.models.review_model import Review

# Import blueprints
from src.routes.auth_routes import auth_blueprint
from src.routes.gig_routes import gig_blueprint
from src.routes.review_routes import review_blueprint

# Create Flask app instance
app = Flask(__name__)
CORS(app)

# Configuration
app.config.from_pyfile('../config/config.py', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize SQLAlchemy
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth') 
app.register_blueprint(review_blueprint, url_prefix='/reviews')
app.register_blueprint(gig_blueprint, url_prefix='/gigs')
app.register_blueprint(application_blueprint, url_prefix='/applications')
app.register_blueprint(notification_blueprint, url_prefix='/notifications')

# ===== PAGE ROUTES =====

@app.route('/')
def home():
    return render_template('GWIndex.html')

@app.route('/test')
def test_page():
    return render_template('test_backend.html')

@app.route('/login')
def login_page():
    return render_template('GWLogin.html')

@app.route('/register')
def register_page():
    return render_template('GWRegister.html')

@app.route('/role')
def role_page():
    return render_template('GWRole.html')

@app.route('/dash')
def dash_page():
    return render_template('GWDash.html')

@app.route('/worker-dash')
def worker_dash_page():
    return render_template('GWWorkerDash.html')

@app.route('/viewapp')
def view_app_page():
    return render_template('GWViewApp.html')

@app.route('/post-gig')
def post_gig_page():
    return render_template('GWPostGig.html')

@app.route('/profile')
def profile_page():
    return render_template('GWProfile.html')

@app.route('/available')
def available_page():
    return render_template('GWAvailable.html')

@app.route('/apply')
def apply_page():
    return render_template('GWApply.html')

@app.route('/my-posted-gigs')
def my_posted_gigs_page():
    return render_template('GWMyPostedGigs.html')

@app.route('/worker-my-apps')
def worker_my_apps_page():
    return render_template('GWWorkerMyApps.html')

@app.route('/gig-details')
def gig_details_page():
    return render_template('GWGigDetails.html')

@app.route('/complete')
def complete_page():
    return render_template('GWAppComplete.html')

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)