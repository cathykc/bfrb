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


@API_BP.route('/webhook_fb', methods=['POST'])
def webhook_fb():
    req_data = request.get_json()
    print(req_data)

    mode = req_data['hub.mode']
    token = req_data['hub.verify_token'];
    challenge = req_data['hub.challenge'];

    VERIFY_TOKEN = "<YOUR_VERIFY_TOKEN>"

    if (mode and token):
        if (mode == 'subscribe' and token == VERIFY_TOKEN):
            return challenge, 200
        else:
            return {}, 403

    return {}, 403


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
