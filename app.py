from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</<h1>'

# one way to run flask app:
if __name__ == '__main__':
    app.run()

# other way is to run command flask run on command line
# (export FLASK_APP=app.py)