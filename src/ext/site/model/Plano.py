from ...db import db

class Plano(db.Model):
    __tablename__ = "planos"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String)
    descricao = db.Column("descricao", db.String)
    tipo = db.Column("tipo", db.String)
    quantidadeDias = db.Column("quantidadeDias", db.Integer)
    ativo = db.Column("ativo", db.Boolean)

    def __repr__(self):
        return '<Plano %r>' % self.id