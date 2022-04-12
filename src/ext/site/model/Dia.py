from ...db import db, ma

class Dias(db.Model):
    __tablename__ = "dias"
    id = db.Column("id", db.Integer, primary_key=True)
    planoId = db.Column("planoId", db.Integer,  db.ForeignKey("planos.id"))
    dia = db.Column("dia", db.Integer)
    quantidade = db.Column("quantidade", db.Integer)

    plano = db.relationship("Plano", foreign_keys=planoId)

class DiasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dias
        include_fk = True

