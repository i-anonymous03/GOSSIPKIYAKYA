from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
import sqlite3
from models import init_db

app = Flask(__name__)
app.secret_key = 'secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Call DB init
init_db()

@app.route('/')
def home():
    return redirect(url_for('signup_step1'))

@app.route('/signup/step1', methods=['GET', 'POST'])
def signup_step1():
    if request.method == 'POST':
        session['full_name'] = request.form['full_name']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm_password'] = request.form['confirm_password']
        return redirect(url_for('signup_step2'))
    return render_template('signup_step1.html')

# signup_step2 and signup_step3 routes will follow next
