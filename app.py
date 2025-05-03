from models import User
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)


# Step 1 route

@app.route('/', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        # Save data to session or db temporarily
        return redirect(url_for('step2'))
    return render_template('step1.html')

# (More steps will be added later...)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
