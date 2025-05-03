# Flask app entry point

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Gossip Kiya Kya!'

if __name__ == '__main__':
    app.run(debug=True)