from extensions import db


class Agua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    data = db.Column(db.String(10))
