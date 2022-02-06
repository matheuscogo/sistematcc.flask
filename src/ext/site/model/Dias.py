from ...db import db, ma

class Dias(db.Model):
    __tablename__ = "dias"
    id = db.Column("id", db.Integer, primary_key=True)
    plano = db.Column(db.Integer, db.ForeignKey("planos.id"))
    dia = db.Column("dia", db.Integer)
    quantidade = db.Column("quantidade", db.Integer)

    def __init__(
        id = id,
        plano = plano,
        dia = dia,
        quantidade = quantidade
    ):
        Dias.id = id
        Dias.plano = plano
        Dias.dia = dia
        Dias.quantidade = quantidade  

class DiasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dias
        include_fk = False

