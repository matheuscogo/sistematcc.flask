from ...db import db
from .Plano import Plano

class Dias(db.Model):
    __tablename__ = "dias"
    id = db.Column("id", db.Integer, primary_key=True)
    plano = db.Column(db.Integer, db.ForeignKey("planos.id"))
    # plano_relation = db.relationship(Plano)
    dia = db.Column("dia", db.Integer)
    quantidade = db.Column("quantidade", db.Integer)  


    def __repr__(self):
        return '<Dias {}>'.format(self.dias)