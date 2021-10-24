from ...db import db
from .Confinamento import association_table

class Registro(db.Model):
    __tablename__ = "registros"
    id = db.Column("id", db.Integer, primary_key=True)
    matriz = db.Column(db.Integer, db.ForeignKey("confinamento.matriz"))
    dataEntrada = db.Column("dataEntrada", db.VARCHAR)
    dataSaida = db.Column("dataSaida", db.VARCHAR)
    horaEntrada = db.Column("horaEntrada", db.VARCHAR)
    horaSaida = db.Column("horaSaida", db.VARCHAR)
    tempo = db.Column("tempo", db.VARCHAR)
    quantidade = db.Column("quantidade", db.Integer)
    
    def __repr__(self):
        return '<Registro {}>'.format(self.matriz)
