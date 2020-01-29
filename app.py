from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
login_manager = LoginManager()
login_manager.init_app(app)

import models
from resources.boards import boards
from resources.users import users
from resources.message import messages
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data = {
            'error': 'User not logged in.'
        },
        status = {
            'code': 401,
            'message': 'You must be logged in to access that resource.'
        }
    )

from resources.users import users
from resources.boards import boards
from resources.message import messages

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(boards, origins=['http://localhost:3000'], supports_credentials=True)
CORS(messages, origins=['http://localhost:3000'], supports_credentials=True)


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(boards, url_prefix='/api/v1/boards')
app.register_blueprint(messages, url_prefix='/api/v1/messages')

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'hi'

DEBUG = True
PORT = 8000
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)