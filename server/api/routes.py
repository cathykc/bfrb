""" API endpoints """
from flask import Blueprint, jsonify, request
from models import TherapyConfig
from store import DB as db

from messenger.handler import handleMessage

API_BP = Blueprint('api', __name__)

@API_BP.route('/')
def hello():
    return "Hello World!"


@API_BP.route('/webhook_fb')
def webhook_fb_verification():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    VERIFY_TOKEN = "this_is_a_token"

    if (mode and token):
        if (mode == 'subscribe' and token == VERIFY_TOKEN):
            return challenge, 200
        else:
            return {}, 403

    return {}, 403


@API_BP.route('/webhook_fb', methods=['POST'])
def webhook_fb():
    req_data = request.get_json()
    print(req_data)
    if (req_data['object'] == 'page'):
        for entry in req_data['entry']:
            webhook_event = entry['messaging'][0];
            qr_payload = None
            if 'quick_reply' in webhook_event['message']:
                qr_payload = webhook_event['message']['quick_reply']['payload']
            handleMessage(webhook_event['sender']['id'], webhook_event['message']['text'], qr_payload)

    return "", 200


@API_BP.route('/get_configs')
def get_configs():
    configs = TherapyConfig.query.all()
    return jsonify([config.serialize() for config in configs])


@API_BP.route('/update_config', methods=['POST'])
def update_config():
    req_data = request.get_json()
    name = req_data['name']
    config = req_data['config']


    config = TherapyConfig.query.filter(TherapyConfig.id == req_data['id']).first()
    if config:
        config.name = name
        config.config = config
    else:
        config = TherapyConfig(name, config)
        db.session.add(config)
    db.session.commit()

    return jsonify(config.serialize())


@API_BP.route('/fetch_data', methods=['GET'])
def fetch_tasks():
    client_id = request.args.get('client_id')
    return jsonify({
        'session_id': 1,
        'data': [
            # What area of your body were you picking? (Quick response)
            # response choices:
            # - Scalp
            # - Brows
            # - Lashes
            # - Public
            # - Other
            {
                'key': "site",
                'question_text': "Where did you ",
                'answer': "Nails",
                'timestamp': ""
            },
            # Where or what were you doing? (Quick response)
            # response choices:
            # - Work
            # - School
            # - Bedroom
            # - Bathroom
            # - Other
            {
                'key': "context",
                'question_text': "",
                'answer': "SCHOOL",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
                        {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },
                        {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "HOME",
                'timestamp': ""
            },
            {
                'key': "context",
                'question_text': "",
                'answer': "WORK",
                'timestamp': ""
            },

            # How strong was your urge? 
            # response choice: 1-10 (Int)
            {
                'key': "strength_of_urge",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            # At what point did you notice? (quick question)
            # response choice:
            # - Before
            # - During
            # - After
            {
                'key': "awareness",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            # How much willpower did you have to resist? 
            # response choice: 1-10 (Int)
            {
                'key': "strength_resist",
                'question_text': "IM A QEUSTION",
                'answer': "IM AN ANSWER",
                'timestamp': ""
            },
            # How many times did you (ie pull you hair)? 
            # response choice: 0-Infinity (Int)
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
