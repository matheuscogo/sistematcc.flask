from ...db import db, ma

# class Confinamento():
#     db.Table('confinamento',
#     db.Column('matriz', db.Integer, db.ForeignKey('matrizes.id'),primary_key=True),
#     db.Column('plano', db.Integer, db.ForeignKey('planos.id'),primary_key=True),
#     db.Column("dataEntrada", db.VARCHAR,  primary_key=True)
# )
class Confinamento(db.Model):
    __tablename__ = "confinamento"
    plano = db.Column(db.Integer, db.ForeignKey("planos.id"), primary_key=True)
    matriz = db.Column(db.Integer, db.ForeignKey("matriz.id"), primary_key=True)
    dataConfinamento = db.Column("dataConfinamento", db.VARCHAR, primary_key=True)

    def __init__(
        matriz = matriz,
        plano = plano,
        dataConfinamento = dataConfinamento
    ):
        Confinamento.matriz = matriz
        Confinamento.plano = plano,
        Confinamento.dataConfinamento = dataConfinamento

# association_table = db.Table('confinamento',
#     db.Column('matriz', db.Integer, db.ForeignKey('matrizes.id'),primary_key=True),
#     db.Column('plano', db.Integer, db.ForeignKey('planos.id'),primary_key=True),
#     db.Column("dataEntrada", db.VARCHAR,  primary_key=True)
# )

class ConfinamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Confinamento
        include_fk = False

