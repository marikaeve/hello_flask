from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return f'<h1>Hello {name}, you are on the home page</h1>'


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})


@app.route('/query')
def query():
    # example:
    # /query?name=sara&location=Florida
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hi {name}. You are from {location}. You are on the query page! </h1>'


# one way to run flask app:
if __name__ == '__main__':
    app.run(debug=True)

# other way is to run command flask run on command line
# (export FLASK_APP=app.py)