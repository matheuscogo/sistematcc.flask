from ...db import db

association_table = db.Table('confinamento',
    db.Column('matriz', db.Integer, db.ForeignKey('matrizes.id'),primary_key=True),
    db.Column('plano', db.Integer, db.ForeignKey('planos.id'),primary_key=True),
    db.Column("dataEntrada", db.VARCHAR,  primary_key=True)
)