from ...db import db, ma

class Plano(db.Model):
    __tablename__ = "planos"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String)
    descricao = db.Column("descricao", db.String)
    tipo = db.Column("tipo", db.String)
    quantidadeDias = db.Column("quantidadeDias", db.Integer)
    deleted = db.Column("deleted", db.Boolean, default=False)
    active = db.Column("active", db.Boolean, default=True)

class PlanoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plano
        include_fk = True