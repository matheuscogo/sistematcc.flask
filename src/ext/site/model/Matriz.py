from ...db import db, ma
from .Confinamento import association_table

class Matriz(db.Model):
    __tablename__ = "matrizes"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    rfid = db.Column("rfid", db.VARCHAR)
    numero = db.Column("numero", db.Integer)
    ciclos = db.Column("ciclos", db.Integer)

    def __init__(
        id = id,
        rfid = rfid,
        numero = numero,
        ciclos = ciclos
    ):
        Matriz.id = id
        Matriz.rfid = rfid
        Matriz.numero = numero
        Matriz.ciclos = ciclos

class MatrizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Matriz
        include_fk = False