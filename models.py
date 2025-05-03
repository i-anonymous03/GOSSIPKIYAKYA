from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    security_question = db.Column(db.String(200))
    security_answer = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    address = db.Column(db.String(200))
    country = db.Column(db.String(100))
    language = db.Column(db.String(50))
    profile_pic = db.Column(db.String(200))
    referral_code = db.Column(db.String(100))
    terms_accepted = db.Column(db.Boolean, default=False)
