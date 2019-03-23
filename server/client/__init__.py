""" Serving the frontend application """
from flask import Blueprint, Flask

CLIENT_BP = Blueprint('client', __name__, static_folder='../../client/build')

RESERVED_PATHS = [
    'favicon.ico',
    'manifest.json',
]

@CLIENT_BP.route('/', defaults={'path': ''})
@CLIENT_BP.route('/<path:path>')
def index(path):
    """ Routing to React app """
    if path in RESERVED_PATHS:
        return CLIENT_BP.send_static_file(path)
    return CLIENT_BP.send_static_file('index.html')


def create_frontend_app():
    """ Returns the frontend app """
    app = Flask(__name__, instance_relative_config=True)
    app.static_folder = '../../client/build/static'
    app.static_url_path = ''

    app.register_blueprint(CLIENT_BP)

    return app
