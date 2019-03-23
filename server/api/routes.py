""" API endpoints """
from flask import Blueprint, jsonify, request
from store import DB as db

API_BP = Blueprint('api', __name__)

@API_BP.route('/')
def hello():
    return "Hello World!"


@API_BP.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@API_BP.route('/fetch_data', methods=['GET'])
def fetch_tasks():
    client_id = request.args.get('client_id')
    return jsonify([
        {
            'client_id': client_id,
            'config_id': 'example_config',
            'prompt': 'What are you doing?',
            'response': 'I biting nails',
        }
    ])
