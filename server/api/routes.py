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
