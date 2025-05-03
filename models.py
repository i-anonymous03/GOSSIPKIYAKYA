from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a SQLAlchemy object
db = SQLAlchemy()

# Define a User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID (auto-generated)
    
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    
    profile_pic = db.Column(db.String(100))  # We'll store image filename here
    address = db.Column(db.String(200))
    country = db.Column(db.String(50))
    language = db.Column(db.String(50))
    
    security_question = db.Column(db.String(150))
    security_answer = db.Column(db.String(150))
    referral_code = db.Column(db.String(50))
    
    terms_accepted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
