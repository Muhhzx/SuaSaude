from extensions import db
from datetime import date



class ConsumoAgua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False, default=date.today)