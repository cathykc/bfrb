""" Model definitions """
import datetime

from store import DB as db


class ClientData(db.Model):
    __tablename__ = 'client_data'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String)
    config_id = db.Column(db.String)
    session_id = db.Column(db.Integer)

    prompt_key = db.Column(db.String)
    prompt_text = db.Column(db.String)

    response = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


class ChatState(db.Model):
    __tablename__ = 'chat_state'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String)
    prompt_key = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


class TherapyConfig(db.Model):
    __tablename__ = 'therapy_configs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    config = db.Column(db.JSON)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'config': self.config,
        }
