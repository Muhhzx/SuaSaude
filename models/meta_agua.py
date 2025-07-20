from extensions import db


class   MetaAgua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meta = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False, unique=True)

