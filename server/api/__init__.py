""" Serving backend application """
import os
from flask import Blueprint, Flask
from store import DB
from api.routes import API_BP

def create_api_app():
    """ Returns the backend app """
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(API_BP)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    return app
