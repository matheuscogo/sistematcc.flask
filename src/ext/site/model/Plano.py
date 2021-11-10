from ...db import db, ma

class Plano(db.Model):
    __tablename__ = "planos"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String)
    descricao = db.Column("descricao", db.String)
    tipo = db.Column("tipo", db.String)
    quantidadeDias = db.Column("quantidadeDias", db.Integer)
    ativo = db.Column("ativo", db.Boolean)

    def __init__(
        id = id,
        nome = nome,
        descricao = descricao,
        tipo = tipo,
        quantidadeDias = quantidadeDias,
        ativo = ativo
    ):
        Plano.id = id
        Plano.nome = nome
        Plano.descricao = descricao
        Plano.tipo = tipo
        Plano.quantidadeDias = quantidadeDias
        Plano.ativo = ativo

class PlanoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plano
        include_fk = False