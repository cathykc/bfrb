""" Model definitions """
from store import DB as db

class Example(db.Model):
    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def serialize(self):
        pass

