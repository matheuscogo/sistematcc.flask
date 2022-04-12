from ...db import db, ma
from sqlalchemy.orm import relationship

class Confinamento(db.Model):
    __tablename__ = "confinamento"
    id = db.Column("id", db.Integer, primary_key=True)
    planoId = db.Column(db.Integer, db.ForeignKey("planos.id"))
    matrizId = db.Column(db.Integer, db.ForeignKey("matrizes.id"))
    dataConfinamento = db.Column("dataConfinamento", db.VARCHAR)
    active = db.Column("active", db.Boolean, default=True)
   
    matrizes = relationship("Matriz", foreign_keys=matrizId)
    planos = relationship("Plano", foreign_keys=planoId)

class ConfinamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Confinamento
        include_fk = True

