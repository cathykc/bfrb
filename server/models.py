""" Model definitions """
import datetime

from store import DB as db


class ClientData(db.Model):
    __tablename__ = 'client_data'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String)
    config_id = db.Column(db.String)

    prompt_key = db.Column(db.String)
    prompt_text = db.Column(db.String)

    response = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
