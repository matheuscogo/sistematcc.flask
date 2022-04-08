from ...db import db, ma
from sqlalchemy.orm import relationship
from .Matriz import Matriz

class Inseminacao(db.Model):
    __tablename__ = "inseminacao"
    id = db.Column("id", db.Integer, primary_key=True)
    planoId = db.Column(db.Integer, db.ForeignKey("planos.id"))
    matrizId = db.Column(db.Integer, db.ForeignKey("matrizes.id"))
    confinamentoId = db.Column(db.Integer, db.ForeignKey("confinamento.id"))
    dataInseminacao = db.Column("dataInseminacao", db.VARCHAR)
    active = db.Column("active", db.Boolean, default=True)
   
    matrizes = relationship(Matriz, foreign_keys=[matrizId])
    planos = relationship("Plano", foreign_keys=[planoId])

class InseminacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inseminacao
        include_fk = False