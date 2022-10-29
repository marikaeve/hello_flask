from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</<h1>'

@app.route('/home')
def home():
    return '<h1>You are home</<h1>'

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})

# one way to run flask app:
if __name__ == '__main__':
    app.run()

# other way is to run command flask run on command line
# (export FLASK_APP=app.py)