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
    return jsonify({
        'session_id': 1,
        'data': [
            {
                'key': "site",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "strength_urges",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "awareness",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "strength_resist",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "severity",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            {
                'key': "thoughs",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
        ]
    })
