# models.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT,
        password TEXT,
        phone TEXT,
        dob TEXT,
        gender TEXT,
        username TEXT,
        profile_pic TEXT,
        address TEXT,
        country TEXT,
        language TEXT,
        security_question TEXT,
        security_answer TEXT,
        referral_code TEXT
    )''')
    conn.commit()
    conn.close()
